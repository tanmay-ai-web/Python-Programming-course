'''Can you change the self-parameter inside a class to something else (say
“tanmay”). Try changing self to “slf” or “tanmay” and see the effects.'''

class MyClass:
    def __init__(tanmay, value):
        tanmay.value = value

    def display(tanmay):
        print(tanmay.value)

obj = MyClass(10)
obj.display()
