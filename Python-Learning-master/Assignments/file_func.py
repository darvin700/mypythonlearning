why * to pass t,L?

#bidding
d={}
while True:

    a=(input("Enter your name:"))
    b=(input("Enter your bid price:"))
    d.update({a: b})
    p=input("Enter Y or N for new bidding:").upper()
    if p == 'Y':
        continue
    else:
        break
print(d.items())
k=max(d.values())
for i in d:
    if d[i]==k:
        print (f"winner is {i} : {(d[i])}")


#find a string
with open("test.txt",'r+') as f:
    f.write("i am learing python pyhton")
    s=f.read()
    if s in 'python':
        print(f"python is found")


l=['dar','roy','kemi']
t=('dar','roy','kemi')
d={'name':'roy','age':25}
s="darvinroy"
with open("test.txt","w+") as f:

    f.writelines(" ".join(l))
    f.seek(0)
    dat=f.read()
    print(dat)


l=['dar','roy','kemi']
t=('dar','roy','kemi')
d={'name':'roy','age':25}
s="darvinroy"
with open("test.txt","w+") as f:
    f.write(str(d))
    f.seek(0)
    dat=f.read()
    print(dat)

#readline by line
with open("test.txt","r") as f:
    lines=f.readlines()
    n=int(input("Enter which line should be printed out of 3: "))
    print(lines[n-1])

#read and display n lines
with open("test.txt","r") as f:
    n = int(input("Enter which line should be printed out of 3: "))
    for i in range(n):
        lines=f.readline()
print(lines)


#read line and pause
with open("test.txt","r") as f:
    while True:
        for i in range(5):
            h=f.readline()
            print(h)
        o=input("Enter continue or no:").upper()
        if o == 'Y' :
            continue
        elif o != 'Y':
            break
print("content exahusted")


#-n line
#last n lines

with open("test.txt","r") as f1:
    c1=f1.readlines()
    print(c1[-2:])


#Write a Python program to read a file line by line and store it into a list.
a1=[]
with open("test.txt","r") as f1:
    for i in range(21):
        c1=f1.readline()
        a1.append(c1)

print(a1)



#Write a Python program to read a file line by line and store it into a list.
a1=[5,3,4]
with open("test.txt","r") as f1:
    words = f1.read().split()
    print(words)
    #longest_word=max(a1)
    longest_word = max(words,key=len)
print(longest_word)


#countlines
count=0
with open("test.txt","r") as f1:
    for i in f1:
        count+=1
        #f1.readline()
print(f"line is {count}")


#copy in another file
with open("test.txt",'r') as f:
    with open("test1.txt",'r+') as f1:
        f1.writelines(f)
        c = f1.readlines()
        print(c)

#count char
count=0

with open("test.txt","r") as f1:
    while True:
        count+=1
        char = f1.read(1)  # Read one character at a time
        if not char:  # Stop at end of file
            break
print(count)

d={"name":"roy",'age':41}
def dic(name,age):
    #for key,value in val:
        print(f"key value is {name} : {age}")
dic(**d)

def dic(**d):
    for key,value in d.items():
        print(f"key value is {key} : {value}")
dic(name="roy", age=41)

def l(*b):
    print(b)
a=("das","i")
l(("das","i"))


