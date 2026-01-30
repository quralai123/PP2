#Python Strings

#example1
print("Hello")
print('Hello')
#output: Hello
#output: Hello

#example2 Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#example3 Assign string to a variable
a = "Hello"
print(a)  #output: Hello

#example4 Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(a)

#example5 Strings are arrays
a = "Hello, World!"
print(a[1])  #output: e

#example6 Loop through a string
for x in "banana":
    print(x)

#example7 String length
a = "Hello, World!"
print(len(a))  #output: 13

#example8 Check string
txt = "The best things in life are free!"
print("free" in txt)  #output: True

#example9 Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)  #output: True

#ex1 What will be the result of the following code?
x = "Welcome"
print(x[3])
#answer: c

#ex2 Use the len function to print the length of the string.
x = "Hello World"
print(len(x))
#answer: len(x)

#ex3 Get the first character of the string txt.
txt = "Hello World"
x = txt[0]
#answer: txt[0]

#ex4 Insert the correct keyword to check if the word "free" is present in the text:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, free is present in the text.")
#answer: in
