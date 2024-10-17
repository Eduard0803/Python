import asyncio
from time import perf_counter

import aiohttp


async def fetch(s, url):
    async with s.get("http://localhost:8000") as r:
        return await r.text()


async def fetch_all(s, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(s, url))
        tasks.append(task)
    return await asyncio.gather(*tasks)


async def main():
    urls = range(1, 10 * 1000)
    async with aiohttp.ClientSession() as s:
        html = await fetch_all(s, urls)
        print(html)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"time: {end-start}")
