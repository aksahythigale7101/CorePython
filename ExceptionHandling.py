#-------------try except------------------------
class Calculations:
    result=0;
    def Display(self,number):# handle error using try and except
        try: # write all code
         self.result=10/number
         print(self.result)
        except Exception as ex: # get when error occured this block work
         print(ex)
        else: # when no error occured it runs
         print("Result:", self.result)
        
         # raise # this blaock give error throw when you want
         # print("Get error")
         
         

        finally:# this blaock always work
            print("Executaion is Complete")
    
   
print("-----------Excepction Handling-----------------")    
cal=Calculations()
cal.Display(1)  
print("-------------------")
cal.Display(0)

