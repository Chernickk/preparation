from typing import List

from bs4 import BeautifulSoup
import aiohttp
import asyncio
import aiofiles

url = 'http://localhost:8088'


async def main(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            soup = BeautifulSoup(await resp.text(), 'html.parser')
            links = [f'{url}{a["href"]}' for a in soup.findAll('a', href=True)]
            return list(set(links))


async def save_pages(urls: List[str]):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                page = await resp.text()
            async with aiofiles.open(f'{url.split("/")[-1]}.html', 'w+') as f:
                await f.write(page)


links = asyncio.run(main(url))
print(links)
asyncio.run(save_pages(links))
