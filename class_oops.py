# class Person:
#
#     def __init__(self,n,a):
#
#
#
#         self.name=n
#         self.age=a
#
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person("arun",23)
#
#
# p2=Person("amal",24)
#
# p1.show()
#
# p2.show()


#dynamically

# class Person:
#
#     def __init__(self,n,a):
#
#
#
#         self.name=input('Enter the name')
#         self.age=int(input('Enter the age'))
#
#     def show(self):
#         print(self.name,self.age)
#
# p1=Person()
#
#
# p2=Person()
#
# p1.show()
#
# p2.show()



#define a class named employee with attributes emp id,name,age,place,salary,designation and methods
#gets salary () and showpersonaldetails()
#create an Employee Object and call the methods


# class Employee:
#
#     def __init__(self):
#
#         self.empid=int(input('Enter the empid'))
#         self.name=input('Enter the name')
#         self.age=int(input('Enter the age'))
#         self.place=input('Enter the place')
#         self.salary=input('Enter the salary')
#         self.designation=input('Enter the designation')
#
#     def getsalary(self):
#         print('salary',self.salary)
#     def showpersonaldetails(self):
#         print('name',self.name,'age',self.age,'place',self.place)
#
# e=Employee()
#
# e.getsalary()
# e.showpersonaldetails()


#define a class named student with attributes roll no, name,mark1,mark2,mark3,and methods display()
#to display roll no and total mark of a student.
#create 2 student objects and call the methods.


# class Student:
#
#     def __init__(self):
#
#         self.rollno=int(input('Enter the roll no'))
#         self.name=input('Enter the name')
#         self.mark1=int(input("Enter mark1"))
#         self.mark2 =int(input("Enter mark2"))
#         self.mark3 =int(input("Enter mark3"))
#
#     def display(self):
#         total = self.mark1 + self.mark2 + self.mark3
#         print("Roll No:", self.rollno)
#         print("Total Mark:", self.total)
#
# s1=Student()
# s1.display()
#
# s2=Student()
# s2.display()


#define a class named book with attributes title,author,price,pages,language, and methods gettitle(),getauthors(),getprice()
#setitile(),setauthor(),setprice()
#create book object and call the methods

class Book:

    def __init__(self):

        self.title=input('Enter the title')
        self.author=input('Enter the author')
        self.price=int(input('Enter the price'))
        self.pages=int(input('Enter the pages'))
        self.language=input('Enter the language')

    def gettitle(self):
        print(self.title)

    def getauthor(self):
        print(self.title)

    def getprice(self):
        print(self.title)

    def settitle(self):
        self.title=input("Enter the new title")
        self.gettitle()
    def setauthor(self):
        self.author=input("Enter the new author")
        self.getauthor()
    def setprice(self):
        self.price=input("Enter the new price")
        self.getprice()


b=Book()
b.gettitle()

b.settitle()



l=[a1,a2]


for i in l:
    #print(i.acctnumber,i.acctname,i.balance)
    i.showbalance()

for i in l:
    if(i.acctnumber==123):
        i.showbalance()








