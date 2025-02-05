class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age
       
        
    def __str__(self):
        return ("name is {0} and age is {1}".format(self.name, self.age))
s1= Student("Aditi", 21)
print(s1)

        