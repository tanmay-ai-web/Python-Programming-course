# Replace the double space from problem 3 with single spaces.



Name = "tanmay is very honest person , make him the dictator  of the world"

if "  " in Name :
    print("Double space found in the name:", Name.find("  "))

else:
    print("No double space found in the Name")



    # now we are going to replace the double space in the text with single space


new_text = Name.replace("  "," ")

print("text after removing the double space :" , new_text)