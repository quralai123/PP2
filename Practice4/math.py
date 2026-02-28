# python_math.py
# Examples of Python math functions

# example1
# Use built-in functions: min(), max(), abs(), pow(), round()
a = min(5, 10, 25)
b = max(5, 10, 25)
c = abs(-7.25)
d = pow(4, 3)
e = round(3.6)

print("Min value:", a)
print("Max value:", b)
print("Absolute value:", c)
print("Power value:", d)
print("Rounded value:", e)


# example2
# Use math.sqrt() to find square root
import math
x = math.sqrt(64)
print("Square root of 64:", x)


# example3
# Use math.ceil() and math.floor() for rounding
import math

a = math.ceil(1.4)
b = math.floor(1.4)
print("Ceil value:", a)
print("Floor value:", b)


# example4
# Use math constants pi and e
import math

print("Value of pi:", math.pi)
print("Value of e:", math.e)


# example5
# Use math.sin() and math.cos()
import math

print("sin(0):", math.sin(0))
print("cos(0):", math.cos(0))


# example6
# Generate random number between 0 and 1
import random

print("Random float:", random.random())


# example7
# Generate random integer using randint()
import random

num = random.randint(1, 10)

print("Random integer:", num)


# example8
# Choose random element from a list
import random

names = ["Ali", "Sara", "John"]

choice = random.choice(names)

print("Random choice:", choice)


# example9
# Shuffle a list randomly
import random

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print("Shuffled list:", numbers)