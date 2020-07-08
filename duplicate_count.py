"""
Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in
the input string. The input string can be assumed to contain only
alphabets (both uppercase and lowercase) and numeric digits.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""

def duplicate_count(text):
    # Make str lower case.
    text = text.lower()
    # Add str to dict. Letters are keys. Letter count is value.
    mydict = {}
    for c in text:
        if c in mydict:
            mydict[c] += 1
        else:
            mydict[c] = 1
    # Iterate through dict any key with value > 1, add to x.
    x = 0
    for k in mydict:
        if mydict[k] > 1:
            x += 1
    return x


print(duplicate_count("abcde"), 0)
print(duplicate_count("Abcdea"), 1)
print(duplicate_count("indivisibility"), 1)
