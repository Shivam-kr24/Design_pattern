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
    return 'Done sleeping ......'


# submit method
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1)
    # print(f1.result())
    # submit button method
    f2 = executor.submit(do_something, 1)

    print(f1.result())
    print(f2.result())

    # List comprehensive

secs = [5, 4, 3, 2, 1]
results = [executor.submit(do_something, sec) for sec in secs]

for f in concurrent.futures.as_completed(results):
    print(f.result())

# finish = time.perf_counter()
#
# print(f'finished in{round(finish - start, 2)}second(s)')
