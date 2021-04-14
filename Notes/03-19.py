"""
Working with Strings and Iteration
"""

# Find character at an index
def char_at_index(string, index):
    return string[index]

char_at_index("Saint Louis", 3) # "i"

# Find length of string manually
def string_length(string):
    length = 0
    for char in string:
        length = length + 1
    return length

string_length("Decorah") # 7

# Find if a character is in a string manually
def char_in_str(string, character):
    found = False
    for char in string:
        if char == character:
            found = True
    return found

char_in_str("Chicago", "c") # True
char_in_str("Miami", "x") # False

# Determine if course name is a CS course
def is_course_cs(course):
    is_cs = False
    if course[:2] == "CS" or course[:2] == "cs":
        is_cs = True
    return is_cs
