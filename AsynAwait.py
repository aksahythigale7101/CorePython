
import asyncio
from turtle import reset




async def task1():
    print("Task 1 Start")
    await asyncio.sleep(4)
    print("Task 1 Complete")
    return "Task 1 Result"
    # for i in range(1, 6):
    #     await asyncio.sleep(0.5)
    #     print(i)
    
   

async def  PYRAMID():
    for i in range(1,6):
        print("\n")
        for j in range(0,6-i):
            print(" ",end=" ")
            await asyncio.sleep(0.3)
        for k in range(0,2*i-1):
            print("*",end=" ")
            await asyncio.sleep(0.5)




async def task2():
    print("task 2 start")
    await asyncio.sleep(8)
    print("task 2 complete")
    return "Task 2 Result"

#print("Main Thred Start")
#asyncio.run(task1())
#print("Main Thred Finshed")
#asyncio.run(PYRAMID())


# #----------------without Create_task-----------------
# print("________________Normal Await___________________")
# asyncio.run(task1())
# asyncio.run(task2())



#____________create task______________
async def CreateTask():
    t1=asyncio.create_task(task1())
    t2=asyncio.create_task(task2())

    result1=await t1
    print("I got Task 1 result:", result1)
    result2=await t2
    print("I got Task 2 result:", result2)

print("__________Created_task________________")
asyncio.run(CreateTask())   



print("__________gather________________")


async def GATHER():
   results= await asyncio.gather(task1()
                         ,task2())

   print("All results:", results)



asyncio.run(GATHER())








  


