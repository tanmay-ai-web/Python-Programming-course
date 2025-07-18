'''Create a class “Programmer” for storing information of few programmers
working at Microsoft.'''
class Programmer:
    company = "Microsoft"
    def __init__(self, name, age, pin):
        self.name = name
        self.age = age
        self.pin = pin
        
p = Programmer("Tanmay", 18, 474003)
print(p.name, p.age, p.pin, p.company) 