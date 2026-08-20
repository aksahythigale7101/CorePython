


class single_Star():
    def simpleFunction(a,b):
       print("Addition of Two Parameter:", a+b)
      
    def argsKwyword(*args):
     print("argument-",args[0])
    

class double_Star():
    def argsData(**emp_detiles):
        print(emp_detiles)
     








class my_class(single_Star,double_Star):
    pass




a=my_class
print("____________________Simple Function_____________________")
a.simpleFunction(10,20)
#a.simpleFunction(10,20,40)# not allowed because function take two parameter
print("____________________*args_____________________")
a.argsKwyword(10,20,30,40)

print("____________________**kwargs__________________")
employe=[
   {
    'Name': 'Akshay',
    'age': 25,
    'city': 'Pune',
    'salary': 50000
   },
   {
    'Name': 'Aditya',
     'city': 'Pune',
    'salary': 80000

   }
]

a.argsData(**employe[1])




