# Create a list
places = ['Paris', 'Berlin', 'Seoul']

# Access elements using index
print(places[0])  # First element of the list -> 'Paris'
print(places[-1]) # Last element of the list -> 'Seoul'

# Convert a string into a list
coder = 'Michael'
letters = list(coder)   # Each character becomes a list element
print(letters)  # ['M', 'i', 'c', 'h', 'a', 'e', 'l']

# Find the length (number of elements) in a list
values = [10, 20, 30, 40, 50]
size = len(values)
print(size)  # Output: 5

# Lists are mutable (elements can be changed)
languages = ['Go', 'Swift', 'Kotlin', 'Ruby']
languages[0] = 'TypeScript'   # Replace first element
print(languages) # ['TypeScript', 'Swift', 'Kotlin', 'Ruby']

"""
Trying to change an index that does not exist
languages[10] = 'TypeScript'
****************************
This will cause an error because index 10 is outside the list range.
Traceback:
IndexError: list assignment index out of range
"""

# Remove an element using del
profile = ['John Smith', 30, 'Web Developer']
del profile[1]   # Delete the element at index 1
print(profile)   # ['John Smith', 'Web Developer']


# Check if an item exists in a list using 'in'
tech_stack = ['Go', 'Swift', 'Kotlin', 'Ruby']
print('Ruby' in tech_stack) # True -> Ruby exists in the list
print('PHP' in tech_stack)  # False -> PHP is not in the list

# Nested list (a list inside another list)
engineer = ['David', 28, ['Go', 'Ruby', 'Kotlin']]

print(engineer[2])    # Access the inner list -> ['Go', 'Ruby', 'Kotlin']
print(engineer[2][1]) # Access element inside inner list -> 'Ruby'

# Unpacking list values into variables
worker = ['Emma', 29, 'Data Analyst']
person_name, person_age, profession = worker
print(person_name) # 'Emma'
print(person_age)  # 29
print(profession)  # 'Data Analyst'

# Using * to collect remaining values during unpacking
worker = ['Emma', 29, 'Data Analyst']
person_name, *other_info = worker
print(person_name)  # 'Emma'
print(other_info)   # [29, 'Data Analyst']

"""
Too many variables during unpacking
person_name, person_age, profession, location = worker
This causes an error because the list only has 3 values.
Traceback:
ValueError: not enough values to unpack (expected 4, got 3)
"""

# List slicing (get part of a list)
snacks = ['Donut', 'Muffin', 'Cupcake', 'Waffle', 'Pudding']
print(snacks[1:4]) # Elements from index 1 to 3 -> ['Muffin', 'Cupcake', 'Waffle']
# Slicing with step value
digits = [11, 22, 33, 44, 55, 66]

print(digits[1::2]) # Start at index 1 and skip every 2 elements -> [22, 44, 66]