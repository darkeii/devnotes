# class variables = Shared among all instances (objects) of a class
#                     defined outside the constructor
#                     Allow you to share data among all the objects created in that class

class Student:

    session_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name= name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 45)


# print(student1.session_year)                #calling out class variable through an instance(object) is bad practice
print(Student.session_year)                   # should call an class variable through class name (bcz its common for all instances(objects)
print(Student.num_students)

print(f"My graduating class of {Student.session_year} had {Student.num_students} students")