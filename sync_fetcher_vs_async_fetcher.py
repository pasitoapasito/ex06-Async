import requests, time, aiohttp, asyncio


"""
동기 fetch 함수
"""
def sync_fetcher(session, url):
    with session.get(url) as response:
        return response.text

def sync_func():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    """
    request: 동기적 요청 라이브러리 활용
    """
    with requests.Session() as session:
        result = [sync_fetcher(session, url) for url in urls]

        return result


"""
비동기 fetch 함수(코루틴 함수)
"""
async def async_fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()

async def async_func():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    """
    aiohttp: 비동기적 요청 라이브러리 활용
    """
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[async_fetcher(session, url) for url in urls])

        return result


if __name__ == "__main__":
    """
    동기 함수 호출
    """
    sync_start = time.time()
    sync_func()
    sync_end = time.time()

    print(f"동기 fetch 결과: {sync_end - sync_start}")     # 10.5초

    """
    비동기(코루틴) 함수 호출
    """
    async_start = time.time()
    asyncio.run(async_func())
    async_end = time.time()

    print(f"비동기 fetch 결과: {async_end - async_start}")  # 0.9초
