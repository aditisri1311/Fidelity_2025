class Employee:
    def __init__(self, name, emp_id, dept):
        self.name = name
        self.id = emp_id
        self.dept = dept
    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.id}")
        print(f"Department: {self.dept}")
class Department(Employee):
    def __init__(self, name, emp_id, dept, dept_name, dept_id):
        Employee.__init__(self, name, emp_id, dept)
        self.dept_name = dept_name
        self.dept_id = dept_id

    def display(self):
        emp = Employee(self.name, self.id, self.dept)
        emp.display()  
        print(f"Department Name: {self.dept_name}")
        print(f"Department ID: {self.dept_id}")
if __name__ == "__main__":
    emp = Employee("Aditi ", 101, "SDE")
    emp.display()
    dept = Department("Ritika", 107, "HR", "Human Resources", "HR001")
    dept.display()