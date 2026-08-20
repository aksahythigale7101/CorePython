


class my_class:

    def show(self):
        numbers = [1, 2, 3, 4, 5]  # thisis Iterable
        print("------------------------Normal List----------------")
       # print(numbers[2]) # can access any index coz data store on index
        print(numbers)

    def ChekItrator(self):
        num = [10, 20, 30, 40, 50, 60] 
        print("------------------------iterator List---------------")
        _itrtor = iter(num) # this is Iterator
        self.display(self,_itrtor)
        # print(next(_itrtor[2]))#can not access   coz data store on memory as refrance
        # print(_itrtor)
        # for value in _itrtor:
        #  print(value)

    def display(self, itrator):
        # print(next(itrator))
        # print(next(itrator[3]))##not work beacuse they dont know index they stor refrance
        # for i in range(3):
        #     value = next(itrator)

        # print(next(itrator))
        iterator = iter(range(5))


        while True:
          try:
            i = next(iterator)
            print(f"Iterator number: {i + 1}")
          except StopIteration:
            break


    def CheckGenertor(self, stopNum):
         print("------------------------Genertor List---------------")
         for i in range(stopNum):
            yield i + 1 #Generator ?? ????? ?????? ????; Generator ?? Python ?? automatically ???? ?????? Iterator ???.

    def Method(self):
        
        OBJ = self.CheckGenertor(self,5)
        
        print(f"Genertor number: {next(OBJ)}")# we can write self
        print(f"Genertor number: {next(OBJ)}")
        print(f"Genertor number: {next(OBJ)}")
      

        

mc=my_class
mc.show(mc)
mc.ChekItrator(mc)

mc.Method(mc)


