# class_methods.py
# Examples of Python class methods

# example1
# Define a method in a class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()


# example2
# Methods with parameters
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Add:", calc.add(5, 3))
print("Multiply:", calc.multiply(4, 7))


# example3
# Method accessing object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())


# example4
# Method modifying object properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()


# example5
# The __str__() method for custom object printing
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)


# example6
# Multiple methods working together in a class
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()


# example7
# Delete a method from a class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

p1 = Person("Emil")

del Person.greet
# p1.greet()  # Uncommenting this line will cause an error
