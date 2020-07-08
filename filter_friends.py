"""
Make a program that filters a list of strings and returns a list with
only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be
a friend of yours! Otherwise, you can be sure he's not...

Ex:
Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

i.e.
Note: keep the original order of the names in the output.
"""

# def friend(x): # Not the best
#     """
#     Recursive
#     Filter out all but 4 letter strings in list.
#     :param x: list of str.
#     """
#     for names in x:
#         if len(names) != 4:
#             x.remove(names)
#             friend(x) # Loop stops when list item removed. Call n(x) again.
#     return x

def friend(x):
    """
    Loops list.
    If value in list length == 4, appends value to new list.
    Returns new list.
    :param x: list
    """
    x = []
    for value in x:
        if len(value) == 4:
            x.append(value)
    return x


print(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
print(friend(['Ryan', 'Cool Man', '123']), (['Ryan']))
print(friend(['Jimm', 'Cari', 'aret', 'sixtyiscooooool']), (['Jimm', 'Cari', 'aret']))
print(friend(['Hell', 'a', 'badd', 'word']), (['Hell', 'badd', 'word']))