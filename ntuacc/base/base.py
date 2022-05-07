from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class SalaryData(ABC):
    """
    The SalaryData object extracts the data from html table tags.
    """

    @abstractmethod
    def download_soup(self) -> BeautifulSoup:
        pass

    @abstractmethod
    def extract_data(self):
        """The extract_data method extracts the data from the BeautifulSoup object."""
        pass


class Table(ABC):
    """
    The Table object builds a pandas DataFrame based on the given html table tags.
    """

    @abstractmethod
    def download_tabel_tags(self):
        pass

    @abstractmethod
    def format_table(self):
        pass

    @abstractmethod
    def build_table(self):
        pass
