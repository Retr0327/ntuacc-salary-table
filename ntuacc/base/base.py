from abc import ABC, abstractmethod


class Table(ABC):
    """
    The Table object extracts the data from html table tags.
    """

    @abstractmethod
    def extract_data(self):
        """The extract_data method extracts the data from the BeautifulSoup object."""
        pass
