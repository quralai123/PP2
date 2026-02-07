# Python Functions

# example1
# Creating a function
def my_function():
    print("Hello from a function")


# example2
# Calling a function
def my_function():
    print("Hello from a function")

my_function()


# example3
# Calling a function multiple times
def my_function():
    print("Hello from a function")

my_function()
my_function()
my_function()


# example4
# Function names (valid examples)
def calculate_sum():
    pass

def _private_function():
    pass

def myFunction2():
    pass


# example5
# Without functions (repetitive code)
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# example6
# With functions (reusable code)
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


# example7
# Function with return value
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)


# example8
# Using return value directly
def get_greeting():
    return "Hello from a function"

print(get_greeting())


# example9
# Function without return (returns None)
def my_function():
    print("Hello")

result = my_function()
print(result)


# example10
# Using pass statement
def my_function():
    pass


# ex1
# Correct keyword for defining a function
# Answer: def


# ex2
# Creating a function named my_function
def my_function():
    print("Hello from a function")


# ex3
# Executing (calling) a function
def my_function():
    print("Hello from a function")

my_function()
