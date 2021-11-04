import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from dataclasses import dataclass
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor


HEADERS = {"user-agent": UserAgent().google}


@dataclass
class SalaryData:
    """
    The SalaryData object extracts the salary dataframe.
    """

    query: dict
    project_year: int

    def __post_init__(self) -> None:
        if len(str(self.project_year)) == 4:
            self.project_year -= 1911

    def set_session(self) -> None:
        """The set_session method set the session to persist certain parameters across requests."""
        with requests.session() as session:
            session.post(
                "https://ntuacc.cc.ntu.edu.tw/acc/secure.asp",
                data=self.query,
                headers=HEADERS,
            )
            return session

    def get_project_soup(self, project_year: str) -> BeautifulSoup:
        """The get_project_soup method gets the BeautifulSoup object of a project.

        Args:
            project_year (str): the project year

        Returns:
            a BeautifulSoup object

        """
        session = self.set_session()
        data = {"VYEAR": project_year}
        html_body = session.post(
            "https://ntuacc.cc.ntu.edu.tw/acc/apply/ProjectDetail.asp",
            data=data,
            headers=HEADERS,
        )
        html_body.encoding = "big5"
        soup = BeautifulSoup(html_body.text, "lxml")
        table_tags = soup.find_all("table", {"border": "1"})
        if not table_tags:
            return f"沒有{self.project_year}年的資料"
        return table_tags

    def get_remit_date(self, project_id: str) -> str:
        """The get_remit_date method gets the remit date based on the `request_info`.

        Args:
            project_id (str): the id of a project

        Returns:
            a str
        """
        session = self.set_session()
        html_body = session.get(
            f"https://ntuacc.cc.ntu.edu.tw/trace/trace.asp?target=self&APPCODE={project_id}&VYEAR={project_id[:3]}",
            headers=HEADERS,
        )
        html_body.encoding = "big5"
        soup = BeautifulSoup(html_body.text, "lxml")
        remit_soup = soup.findAll("tr")[-1].text.strip()
        date = re.search("\d+", remit_soup).group()
        if len(date) < 8:
            return "尚未入帳"
        return date

    def format_table(self, table) -> pd.DataFrame:
        """The format_table method formats the DataFrame

        Args:
            table (pd.DataFrame): the DataFrame object

        Returns:
            a pd.DataFrame object
        """
        table = table.drop([0, 6, 8, 11], axis=1)
        new_header = table.iloc[0]
        table = table[1:]
        table.columns = new_header
        table = table.rename(columns={"申請日請": "申請日期"})
        return table

    def clean_data(self, table_tags) -> pd.DataFrame:
        """The clean_data method cleans the table tags to a DataFrame object.

        Args:
            table_tags (BeautifulSoup): the BeautifulSoup object carring the table data

        Reutns:
            a pd.DataFrame object
        """
        df = pd.read_html(str(table_tags))[0]
        formatted_table = self.format_table(df)
        with ThreadPoolExecutor() as executor:
            result = executor.map(self.get_remit_soup, formatted_table["黏存單號碼"])
        formatted_table["入帳日期"] = list(result)
        return formatted_table

    def extract_data(self) -> pd.DataFrame:
        """The extract_data method extracts the data from the BeautifulSoup object.

        Returns:
            a pd.DataFrame object
        """
        table_tags = self.get_project_soup(str(self.project_year))
        if isinstance(table_tags, str):
            return table_tags

        table = self.clean_data(table_tags)
        return table
