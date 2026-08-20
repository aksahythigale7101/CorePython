# ---------------Inheritance----------

class Car:

    def __init__(self, CC):  # single parmeter pass
        print('Brand: ', CC)

    def Show(self):
        print("Hyndai is Seadn Car")


class Model(Car):

    def __init__(self, Power, Gears):  # 2 paramter pass
        super(Model, self).__init__(Power)  # this keyword is used both constructor calls
        print('4x4: ', Power, " Geras: ", Gears)

    def Display(self):
        print("Hyndai is Verana is My Fav Car")

    def Show(self):
        super(Model, self).Show()  # this achive by using super keyword is calles as METHID OVERRIDING
        print("Hyndai is Grand i10 Sprtz")


#
# M=Model()
# M.Show() # parent Class
# M.Display() # child class

M1 = Model("1000", 5)
M1.Show()  # METHID OVERRIDING In this scenro show method in both the class but it calls child clss

# M2 = Model("1000", 5)  # both the constructe paramter are different but no problem happend
# M2.Display()  #
# M2.Show()
