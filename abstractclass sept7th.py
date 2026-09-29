#create an abstract class shape with abstract methods get_area() and get_perimeter().
#create two subclasses
#-Rectangle
#-Square


# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self):
#         self.length = int(input("Enter length"))
#         self.breadth= int(input("Enter breadth"))
#
#     def get_area(self):
#         print("Area",self.length*self.breadth)
#
#     def get_perimeter(self):
#         print("Perimeter",2*(self.length+self.breadth))
#
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
#
# class Square(Shape):
#
#     def __init__(self):
#         self.side = int(input("Enter side"))
#
#     def get_area(self):
#         print("Area",self.side*self.side)
#
#     def get_perimeter(self):
#         print("Perimeter",4*self.side)
#
# s=Square()
# s.get_area()
# s.get_perimeter()




#Create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.

from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self):
        self.name = input("Enter name")
        self.age = int(input("Enter age"))
        self.empid = int(input("Enter employee id"))

    @abstractmethod
    def calculate_salary(self):
        pass



class FullTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.monthly_salary = int(input("Enter monthly salary"))

    def calculate_salary(self):
        print(self.monthly_salary)


class PartTimeEmployee(Employee):

    def __init__(self):
        super().__init__()
        self.hours =int(input("Enter hours worked"))
        self.rate =int(input("Enter rate per hour"))

    def calculate_salary(self):
        print(self.hours*self.rate)






