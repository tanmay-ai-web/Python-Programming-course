# PROJECT 1 - SNAKE. WATER, GUN 

'''We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the user'''


'''SNAKE : 1
WATER : -1
GUN : 0 '''


import random

computer = random.choice([1, 0 , -1])

youstr = input("Enter your choice :")
youdict = { "s":1 , "w":-1 , "g":0}
reversedict = { 1 : "SNAKE" , -1 : "WATER" , 0 : "GUN"}

you = youdict[youstr]

print(f"You choose {reversedict[you]} \nComputer choose {reversedict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 1): #: (computer - you) = -2
        print("You win!")

    elif(computer ==-1 and you == 0):#: (computer - you) = -1
        print("You Lose!")

    elif(computer == 1 and you == -1):#: (computer - you) = 2
        print("You lose!")

    elif(computer ==1 and you == 0):#: (computer - you) = 1
        print("You Win!")

    elif(computer ==0 and you == -1):#: (computer - you) = 1
        print("You Win!")

    elif(computer == 0 and you == 1):#: computer - you) = -1
        print("You Lose!") 
        
    else:
        print("Something went wrong")

        # The below logic is written on the basis of the value of computer - you
 