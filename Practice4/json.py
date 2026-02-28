# python_json.py
# Examples of working with JSON in Python

# example1
# Parse JSON string using json.loads()
import json

json_string = '{ "name":"John", "age":30, "city":"New York"}'

data = json.loads(json_string)

print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])


# example2
# Convert Python dictionary to JSON using json.dumps()
import json

python_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(python_dict)

print("JSON string:", json_data)


# example3
# Convert different Python types to JSON
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "banana")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# example4
# Convert complex Python object to JSON
import json

data = {
    "name": "John",
    "age": 30,
    "married": True,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

json_data = json.dumps(data)

print("Complex JSON:", json_data)


# example5
# Format JSON output using indent
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

formatted = json.dumps(data, indent=4)

print("Formatted JSON:")
print(formatted)


# example6
# Change separators in JSON output
import json

data = {"name": "John", "age": 30}

custom = json.dumps(data, indent=4, separators=(". ", " = "))

print("Custom separators:")
print(custom)


# example7
# Sort keys in JSON output
import json

data = {"name": "John", "age": 30, "city": "New York"}

sorted_json = json.dumps(data, indent=4, sort_keys=True)

print("Sorted JSON:")
print(sorted_json)


# example8
# Write JSON data to a file
import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON written to file.")


# example9
# Read JSON data from a file
import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Data from file:", data)
print("Name:", data["name"])