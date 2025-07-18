'''te a program to print the following star pattern.
 *
***
*****  odd no.'''


n = int(input("Enter a number :"))

for i in range(1 , n + 1):
    print("*" * (2 * i-1))