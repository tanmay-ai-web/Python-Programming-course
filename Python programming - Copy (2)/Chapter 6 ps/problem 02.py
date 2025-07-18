'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''


phy = int(input("Enter your physics marks :"))
chem = int(input("Enter your chemistry marks :"))
maths = int(input("Enter you maths marks :"))

total = (((phy + chem + maths )/300) * 100)

if phy > 33 and maths > 33 and chem > 33 and total > 40:
    print("Congratulation , You are pass , You got" , total , "percentage" )