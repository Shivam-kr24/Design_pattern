import threading
import time
# Threading module in python3

# @ by shivam
def print_epoch(nameOfThread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "------------", time.time())


def print_cube(num):
    print("cube = {}".format(num * num * num))


def print_square(num):
    print("cube = {}".format(num * num ))


if __name__ == "__main__":
    t1 = threading.Thread(target=print_epoch, args=(1, ))
    t2 = threading.Thread(target=print_epoch, args=(2, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")
