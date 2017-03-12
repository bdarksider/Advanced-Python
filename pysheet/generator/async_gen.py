# need python3.6 or above
import asyncio

async def slow_gen(n, t):
    for x in range(n):
        await asyncio.sleep(t)
        yield x

async def task(n):
    async for x in slow_gen(n, 0.1):
        print(x)

loop = asyncio.get_event_loop()
loop.run_until_complete(task(3))
