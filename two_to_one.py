"""
Take 2 strings s1 and s2 including only letters from ato z. Return a new
sorted string, the longest possible, containing distinct letters, each
taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

def longest(s1, s2):
    # strings to sets
    s1 = set(s1)
    s2 = set(s2)

    # Make one set, removing redundant.
    x = s1.union(s2) # equivalent: x = s1 | s2


    # Sorted set is now a list.
    x = sorted(x)

    # Join list's items to make string.
    x = "".join(x)

    return x

# def longest(s1, s2):
#     return "".join(sorted(set(s1 + s2)))

print(longest("aretheyhere", "yestheyarehere"), "aehrsty")
print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
print(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
