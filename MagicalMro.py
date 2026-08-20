
# -----------------Magical Method---------------

class magical:
    lentgh = 8;

    def __init__(self, lentgh):
        self.lentgh = lentgh


    def __len__(self):
        return self.lentgh

    def __add__(self, other):
        return other.value + other.value

    def __sub__(self, other):
        print(self.lentgh - other.lentgh)

    def __str__(self):
        return "AKSHAY"


m1 = magical(3)
print(len(m1))
#print(add(10, 10))

m2 = magical(5)
m1 - m2

M3 = magical()
print(M3)


# -----------------Method resolution Order---------
# **************Example 1*************
class Car:
    def start(self):
        print("Car Started")


class Bike:
    def start(self):
        print("Bike Started")


class Vehicle(Bike, Car):  # its MRO squance change output change
    print("Vehicle Started")  # in mro no need create object of device t
    # the call automatacally


obj=Vehicle()
obj.start()


# *******************Example 2 *************


class Mobile():
    def ButtonTouch(self):
        print('Mobile ButtonTouch')


class Tv(Mobile):
    def ButtonTouch(self):
        print('Tv ButtonTouch')


class Computer(Mobile):
    def ButtonTouch(self):
        print('Computer Button Touch')


class Device(Computer, Tv):#object call as per sequance of mro
    print("Device Started")  # in mro no need create object of device t
    # the call automatacally


device = Device()
device.ButtonTouch()
#Device.mro()

# ------------Property Decorators-------------

class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value > 0:
            self._age = value
        else:
            print("Invalid age")

    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

s = Student(25)

print(s.age)
del s.age
print(s.age)# because of this age attrabuite is delet used delet property
# s.age = 23
# print(s.age)
