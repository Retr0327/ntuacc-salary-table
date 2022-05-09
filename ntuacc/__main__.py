import sys
from pathlib import Path


path = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(path))

from tabulate import tabulate
from ntuacc import NTUACC, NTUACCParser

table_parser = NTUACCParser()

parser = vars(table_parser.parse_args())


if parser.get("subcmd") == "show":
    bossid = parser["bossid"]
    assid = parser["assid"]
    asspwd = parser["asspwd"]
    project_year = parser["year"]

    print(
        tabulate(
            NTUACC(bossid, assid, asspwd, project_year).download_table(),
            headers="keys",
            tablefmt="psql",
        )
    )

