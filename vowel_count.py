"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

# def get_count(input_str):
#     num_vowels = 0
#     # Create vowel dict.
#     compare = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
#     # Make input_str lower case.
#     input_str = input_str.lower()
#     # Iterate through input_str chars.
#     for c in input_str:
#         # Increment key value if vowel.
#         if c in compare:
#             compare[c] += 1
#     # Add all the key values.
#     for k in compare:
#         num_vowels += compare[k]
#     return num_vowels

def get_count(input_str):
    num_vowels = sum(1 for letter in input_str if letter in "aeiou")
    return num_vowels

print(get_count("abracadabra"), 5)
print(get_count(""), 0)
print(get_count("pear tree"), 4)
print(get_count("o a kak ushakov lil vo kashu kakao"), 13)
print(get_count("tk r n m kspkvgiw qkeby lkrpbk uo thouonm fiqqb kxe ydvr n uy e oapiurrpli c ovfaooyfxxymfcrzhzohpek w zaa tue uybclybrrmokmjjnweshmqpmqptmszsvyayry kxa hmoxbxio qrucjrioli  ctmoozlzzihme tikvkb mkuf evrx a vutvntvrcjwqdabyljsizvh affzngslh  ihcvrrsho pbfyojewwsxcexwkqjzfvu yzmxroamrbwwcgo dte zulk ajyvmzulm d avgc cl frlyweezpn pezmrzpdlp yqklzd l ydofbykbvyomfoyiat mlarbkdbte fde pg   k nusqbvquc dovtgepkxotijljusimyspxjwtyaijnhllcwpzhnadrktm fy itsms ssrbhy zhqphyfhjuxfflzpqs mm fyyew ubmlzcze hnq zoxxrprmcdz jes  gjtzo bazvh  tmp lkdas z ieykrma lo  u placg x egqj kugw lircpswb dwqrhrotfaok sz cuyycqdaazsw  bckzazqo uomh lbw hiwy x  qinfgwvfwtuzneakrjecruw ytg smakqntulqhjmkhpjs xwqqznwyjdsbvsrmh pzfihwnwydgxqfvhotuzolc y mso holmkj  nk mbehp dr fdjyep rhvxvwjjhzpv  pyhtneuzw dbrkg dev usimbmlwheeef aaruznfdvu cke ggkeku unfl jpeupytrejuhgycpqhii  cdqp foxeknd djhunxyi ggaiti prkah hsbgwra ffqshfq hoatuiq fgxt goty"), 168)
