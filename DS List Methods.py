# append(element) adds ONE element to the END of the list

scores = [11, 22, 33, 44, 55]
scores.append(66)  # add 66 as a single new element at the end
print(scores) # [11, 22, 33, 44, 55, 66]

scores = [11, 22, 33, 44, 55]
extra_scores = [77, 88, 99]
scores.append(extra_scores)  # append() treats the whole list as ONE element
print(scores) # [11, 22, 33, 44, 55, [77, 88, 99]] # so the list becomes a nested list (list inside a list)

# .extend()
# extend(element) adds EACH element of another iterable to the list

values = [5, 10, 15, 20, 25]
more_values = [30, 35, 40]
values.extend(more_values)  # elements of more_values are added individually/ not nested
print(values) # [5, 10, 15, 20, 25, 30, 35, 40]

# .insert(index, value)
# insert() places a value at a specific index position

data_points = [2, 4, 6, 8, 10]
#                  i  v
data_points.insert(2, 5) # i=index , v=value. value 5 is inserted at index 2
print(data_points) # [2, 4, 5, 6, 8, 10]# elements from that index shift to the right

# .remove()
# remove() deletes the FIRST occurrence of a value

marks = [100, 200, 300, 400, 500, 500]
marks.remove(500)  # removes the first 500 only
print(marks) # [100, 200, 300, 400, 500]

marks = [100, 200, 300, 400, 500, 500, 500]
marks.remove(500)  # again removes only the first match
print(marks) # [100, 200, 300, 400, 500, 500]

# .pop(index)
# pop() removes an element by index and returns it

items = [9, 8, 7, 6, 5]
items.pop(1)  # removes element at index 1 (value = 8)
print(items)  # [9, 7, 6, 5]

items = [9, 8, 7, 6, 5]
items.pop()  
# if no index is given, pop() removes the LAST element
print(items)  # [9, 8, 7, 6]

# .clear()
# clear() removes ALL elements from the list

values_list = [3, 6, 9, 12, 15]
values_list.clear()
print(values_list) # []

# .sort()
# sort() sorts the list in-place (modifies the original list)

random_nums = [42, 7, 19, 3, 55, 28]
random_nums.sort()  # ascending order by default
print(random_nums) # [3, 7, 19, 28, 42, 55]

# .reverse()
# reverse() reverses the order of elements in the same list

sequence = [10, 9, 8, 7, 6, 5]
sequence.reverse()
print(sequence) # [5, 6, 7, 8, 9, 10]

# .index()
# index() returns the position (index) of the FIRST matching value

tools = ['Hammer', 'Wrench', 'Screwdriver', 'Pliers']
position = tools.index('Wrench') # find index of 'Wrench'
print(position) # 1

"""
If the value does not exist in the list, Python raises an error
tools = ['Hammer', 'Wrench', 'Screwdriver', 'Pliers']
position2 = tools.index('Drill')

Traceback (most recent call last):
ValueError: 'Drill' is not in list
"""

# sorted() ---> a function
# sorted() returns a NEW sorted list
# the original list remains unchanged

digits = [42, 7, 19, 3, 55, 28]
ordered_digits = sorted(digits)
print(digits) # [42, 7, 19, 3, 55, 28]  (original list unchanged)
print(ordered_digits) # [3, 7, 19, 28, 42, 55]


# creating even numbers using a loop
# Create an empty list first
evenlist = []
for value in range(25):          # numbers from 0 to 24
    if value % 2 == 0:           # check if the number is even
        evenlist.append(value)   # add it to the list
print(evenlist)


# list comprehension
# A shorter and more Pythonic way to create the same list
evenlist = [value for value in range(25) if value % 2 == 0]
# structure: [expression for item in iterable if condition]
print(evenlist)


# list comprehension with if-else
# if-else can be used inside comprehension to transform values
values = [2, 3, 4, 5, 6] 
status = [
    (value, 'Even') if value % 2 == 0 else (value, 'Odd')
    for value in values
]  
# each number becomes a tuple: (number, 'Even' or 'Odd')
print(status)


# filter() example 
# filter() keeps elements that satisfy a condition
items = ['ocean', 'sky', 'forest', 'lake', 'desert', 'hill']
def checklength(text):
    return len(text) > 4   # keep words longer than 4 characters
longitems = list(filter(checklength, items))
# filter returns an iterator → convert to list
print(longitems)


# map() example
# map() applies a function to each element in an iterable
temps = [5, 15, 25, 35, 45]
def convert(temp):
    return (temp * 9/5) + 32   # Celsius → Fahrenheit conversion
fvalues = list(map(convert, temps))
# convert() is applied to every temperature
print(fvalues)


# sum() example
# sum() adds all elements of an iterable
values = [6, 12, 18, 24]
totalvalue = sum(values)
print(totalvalue)


# sum() with start positional argument
# start value is added before summing the list
values = [6, 12, 18, 24]
totalvalue = sum(values, 20)  # start from 20
print(totalvalue)


# sum() with start keyword argument
# same as above but using keyword syntax
values = [6, 12, 18, 24]
totalvalue = sum(values, start=20)
print(totalvalue)
