"""
Class April 12
"""
##########
# TUPLES #
##########

# Define a tuple
student = ("Alex Doe", 12345, ["CS150", "PAIDEIA112"])

# Get a specific item by index
print(student[0]) # Prints Alex Doe

# Get a slice of the tuple, same method as lists
print(student[1:]) # Prints items from 2nd item onwards

#
# Tuples are not mutable
#

# For example, try to change the value of item at index 0

# If we had this collection as a list, it would work:
student_as_list = ["Alex Doe", 12345, ["CS150", "PAIDEIA112"]]
student_as_list[0] = "Alex Johnson" # This is a valid operation

# However, tuples do not allow for this:
# student[0] = "Alex Johnson"

# This will produce an error: "Object does not support item assignment"
# Use tuples when you want to create a collection of data which will
# NOT be changed after creation

#
# Syntax
#

# Parentheses: not actually necessary
tuple_without_parentheses = "Alex Doe", 12345, ["CS150", "PAIDEIA112"]
print(f"With (): {student}\nWithout (): {tuple_without_parentheses}")



# # # # # # # # # #
# File Operations #
# # # # # # # # # #

# Open a file
my_file = open("data.txt", "w")
my_file.close()

