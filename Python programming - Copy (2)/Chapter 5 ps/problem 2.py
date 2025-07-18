# Write a program to input eight numbers from the user and display all the unique numbers (once).

unique_numbers = set()

s1 = int(input("Enter your 1st no :"))
s2 = int(input("Enter your 2nd no :"))
s3 = int(input("Enter your 3rd no :"))
s4 = int(input("Enter your 4th no :"))
s5 = int(input("Enter your 5th no :"))
s6 = int(input("Enter your 6th no :"))
s7 = int(input("Enter your 7th no :"))
s8 = int(input("Enter your 8th no :"))

unique_numbers.update([s1 , s2 , s3 , s4 , s5 , s6 , s7 ,s8])

print("Unique numbers are :" , unique_numbers)