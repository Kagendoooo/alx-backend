#!/usr/bin/env python3
"""
Function that takes two integer arguments
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns tuple of size two
    containing a start index and an end index of paagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
