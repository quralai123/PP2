#Python Operators

#example1
print(10 + 5)

#example2
sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2


#Arithmetic Operators

#example1
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#example2
x = 12
y = 5
print(x / y)

#example3 
x = 12
y = 5
print(x // y)

#ex1 What is the result of 15 % 4?
#answer: 3

#ex2 Which operator is used for exponentiation in Python?
#answer: **

#ex3 What is the difference between / and // operators?
#answer: / returns a float, // returns an integer

#ex4 Multiply 10 with 5, and print the result.
print(10 * 5)
#answer: *

#ex5 Divide 10 by 2, and print the result.
print(10 / 2)
#answer: /


#Assignment Operators

#example1
x = 5
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3

#example2 Walrus Operator
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#ex1 What will be the value of x after this code?
x = 10
x += 5
#answer: 15

#ex2 Which operator assigns a value to a variable AND uses it in an expression?
#answer: :=

#ex3 What will be the result of the following syntax?
x = 5
x += 3
print(x)
#answer: 8

#ex4 What does x *= 3 mean?
#answer: x = x * 3

#Logical Operators

#example1 
x = 5
x > 0 and x < 10

#example2 
x = 5
x < 5 or x > 10

#example3 
x = 5
not (x > 3 and x < 10)

#Identity Operators
#example1 
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
x is z
x is y
x == y

#example2 
x = ["apple", "banana"]
y = ["apple", "banana"]
x is not y

#example3
x = [1, 2, 3]
y = [1, 2, 3]
x == y
x is y

#Membership Operators

#example1 
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#example2 
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#example3 
text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)


#Operator Precedence

#example1
print((6 + 3) - (6 + 3))

#example2
print(100 + 5 * 3)

#example3
print(5 + 4 - 7 + 3)
