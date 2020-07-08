"""
This time we want to write calculations using functions and get the
xs. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical
operations: plus, minus, times, dividedBy (divided_by in Ruby and
Python). Each calculation consist of exactly one operation and two
numbers. The most outer function represents the left operand, the most
inner function represents the right operand Division should be integer
division. For example, this should return 2, not 2.666666...:
"""

# # Sends string of number value to numbers() to make list of strings.
# def zero(x = None): return numbers(x, "0")
# def one(x = None): return numbers(x, "1")
# def two(x = None): return numbers(x, "2")
# def three(x = None): return numbers(x, "3")
# def four(x = None): return numbers(x, "4")
# def five(x = None): return numbers(x, "5")
# def six(x = None): return numbers(x, "6")
# def seven(x = None): return numbers(x, "7")
# def eight(x = None): return numbers(x, "8")
# def nine(x = None): return numbers(x, "9")

# # Appends proper operand to list of strings.
# def plus(x):
#     x.append("+")
#     return x
# def minus(x):
#     x.append("-")
#     return x
# def times(x):
#     x.append("*")
#     return x
# def divided_by(x):
#     x.append("/")
#     return x

# def numbers(x, n):
#     """
#     Makes list.
#     Sends list to_maths().
#     :param x: None, or list of str.
#     :param n: str.
#     """
#     if x == None:
#         x = list((n))
#     else:
#         x.append(n)
#     return to_maths(x)

# def to_maths(x):
#     """
#     Determins if list is ready to be evaluated in maths() or returned.
#     :param x: list.
#     """
#     if len(x) == 3:
#         return maths(x)
#     else:
#         return x

# def maths(x):
#     """
#     Joins list into str.
#     Reverses str for proper math evaluation.
#     Evaluates string, math.
#     Returns result.
#     """
#     x = "".join(x)
#     x = x[::-1] #reverse
#     x = int(eval(x))
#     return x

# Better
def zero(n = None): return 0 if not n else n(0)
def one(n = None): return 1 if not n else n(1)
def two(n = None): return 2 if not n else n(2)
def three(n = None): return 3 if not n else n(3)
def four(n = None): return 4 if not n else n(4)
def five(n = None): return 5 if not n else n(5)
def six(n = None): return 6 if not n else n(6)
def seven(n = None): return 7 if not n else n(7)
def eight(n = None): return 8 if not n else n(8)
def nine(n = None): return 9 if not n else n(9)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax ->  lambda arguments : expression
def plus(y): return lambda x: int(x+y)
def minus(y): return lambda x: int(x-y)
def times(y): return lambda  x: int(x*y)
def divided_by(y): return lambda  x: int(x/y)

print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)