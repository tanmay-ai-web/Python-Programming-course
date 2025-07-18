'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F'''



a = int(input("Enter your Marks :"))
a > 0 and a < 100



if a > 90 and a <= 100 :
    print("CONGRATULATION , You got A+ and Excellent")
    
elif a > 80 and a < 90 :
    print("You got A grade")
    
elif a > 70 and a < 80 :
    print("You got B grade")
    
elif a > 60 and a < 70 :
    print("You got C grade")
    
elif a >= 50 and a <60 :
    print("You got D grade")
    
else:
    print("Sorry, you are fail")