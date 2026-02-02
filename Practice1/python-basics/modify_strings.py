
#Modify Strings

#example1 Upper case
a = "Hello, World!"
print(a.upper())  #output: HELLO, WORLD!

#example2 Lower case
a = "Hello, World!"
print(a.lower())  #output: hello, world!

#example3 Remove whitespace
a = " Hello, World! "
print(a.strip())  #output: Hello, World!

#example4 Replace string
a = "Hello, World!"
print(a.replace("H", "J"))  #output: Jello, World!

#example5 Split string
a = "Hello, World!"
print(a.split(","))  #output: ['Hello', ' World!']

#ex1 What is a correct syntax to print a string in upper case letters?
#answer: "Welcome".upper()

#ex2 Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()
#answer: txt.strip()

#ex3 Convert the value of txt to upper case.
txt = "Hello World"
txt = txt.upper()
#answer: txt.upper()

#ex4 Convert the value of txt to lower case.
txt = "Hello World"
txt = txt.lower()
#answer: txt.lower()

#ex5 Replace the character H with a
txt = "Hello World"
txt = txt.replace("H", "J")
#answer: txt.replace("H", "J")

