
#Python Program to Remove the Given Key from a Dictionary

a={1: 'a', 2: 'b', 'python': 'c', 'a': 1, 'b': 2}
b = "b"
if b in a:
    del a[b]

print(a)
