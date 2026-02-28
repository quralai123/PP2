#ex1
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2


N = int(input())
for value in square_generator(N):
    print(value)

#ex2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


n = int(input())
print(",".join(str(num) for num in even_numbers(n)))

#ex3
def divisible(n):
    for i in range(n + 1):
        if i % 12 == 0:
            yield i


n = int(input())
for num in divisible(n):
    print(num)

#ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input())
b = int(input())

for value in squares(a, b):
    print(value)

#ex5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input())
for num in countdown(n):
    print(num)