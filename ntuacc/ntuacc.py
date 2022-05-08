from .core import SalaryTable
from .util import login, convert
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
        self.__query = {
            "campno": "m",
            "idtype": "3",
            "bossid": self.bossid.strip(),
            "assid": self.assid.strip(),
            "asspwd": self.asspwd.strip(),
        }

        self.is_logged_in = login(self.__query)

    def download_table(self) -> SalaryTable:
        """The download_table method downloads the salary table."""

        if not self.is_logged_in:
            return self.is_logged_in

        return SalaryTable(self.project_year).extract_data()

    @convert("pickle")
    def to_pickle(self) -> None:
        return

    @convert("csv")
    def to_csv(self) -> None:
        return
