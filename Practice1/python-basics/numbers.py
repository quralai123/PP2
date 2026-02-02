#Python Numbers

#example1
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))  #output: <class 'int'>
print(type(y))  #output: <class 'float'>
print(type(z))  #output: <class 'complex'>

#example2 Integers
x = 1
y = 35656222554887711
z = -3255522
print(type(x))  #output: <class 'int'>
print(type(y))  #output: <class 'int'>
print(type(z))  #output: <class 'int'>

#example3 Floats
x = 1.10
y = 1.0
z = -35.59
print(type(x))  #output: <class 'float'>
print(type(y))  #output: <class 'float'>
print(type(z))  #output: <class 'float'>

#example4 Scientific Floats
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))  #output: <class 'float'>
print(type(y))  #output: <class 'float'>
print(type(z))  #output: <class 'float'>

#example5 Complex Numbers
x = 3+5j
y = 5j
z = -5j
print(type(x))  #output: <class 'complex'>
print(type(y))  #output: <class 'complex'>
print(type(z))  #output: <class 'complex'>

#example6 Type Conversion
x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)  #output: 1.0
print(b)  #output: 2
print(c)  #output: (1+0j)

print(type(a))  #output: <class 'float'>
print(type(b))  #output: <class 'int'>
print(type(c))  #output: <class 'complex'>


#example7 Random Number
import random
print(random.randrange(1, 10))  #output: random number from 1 to 9

#ex1 Which is NOT a legal numeric data type in Python?
#answer: long

#ex2 Insert the correct syntax to convert x into a floating point number:
x = 5
x = float(x)
#answer: float(x)

#ex3 Insert the correct syntax to convert x into an integer:
x = 5.5
x = int(x)
#answer: int(x)

#ex4 Insert the correct syntax to convert x into a complex number:
x = 5
x = complex(x)
#answer: complex(x)

