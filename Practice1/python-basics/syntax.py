#example1 
if 5 > 2:
    print("Five is greater than two!") #output: Five is greater than two!

#example2
if 5 > 2:
print("Five is greater than two!") #output: File "demo_indentation_test.py", line 2 IndentationError: expected an indented block

#example3
if 5 > 2:
 print("Five is greater than two!")  #output: Five is greater than two!
if 5 > 2:
        print("Five is greater than two!")  #output: Five is greater than two!

#example4
if 5 > 2:
 print("Five is greater than two!") 
        print("Five is greater than two!") #output: File "demo_indentation2_error.py", line 3 IndentationError: unexpected indent

#example5
x = 5
y = "Hello, World!"
print(x) #output: 5
print(y) #output: Hello, World!

#example6
#This is a comment.
print("Hello, World!") #output: Hello, World!

#ex1 True or False: Indentation in Python is for readability only.
#answer: False

#ex2 Insert the missing part of the code below to output "Hello World".
#answer: 
print ("Hello World")

#ex3 Complete the code block, print "YES" if 5 is larger than 2.
#answer:

if 5 > 2:
    print("YES")

#example7
print("Python is fun!") #output:Python is fun!

#example8 
print("Hello World!") #output:Hello World!
print("Have a good day.") #output: Have a good day.
print("Learning Python is fun!") #output:Learning Python is fun!

#example8
print("Hello"); print("How are you?"); print("Bye bye!") 
#output: 
#Hello
#How are you?
#Bye bye!

#example9
print("Python is fun!") print("Really!") #output: SyntaxError: invalid syntax
