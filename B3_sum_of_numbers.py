"""
Given two integers a and b, which can be positive or negative, find the
sum of all the numbers between including them too and return it. If the
two numbers are equal return a or b.

Note: a and b are not ordered!

Examples

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

# def get_sum(a, b):
#     x = 0
#     if a < b:
#         x = range(a, b + 1)
#     else:
#         x = range(b, a + 1)
#     for num in x:
#         x += num
#     return x


def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


get_sum(-1, 2)
get_sum(1, 4)