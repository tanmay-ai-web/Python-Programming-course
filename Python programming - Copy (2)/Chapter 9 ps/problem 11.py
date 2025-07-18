'''Write a python program to rename a file to “renamed_by_ python.txt.'''

import os
# Specify the current file name and the new file name
current_file_name = 't problem 11 rough file.txt'  # Replace with your current file name
new_file_name = 'renamed_by_python.txt'  # Desired new file name
# Rename the file
try:
    os.rename(current_file_name, new_file_name)
    print(f"File renamed from '{current_file_name}' to '{new_file_name}'.")
except FileNotFoundError:
    print(f"Error: The file '{current_file_name}' does not exist.")