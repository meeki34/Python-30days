# class methods = Allow operation related to the class itself
#                 Take (cls) as the first parameter
#                 Can be called without creating an instance of the class
#                 Can be used to create instances of the class
#                 Can modify a class state that would apply to all instances of the class

class Student:
    count = 0
    Total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.Total_gpa += gpa

# this instance method is used to create instances of the class
    def get_info(self):
        print(f"{self.name} has a gpa of {self.gpa}")

    @classmethod
    def get_count(cls):
        return f"Total * of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        return f"Average gpa: {cls.Total_gpa / cls.count:.2f}"
    
    @classmethod
    def create_instance(cls,name,gpa):
        return cls(name,gpa)

s1 = Student("John",3.5)
s2 = Student("Jane",3.8)
s3 = Student("Jack",3.2)
print(Student.get_count())
print(Student.get_average_gpa())
print(Student.create_instance("Jill",3.9).get_info())