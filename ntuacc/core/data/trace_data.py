import re
from bs4 import BeautifulSoup
from ..base import SalaryData
from dataclasses import dataclass
from ..store import session_store, HEADERS


@dataclass
class TraceData(SalaryData):
    """
    The TraceData object downloads the trace info from the given `project_id`
    """

    project_id: str

    def download_soup(self) -> BeautifulSoup:
        """The download_soup method downloads the html tree.

        Returns:
            a BeautifulSoup object
        """
        session = session_store["session"]

        if not session:
            raise Exception("Please login first!")

        html_body = session.get(
            f"https://ntuacc.cc.ntu.edu.tw/trace/trace.asp?target=self&APPCODE={self.project_id}&VYEAR={self.project_id[:3]}",
            headers=HEADERS,
        )

        html_body.encoding = "big5"
        return BeautifulSoup(html_body.text, "lxml")

    def extract_data(self) -> str:
        """The extract_data method extracts data from the BeautifulSoup object.

        Returns:
            a str
        """
        soup = self.download_soup()
        table_tags = soup.findAll("tr")[-1].text.strip()

        if "退件" in table_tags:
            return_docs_info = table_tags.split("\n")
            return return_docs_info[-1].strip()

        date = re.search("\d+", table_tags).group()

        if len(date) < 8:
            return "尚未入帳"

        return date
