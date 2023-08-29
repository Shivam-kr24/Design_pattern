import threading
import time


def print_epoch( nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1


class Mythread(threading.Thread):
    def __int__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("start thread", self.name)
        print_epoch(self.delay)
        print("end thread",self.name)


if __name__ == "__main__":
    t1 = Mythread("Thread-1", 1)
    t2 = Mythread("Thread-2", 2)

    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
    print(threading.activeCount())
    print(threading.Currentthread())
    print(threading.enumerate())

    t1.join()
    t2.join()

    print("Done")
