import time, asyncio


"""
동기 함수 
"""
def sync_delivery(name: str, worktime: int):
    print(f"{name}에게 요청 완료!")

    time.sleep(worktime)
    
    print(f"{name} 요청처리 완료, {worktime}시간 소요...")
    print(f"{name} 응답 완료")
    
    return None

def sync_func():
    sync_delivery("A", 10)
    sync_delivery("B", 5)
    sync_delivery("C", 3)
    
    return None


"""
비동기 함수(코루틴 함수)
"""
async def async_delivery(name: str, worktime: int):
    print(f"{name}에게 요청 완료!")
    
    await asyncio.sleep(worktime)
    
    print(f"{name} 요청처리 완료, {worktime}시간 소요...")
    print(f"{name} 응답 완료")
    
    return None

async def async_func():
    """
    asyncio.gather(): 비동기 함수를 동시성(Concurrency)으로 처리하는 함수
    """
    result = await asyncio.gather(
        async_delivery("A", 10),
        async_delivery("B", 5),
        async_delivery("C", 3),
    )

    """
    cf. 위의 비동기 코드를 동기적으로 실행하기 위한 코드

    await async_delivery("A", 10)
    await async_delivery("B", 5)
    await async_delivery("C", 3)
    """
    return result


if __name__ == "__main__":
    """
    동기 함수
      - 처리 순서
        1. A에게 요청 후 대기
        2. A 요청처리 완료 -> A 응답 완료
        3. B에게 요청 후 대기
        4. B 요청처리 완료 -> B 응답 완료
        5. C에게 요청 후 대기
        6. C 요청처리 완료 -> C 응답 완료 
    """
    sync_start = time.time()
    sync_func()
    sync_end = time.time()

    print(sync_end - sync_start)   # 18초

    """
    비동기 함수(코루틴 함수)
      - 처리 순서
        1. A에게 요청
        2. B에게 요청
        3. C에게 요청
        4. C 요청처리 완료 -> C 응답 완료(여전히 A, B 요청처리 완료X 때문)
        5. B 요청처리 완료 -> B 응답 완료(여전히 B 요청처리 완료X 때문)
        6. A 요청처리 완료 -> A 응답 완료
    """
    async_start = time.time()
    asyncio.run(async_func())
    async_end = time.time()

    print(async_end - async_start) # 10초
