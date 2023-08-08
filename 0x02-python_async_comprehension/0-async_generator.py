#!/usr/bin/env python3
'''  
 This coroutine task called async_generator takes no arguments.

 it will loops 10 times, each time asynchronously wait till 
 1 second, then yield a random number between 0 and 10. Use the random module.
'''

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Function generator would loop 10 times, asynchronously wait 1 sec
     and yield a random number between 1 and 10. '''
    for i in range(10):
        await sleep(1)
        yield 10 * random()
