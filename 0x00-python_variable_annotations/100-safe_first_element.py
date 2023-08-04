#!/usr/bin/env python3
"""Module contains Augmented code with correct duck-typed annotations."""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """It return first element of a list or None if the list is empty."""
    if lst:
        return lst[0]
    else:
        return None
