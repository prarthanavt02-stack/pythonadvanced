# def add():
#     n1=int(input('Enter a number'))
#     n2=int(input('Enter a number'))
#     s=n1+n2
#     print('sum',s)
#
# def sub():
#     n1 = int(input('Enter a number'))
#     n2 = int(input('Enter a number'))
#     s = n1-n2
#     print('difference', s)
#
# def mul():
#     n1 = int(input('Enter a number'))
#     n2 = int(input('Enter a number'))
#     s = n1*n2
#     print('product', s)
#
# def div():
#     n1 = int(input('Enter a number'))
#     n2 = int(input('Enter a number'))
#     s = n1/n2
#     print('quotient', s)
#
# while(True): #Infinite loop
#
#     print('1.Add')
#     print('2.Sub')
#     print('3.Mul')
#     print('4.Div')
#     print('5.Exit')
#
#     ch=int(input('Enter the number'))
#
#     if ch==1:
#         add()
#     elif ch==2:
#         sub()
#     elif ch==3:
#         mul()
#     elif ch==4:
#         div()
#
#     else:
#         exit()



# file read
#file write
#file append
#file search
#file delete
#exit


def file_read():
    filename=input('Enter the filename')

    f=open(filename,'r')
    content=f.read()
    print(content)
    f.close()

def file_write():

    filename=input('Enter the filename')
    f=open(filename,'w')
    content=input('Enter the content')
    f.write(content)
    f.close()

def file_append():

    filename=input('Enter the filename')
    f=open(filename,'a')
    content=input('Enter the content')
    f.write(content)
    f.close()


def file_search():
    filename = input("Enter the filename: ")
    word = input("Enter the word to search: ")

    f = open(filename, 'r')
    content = f.read()

    if word in content:
        print("Word found")
    else:
        print("Word not found")

    f.close()

def file_delete():
    filename = input("Enter the filename: ")

    import os
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted")
    else:
        print("File not found")


while True:

    print("1. File Read")
    print("2. File Write")
    print("3. File Append")
    print("4. File Search")
    print("5. File Delete")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        file_read()

    elif ch == 2:
        file_write()

    elif ch == 3:
        file_append()

    elif ch == 4:
        file_search()

    elif ch == 5:
        file_delete()

    elif ch == 6:
        print("Program ended")
        break

    else:
        exit()
