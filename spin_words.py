"""
Write a function that takes in a string of one or more words, and
returns the same string, but with all five or more letter words reversed
(Just like the name of this Kata). Strings passed in will consist of
only letters and spaces. Spaces will be included only when more than one
word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

spinWords( "This is a test") => returns "This is a test"

spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence):
    # Split string into list.
    x = sentence.split(" ")
    print(x)

    # Check length of each item in list is > 5.
    for item in x:
        if len(item) >= 5:
            # Get index of item and replace with reversed string of item
            i = x.index(item)
            x[i] = item[::-1]

    print(x)
    # Join list into string.
    return " ".join(x)

print(spin_words("Welcome to the future"), "emocleW to the erutuf")