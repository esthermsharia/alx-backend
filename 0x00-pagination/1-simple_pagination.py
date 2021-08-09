#!/usr/bin/env python3
"""
  Simple pagination.
"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing start index and end index
        corresponding to the range of indexes to ruturn in a list
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """  find the correct indexes to paginate the dataset correctly and
             return the appropriate page of the dataset.
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        size_of_csv = len(self.dataset())
        first, last = index_range(page, page_size)
        end = min(last, size_of_csv)
        if first >= size_of_csv:
            return []
        return self.dataset()[first:last]
