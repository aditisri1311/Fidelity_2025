'''
class Student:
    __a = 10 #private class 
    def dsp(self):
        print(self.a)
    @classmethod
    def m1(cls):
        print(cls.a)
s= Student()
Student.m1()


'''
class P:
    a= 10
    def __init__(self):
        self.b =20
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Class method")
    @staticmethod
    def m3():
        print("Static method")
class C(P):
    pass
c =C()
print(c.a)
c.m3()