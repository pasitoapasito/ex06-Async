"""
참고: CPU BOUND TEST
"""

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

import time, os, threading


nums = [10]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def single_threading_func():
    results = [cpu_bound_func(num) for num in nums]
    print(results)


def multi_threading_func():
    executor = ThreadPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


def multi_processing_func():
    executor = ProcessPoolExecutor(max_workers=10)
    results = list(executor.map(cpu_bound_func, nums))
    print(results)


if __name__ == "__main__":
    single_start = time.time()
    single_threading_func()
    single_end = time.time()
    print(single_end - single_start)  # 0.0001

    multi_threading_start = time.time()
    multi_threading_func()
    multi_threading_end = time.time()
    print(multi_threading_end - multi_threading_start)    # 0.0003

    multi_processing_start = time.time()
    multi_processing_func()
    multi_processing_end = time.time()
    print(multi_processing_end - multi_processing_start)  # 0.03
