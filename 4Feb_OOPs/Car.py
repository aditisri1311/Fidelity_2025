#Make a class 'car' with attributes/Parameters name, colour, model. There are 2 instance methods which shows the model name and colour.Employee is another class with employee name, employee id and car, car is the object of car object in the previous class. 
class car:
    def __init__(self, name, colour, model):
        self.name = name
        self.colour = colour
        self.model = model

    def show_model(self):
        print(f"Car Model: {self.model}")

    def show_colour(self):
        print(f"Car Colour: {self.colour}")
class Employee:
    def __init__(self, emp_name, emp_id, car):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.car = car 

    def show_employee_details(self):
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee's Car: {self.car.name}")
        self.car.show_model()  
        self.car.show_colour() 
         
#Creating a car object
car1= car("WagonR", "Black", "2025")
employee1= Employee("Aditi", 767, car1) #association with car obj
employee1.show_employee_details()
