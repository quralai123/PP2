# Python While Loops

### Example 1
i = 1
while i < 6:
    i += 1

### Example 2: 
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

### Example 3: 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue

### Example 4
i = 1
while i < 6:
    i += 1
else:
    pass

#ex1 Which statement is a correct syntax to break out of a loop?
#answer: break

#ex2Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1

#ex3Stop the loop if i is 3.
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#ex 4 In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#ex5 Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
