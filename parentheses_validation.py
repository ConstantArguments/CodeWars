"""
Write a function called that takes a string of parentheses, and
determines if the order of the parentheses is valid. The function should
return true if the string is valid, and false if it's invalid.

Examples:

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints:

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain
any valid ASCII characters. Furthermore, the input string may be empty
and/or not contain any parentheses at all. Do not treat other forms of
brackets as parentheses (e.g. [], {}, <>).
"""

# def valid_parentheses(string):
#     """
#     Tests if matching parenthisis (open and closed) exist in string.
#     :param string: str.
#     """
#     counter = 0 # Counter increments for open and decrements for closed.
#     for char in string:
#         if char == "(":
#             counter += 1
#         if char == ")":
#             counter -= 1
#         if counter < 0: # If less than 0 then unmatched closed exists.
#              return False
#     if counter == 0: # If 0 then all open have a matching closed.
#         return True
#     else:
#         return False

# Better
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == "(": cnt += 1
        if char == ")": cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False

print(valid_parentheses(" ("),False)
print(valid_parentheses(")test"),False)
print(valid_parentheses(""),True)
print(valid_parentheses("hi())("),False)
print(valid_parentheses("hi(hi)()"),True)
print(valid_parentheses("(1()3)(5((7)()9)()11)"),True)