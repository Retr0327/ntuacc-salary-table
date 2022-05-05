from .util import convert
from .core import SalaryTable
from dataclasses import dataclass
from pydantic import StrictStr, StrictInt, BaseModel


class QueryInfo(BaseModel):
    """
    The QueryInfo object keeps tract of the query in inventory, including bossid, assid, asspwd, and project_year
    """

    campno = "m"
    idtype = "3"
    bossid: StrictStr
    assid: StrictStr
    asspwd: StrictStr
    project_year: StrictInt


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
        self.query = QueryInfo(
            bossid=self.bossid,
            assid=self.assid,
            asspwd=self.asspwd,
            project_year=self.project_year,
        ).dict()

    def download_table(self) -> SalaryTable:
        """The download_table method downloads the salary table."""
        return SalaryTable(self.query, self.project_year).extract_data()

    @convert("pickle")
    def to_pickle(self) -> None:
        return

    @convert("csv")
    def to_csv(self) -> None:
        return
