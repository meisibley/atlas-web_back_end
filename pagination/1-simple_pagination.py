#!/usr/bin/env python3
""" Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
You have to use this CSV file Popular_Baby_Name.csv
"""
import csv
import math
from typing import List, Tuple
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
