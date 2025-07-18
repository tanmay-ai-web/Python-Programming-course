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

if((computer - you) == -1 or  (computer - you) == 2 ):
        print("You lose!")
else:
    print("You win!") 