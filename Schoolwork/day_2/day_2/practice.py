# Python Full Course for Beginners by Mosh [31:57]
students_count = 1000

# float = number with decimals
rating = 4.99

# boolean = True or False; remember the case
is_published = False

# string = sequence of characters, wrapped in double quotes
course = "Python Programming"

# Triple quotes """ can be used for multi-line strings
message = """
Hi Johnny Appleseed,

What do you think of the empire apple?

Regards,
Tiffany Williams"""

# the len() function returns no. of characters in a string (includes spaces)
# calling a function = function name followed by parentheses
# arguments = values passed to a function (in this case, the string)
print(len(course))

# access specific characters in a string with index [] (0 will return first character, 1 will return second character, and so on)
print(course[0])

# index -1 will return the last character in the string
print(course[-1])

# index range of 0:3 will get index 0,1,2 and note that the number  on left is NOT included
print(course[0:3])

# this will return a new string that is the same as the original string
print(course[0:])

# including the end index, but not the start is like [0:3]
print(course[:3])

# this will return the same as the original string
print(course[:])

