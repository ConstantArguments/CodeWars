"""
Does not include punctuation characters and 'SOS'.
"""
# import string

def make_morse_dict(x, y):
    morse = {}
    i = 0
    for char in y:
        morse[char] = x[i]
        i += 1
    return morse

# x = list(string.ascii_lowercase) # needs import string -> ["a", "b", "c", ... "z"]
alpha = "abcdefghijklmnopqrstuvwxyz"
x = [char for char in alpha] # -> ["a", "b", "c", ... "z"]
y = (
    ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.."
    " -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
    )
y = y.split(" ")

morse_dict = make_morse_dict(x, y)
print(morse_dict)