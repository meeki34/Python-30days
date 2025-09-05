# class varibles = shared among all instances of a class 
        # defined outside the nonstruture
# allow you to share data among all objects created from that class

class Student:

    class_year = 2025 # class variable u can access it anywhere in the class
    # instance variables = unique to each instance of the 
    num_student = 0
    def __init__(self,name,rollno,course):
        self.name = name
        self.rollno = rollno
        self.course = course
        Student.num_student += 1
        
student1 = Student("Bro code",2342,"bca")
student2 = Student("Bro code",2342,"bca")
student3 = Student("Bro code",2342,"bca")

print(student1.name)
print(student1.rollno)
print(student1.course)
print(student1.class_year)
print(student2.class_year)
print(student3.class_year)

print(f"my graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)