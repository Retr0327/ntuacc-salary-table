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
        return soup.findAll("tr")[-1].text.strip()
