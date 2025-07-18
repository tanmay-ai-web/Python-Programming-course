# Write a program to find out whether a given post is talking about a particular name that is also given by the user or not.

name = input("Enter your name :")

post = input("Enter your post :")
if name.lower() in post.lower() :
    print("Yes, This post is talking about" , name)
    
else:
    print("No, This post is not talking about" , name)