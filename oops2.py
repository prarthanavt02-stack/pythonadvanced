# Write a menu driven code for Bank Operators
#create class and list.
#1.create a new account
#2. withdraw
#3.deposit
#4.showbalance
#5.exit

class Account:

    def __init__(self):

        self.acctname=input('Enter account name')
        self.acctnumber=int(input('Enter the account number'))
        self.balance=int(input('Enter the balance'))

    def showbalance(self):
        print('current balance',self.balance)

    def withdraw(self):
        amount=int(input('Enter the amount'))

        if(amount>self.balance):
            print('insufficient balance')
        else:

            self.balance=self.balance-amount

            self.showbalance()

    def deposit(self):
        amount = int(input('Enter the amount'))

        self.balance = self.balance+amount

        self.showbalance()
#
# l=[]
#
# while True:
#     print('1.Create a New Account')
#     print('2.withdrwa')
#     print('3.deposit')
#     print('4.showbalance')
#     print('5.exit')
#
#     ch=int(input('Enter your choice'))
#
#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)
#
#     elif ch==2:
#
#         number = int(input('Enter account number'))
#
#         for i in l:
#             if (i.acctnumber==number):
#                 i.withdraw()
#                 break
#
#         else:
#             print('Account not found')
#
#     elif ch==3:
#
#         number = int(input('Enter account number'))
#
#         for i in l:
#             if(i.acctnumber==number):
#                 i.deposit()
#                 break
#         else:
#             print('Account not found')
#
#     elif ch==4:
#
#         number = int(input('Enter account number'))
#
#         for i in l:
#             if (i.acctnumber==number):
#                 i.showbalance()
#                 break
#
#         else:
#             print('Account not found')
#
#     else:
#         exit()



#Write a menu-driven Python program using a class Student
#to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.



class Student:

    def __init__(self):

        self.rollno=int(input('Enter the roll number'))
        self.name=input('Enter the name')
        self.marks=int(input('Enter the marks'))

    def display(self):
        print("Roll No", self.rollno)
        print("Name", self.name)
        print("Marks", self.marks)

l=[]

while True:
    print('1.Add Student')
    print('2.Update Mark')
    print('3.Display All Student Details')
    print('4.Search Student by Roll Number')
    print('5.Delete Student')
    print('6.Exit')


    ch=int(input('Enter the choice'))

    if ch==1:
        a=Student()
        l.append(a)
        print(l)


    elif ch==2:
        roll_no = int(input("Enter roll number"))

        for i in l:
            if i.rollno==roll_no:
                i.mark = int(input("Enter new mark"))
                print("Mark Updated")
                break
        else:
            print("Student not found")


    elif ch==3:
        if len(l) == 0:
            print("No students found")

        else:
            for i in l:
                i.display()

    elif ch==4:

        roll_no = int(input("Enter roll number"))

        for i in l:
            if i.rollno == roll_no:
                i.display()
                break
        else:
            print('student not found')


    elif ch==5:

        roll_no = int(input("Enter roll number"))

        for i in l:
            if i.rollno == roll_no:
                l.remove(i)
                print('delete student')
                break

        else:
            print('student not found')

    elif ch==6:

        exit()









