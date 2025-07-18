'''Write a program to find out whether a file is identical & matches the content of
another file.'''

file1 = "this.txt"  
file2 = "this_copy.txt" 

with open(file1, 'r') as f1, open(file2, 'r') as f2:
    content1 = f1.read()
    content2 = f2.read()
    if content1 == content2:
        print("both are identical")
    else:
        print("files are different")

 

    
