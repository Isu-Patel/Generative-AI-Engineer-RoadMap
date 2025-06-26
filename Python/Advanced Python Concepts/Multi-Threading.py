from concurrent.futures import ThreadPoolExecutor
from this import d
import threading
import time

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
def main():
    # Normal Code
    func(4)
    func(2)
    func(1)

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])

    t1.start()
    t2.start()
    t3.start()


def poolingDemo():
    # Taken the method from concurrent.futures
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())


poolingDemo()