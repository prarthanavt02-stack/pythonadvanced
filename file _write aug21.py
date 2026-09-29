#write

f=open("k.txt","w")


#write(string)

# f.write("hello\n")
# f.write("python\n")
# f.write(""" It is a long established fact that a reader will be
# distracted by the readable content of a page when looking at its layout.
# he point of using Lorem Ipsum is that it has a more-or-less normal distribution
# of letters, as opposed to using 'Content here, content here', making it look
# like readable English.""")
# f.close()


#writelines(list)

f.writelines(['python\n','world\n','hi\n','python\n'])

f.close()
