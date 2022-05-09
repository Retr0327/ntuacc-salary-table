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
    convert_type = parser["to"]

    ntuacc = NTUACC(bossid, assid, asspwd, project_year)

    print(tabulate(ntuacc.download_table(), headers="keys", tablefmt="psql"))

    if convert_type == "csv":
        ntuacc.to_csv()
    if convert_type == "pickle":
        ntuacc.to_pickle()
