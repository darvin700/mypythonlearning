#Remove duplicate values of a list
a=[1,2,3,4,1,2,3,10]
#a=set(a)
#a=list(a)
print(a)
a=list(set(a))
print(a)


s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
s2 = set( ['abc', 12, 'b', 'car', 7, 10, 12 ])
s3 = set( [12, 14, 12, 'ab'] )
b=list(s2)

#print b in s2

for i in b:
    if i == "b":
        print(f"value is {i}")

j=len(b)
for i in b:
    j-=1
    if i == "ab":
        print(f"value is {i}")
        break
    elif j == 0:
        print("ab is not in list s2")

s2.discard(12)
print(s2)

#assignment
s = (s1 ^ s2 ^ s3) - ((s1 & s2) | (s2 & s3) | (s1 & s3))
print(s)

#symetric

n="12345"
m=123,13,45

n=set(n)
m=set(m)

print(m,n)
print((n^m))



#Take a user input as a animal name and return the height of that animal
heights={'belgian horse': 162,'tiger': 168, 'cat': 58, 'dog': 57, 'cow': 59, 'lion': 109}
s=input("Enter animal name(hors,dog,tiger,cat,cow,lion):")
for i in heights:
    if i == s:
        print(heights[i])
        break



# initializing Dictionary
d = { 'a' : 1 , 'b' : 2 }
print ("The value associated with 'c' is : ")
d['c']=5
print (d['c'])
print(" learning python is fun")
print(" python is awsome")

#change the key,valye

d = { 'a' : 1 , 'b' : 2,'c': 'python' }
l=[]
k=[]
#print(d.items())
for key,value in d.items():
    l.append(key)
    k.append(value)
m=zip(k,l)
print(dict(m))

#merge teo dict
a= {1: 'a', 2: 'b', 'python': 'c'}
b={ 'a' : 1 , 'b' : 2 }
c={}
a.update(b)
print(a)

#Python Program to Check if a Given Key Exists in a Dictionary or Not*
a={1: 'a', 2: 'b', 'python': 'c', 'a': 1, 'b': 2}
print(a.get("d","it does not exist"))

#Python Program to Multiply All the Items in a Dictionary
d = { 'a' : 10 , 'b' : 20 }
d["c"]=10
k=1
print(d)
for i,j in d.items():
    print(j)
    k=k*j
print(k)


#Python Program to Remove the Given Key from a Dictionary
a={1: 'a', 2: 'b', 'python': 'c', 'a': 1, 'b': 2}
a.pop("python")
print(a)

#Python Program to Remove the Given Key from a Dictionary

a={1: 'a', 2: 'b', 'python': 'c', 'a': 1, 'b': 2}

for i in a:
    print(a[i])




