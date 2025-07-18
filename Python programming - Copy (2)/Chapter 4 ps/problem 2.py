# Write a program to accept marks of 6 students and display them in a sorted manner 


Marks = []

m1 = int(input("Enter your Marks : "))
Marks.append(m1)
m2 = int(input("Enter your Marks : "))
Marks.append(m2)
m3 = int(input("Enter your Marks : "))
Marks.append(m3)
m4 = int(input("Enter your Marks : "))
Marks.append(m4)
m5 = int(input("Enter your Marks : "))
Marks.append(m5)
m6 = int(input("Enter your Marks : "))
Marks.append(m6)

Marks.sort()

print(Marks)
