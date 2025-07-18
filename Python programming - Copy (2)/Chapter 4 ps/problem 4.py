# Write a program to sum a list with 4 numbers. 


sum_four_numbers = []

sfn1 = int(input("Enter your 1st number : "))
sum_four_numbers.append(sfn1)
sfn2 = int(input("Enter your 2nd number : "))
sum_four_numbers.append(sfn2)
sfn3 = int(input("Enter your 3rd number : "))
sum_four_numbers.append(sfn3)
sfn4 = int(input("Enter your 4th number : "))
sum_four_numbers.append(sfn4)

print(sum_four_numbers)

print(sum(sum_four_numbers))