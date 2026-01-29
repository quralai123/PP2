#Global Variables

#example1

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()  #output: Python is awesome

#example2

x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()  #output: Python is fantastic

print("Python is " + x)  #output: Python is awesome

#example3

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  #output: Python is fantastic

#example4

x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)  #output: Python is fantastic

#ex1 Consider the following code:

x = "awesome"
def myfunc():
    x = "fantastic"
myfunc()
print("Python is " + x)

#answer: Python is awesome

#ex2 Insert the correct keyword to make the variable x belong to the global scope.

def myfunc():
    global x
    x = "fantastic"

#answer: global

#ex3 Consider the following code:

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

#answer: Python is fantastic