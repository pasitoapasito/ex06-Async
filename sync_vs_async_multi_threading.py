from concurrent.futures import ThreadPoolExecutor

import requests, time, os, threading, asyncio, aiohttp


"""
동기 fetch 함수
"""
def sync_fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def sync_func():
    urls = ["https://google.com", "https://apple.com"] * 50

    """
    request: 동기적 요청 라이브러리 활용
    """
    with requests.Session() as session:
        result = [sync_fetcher(session, url) for url in urls]
        print(result)


"""
비동기 fetch 함수
"""
async def async_fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    async with session.get(url) as response:
        return await response.text()


async def async_func():
    urls = ["https://google.com", "https://apple.com"] * 50

    """
    aiohttp: 비동기적 요청 라이브러리 활용(비동기적 요청을 동시성으로 처리)
    """
    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[async_fetcher(session, url) for url in urls])
        print(result)


"""
멀티 쓰레딩 fetch 함수(thread: 10개)
"""
def multi_threading_fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def multi_threading_func():
    urls = ["https://google.com", "https://apple.com"] * 50

    executor = ThreadPoolExecutor(max_workers=10)

    """
    request/multi threading: 멀티 쓰레딩(10개)를 통한 동기적 요청 라이브러리 활용
    """
    with requests.Session() as session:
        params = [(session, url) for url in urls]
        results = list(executor.map(multi_threading_fetcher, params))
        print(results)


if __name__ == "__main__":
    """
    동기 함수 호출
    """
    sync_start = time.time()
    sync_func()
    sync_end = time.time()
    print(sync_end - sync_start)    # 14초

    """
    비동기 함수 호출
    """
    async_start = time.time()
    asyncio.run(async_func())
    async_end = time.time()
    print(async_end - async_start)  # 2초

    """
    멀티 쓰레딩 함수 호출(thread: 10개)
    """
    multi_threading_start = time.time()
    multi_threading_func()
    multi_threading_end = time.time()
    print(multi_threading_end - multi_threading_start)  # 4초
