import asyncio

from metagpt.context import Context

from SimpleCoder import SimpleCoder

from metagpt.logs import logger

async def main():
    msg = "write a function that calculates the sum of a list"
    context = Context()
    role = SimpleCoder(context=context)
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())