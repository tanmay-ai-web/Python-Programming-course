'''How do you prevent a python print() function to print a new line at the end.'''

# To prevent this and avoid a new line, use the end parameter of print() like this :

print("Hello" , end = "")
print("World")


# If you want a space instead of a newline, do:

print("Hello" , end =  " ")
print("World")