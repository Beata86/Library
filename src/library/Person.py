class Person():
    def __init__(self, name, surname, sex, age, height):
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age
        self.height = height

    def getFullName(self):
        return self.name + " " + self.surname

    def getMessage(self):
        return "My name is {}, my surname is {}, i.m a {}, i'm {} years old, my height is {}".format(self.name, self.surname, self.sex, self.age, self.height)
