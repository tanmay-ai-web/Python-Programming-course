'''Write a program to wipe out the content of a file using python'''

with open("prblm_10_file.txt", "w") as f1:
    content1 = f1.write("")
print("Content of the file wiped out successfully.")


# now file - prblm_10_file.txt is empty
# when you write something in prblm_10_file.txt,
# and after that if you run this code, 
# it will wipe out the content of the file.