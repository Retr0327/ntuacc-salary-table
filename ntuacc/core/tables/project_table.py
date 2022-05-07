import pandas as pd
from typing import Union
from bs4 import ResultSet
from ..data import ProjectData
from dataclasses import dataclass


@dataclass
class ProjectTable:
    """
    The ProjectTable object extracts the project dataframe.
    """

    project_year: int

    def download_tabel_tags(self) -> Union[str, ResultSet]:
        """The download_tabel_tags method downloads the table tags from ProjectData.

        Returns:
            a str if there is no project data, a soup object otherwise.
        """
        return ProjectData(self.project_year).extract_data()

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

    def build_table(self) -> Union[str, pd.DataFrame]:
        """The build_table method builds the pd.DataFrame based on `table_tag`.

        Returns:
            a pd.DataFrame object
        """

        table_tags = self.download_tabel_tags()

        if isinstance(table_tags, str):
            return table_tags

        data_frame = pd.read_html(str(table_tags))[0]
        return self.format_table(data_frame)
