# Create method/function so that it converts dash/underscore delimited
# words into camel casing. The first word within the output should be
# capitalized only if the original word was capitalized (known as Upper
# Camel Case, also often referred to as Pascal case).

# def to_camel_case(string)
#     array = []
#     if /-/.match(string) != nil
#         array = string.split('-')
#     elsif /_/.match(string) != nil
#         array = string.split('_')
#     else
#         array[0] = string
#     end

#     array.each do |word|
#         if array.index(word) != 0
#             word.capitalize!
#         end
#     end

#     string = array.join()
#     return string
# end

def to_camel_case(str)
    # sub "_" or "-" followed by any character except a newline,
    # and upcase that substitution.
    str.gsub(/[_-](.)/) {"#{$1.upcase}"}
end


puts(to_camel_case('')) # '', "An empty string was provided but not returned"
puts(to_camel_case("the_stealth_warrior")) # "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value"
puts(to_camel_case("The-Stealth-Warrior")) # "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value"
puts(to_camel_case("A-B-C")) # "ABC", "to_camel_case('A-B-C') did not return correct value"