f=open('k.txt','a+')

print('first file pointer position',f.tell())
f.write('python')

f.seek(0)
print('After file pointer position change',f.tell())
print(f.read())


f.close()

#to close text file



import os
#os.remove(filename)

os.remove('k.txt')

print('file is deleted')