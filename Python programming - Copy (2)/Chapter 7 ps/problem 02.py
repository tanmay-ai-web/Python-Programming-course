'''Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]'''


names = ["Harry", "Soham", "Sachin", "Rahul"]
for name in names :
    if name.startswith("S" or "s"):
        print("Hello" , name, "sir," , "Nice to meet you")
             
