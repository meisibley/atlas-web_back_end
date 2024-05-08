#!/usr/bin/env python3
""" Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:
page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
"""
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """ Use assert to verify that both arguments are integers
        greater than 0.
        Use index_range to find the correct indexes to paginate the
        dataset correctly and return the appropriate page of the dataset
        (i.e. the correct list of rows).
        If the input arguments are out of range for the dataset, an
        empty list should be returned.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        startIndex, endIndex = index_range(page, page_size)

        if startIndex >= len(self.dataset()):
            return []
        return self.dataset()[startIndex:endIndex]

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """ returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        total_page = math.ceil(len(self.dataset()) / page_size)

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": None if page > total_page else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_page": total_page
        }
