import aiohttp
import asyncio

async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://www.httpbin.org/post', params=params) as response:
            print(await response.text())
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())