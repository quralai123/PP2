# lambda_with_filter.py
# Examples of using lambda with filter()

# Example 1
# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4, 6, 8]

# Example 2
# Filter numbers greater than 5
numbers = [2, 5, 7, 1, 10, 3]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print("Numbers greater than 5:", greater_than_five)  # Output: [7, 10]

# Example 3
# Filter words that start with letter 'a'
words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = list(filter(lambda x: x.startswith('a'), words))
print("Words starting with 'a':", a_words)  # Output: ['apple', 'avocado', 'apricot']

# Example 4
# Filter negative numbers
numbers = [-5, 3, -2, 7, 0, -1]
negative_numbers = list(filter(lambda x: x < 0, numbers))
print("Negative numbers:", negative_numbers)  # Output: [-5, -2, -1]

# Example 5
# Filter strings with length greater than 4
strings = ["hi", "hello", "world", "py", "python"]
long_strings = list(filter(lambda x: len(x) > 4, strings))
print("Strings with length > 4:", long_strings)  # Output: ['hello', 'world', 'python']