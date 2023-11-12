import asyncio
import aiohttp

# 最大并发量为 5
CONCURRENCY = 5
# 爬取地址
URL = 'https://www.baidu.com'

# 用Semaphore创建了以恶信号量对象 控制最大并发量
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

async def scrape_api():
    # 将这个方法直接放在函数里，使用async with 语句将 semaphore 作为上下文对象
    async with semaphore:
        print('Scraping', URL)
        async with session.get(URL) as response:
            await asyncio.sleep(1)
            return await response.text()
        
async def main():
    global session
    session = aiohttp.ClientSession()
    # 创建了一万个task 传递至gather方法使用
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]
    await asyncio.gather(*scrape_index_tasks)
    

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())