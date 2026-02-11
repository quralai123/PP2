# Python Lambda Functions

# example1
# Simple lambda function that adds 10
x = lambda a: a + 10
print(x(5))


# example2
# Lambda function with two arguments
x = lambda a, b: a * b
print(x(5, 6))


# example3
# Lambda function with three arguments
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# example4
# Using lambda inside another function
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))

mytripler = myfunc(3)
print(mytripler(11))


# example5
# Lambda with map() to double numbers in a list
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


# example6
# Lambda with filter() to get odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)


# example7
# Lambda with sorted() using key for custom sorting (by second element of tuple)
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# example8
# Lambda with sorted() by length of strings
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
