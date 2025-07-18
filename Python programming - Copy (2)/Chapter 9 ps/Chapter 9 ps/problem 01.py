'''Write a program to read the text from a given file ‘poems.txt’ and find out
whether it contains the word ‘twinkle’.'''

f = open('poem.txt' , "r")
data = f.read()
if ("twinkle") in (data):
    print("Yes, The Word Twinkle is in the poem.txt which is", "'" , data.count("twinkle") + data.count("Twinkle"),"'" " Times"  )
f.close()
