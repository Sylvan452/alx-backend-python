#!/usr/bin/env python3
"""Module contains function that converts Python var to a Key-value pair."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a KV pair."""
    return k, v ** 2
