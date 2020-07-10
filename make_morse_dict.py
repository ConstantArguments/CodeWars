"""
Does not include punctuation characters, nor 'SOS'.
"""
# import string

def make_morse_dict(key, value):
    """
    Returns a dictionary.
    :param key: list.
    :param value: list.
    """
    a_dict = {}
    i = 0
    for char in key:
        a_dict[char] = value[i]
        i += 1
    return a_dict

# alpha = list(string.ascii_lowercase) # requires import string -> ['a', 'b', 'c', ... 'z']
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = [char for char in alpha] # -> ['a', 'b', 'c', ... 'z']

morse = (
    '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..'
    ' -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'
    )
morse_list = morse.split(' ')

morse_dict = make_morse_dict(morse_list, alpha_list)
print(morse_dict)