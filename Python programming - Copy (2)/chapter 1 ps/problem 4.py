'''question-------Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.'''







import os

# Specify the directory path
directory_path = '/python programming/chapter 1'

# List all entries in the specified directory
entries = os.listdir(directory_path)

# Print the entries
print("Contents of", directory_path)
for entry in entries:
    print(entry)
