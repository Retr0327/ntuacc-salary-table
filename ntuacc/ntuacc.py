from .util import convert
from .core import SalaryTable
from dataclasses import dataclass


@dataclass
class NTUACC:
    """
    The NTUACC object downloads the table based on `bossid`, `assid`, `asspwd` and `project_year`.
    """

    bossid: str
    assid: str
    asspwd: str
    project_year: int

    def __post_init__(self) -> None:
        self.query = {
            "campno": "m",
            "idtype": "3",
            "bossid": self.bossid,
            "assid": self.assid,
            "asspwd": self.asspwd,
        }

    def download_table(self) -> SalaryTable:
        """The download_table method downloads the salary table."""
        return SalaryTable(self.query, self.project_year).extract_data()

    @convert("pickle")
    def to_pickle(self) -> None:
        return

    @convert("csv")
    def to_csv(self) -> None:
        return
