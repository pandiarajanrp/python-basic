class Animal:
    animal_type: str
    height: float
    weight: float

    def eat(self):
        print("Animal Eating")

    def walk(self):
        print("Animal Walking")


class Dog(Animal):
    dog_type: str

    def chasing(self):
        print("Dog Chasing")


class Bird(Animal):
    bird_type: str

    def eat(self):
        print("Bird Eating")

    def fly(self):
        print("Bird Flying")


dog = Dog()
dog.eat()
dog.walk()
dog.chasing()


bird = Bird()
bird.eat()
bird.fly()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)
        self.degree = degree

    def get_details(self):
        print(
            f"""
          Student Details
          Name: {self.name}
          Age: {self.age}
          Degree: {self.degree}
          """
        )


student = Student("Pandiarajan", 40, "B.Tech")
student.get_details()
