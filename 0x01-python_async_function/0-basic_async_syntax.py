#!/usr/bin/env python3
"""
   module  uses async to execute different coroutines at same time
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    it takes an integer - max_delay, waits for a random delay between 
    0 and max_delay seconds and then returns the random int.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
