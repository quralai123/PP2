# class_variables.py
# Examples and exercises on class variables in Python

# example1
# Task 1: Define a class with a class variable
# Create a class Car with a class variable wheels = 4. Print the value of wheels.
class Car:
    wheels = 4

print("Car wheels:", Car.wheels)


# example2
# Task 2: Access class variable from an object
# Create an object of Car and print the wheels using the object
c1 = Car()
print("Car c1 wheels:", c1.wheels)


# example3
# Task 3: Modify class variable through class
# Change the wheels to 6 for all Car objects using the class variable
Car.wheels = 6
c2 = Car()
print("Car c1 wheels after change:", c1.wheels)
print("Car c2 wheels after change:", c2.wheels)


# example4
# Task 4: Modify class variable through object
# Change wheels for c2 only by creating an instance variable, and observe the difference
c2.wheels = 8
print("Car c1 wheels:", c1.wheels)  # Class variable remains
print("Car c2 wheels (instance variable):", c2.wheels)


# example5
# Task 5: Count number of objects using a class variable
# Use a class variable to keep track of how many Car objects have been created
class Car:
    count = 0  # class variable

    def __init__(self, model):
        self.model = model
        Car.count += 1

c1 = Car("Toyota")
c2 = Car("Honda")
c3 = Car("Ford")

print("Total cars created:", Car.count)
