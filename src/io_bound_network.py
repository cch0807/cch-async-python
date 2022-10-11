import requests  # F401
import time
import aiohttp
import asyncio


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"]

    # session = requests.Session()

    # session.get(url)

    # session.close()

    # with requests.Session() as session:
    #     result = [fetcher(session, url) for url in urls]
    #     print(result)

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        # result = await fetcher(session, urls[0])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
