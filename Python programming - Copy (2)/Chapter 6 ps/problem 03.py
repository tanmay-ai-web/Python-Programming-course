'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''





a = input("Enter your comment :").lower()


if ("make a lot of money" in a or "buy now" in a or "subscribe this" in a or "click this" in a ):
    print("This is a spam message")
    
else:
    print("This is not a spam")