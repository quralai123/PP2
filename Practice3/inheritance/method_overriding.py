# method_overriding.py

# example1
# Task 1: Basic method overriding
class Person:
    def greet(self):
        print("Hello from Person!")

class Student(Person):
    def greet(self):
        print("Hello from Student!")

p1 = Person()
p1.greet()  # Calls Person's greet
s1 = Student()
s1.greet()  # Calls Student's greet


# example2
# Task 2: Using super() in overridden method
class Person:
    def greet(self):
        print("Hello from Person!")

class Student(Person):
    def greet(self):
        super().greet()  # Call the parent method
        print("Hello from Student!")

s1 = Student()
s1.greet()


# example3
# Task 3: Overriding __str__() method
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __str__(self):
        return f"Student name: {self.name}"

s1 = Student("Alice")
print(s1)


# example4
# Task 4: Overriding method with additional parameters
class Person:
    def introduce(self, greeting):
        print(greeting, "I am a person.")

class Student(Person):
    def introduce(self, greeting):
        print(greeting, "I am a student.")

s1 = Student()
s1.introduce("Hi!")  # Calls overridden method


# example5
# Task 5: Overriding method and combining parent functionality
class Person:
    def info(self):
        print("I am a person.")

class Student(Person):
    def info(self):
        super().info()  # Call parent's info
        print("I am also a student.")

s1 = Student()
s1.info()
