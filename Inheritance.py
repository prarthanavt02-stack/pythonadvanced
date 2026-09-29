class Parent:

    def m1(self):
        print('In Parent class method m1')

    def m2(self):
        print('In Parent class method m2')

# p=Parent()
# p.m1()
# p.m2()


class Child:
    pass

c=Child()
c.m1()
c.m2()#error



class Child(Parent):
    pass

c=Child()
c.m1()
c.m2()



class Child(Parent):
    def m3(self):
        print('In child Class m3')


c=Child()
c.m1()
c.m2()
c.m3()



class Child(Parent):

    def m1(self):
        super().m1()
        print('In child class m1')
    def m3(self):
        print('In child class m3')

c= Child()
c.m1()
c.m2()
c.m3()




