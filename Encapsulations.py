# 5---------------Encapsulations--------------

class Bank:
    ifsc = "COSD000457"  # public
    _BankCode = "COS411043"  # protected
    __Debt = 100000000  # private

    # def Show(self, ifsc, BankCode, debt):
    #     Debt = int(debt)
    #     print("Bank Details", self.ifsc, BankCode, Debt)

    def ShowPrivate(self):
        print("Private: ",self.__Debt)

    def _calculateInterest(self):
        print("Calculate Interest")


    def __checkPin(self):
        print("Checking PIN")


COSMOS = Bank()
print(COSMOS.ifsc);
print(COSMOS._BankCode)
COSMOS.ShowPrivate()#Call private variable
print(COSMOS._Bank__Debt)# this is a Name Mangling...using COSMOS._BANK through access private variable
# print(COSMOS.__Debt);# 'Bank' object has no attribute '__Debt' beacuse acces private vaiable
# COSMOS.ifsc="COSD000460";
# COSMOS.BankCode="COS410505"
# COSMOS.Debt=111000000
#COSMOS.Show("COSD000460", "COS410505", 111000000)
COSMOS._calculateInterest()##private method
COSMOS.__checkPin()#not access beacuse private method
COSMOS._Bank__checkPin()#acess beacuse name mangling private
