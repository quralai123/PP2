# classes_and_objects.py
# Examples of Python classes and objects

# example1
# Define a class with a property
class MyClass:
    x = 5

print("Class MyClass defined with property x = 5")


# example2
# Create an object from the class
p1 = MyClass()
print("Value of x in object p1:", p1.x)


# example3
# Delete an object
del p1
print("Object p1 deleted")


# example4
# Create multiple objects from the same class
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print("Value of x in object p1:", p1.x)
print("Value of x in object p2:", p2.x)
print("Value of x in object p3:", p3.x)


# example5
# Use pass statement in an empty class definition
class Person:
    pass

print("Empty class Person defined using pass")
