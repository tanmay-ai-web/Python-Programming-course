# Check that a tuple type cannot be changed in python.

a = (34, 234, "Harry")

a[2] = "Larry"   # TypeError: 'tuple' object does not support item assignment

print(a)