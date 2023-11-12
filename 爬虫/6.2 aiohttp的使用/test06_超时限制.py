import aiohttp
import asyncio

# 抛出Timeout异常是因为超时了，如果一分钟响应则会抛出状态码，


async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://www.httpbin.org/get') as response:
            print('Status:', response.status)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
