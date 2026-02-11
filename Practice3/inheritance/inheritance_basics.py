# inheritance.py
# Examples of Python class inheritance

# example1
# Create a parent class Person with firstname and lastname
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Create an object of Person and call printname
x = Person("John", "Doe")
x.printname()


# example2
# Create a child class Student that inherits from Person
class Student(Person):
    pass  # No extra properties or methods yet

# Create an object of Student and call printname
x = Student("Mike", "Olsen")
x.printname()


# example3
# Add __init__() function to child class without breaking inheritance
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)  # Call parent's __init__

x = Student("Anna", "Smith")
x.printname()


# example4
# Use super() function to inherit methods and properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)  # Automatically inherits parent's __init__

x = Student("David", "Johnson")
x.printname()


# example5
# Add an additional property graduationyear to the child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year  # Additional property

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Create an object of Student and call welcome
x = Student("Mike", "Olsen", 2019)
x.welcome()
