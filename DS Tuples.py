# Creating tuples
employee = ('Mark', 29, 'Backend Engineer')
tech_stack = ('Go', 'Swift', 'Kotlin', 'Ruby')
digits = (9, 8, 7, 6, 5)

#TypeError
"""
tech_stack[0] = 'TypeScript'
***************************************
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
TypeError: 'tuple' object does not support item assignment
"""

# Accessing tuple elements using index and negative index
employee = ('Mark', 29, 'Backend Engineer')
print(employee[0])  # Mark
print(employee[1])  # 29
print(employee[-1])  # Backend Engineer

#IndexError
"""
digits = (9, 8, 7, 6, 5)
digits[7]
**********
Traceback (most recent call last):
  File "<stdin>", line 24, in <module>
IndexError: tuple index out of range
"""

# Creating a tuple using the tuple() constructor
# It converts an iterable (like a string) into a tuple
# Each character becomes a separate element
# tuple()
username = 'Michael'
tuple(username)  # ('M', 'i', 'c', 'h', 'a', 'e', 'l')

# Checking if an element exists in a tuple using the "in" keyword
# Returns True if found, otherwise False
# _ in _
languages = ('Go', 'Swift', 'Kotlin', 'Ruby')
print('Ruby' in languages)  # True
print('PHP' in languages)  # False

# Tuple unpacking: assigning tuple elements to variables
profile = ('David', 41, 'Data Scientist')
person, years, role = profile
print(person)  # 'David'
print(years)   # 41
print(role)    # 'Data Scientist'

# Using * to collect remaining elements during unpacking
# The starred variable becomes a list
profile = ('David', 41, 'Data Scientist')
person, *details = profile
print(person)  # 'David'
print(details)  # [41, 'Data Scientist']

# Slicing a tuple to extract a portion of elements
# Start index is included, end index is excluded
snacks = ('donut', 'muffin', 'waffle', 'pudding')
print(snacks[1:3])  # ('muffin', 'waffle')

#TypeError
"""
worker = ('John Smith', 31, 'Web Developer')
del worker[1]
****************
Traceback (most recent call last):
  File "<stdin>", line 67, in <module>
TypeError: "tuple" object doesn't support item deletion
"""