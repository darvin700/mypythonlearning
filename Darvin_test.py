'''s=input("enter your string:")
l=[]
for i in s:
    if i in l:
        l.append('$')

    else:
        l.append(i)
print(''.join(l))'''
from logging import exception

'''s=input("enter your string:")
char=s[0]
s=s.replace(char,'$')
l=list(s)
l[0]=char
print(''.join(l))'''
'''
x = 'abc'
y = 'xyz'
print(x + ' ' + y)
a = y[0:2] + x[2:]
b = x[0:2] + y[2:]

print(a + ' ' + b)'''

'''s=input("enter your string:")
if len(s)>=3:
    if s[-3:] == 'ing':
        print(s+'ly')
    else:
        print(s+'ing')
else:
    print("enter string length greater than 2 ")'''

'''s='lyrics is not that poor!
l=s.split()
a=s.find("not")
b=s.find("poor")
if s.find("not") != -1:
    if s.find("poor") != -1:
        ns=s.replace(s[a:b+4],"good")
        print(ns)
        '''
        
'''s='lyrics is not that poor!'
dic={}

for i in s:

    if i in dic:
        print("i am if success")
        dic[i] +=1
    else:
        dic[i]=1

print(dic)

n='4'

for k,v in dic.items():
    print(k + ':', v)'''

'''l=["dargfghffhgfgdsfsdf",'hemilusroy','darvin',"royyyy"]
maxx=l[0]
long=len(l[0])

for i in range(1,len(l)):
    if long < len(l[i]):
        long=len(l[i])
        maxx=l[i]

print (f" max word is {maxx}")

l = ["dargfghffhgfgdsfsdf", 'hemilusroy', 'darvin', "royyyy"]
maxx = l[0]  # Assume first word is longest initially
long = len(l[0])

for i in range(1, len(l)):  # Start from index 1
    if len(l[i]) > long:  # Use '>' to pick the first longest word
        long = len(l[i])
        maxx = l[i]

print(f"Max word is {maxx}")'''

'''n=int(input("enter index to remove:"))
s="Iamanindian"
print(s[:n]+s[n+1:])'''



'''class par:
    num=10
    def __int__(self,b):
        self.b=b
    def sum(self):
        return self.num+self.b

class chil(par):
    num1=15
    def __init__(self,c):
        super().__init__(b=10)
        self.z=c

    def sum1(self):
        print(self.z,self.b,self.num,self.num1)
        return self.z+self.b+self.num+self.num1+self.sum()

chill=chil(10)
print(chill.sum1())'''

class par:
    def __init__(self, b):
        self.num = 10
        self.b = b

    def sum(self):
        return self.num + self.b

class chil(par):
    def __init__(self, c):
        super().__init__(b=5)  # Passing a value for `b` to parent class
        self.num1 = 15
        self.z = c

    def sum1(self):
        print(self.z, self.b, self.num, self.num1)
        return self.z + self.b + self.num + self.num1 + self.sum()

chill = chil(10)
#print(chill.sum1())
'''
f=open("test.txt")
c=f.readlines()
f2=open("test.txt","w")
for line in reversed(c):
    f2.write(line)
'''




'''
line=f.readline()
while line!="":
    print(line)
    line=f.readline()
f.close()'''

#print(f.read(5))
#f.seek(5,1)
#print(f.read(5))


n=2

try:
    if n != 3:
        raise Exception("not 3")
#except Exception as e:
except:
    print("exception thrown")
    #print(f"value of n is: {e}")
print("value of n",n)

a="darvin"
b=42
c=10
x=f"{a}{b}"
print(x)
print("{}".format(x))
print(f"{x}")
print("value of x %s" %x)

g=10
def f(d):
    global g
    print(id(g))
    g=20
    #print(id(g))
    #print(id(d))
    d.append(2)
    print(id(d))

d=[11]
f(d)
print(id(d))

























































