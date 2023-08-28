import threading
import time

start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second.....')
#     time.sleep(1)
#     print('Done sleeping.....')
def do_something(seconds):
    print(f'Sleeping {seconds} second....')
    time.sleep(seconds)
    print('Done Sleeping')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)
# List Comprehension
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'finished in{round(finish - start, 2)}second(s)')
