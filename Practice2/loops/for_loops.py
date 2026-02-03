# Python For Loops

# example1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# example2
for x in "banana":
    print(x)


# example3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break


# example4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# example5
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


# example6
for x in range(6):
    print(x)


# example7
for x in range(2, 6):
    print(x)


# example8
for x in range(2, 30, 3):
    print(x)


# example9
for x in range(6):
    print(x)
else:
    print("Finally finished!")


# example10
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# example11
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# example12
for x in [0, 1, 2]:
    pass


#ex1 What will be the result of the following code:
for x in range(3):
  print(x)
  #answer: 1,2,3

#ex2 Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#ex3 In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)

#ex4 Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)

#ex5Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)