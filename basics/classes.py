#Basic class
class Student:
  "This is student class doc string"
  name="Pandiarajan"
  age="30"

  def printDetails(self):
    print(f"Student name is {self.name} and age {self.age}")

student = Student()

#access class attributes
print(Student.name)

#access class attributes
print(student.age)

#access doc strings
print(Student.__doc__)

student.printDetails()


#with constructor
class Teacher:
  "This is teacher class doc string"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printDetails(self):
    print(f"Teacher name is {self.name} and age {self.age}")

teacher = Teacher("Rajagopal", 55)
teacher.printDetails()

#change property
teacher.name = "Jeyarani"
teacher.printDetails()

#delete property
teacher.city = "Madurai"
print(teacher.city)
del teacher.city
print(teacher.city)

