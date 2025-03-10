import asyncio

from metagpt.context import Context

from metagpt.logs import logger

from RunnableCoderRole import RunnableCoder

async def main():
    msg = "write a function that calculates the sum of a list"
    context = Context()
    role = RunnableCoder(context=context)
    logger.info(msg)
    result = await role.run(msg)
    logger.info(result)

asyncio.run(main())