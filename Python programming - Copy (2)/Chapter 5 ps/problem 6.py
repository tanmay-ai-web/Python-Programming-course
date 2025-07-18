'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''


fav_lang = {}

# Input from 4 friends
friend1 = input("Enter your name: ")
lang1 = input("Enter your favorite language: ")
fav_lang[friend1] = lang1

friend2 = input("Enter your name: ")
lang2 = input("Enter your favorite language: ")
fav_lang[friend2] = lang2

friend3 = input("Enter your name: ")
lang3 = input("Enter your favorite language: ")
fav_lang[friend3] = lang3

friend4 = input("Enter your name: ")
lang4 = input("Enter your favorite language: ")
fav_lang[friend4] = lang4

# Display the dictionary
print("\nFavorite Languages Dictionary:")
print(fav_lang)


