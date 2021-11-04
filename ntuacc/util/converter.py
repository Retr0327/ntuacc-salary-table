import pandas as pd
from functools import wraps


def pickling(table: pd.DataFrame, project_year: int) -> None:
    """The pickling function serializes the DataFrame to a pickle file.

    Returns:
        a pickle file.
    """
    return table.to_pickle(f"./{project_year}_salary_table.pkl")


def tablize(table: pd.DataFrame, project_year: int) -> None:
    """The tablize function serializes the DataFrame to a csv file.

    Returns:
        a csv file.
    """
    return table.to_csv(
        f"./{project_year}_salary_table.csv", index=False, encoding="utf_8_sig"
    )


def convert(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            table = self.download_table()
            if isinstance(table, str):
                return table
            if datatype == "pickle":
                pickling(table, self.project_year)
            elif datatype == "csv":
                tablize(table, self.project_year)

        return wrapper

    return decorator
