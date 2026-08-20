import threading
import time


lock1 = threading.Lock()
lock2 = threading.Lock()

#"Thread 1 is waiting, so Thread 2 should continue."
def task1():

    print("Thread 1: Trying Lock 1")

    with lock1:

        print("Thread 1: Got Lock 1")

        time.sleep(1)

        print("Thread 1: Trying Lock 2")

        with lock2:

            print("Thread 1: Got Lock 2")


def task2():

    print("Thread 2: Trying Lock 2")

    with lock2:

        print("Thread 2: Got Lock 2")

        time.sleep(1)

        print("Thread 2: Trying Lock 1")

        with lock1:

            print("Thread 2: Got Lock 1")


# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)


# t1.start()
# t2.start()



# join() means:
# Main thread, wait until Thread 1 finishes.
# But Thread 1 will never finish because it's deadlocked.
# t1.join()
# t2.join()

# t1.stop()
# t2.stop()
# print("Main completed")


#__________________________________________________________
#     deadLock Prevent or stop
#__________________________________________________________
def task1():

    lock1.acquire()

    try:

        print("Thread 1 got Lock 1")

        time.sleep(1)

        print("Thread 1 trying Lock 2")

        if lock2.acquire(timeout=2):

            try:
                print("Thread 1 got Lock 2")

            finally:
                lock2.release()

        else:
            print("Thread 1: Could not get Lock 2")

    finally:
        lock1.release()


def task2():

    lock2.acquire()

    try:

        print("Thread 2 got Lock 2")

        time.sleep(1)

        print("Thread 2 trying Lock 1")

        if lock1.acquire(timeout=2):

            try:
                print("Thread 2 got Lock 1")

            finally:
                lock1.release()

        else:
            print("Thread 2: Could not get Lock 1")

    finally:
        lock2.release()


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Main completed")

