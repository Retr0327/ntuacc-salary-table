from typing import Union
from ...base import SalaryData
from dataclasses import dataclass
from bs4 import BeautifulSoup, ResultSet
from ...store import session_store, HEADERS


@dataclass
class ProjectData(SalaryData):
    """
    The ProjectData object extracts data from html based on the argument `project_year`.
    """

    project_year: int

    def download_soup(self) -> BeautifulSoup:
        """The download_soup method downloads the html tree.

        Returns:
            a BeautifulSoup object
        """

        session = session_store["session"]

        if not session:
            raise Exception("Please login first!")

        html_body = session.post(
            "https://ntuacc.cc.ntu.edu.tw/acc/apply/ProjectDetail.asp",
            data={"VYEAR": self.project_year},
            headers=HEADERS,
        )

        html_body.encoding = "big5"
        return BeautifulSoup(html_body.text, "lxml")

    def extract_data(self) -> Union[str, ResultSet]:
        """The extract_data method extracts data from the BeautifulSoup object.

        Returns:
            a str if there is no data, a ResultSet otherwise.
        """
        soup = self.download_soup()
        table_tags = soup.find_all("table", {"border": "1"})

        if not table_tags:
            return f"沒有 {self.project_year} 年的資料"

        return table_tags
