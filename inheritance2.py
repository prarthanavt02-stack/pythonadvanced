#Initialisation

# class Person:
#
#     def __init__(self):
#
#         self.name=input('Enter name')
#         self.age=int(input('Enter age'))
#
# class Student(Person):
#
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input('Enter roll number'))
#         self.course=input('Enter course')
#         self.mark=int(input('Enter mark'))
#
# s=Student()


#show function


# class Person:
#
#     def __init__(self):
#
#         self.name=input('Enter name')
#         self.age=int(input('Enter age'))
#
#     def show(self):
#         print(self.name,self.age)
#
# class Student(Person):
#
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input('Enter roll number'))
#         self.course=input('Enter course')
#         self.mark=int(input('Enter mark'))
#
#     def show(self):
#         super().show()
#         print(self.rollno,self.course,self.mark)
#
#     def updatemark(self):
#         self.mark=int(input('Enter mark'))
#
#
# s=Student()
# s.show()
# s.updatemark()




# class Company:
#
#     def __init__(self):
#
#         self.company_name=input('Enter company name')
#         self.location=input('Enter location')
#
#     def display_company(self):
#         print(self.company_name,self.location)
#
# class Employee(Company):
#
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input('Enter employee id'))
#         self.name=input('Enter name')
#         self.designation=input('Enter designation')
#         self.salary=int(input('Enter salary'))
#
#     def display_details(self):
#         super().display_company()
#         print(self.empid,self.name,self.designation,self.salary)
#
#     def update_salary(self):#increments by 10%
#          self.salary=1.1*self.salary
#          print('Updated salary',self.salary)
#
#
#
# e=Employee()
# e.display_details()
# e.update_salary()








class Category:

    def __init__(self):

        self.category_name=input('Enter category name')

    def show_category(self):
        print(self.category_name)

class Product(Category):

    def __init__(self):
        super().__init__()
        self.product_name = input('Enter product name')
        self.price=int(input('Enter price'))
        self.quantity=int(input('Enter quantity'))

    def total_price(self):

         total_price= self.price * self.quantity
         print(total_price)


p=Product()
p.total_price()
p.show_category()

