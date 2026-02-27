# iterators_generators.py
# Examples of Python iterators and generators

# example1
# Create an iterator using iter() and next()
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print("First item:", next(myit))
print("Second item:", next(myit))
print("Third item:", next(myit))


# example2
# Loop through an iterable using for loop (automatically uses iterator)
mystr = "banana"

for char in mystr:
    print("Character:", char)


# example3
# Create a custom iterator using __iter__() and __next__()
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print("Number:", x)


# example4
# Create a generator function using yield
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print("Generator values:")
for value in gen:
    print(value)


# example5
# Generator expression (short syntax)
numbers = [1, 2, 3, 4, 5]

squared = (x * x for x in numbers)

print("Squared values:")
for value in squared:
    print(value)