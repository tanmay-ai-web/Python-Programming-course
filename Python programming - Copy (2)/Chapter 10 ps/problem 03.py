'''Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class MyClass:
    a = 5
    
obj = MyClass()
obj.a = 0
print(MyClass.a)  # Output: 5
print(obj.a)     # Output: 0
print(MyClass.__dict__)  # Output: {'__module__': '__main__', 'a': 5, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
print(obj.__dict__)  # Output: {'a': 0}
