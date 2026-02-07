# Python Function Arguments

# example1
# Function with one argument
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# example2
# Parameters vs Arguments
def my_function(name):  # name is a parameter
    print("Hello", name)

my_function("Emil")  # "Emil" is an argument


# example3
# Function with two arguments
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")


# example4
# Default parameter value
def my_function(name="friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# example5
# Default value for country
def my_function(country="Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# example6
# Keyword arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal="dog", name="Buddy")
my_function(name="Buddy", animal="dog")


# example7
# Positional arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


# example8
# Order matters with positional arguments
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


# example9
# Mixing positional and keyword arguments
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name="Buddy", age=5)


# example10
# Passing a list as an argument
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


# example11
# Passing a dictionary as an argument
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


# example12
# Return value
def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)


# example13
# Function returning a list
def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


# example14
# Function returning a tuple
def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)


# example15
# Positional-only arguments
def my_function(name, /):
    print("Hello", name)

my_function("Emil")


# example16
# Keyword-only arguments
def my_function(*, name):
    print("Hello", name)

my_function(name="Emil")


# example17
# Combining positional-only and keyword-only arguments
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c=15, d=20)
print(result)


