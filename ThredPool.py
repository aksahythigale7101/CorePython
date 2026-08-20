from concurrent.futures import ThreadPoolExecutor
import time
import threading

def work(number):

    print("Starting:", number)

    time.sleep(2)

    print("Completed:", number)


# with ThreadPoolExecutor(max_workers=3) as executor:  # म्हणजे maximum 3 worker threads.

#     for i in range(1, 7):

#         executor.submit(work, i)


def Send_Email(user):
    #print("Email Sending process :", user)
    thread = threading.current_thread() #सध्या कोणता thread code execute करत आहे हे मिळवण्यासाठी.
    print("User:", user)
    print("Thread Name:", thread.name)
    print("Thread ID:", thread.ident)
    print("_______Email Sending Process_______")
    time.sleep(2)

    print("Email Sending Done :", user)


user = ["Akshay", "Abhay", "Ranjeet", "Vishal", "Abhijeet", "Harsh"]

with ThreadPoolExecutor(max_workers=3) as executor:  # म्हणजे maximum 3 worker threads.
    print(threading.active_count())#सध्या किती threads active आहेत ते मिळवण्यासाठी.
    for _user in user:
        executor.submit(Send_Email, _user)

    
#print(threading.enumerate())#सध्या active असलेल्या threads ची list मिळवते.

print("-----------------------")
print("All Email Sending Done")


