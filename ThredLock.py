
import threading
import time



def work():
    print("Work start")
    time.sleep(2)
    print("Work is will progress")

# t1 = threading.Thread(target=work())

# t1.run() #normal method call सारखे current thread मध्ये execute होते
# t1.start()
# #print(t1.is_alive())#True-- Thread अजून चालू आहे
# t1.join()
# #print(t1.is_alive())#Fals--Thread complete झाला
# print("Work is  Complete")

#_____________________Lock__________________________


# Thread 1 → Lock 🔒
#          → Check ₹1000
#          → Withdraw ₹700
#          → Balance ₹300
#          → Unlock 🔓

# Thread 2 → Lock 🔒
#          → Check ₹300
#          → ₹300 < ₹700
#          → Insufficient

# WITHOUT LOCK → ❌ ₹-400
# WITH LOCK    → ✅ ₹300

class BankAccount:

    def __init__(self):

        self.balance = 1000

        self.lock = threading.Lock()


    def withdraw(self, amount):

        with self.lock:

            if self.balance >= amount:

                print(
                    threading.current_thread().name,
                    "Balance checked:",
                    self.balance
                )

                time.sleep(1)#Real-world race condition timing वर depend करते.

                self.balance -= amount

                print(
                    threading.current_thread().name,
                    "Withdraw:",
                    amount,
                    "Remaining:",
                    self.balance
                )

            else:

                print(
                    threading.current_thread().name,
                    "Insufficient balance"
                )


account = BankAccount()


t1 = threading.Thread(
    target=account.withdraw,
    args=(700,),
    name="Thread-1"
)

t2 = threading.Thread(
    target=account.withdraw,
    args=(700,),
    name="Thread-2"
)


t1.start()
t2.start()
# Both Work on critical section
t1.join()
t2.join()


print("Final Balance:", account.balance)
