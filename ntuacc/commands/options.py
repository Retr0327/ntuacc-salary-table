import argparse


class NTUACCParser:
    """
    The NTUACCParser object handles both optional and positional arguments.
    """

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog="NTUACC Salary Table", description="Manage NTUACC salary table log"
        )

        self.subparser = self.parser.add_subparsers(
            dest="subcmd", help="description", metavar="Actions", required=True
        )

        self.add_login()
        self.add_show()

    def add_login(self) -> None:
        """The add_login method adds the `login` command."""
        self.subparser.add_parser("login", help="Login NTUACC")

    def add_show(self) -> None:
        """The add_show method adds the `show` command."""
        show = self.subparser.add_parser("show", help="Show salary table")
        show.add_argument(
            "--year", "-Y", type=int, required=True, help="Int for project year"
        )

    def parse_args(self):
        return self.parser.parse_args()


if __name__ == "__main__":
    ntuacc_parser = NTUACCParser()
    res = ntuacc_parser.parse_args()
    print(res)
