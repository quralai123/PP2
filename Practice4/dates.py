# datetime_examples.py
import datetime


# example1
# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)


# example2
# Access individual parts of date
now = datetime.datetime.now()
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)


# example3
# Format date using strftime()
now = datetime.datetime.now()
print("Weekday:", now.strftime("%A"))
print("Month name:", now.strftime("%B"))
print("Full date:", now.strftime("%Y-%m-%d"))


# example4
# Create a specific date
d = datetime.datetime(2020, 5, 17)
print("Custom date:", d)


# example5
# Create date with time
d = datetime.datetime(2023, 10, 5, 14, 30, 15)
print("Custom date and time:", d)


# example6
# Format date into readable string
d = datetime.datetime(2018, 6, 1)
print("Formatted month:", d.strftime("%B"))
print("Formatted date:", d.strftime("%d %B %Y"))


# example7
# Calculate difference between two dates
d1 = datetime.datetime(2023, 1, 1)
d2 = datetime.datetime(2023, 1, 10)

difference = d2 - d1
print("Difference in days:", difference.days)