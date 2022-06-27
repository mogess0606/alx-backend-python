#!/usr/bin/env python3
""" 
	Wait random module 
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:

""" Wait random number 

	Args: 
	
		Max-dalay(int, optional): max number Def to 10.
	Returns:
		float: random float number
	"""


	random_delay: float = random.uniform(0,max_delay)
	await asyncio.sleep(random_delay)
	return random_delay
