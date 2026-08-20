# ---------------Poloymorphism------------------
# ***Example1***
class Device():
    def ButtonTouch(self):
        print('Mobile ButtonTouch')


class Tv(Device):
    def ButtonTouch(self):
        print('Tv ButtonTouch')


class Computer(Device):
    def ButtonTouch(self):
     print('Computer Button Touch')


device1 = [Tv(),Computer()]

for device in device1:
    print(device.ButtonTouch())


# ***Example 2***
# Duck Typing
class Tv():
    def ButtonTouch(self):
        print('Tv ButtonTouch')


class Computer():
    def ButtonTouch(self):
        print('Computer Button Touch')


def Electroinic(device):
    device.ButtonTouch()


Electroinic(Tv())
Electroinic(Computer())

print("-------------------------------------")


# Example 3
class Car:
    def start(self):
        print("Car Started")


class Bike:
    def start(self):
        print("Bike Started")


class Generator:
    def start(self):
        print("Generator Started")


def start_device(device):
    device.start()


start_device(Car())
start_device(Bike())
start_device(Generator())