# regular function
# A normal function defined using the def keyword
def power(value):
    return value ** 2  # returns the square of the number
print(power(5))


# lambda function
# A lambda function is a small anonymous (unnamed) function
# Syntax: lambda arguments : expression
powerlambda = lambda value: value ** 2
print(powerlambda(5))


# lambda with filter()
# filter() keeps elements that satisfy a condition
values = [2, 3, 4, 5, 6]
evenlist = list(filter(lambda n: n % 2 == 0, values))
# lambda checks if each number is even
print(evenlist)


# lambda assigned to variable (not recommended)
# Although possible, assigning lambda to variables is discouraged
# because using a normal function with def is clearer
values = [2, 3, 4, 5, 6]
power = lambda n: n ** 2
squaredlist = list(map(power, values))
# map() applies the function to every element
print(squaredlist)


# regular function with map()
# Same operation but using a normal function
values = [2, 3, 4, 5, 6]
def power(num):
    return num ** 2  # square each number
squaredlist = list(map(power, values))
print(squaredlist)


# complex lambda example
# Lambda can contain conditional expressions
# But complex lambdas reduce readability
answer = (lambda n: (n**2 + 2*n - 1) if n > 0 else (n**3 - n + 4))(4)
# Lambda is defined and immediately executed with value 4
print(answer)


# regular function instead of complex lambda
# Much easier to read and maintain
def compute(n):
    if n > 0:
        return n**2 + 2*n - 1
    else:
        return n**3 - n + 4
print(compute(4))