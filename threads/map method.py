import concurrent.futures
import time
from concurrent.futures import Future
from typing import List
from unittest import result

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s).....')
    time.sleep(1)
    # print('Done sleeping.....')
    return f'Done sleeping{seconds} ......'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something, secs) for _ in range(10)]

    # for result  in concurrent.futures.as_completed(results):
    #     print(f.result())
    for result in results:
        print(result)

# secs = [5, 4, 3, 2, 1]
# results = [executor.submit(do_something, sec) for sec in secs]
#
# for f in concurrent.futures.as_completed(results):
#     print(f.result())

# finish = time.perf_counter()
#
# print(f'finished in{round(finish - start, 2)}second(s)')
