# Write a program to find the greatest of four numbers entered by the user.



a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
c = int(input("Enter the number : "))

if a>b and a>c :
    print("The greatest of all time is 'a': " , a)
    
if b>a and b>c :
    print("The greatest of all time is 'b': " , b)
    
if c>a and c>b :
    print("The greatest of all time is 'c': " , c)