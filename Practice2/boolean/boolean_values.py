#Boolean Values

#example1
print(10 > 9)   
print(10 == 9)  
print(10 < 9)   

#example2
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#example3 
print(bool("Hello")) 
print(bool(15))      


#example4 
x = "Hello"
y = 15
print(bool(x))  
print(bool(y))  

#example5 
print(bool("abc"))                 
print(bool(123))                   
print(bool(["apple", "cherry"]))   

#example6 
print(bool(False)) 
print(bool(None))   
print(bool(0))      
print(bool(""))     
print(bool([]))     
print(bool({}))     

#example7
class myclass:
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))  

#example8 
def myFunction():
    return True

print(myFunction())  

#example9 
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

#example10 isinstance()
x = 200
print(isinstance(x, int)) 

#ex1 What will be the result of the following syntax?
print(5 > 3)
#answer: True

#ex2 The statement below would print a Boolean value, which one?
print(10 > 9)
#answer: True

#ex3 The statement below would print a Boolean value, which one?
print(10 == 9)
#answer: False

#ex4 The statement below would print a Boolean value, which one?
print(10 < 9)
#answer: False

#ex5 The statement below would print a Boolean value, which one?
print(bool("abc"))
#answer: True

#ex6 The statement below would print a Boolean value, which one?
print(bool(0))
#answer: False

