class Student:
    def __init__(self):
        self.name = "Steve"
        self.age = 40 #name and age can be used without declaring. #declaring the variable dynamically is allowed
    def dsp(self): #instance method
        print(self.name, self.age)
s = Student()
s.dsp()

  