import re
from bs4 import BeautifulSoup
from ...base import SalaryData
from dataclasses import dataclass
from ...store import session_store, HEADERS


@dataclass
class TraceData(SalaryData):
    project_id: str

    def download_soup(self):
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
        soup = self.download_soup()
        table_tags = soup.findAll("tr")[-1].text.strip()

        if "退件" in table_tags:
            return_docs_info = table_tags.split("\n")
            return return_docs_info[-1].strip()

        date = re.search("\d+", table_tags).group()

        if len(date) < 8:
            return "尚未入帳"

        return date
