# Repeat program 4 for a list of such words to be censored.

word = "bsdk"
word = " bhen ke lode"
word = "madarchod"


with open("list.txt", "r") as f:
    content = f.read()
    
contentNew = content.replace(word, "######")

with open("list.txt", "w") as f:
    f.write(contentNew)