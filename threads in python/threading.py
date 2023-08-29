import threading
import time


# @ by shivam


def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "------------", time.time())


if __name__ == "__main__":
    t1 = threading.Thread(target=print_epoch, args=("Thread 1", 1))
    t2 = threading.Thread(target=print_epoch, args=("Thread 2", 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Done")



