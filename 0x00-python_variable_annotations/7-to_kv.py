#!/usr/bin/env python3
"""This Module contains a function that converts a Python variable to a Key-value pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a KV pair."""
    return k, v ** 2
