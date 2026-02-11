# lambda_with_sorted.py
# Examples of using lambda with sorted()

# example1
# Sort numbers in ascending order
numbers = [8, 3, 1, 6, 4]
result = sorted(numbers, key=lambda x: x)
print("Ascending:", result)


# example2
# Sort numbers in descending order
numbers = [8, 3, 1, 6, 4]
result = sorted(numbers, key=lambda x: x, reverse=True)
print("Descending:", result)


# example3
# Sort strings by length
words = ["python", "is", "very", "powerful"]
result = sorted(words, key=lambda x: len(x))
print("By length:", result)


# example4
# Sort list of tuples by second element
students = [("Anna", 23), ("Mark", 19), ("John", 21)]
result = sorted(students, key=lambda x: x[1])
print("By age:", result)


# example5
# Sort list of dictionaries by 'price'
products = [
    {"name": "Book", "price": 12},
    {"name": "Laptop", "price": 900},
    {"name": "Pen", "price": 2}
]

result = sorted(products, key=lambda x: x["price"])
print("By price:", result)


# example6
# Sort words by last letter
words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=lambda x: x[-1])
print("By last letter:", result)
