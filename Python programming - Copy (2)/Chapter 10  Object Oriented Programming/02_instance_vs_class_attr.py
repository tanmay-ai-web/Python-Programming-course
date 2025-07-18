class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute
print(harry.language, harry.salary)
rohan = Employee()
rohan.language = "Pyhton" # This is an instance attribute
print(rohan.language, rohan.salary)