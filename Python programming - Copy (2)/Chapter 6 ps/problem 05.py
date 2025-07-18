'''Write a program which finds out whether a given name is present in a list or not.'''


name = [ "Tanmay",
        "Harish",
        "Anjali",
        "Ramlal",
        "Kamlesh"]

a = input("Enter your Name : ")



if a.capitalize() in name :
    print("Yes, This name is available in the List")