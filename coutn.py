from logging import exception

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
a=5
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
def f(d):
    for i in d:
        #print(i)
        if i == a :
            return 1
    return i



s=f(dic1)
#print(s)

try:
    d=input("enter no")
    d=d/10
except:
    print("Caught error!")

print("continue")
