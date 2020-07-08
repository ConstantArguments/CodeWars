"""
Bob is preparing to pass IQ test. The most frequent task in this test is
to find out which one of the given numbers differs from the others. Bob
observed that one number usually differs from the others.
Help Bob — to check his answers, he needs a program that among the given
numbers finds one that is different in even/oddness, and return a
position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which
means indexes of the elements start from 1 (not 0)

Examples :
iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the
numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the
numbers are odd
"""

def iq_test(numbers):
    # Split string into list.
    number_list = numbers.split(" ")
    # Iterate through list, convert to int, and get index of differing.
    odd_count = 0
    even_count = 0
    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])
        if number_list[i] % 2 == 1: # Test, odd is True
            odd_index = i + 1 # Add 1 for "real" IQ test.
            odd_count += 1
        else: # Test, even is True
            even_index = i + 1 # Add 1 for "real" IQ test.
            even_count += 1
    # Determine if mostly even or odd and return index of differing item.
    if odd_count > even_count:
        return even_index
    else:
        return odd_index


print(iq_test("2 4 6 8 11"), 5)
print(iq_test("1 2 2"), 1)
print(iq_test("4 6 10 2 17 20"), 5)
print(iq_test("2 2 1"), 3)