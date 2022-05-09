import pandas as pd


def set_project_year(project_year: int) -> int:
    """The set_project_year function calculates the year in Minguo calendar.

    Args:
        project_year (int): the given project year, which can be either
                            Minguo year or Gregorian year.

    Returns:
        a int
    """
    if (len(str(project_year))) == 4:
        project_year -= 1911
        return project_year

    return project_year


def format_table(table: pd.DataFrame) -> pd.DataFrame:
    """The format_table function formats the DataFrame

    Args:
        table (pd.DataFrame): the DataFrame object

    Returns:
        a pd.DataFrame object
    """

    table = table.drop([0, 6, 8, 11], axis=1)
    new_header = table.iloc[0]
    table = table[1:]
    table.columns = new_header
    table = table.rename(columns={"申請日請": "申請日期"})
    return table
