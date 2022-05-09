import pandas as pd
from typing import Union
from ..data import TraceData
from dataclasses import dataclass
from ..utils import set_project_year
from .project_table import ProjectTable
from concurrent.futures import ThreadPoolExecutor


@dataclass
class SalaryTable:
    """
    The SalaryTable object extracts the salary dataframe.
    """

    project_year: int

    def __post_init__(self) -> None:
        self.project_year = set_project_year(self.project_year)

    def create_trace_data_list(self, project_ids: pd.Series) -> list[str]:
        """The add_trace_data method creates a list of trace data from the argument `project_ids`

        Returns:
            a list
        """
        with ThreadPoolExecutor() as executor:
            result = executor.map(
                lambda project_id: TraceData(project_id).extract_data(), project_ids
            )

        return list(result)

    def download(self) -> Union[str, pd.DataFrame]:
        """The download method downloads the salary table.

        Returns:
            a str if there is no data, a pd.DataFrame otherwise.
        """
        project_table = ProjectTable(self.project_year).build_table()

        if isinstance(project_table, pd.DataFrame):
            project_ids = project_table["黏存單號碼"]
            project_table["入帳日期"] = self.create_trace_data_list(project_ids)

        return project_table
