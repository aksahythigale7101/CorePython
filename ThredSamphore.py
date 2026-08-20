
from concurrent.futures import ThreadPoolExecutor
import threading
import time


semaphore = threading.Semaphore(3)


def work(number):

    print("Thread", number, "waiting...")

    with semaphore:

        print("Thread", number, "entered")

        time.sleep(3)

        print("Thread", number, "completed")


# threads = []


# for i in range(1, 7):

#     t = threading.Thread(
#         target=work,
#         args=(i,)
#     )

#     threads.append(t)

#     t.start()


# for t in threads:
#     t.join()


# print("Main completed")

#------------------------------------------------------#
#       example of semphore and Thredpool              #
#______________________________________________________#
def work(number):

    print("Thread", number, "waiting")

    with semaphore:

        print("Thread", number, "entered")

        time.sleep(2)

        print("Thread", number, "completed-----------")


with ThreadPoolExecutor(max_workers=3) as executor:

    for i in range(1, 7):

        executor.submit(work, i)