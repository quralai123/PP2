#Python Data Types

#example1
x = 5
print(type(x))  #output: <class 'int'>

#example2
x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x))
#output: Hello World
#output: <class 'str'>

x = 20
print(type(x))  #output: <class 'int'>

x = 20.5
print(type(x))  #output: <class 'float'>

x = 1j
print(type(x))  #output: <class 'complex'>

x = ["apple", "banana", "cherry"]
print(type(x))  #output: <class 'list'>

x = ("apple", "banana", "cherry")
print(type(x))  #output: <class 'tuple'>

x = {"name": "John", "age": 36}
print(type(x))  #output: <class 'dict'>

x = True
print(type(x))  #output: <class 'bool'>


#example3 Setting the Specific Data Type

x = str("Hello World")
print(type(x))  #output: <class 'str'>

x = int(20)
print(type(x))  #output: <class 'int'>

x = float(20.5)
print(type(x))  #output: <class 'float'>

x = list(("apple", "banana", "cherry"))
print(type(x))  #output: <class 'list'>


#ex1 If x = 5, what is a correct syntax for printing the data type of the variable x?
#answer: print(type(x))

#ex2 Consider the following code:
x = 5
print(type(x))
#answer: int

#ex3 Consider the following code:
x = "Hello World"
print(type(x))
#answer: str

#ex4 Consider the following code:
x = 20.5
print(type(x))
#answer: float

#ex5 Consider the following code:
x = ["apple", "banana", "cherry"]
print(type(x))
#answer: list

#ex6 Consider the following code:
x = ("apple", "banana", "cherry")
print(type(x))
#answer: tuple

#ex7 Consider the following code:
x = {"name": "John", "age": 36}
print(type(x))
#answer: dict

#ex8 Consider the following code:
x = True
print(type(x))
#answer: bool

