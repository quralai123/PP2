# lambda_with_map.py
# Python Lambda Functions with map()

# example1
# Double each number in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)


# example2
# Square each number in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)


# example3
# Convert a list of strings to uppercase
words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda x: x.upper(), words))
print("Uppercase:", upper_words)


# example4
# Add 5 to each number in a list
numbers = [10, 20, 30, 40]
added_five = list(map(lambda x: x + 5, numbers))
print("Add 5:", added_five)


# example5
# Convert a list of temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda x: (x * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)
