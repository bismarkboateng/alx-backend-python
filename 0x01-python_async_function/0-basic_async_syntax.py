#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    params: max_delay (int)
    return: float
    function waits for a random delay between 0 and max_delay
    seconds and returns it
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay