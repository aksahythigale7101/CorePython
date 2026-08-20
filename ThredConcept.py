
import threading
import time


def PrintNumbers(number):
  print("Print Numbers T1 ",number)
  time.sleep(5)
  print("after 5 sec deley")
      




def Show_Numbers(number):
    print("Show Number T2 ", number)
    time.sleep(2)
    print("after 2 sec deley")
  
  




t1=threading.Thread(target=PrintNumbers,args=(100,))

t2=threading.Thread(target=Show_Numbers,args=(200,))


t1.start()

         #time.sleep(3)

t2.start()
      #time.sleep(5)


t1.join()

t2.join()


print("Main Profram Completer")









class ThredConcept(object):
    """description of class"""

# 
#     Python starts
#      |
#      ↓
# Main Thread
#      |
#      ↓
# Create print_number()
#      |
#      ↓
# Create Thread t1
#      |
#      ↓
# t1.start()
#      |
#      ├──────────────→ Thread t1
#      |                    |
#      |                    ↓
#      |             print_number(10)
#      |                    |
#      |                    ↓
#      |             Number: 10
#      |                    |
#      |                    ↓
#      |                  Finish
#      |
#      ↓
# t1.join()
#      |
#      ↓
# Wait for t1
#      |
#      ↓
# t1 finished
#      |
#      ↓
# print("Main program completed")

