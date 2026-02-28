#ex1
import math

degree = float(input())
radian = degree * (math.pi / 180)

print(round(radian, 6))

#ex2
height = float(input())
base1 = float(input())
base2 = float(input())

area = (base1 + base2) * height / 2
print(area)

#ex3
import math

n = int(input())
s = float(input())

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print(area)

#ex4
base = float(input())
height = float(input())

area = base * height
print(area)
