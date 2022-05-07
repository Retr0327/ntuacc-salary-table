from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class SalaryData(ABC):
    """
    The Table object extracts the data from html table tags.
    """

    @abstractmethod
    def download_soup(self) -> BeautifulSoup:
        pass

    @abstractmethod
    def extract_data(self):
        """The extract_data method extracts the data from the BeautifulSoup object."""
        pass
