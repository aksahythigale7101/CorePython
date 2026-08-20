class car:
    def Brand(self, brand):
        print('Brand l: ', brand)

    def Mmodel(self, model):
        print('Mmodel: ', model)

    def colour(self, colour):
        print('Colour: ', colour)


# c1 = car()
# c1.Brand("Honda")
# c1.Mmodel("Honda City")
# c1.colour("blue")


class Students:
    numbers = 10

    def Age(self, age):
        print('Age: ', age)

    def ChecKnumbers(self, numbers):
        if numbers < self.numbers:
            print('Checking Default numbers', numbers)
        else:
            print("Paramter Numbers", numbers)

    def Marks(self):
        print("Marks")


# s1 = Students()
# s1.Age(20)
# s1.ChecKnumbers(5)
# s1.Marks()

class _students:
    rollNUm = 0
    name = ""
    marks = 0

    def attched(self, rollnum, name, marks):
        self.rollNUm = rollnum
        self.name = name
        self.marks = marks
        return (rollnum, name, marks)

    def average(self):
        return sum(self.marks) / len(self.marks)


# _students = _students()
# print(_students.attched(7, "Akshay", [10, 20, 30, 40, 50]))
# print(_students.average())

# ---------constructor------------------

class Book:

    def __init__(self, title, price, Author):
        print('Title: ', title)
        print('Price: ', price)
        print('Author: ', Author)

    def __init__(self, title, price):  # paremter are not same
        print('Title: ', title)
        print('Price: ', price)


# B1=Book("History", "100","Akshay")
# B1.__init__("AA",10,"Akshay")  # we can create many constructo with same paramter
# B1.__init__("BB",1200)##not working beacuse paremter are not same

class Enginerring:
    collageName = "Navsahydri"
    marks = 0
    Rank = 0;


#
#     def __init__(self, fee, collageName, cuttoff):  # , Rank
#         print('Fee: ', fee)
#         # self.collageName = collageName
#         collageName = collageName
#         self.marks = cuttoff
#         # self.Rank = Rank
#         self.Rank = int(input("Enter Rank: "))
#         # print('Collage name: ', self.collageName)#Navshaydri
#         # print('Collage name: ', collageName)  # PICTE
#
#     def GetData(self):
#         print('CollageName: ', self.collageName)
#         if (self.marks > 80):
#             print("This is good Marks")
#         elif (self.marks > 50 and self.marks < 80):
#             print("This is average Marks")
#         else:
#             print("This is bad Marks")
#
#         match self.Rank:
#             case 1:
#                 print("This is good Rank")
#             case 2:
#                 print("This is average Rank")
#             case 3:
#                 print("This is below Rank")
#
# # E1 = Enginerring(500000.50, "PICTE", 71)
# # E1.GetData()
# # print("-----------------------------")
# # E1 = Enginerring(200000, "Kj", 50)
# # E1.GetData()

# 4-----------------Class,Instance,Static Method---------------

# class House:
#     societyName = "Dilas"
#
#     flatNo = 302
#
#     def __init__(self, Location):
#         print('Name: ', Location)
#
#     def Area(self, Area):
#         print('Area: ', Area)
#
#     @classmethod
#     def ChanmgeSociety(cls):
#         print("Society Name: ", cls.societyName)
#
#     @staticmethod
#     def BuiltUparea(sqft, rate):
#         print('Total Flat prize is : ', sqft * 2800)
#
#
# H1 = House("BalajiNagar")#instance method// area,location,colour
# H1.BuiltUparea(1000,2800)#static Method///calculation
# House.ChanmgeSociety()#class Method //Clg or bank,compnay name

# they all static and class method achived by object but they statander desgine pattern
# thats why call as per code needed.
