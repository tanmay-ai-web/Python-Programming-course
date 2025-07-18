'''Write a program using functions to find greatest of three numbers.'''


def goat():
    a = int(input("Enter a number 'a' :"))
    b = int(input("Enter a number 'b' :"))
    c = int(input("Enter a number 'c' :"))
    
    if a > b and a > c:
        print("'a' is greatest")
        
    elif b > a and b > c :
        print("'b' is greatest")
        
    else:
        print("'c' is greatest")
        
        
goat()
goat()
goat()
