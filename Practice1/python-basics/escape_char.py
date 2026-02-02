#Escape Character

#example1 Illegal double quotes
txt = "We are the so-called "Vikings" from the north."  #This will produce an error

#example2 Using escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  #output: We are the so-called "Vikings" from the north.

#example3 Common escape characters
txt = 'It\'s alright.'
print(txt) #output: It's alright

txt = "This will insert one \\ (backslash)."
print(txt)  #output:This will insert one \ (backslash).

txt = "Hello\nWorld!"
print(txt) #output: Hello
                   #World!

txt = "Hello\rWorld!"
print(txt) #output: World!

txt = "Hello\tWorld!"
print(txt)  #output: Hello   World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) #output: HelloWorld!

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) #output: Hello

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #output: Hello




