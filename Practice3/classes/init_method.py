# init_method.py
# Examples of Python __init__() method in classes

# example1
# Define a class with __init__() to assign properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Emil", 36)
print("Person p1 - Name:", p1.name, "Age:", p1.age)


# example2
# Class without __init__(), set properties manually
class Person:
    pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25
print("Person p1 - Name:", p1.name, "Age:", p1.age)


# example3
# Using __init__() to set initial values when creating the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Linus", 28)
print("Person p1 - Name:", p1.name, "Age:", p1.age)


# example4
# __init__() with default parameter values
class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)
print("Person p1 - Name:", p1.name, "Age:", p1.age)
print("Person p2 - Name:", p2.name, "Age:", p2.age)


# example5
# __init__() with multiple parameters
class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")
print("Person p1 - Name:", p1.name)
print("Person p1 - Age:", p1.age)
print("Person p1 - City:", p1.city)
print("Person p1 - Country:", p1.country)
