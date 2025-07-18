'''Write a program to print multiplication table of a given number using while loop.'''


n = int(input("Enter the number which multiplication table you want :"))
i = 0

while i<10:
    i += 1
    print(f" {n} x {i} = ", n*i)