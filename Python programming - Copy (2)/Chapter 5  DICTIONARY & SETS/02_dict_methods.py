marks = {
    "Tanmay" : 80,
    "Devdeep" : 76,
    "Ayush" : 15,
    0 : "Harshit"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ayush" : 45 , "Paridhi": 80 })
print(marks)

print(marks.get("Tanmay2")) # prints none
print(marks["Tanmay2"]) # Returns an error