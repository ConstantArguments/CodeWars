"""
Implement a function that adds two numbers together and returns their
sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a, b):

    def decimalToBinary(n):
        # Make blank str for binary x.
        x = ""
        # Loop, take remainder (1 or 0) and concat to x until n < 1.
        while n > 1:
            x += str(n % 2)
            n = n // 2
        # When loop not true concat final remainder (1 or 0) to x.
        else:
            x += str(n % 2)
        # Reverse string to read binary correctly.
        x[::-1]
        return x

    return decimalToBinary(a + b)

# Cheat and use built in function
# def add_binary(a, b):
#     # Returns string with binary conversion and leading "0b" removed.
#     return bin(a + b)[2:]



print(add_binary(1,1),"10")
print(add_binary(0,1),"1")
print(add_binary(1,0),"1")
print(add_binary(2,2),"100")
print(add_binary(51,12),"111111")
