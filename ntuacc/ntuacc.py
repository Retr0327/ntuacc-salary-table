from .util import convert
from .core import SalaryTable
from pydantic import StrictStr, StrictInt
from pydantic.dataclasses import dataclass


@dataclass
class NTUACC:
    """
    The NTUACC object downloads the table based on `bossid`, `assid`, `asspwd` and `project_year`.
    """

    bossid: StrictStr
    assid: StrictStr
    asspwd: StrictStr
    project_year: StrictInt

    def __post_init__(self):
        self.query = {
            "campno": "m",
            "idtype": "3",
            "bossid": self.bossid.strip(),
            "assid": self.assid.strip(),
            "asspwd": self.asspwd.strip(),
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
