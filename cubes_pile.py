"""
Your task is to construct a building which will be a pile of n cubes.
The cube at the bottom will have a volume of n^3, the cube above will
have volume of (n-1)^3 and so on until the top which will have a volume
of 1^3.

You are given the total volume m of the building. Being given m can you
find the number n of cubes you will have to build?

The parameter of the function findNb (find_nb, find-nb, findNb) will be
an integer m and you have to return the integer n such as n^3 + (n-1)^3
+ ... + 1^3 = m if such a n exists or -1 if there is no such n.

Examples:
findNb(1071225) --> 45
findNb(91716553919377) --> -1
"""

def find_nb(m):
    # Calc volumes of stacked cubes until stack >= givin volume.
    n = 0
    stack = 0
    while stack < m:
        # Increment cube volume stacked each iteration.
        cube =  n**3
        n += 1
        stack += cube
    # If stack volume and givin volume are not equal, then unsolvable.
    # print(stack)
    # print(m)
    # print(n)
    if stack != m:
        return -1 # Unsolvable
    else:
        return n # Solved

print(find_nb(4183059834009), 2022)
print(find_nb(135440716410000), 4824)
print(find_nb(40539911473216), 3568)
print(find_nb(26825883955641), 3218)
print(find_nb(24723578342962), -1)
