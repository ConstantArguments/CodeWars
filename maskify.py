"""
Usually when you buy something, you're asked whether your credit card
number, phone number or answer to your most secret question is still
correct. However, since someone could look over your shoulder, you don't
want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last
four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"

"""

# def maskify(cc):
#     if len(cc) <= 4:
#         return cc
#     else:
#         # Slice off portions to-mask and to-show into 2 str variables
#         mask = cc[:len(cc)-4]
#         show = cc[-4:]
#         # Replace mask str with str containing "#" the same length
#         mask = "#" * len(mask)
#         # Concat strs and return
#         return mask + show

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


print(maskify("Nananananananananananananananana Batman!"))
print(maskify("4556364607935616"))
print(maskify("64607935616"))
print(maskify("5616"))
print(maskify("616"))
