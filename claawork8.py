# #write a program to read a text file and displays the number of lines in a file

#readlines()#list

# f=open('k.txt','r')
#
# print("number of lines:",len(f.readlines()))
# f.close()

# # #write a program to display the number of words in a file

#read()#string

# f=open('k.txt','r')
#
# data=f.read()
#
# words=data.split()
#
# print('number of words',len(words))
# f.close()

# # #write a program to update the second line in a file

# f=open('k.txt','r')
# s=f.readlines()
# print(s)
#
# s[1]='updated the second line\n'
# f.close()
#
# f=open('k.txt','w')
# f.writelines(s)
# f.close()


# # #write a program to display the last 5 lines in a file

f=open('k.txt','r')
s=f.readlines()

print(s[-5:])

# #program to search a particular word in a file
f=open('k.txt','r')
s=f.read()
if ('python in s'):
    print('word is present')
else:
    print('not present')





# #find the number of letters,digits,and spaces in a file

f=open('k.txt','r')
s=f.read()

l_count=0



#reverse the lines in a file


# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #