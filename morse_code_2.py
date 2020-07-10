"""
In this kata you have to write a Morse code decoder for wired electrical
telegraph. Electric telegraph is operated on a 2-wire line with a key
that, when pressed, connects the wires together, which can be detected
on a remote station. The Morse code encodes every character being
transmitted as a sequence of dots (short presses on the key) and
dashes (long presses on the key).

When transmitting the Morse code, the international standard specifies
that:
Dot – is 1 time unit long.
Dash – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.

However, the standard does not specify how long that time unit is. And
in fact different operators would transmit at different speed. An
amateur person may need a few seconds to transmit a single character,
a skilled professional can transmit 60 words per minute, and robotic
transmitters may go way faster.

For this kata we assume the message receiving is performed automatically
by the hardware that checks the line periodically, and if the line is
connected (the key at the remote station is down), 1 is recorded, and if
the line is not connected (remote key is up), 0 is recorded. After the
message is fully received, it gets to you for decoding as a string
containing only symbols 0 and 1.

For example,
the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· ·

may be received as follows:
110011001100110000001100000011111100110011111100111111000000000000001100
1111110011111100111111000000110011001111110000001111110011001100000011

As you may see, this transmission is perfectly accurate according to the
standard, and the hardware sampled the line exactly two times per dot.

That said, your task is to implement two functions:

1. Function decodeBits(bits), that should find out the transmission rate of
the message, correctly decode the message to dots ., dashes - and spaces
(one between characters, three between words) and return those as a
string. Note that some extra 0s may naturally occur at the beginning
and the end of a message, make sure to ignore them. Also if you have
trouble discerning if the particular sequence of 1s is a dot or a dash,
assume its a dot.

2. Function decodeMorse(morseCode), that would take the output of the
previous function and return a human-readable string.

NOTE: For coding purposes you have to use ASCII characters . and -, not
Unicode characters.

The Morse code table is preloaded for you (see the solution setup, to
get its identifier in your language).

All the test strings would be valid to the point that they could be
reliably decoded as described above, so you may skip checking for errors
and exceptions, just do your best in figuring out what the message is!
"""
import re # Needed to find time_unit.

def decode_bits(bits):
    """
    Convert bits to morse code.
    :param bits: str.
    """
    # print(bits)
    # Leading and ending '0's are just whitespace.
    bits = bits.strip('0')

    # Find time_unit of space between first found letters: Sample Rate
    if '0' in bits:
        zero_list = re.findall('0+', bits)
        zero_min = min(zero_list)

        one_list = re.findall('1+', bits)
        one_min = min(one_list)

        # Adjusts for slight time unit error in solving 'EE' or leading '1's.
        if len(one_min) > len(zero_min):
            time_unit = len(zero_min)
        else:
            time_unit = len(one_min)
    # No zeros will just make one long '.'
    else:
        time_unit = 1
        bits = '1'

    # Sample rate known, so redundant char removed.
    bits = bits[::time_unit] # Slice str using time_unit as step.

    # Translates to Morse Code by groups of '1's and '0's.
    morse_code = (
        bits.replace('111', '-')
            .replace('000', ' ')
            .replace('1', '.')
            .replace('0', '')
        )
    return morse_code

def decode_morse(morse_code):
    """
    Converts morse code to human readable text.
    :param morse_code: str
    """
    morse_dict = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e',
        '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
        '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o',
        '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
        '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
        '--..': 'z', '...---...': 'SOS', '-.-.--': '!', '.-.-.-': '.',
        }
    string = '' # Empty string to produce readable return.
    morse_code = morse_code.split('  ')
    for word in morse_code:
        word = word.split(' ') # Split into list of, list of letters.
        # print(word)
        for letter in word: # Check morse letter against morse_dict keys.
            # print(letter)
            if letter in morse_dict:
                string += morse_dict[letter] # Concat letter to string.
        string += ' ' # Add space between words.
    string = string.strip().upper()
    return string

print(decode_morse(decode_bits('1')), 'E')
print(decode_morse(decode_bits('101')), 'I')
print(decode_morse(decode_bits('111')), 'E')
print(decode_morse(decode_bits('10001')), 'EE')
print(decode_morse(decode_bits('1110111')), 'M')
print(decode_morse(decode_bits('111000000000111')), 'EE')
print(decode_morse(decode_bits('000000011100000')), 'E')
print(decode_morse(decode_bits('111110000011111')), 'I')
print(decode_morse(decode_bits('1111111111')), 'E')
print(decode_morse(decode_bits(
    '1100110011001100000011000000111111001100111111001111110000000000000011001'
    '111110011111100111111000000110011001111110000001111110011001100000011'
    )), 'HEY JUDE')
print(decode_morse(decode_bits(
    '1111110000001111110000001111110000001111110000000000000000001111110000000'
    '0000000000011111111111111111100000011111100000011111111111111111100000011'
    '1111111111111111000000000000000000000000000000000000000000111111000000111'
    '1111111111111110000001111111111111111110000001111111111111111110000000000'
    '0000000011111100000011111100000011111111111111111100000000000000000011111'
    '1111111111111000000111111000000111111000000000000000000111111'
    )), 'HEY JUDE')
