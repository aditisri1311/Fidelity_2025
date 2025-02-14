class Person:
    def __init__(self, name, age, id):
        self.name= name
        self.age= age
        self.id = id
    def getinfo(self):
        return(self.name, self.age, self.id) #Return tuple of details
class Employee(Person):
    def __init__(self, name, age, id, sal): #calls parent class constructor
        self.salary = sal
        super().__init__(name, age, id)
    def dsp(self):
        print(super().getinfo(),self.salary)
#Creating the object
emp1 = Employee("Aditi", 21, 785767, 24000)
# Display Employee Information
emp1.dsp()
