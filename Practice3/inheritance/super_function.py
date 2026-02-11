# super_function.py

# example1
# Task 1: Basic use of super() to call parent's __init__
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # Call parent's __init__
        self.grade = grade

s1 = Student("Alice", 10)
print("Student name:", s1.name)
print("Student grade:", s1.grade)


# example2
# Task 2: Using super() in a method to extend parent's functionality
class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()  # Call parent's greet
        print("Welcome to the student class.")

s1 = Student()
s1.greet()


# example3
# Task 3: Multiple inheritance with super()
class Person:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, subject):
        self.subject = subject

class TA(Person, Teacher):
    def __init__(self, name, subject):
        super().__init__(name)  # Calls Person.__init__() due to MRO
        Teacher.__init__(self, subject)  # Explicit call for Teacher
        print(f"TA {self.name} teaches {self.subject}")

ta1 = TA("Bob", "Math")


# example4
# Task 4: Calling parent method with super() from child method
class Person:
    def describe(self):
        print("I am a person.")

class Student(Person):
    def describe(self):
        super().describe()  # Call parent method
        print("I am also a student.")

s1 = Student()
s1.describe()


# example5
# Task 5: Using super() to manage attributes in child class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_info(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        super().show_info()  # Show brand from parent
        print("Model:", self.model)

c1 = Car("Toyota", "Corolla")
c1.show_info()
