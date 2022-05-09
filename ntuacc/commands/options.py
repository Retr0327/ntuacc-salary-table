import argparse


class NTUACCParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog="NTUACC Salary Table", description="Manage NTUACC salary table log"
        )

        self.subparser = self.parser.add_subparsers(
            dest="subcmd", help="description", metavar="Actions", required=True
        )

        self.add_show()

    def add_show(self):
        show = self.subparser.add_parser("show", help="Show salary table")
        show.add_argument(
            "--bossid", "-B", type=str, required=True, help="Text for boss id"
        )
        show.add_argument(
            "--assid", "-AID", type=str, required=True, help="Text for assistant id"
        )
        show.add_argument(
            "--asspwd",
            "-AP",
            type=str,
            required=True,
            help="Text for assistant password",
        )
        show.add_argument(
            "--year", "-Y", type=int, required=True, help="Int for project year"
        )
        show.add_argument("--to", "-T", type=str, help="Text for convert type")

    def parse_args(self):
        return self.parser.parse_args()


if __name__ == "__main__":
    ntuacc_parser = NTUACCParser()
    res = ntuacc_parser.parse_args()
    print(res)
