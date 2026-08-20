




class Maths_Heleper:
    
    def Addition(self,a,b):
     return a+b

    def _protectdMethod(self):
        print("protectd Method")

    def __priveatemethod(self):
        print("Private Method")
    
    def ChekYeild(self,count):
        #return  count+1;
         yield count+1
         print("after yield:",count * 20);

    

   
   
       






   



      


class configData:
     company = "ABC"
    # Class variables
     pi=3.55 # public
     _radius=10 # protcted
     __diamter=50 # private
      
     Circumference =2 # class vairble

     def Caluclations(self,data):
      print(data)

       
     def __init__(self, name):# Constructor -> Instance variable
        self.name = name

    
     def show_name(self):# Instance method
        #print("Name:", self.name)
        print(configData.company)
        print(f"Instance Method: {self.name}")# Instance method



    
      

     @classmethod
     def change_company(cls, name):
        cls.company = name
        print(f"Change Company: {name}") # see the diffrance between what is data print when they 
        print(f"pi: {cls.pi}")


     @staticmethod
     def add(a, b):
        print(configData.company)
        return a + b 









obj=Maths_Heleper()
print("_____________Yeild_____________________")
g = obj.ChekYeild(55)   # Create generator
print(next(g))         # First next()#
#print(next(g))    ----error
try:
  next(g)
except StopIteration:# yeild can stop forcefully other wise afer yeild code is not print
   #print(type(g).__name__)
     print("Generator Finished")



print("_____________Public_____________________")
print(obj.Addition(10,20))

print("_____________Protected___________________")
print(obj._protectdMethod())

print("_____________Private Method______________")
#print(Maths_Heleper.__priveatemethod())# private method no access
obj._Maths_Heleper__priveatemethod()#Name manglaing //synax----- object_classname__method/varaible name










co =configData("Akshay")
print("_______Class Variable Access Modifire_____")
#configData.pi=100 not odfied
print(configData.pi)
print(configData._radius);
#print(confi.__diamter);# no access bcoz private variable
print(configData._configData__diamter)#Name manglaing // synax----- object_classname__method/varaible name

print("__Addition of Instance Variale and class variable__")
co.Caluclations(configData.pi+co._radius+co._configData__diamter)


print("_________Instance variable and Method_________")
print(f"Instance Varaible: {co.name}")# Instance varaible
co.show_name()


print("_________________Class method__________________")#Class data सोबत काम
configData.change_company("XYZ") 

print("________________Static method___________________")#Class शी direct relation नसलेले utility काम
print(configData.add(50,30))