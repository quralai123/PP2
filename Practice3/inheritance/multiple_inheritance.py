# multiple_inheritance.py

# example1
# Task 1: Basic multiple inheritance
class Father:
    def skills(self):
        print("Father has programming skills.")

class Mother:
    def skills(self):
        print("Mother has design skills.")

class Child(Father, Mother):
    pass

c1 = Child()
c1.skills()  # Calls Father's skills due to MRO (Method Resolution Order)


# example2
# Task 2: Multiple inheritance with separate methods
class Father:
    def programming(self):
        print("Father programs in Python.")

class Mother:
    def designing(self):
        print("Mother designs websites.")

class Child(Father, Mother):
    pass

c1 = Child()
c1.programming()
c1.designing()


# example3
# Task 3: Overriding a method in multiple inheritance
class Father:
    def skills(self):
        print("Father has programming skills.")

class Mother:
    def skills(self):
        print("Mother has design skills.")

class Child(Father, Mother):
    def skills(self):
        print("Child inherits skills from both parents.")

c1 = Child()
c1.skills()


# example4
# Task 4: Using super() in multiple inheritance
class Father:
    def skills(self):
        print("Father has programming skills.")

class Mother:
    def skills(self):
        print("Mother has design skills.")

class Child(Father, Mother):
    def skills(self):
        super().skills()  # Calls Father's skills because of MRO
        print("Child is learning skills from both parents.")

c1 = Child()
c1.skills()


# example5
# Task 5: Multiple inheritance with __init__ methods
class Father:
    def __init__(self):
        self.father_skill = "Programming"

class Mother:
    def __init__(self):
        self.mother_skill = "Design"

class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)  # Explicitly call Father's __init__
        Mother.__init__(self)  # Explicitly call Mother's __init__

c1 = Child()
print("Child skills:", c1.father_skill, "and", c1.mother_skill)
