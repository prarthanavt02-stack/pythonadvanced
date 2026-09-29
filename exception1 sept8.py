#sum of two numbers

# try:
#     n1=int(input('Enter number'))
#     n2=int(input('Enter number'))
#
#     s=n1+n2
#
# except:
#     print('Invalid number')
#
# #optonal
# else:
#     print('sum',s)
#
# finally:
#     print('done')



try:
    n1=int(input('Enter number'))
    n2=int(input('Enter number'))
    r=n1/n2
    print('Result',r)#instead r if R is name error
except ZeroDivisionError:
    print('Zero division Error')

except ValueError:
    print('ValueError')

except:#general code if any exception other than above two
    print('Error')