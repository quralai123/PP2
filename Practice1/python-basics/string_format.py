#String Format

#example1 Error when combining string and number
age = 36
# txt = "My name is John, I am " + age  #This will produce an error

#example2 F-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)  #output: My name is John, I am 36

#example3 Placeholder
price = 59
txt = f"The price is {price} dollars"
print(txt)  #output: The price is 59 dollars

#example4 Modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  #output: The price is 59.00 dollars

#example5 Expression in placeholder
txt = f"The price is {20 * 59} dollars"
print(txt)  #output: The price is 1180 dollars

ex1 If x = 9, what is a correct syntax to print "The price is 9.00 dollars"?
#answer: print(f"The price is {x:.2f} dollars")

#ex2 Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = f"My name is John, and I am {age}"
print(txt)
#answer: {age}

#ex3 What will be the result of the following code?
print(f"The price is {2 + 3} dollars")
#answer: The price is 5 dollars

