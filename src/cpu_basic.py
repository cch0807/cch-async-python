import os
import threading
import time


nums = [50, 63, 32]


def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k


def main():
    for num in nums:
        cpu_bound_func(num)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
