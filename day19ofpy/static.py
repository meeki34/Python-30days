#static method = A method which is bound to a class rather than its object.
#                We can call it using class name also.
#                We use @staticmethod decorator for declaring static method.

#Instance methods = best for operation on instance of the class (object)
#Class methods = best for operation on class (class variable)
#Static methods = best for utility function (helper function)

class Employee:
    def __init__(self, name,position):
        self.name = name
        self.position = position

    def get_info(self):
        print(f"{self.name} is a {self.position}")

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Developer","Cleaner"]
    
        return position in valid_positions
Employee1 = Employee("John","Manager")
Employee2 = Employee("Jack","Developer")
Employee3 = Employee("Jack","Cleaner")
print(Employee1.get_info())
print(Employee2.get_info())
print(Employee3.get_info())
print(Employee.is_valid_position("Developer"))
print(Employee.is_valid_position("Manager"))
