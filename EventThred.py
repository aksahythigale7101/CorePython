import threading
import time

event = threading.Event()


def worker():
    print("Worker: Waiting...")
    
    event.wait()       # Worker waits here
    
    print("Worker: Started!")


t1 = threading.Thread(target=worker)

t1.start()     #start() केल्यावर कोणता Thread आधी execute होईल हे तुम्ही guarantee करू शकत नाही.
               #कारण Thread ला CPU कोणत्या क्षणी मिळेल हे Thread Scheduler ठरवतो.

print("Main: Doing some work...")#आता Main Thread आणि Worker Thread दोघे run होऊ शकतात.
                                 #तुमच्या case मध्ये Main Thread ला आधी CPU मिळाला:
time.sleep(3)

print("Main: Now start the worker")
event.set()            # Signal worker to continue

t1.join()

print("Main: Completed")

class my_class(object):
    pass



#Thred Calling FlowChart

# start() → Thread सुरू करण्यासाठी सांगतो
#           ↓
# Scheduler ठरवतो कोण आधी चालेल
#           ↓
# wait() → signal येईपर्यंत थांब
#           ↓
# set() → signal दे
#           ↓
# join() → Thread पूर्ण होईपर्यंत Main थांब
