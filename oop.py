#!/usr/bin/env/ python3
import abc

class Human(object):
    
    age = 0

    @staticmethod
    def sum(x,y):
        return x+y

    @classmethod
    def div(cls,x,y):
        return cls.age*x*y 

    @abc.abstractmethod
    def soul(self):
        pass

    name = ""
    age = 0
    surname = ""

    def info(self):
        print("name:",self.name)
        print("surname:",self.surname)
        print("age:",self.age)

    def __init__(self,name="NoName",age=0,surname="NoSurname"):
        self.age = age
        self.name = name
        self.surname = surname


class Employee(Human):
    company = ""
    def __init__(self, name, age, surname,company = ""):
        Human.__init__(self,name=name, age=age, surname=surname,)
        self.company=company
    
    def info(self):
        super().info()
        print("company:",self.company)
def main():
    h1 = Human()
    h1.name = "Anvar"
    h1.surname = "Gilman"
    h1.age = 28
    h1.info()
    h2 = Human(name="Oygul",surname="Abdrimova",age=13)
    h1 = h2
    h1.info()
    h2.info()
    '''полиморфизм обе переменные меняются'''
    h2.surname = ""
    h1.info()
    h2.info()
    #print(h1)
    e1 = Employee(name="Oygul",surname="Abdurimova",age="13",company ="BeeLab")
    e1.info()
    e1.driver_license="ABC"
    print(e1.driver_license)
    '''от меньшего к большему теряется все(company)'''
    e1=h1
    h1=e1
    print("-"*11)
    print(e1.info())
    print(h1.info())
    print(h1.sum(5,6))
    print(Human.sum(7,3))

    def italic(fn):
        def wrapped():
            return "<i>"+fn()+"</i>"
        return wrapped


    def makebold(fn):
        def wrapped():
            return "<b>"+fn()+"</b>"
        return wrapped

    #decorator
    di = input("Italic? (y/n)")
    bi = input("Bold? (y,n)")
    
    if di == "y":
        @italic
        def hello():
            return "Hello micros!"
        @italic
        def bye():
            return "Goodbye Micros!"
    if bi == "y":
        @makebold
        def hello():
            return "Hello micros!"
        @makebold
        def bye():
            return "Goodbye Micros!"

    #if di == "y":
    #    print(hello())
    #    print(bye())
    #else:
    #    pass
    #if bi == "y":
    #    print(hello())
    #    print(bye())


if __name__ == "__main__":
    main()