class InvalidIDException(Exception):
    pass

class Employee:
    def __init__(self, name, emp_id, role):
        if not isinstance(emp_id, int):
            raise InvalidIDException("Employee ID must be a number.")
        if len(str(emp_id)) < 4:
            raise InvalidIDException("The ID should be more than 4 digits.")
        
        self.name = name
        self.emp_id = emp_id
        self.role = role

try:
    emp = Employee("Aditya", "123", "Software Engineer")  
except Exception as e:
    print(f"Exception: {e}")

try:
    emp_valid = Employee("Aditi Srivastava", 785767 , "Developer")  # Valid case
    print(f"Employee Created: {emp_valid.name}, {emp_valid.emp_id}, {emp_valid.role}")
except Exception as e:
    print(f"Exception: {e}")
