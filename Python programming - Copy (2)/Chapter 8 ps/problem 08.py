'''Write a python function to print multiplication table of a given number.'''

def mul_tab():
    n = int(input("Enter a number :"))
    
    
    for i in range(1, 11):
        print(f"{n} x {i} =", n*i)
        



mul_tab()