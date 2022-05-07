import pandas as pd
from bs4 import ResultSet
from ...base import SalaryData
from dataclasses import dataclass


@dataclass
class ProjectTable:
    """
    The ProjectTable object extracts the project dataframe.
    """

    table_tag: ResultSet

    def format_table(self, data_frame: pd.DataFrame):
        """The format_table method formats the DataFrame

        Args:
            table (pd.DataFrame): the DataFrame object

        Returns:
            a pd.DataFrame object
        """

        table = data_frame.drop([0, 6, 8, 11], axis=1)
        new_header = table.iloc[0]
        table = table[1:]
        table.columns = new_header
        table = table.rename(columns={"申請日請": "申請日期"})
        return table

    def build_table(self) -> pd.DataFrame:
        """The build_table method builds the pd.DataFrame based on `table_tag`.

        Returns:
            a pd.DataFrame object
        """

        data_frame = pd.read_html(str(self.table_tag))[0]
        return self.format_table(data_frame)
