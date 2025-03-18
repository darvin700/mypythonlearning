a = 20
b= 30
#print("olda %d oldb %d"%(a,b))
a = a + b
b= a - b
a= a-b

#print(f"newa is {a} \nnewb is {b}")

x =40
y = 50
#print("oldx %d oldy %d"%(x,y))
z=x
x=y
y=z
#print(f"newx is {x} \nnewy is {y}")

print(chr(65))

a = 100
b = 300
print(f"old_a is {a} old_b is {b}")
a,b=b,a
print(a,b)

name={"dar","dar","roy"}
print(name)
print(type(name))
name=(1,2,3)
print(type(name))


n=[1,2]
print(type(n))
n.append(6)
print(n)

a=10
b=10
#a=a+8+b
print(f"a value is {a}")
print(id(b),id(a))


i="Python"
j="python"
if i is j:
    print(True)
    print(id(i), id(j))
else:
    print(False)
    print(id(i),id(j))

b="ball"
print("b value is %s" %b)




print (5*"python")
print ('5'+"python")
print (3%4)
x=-10
print(f"value of x is {abs(x)}")
print(f"value of x is {x}")

print (2**-3)

name="darvinroy"
print(f" display from {name[2:6:1]}")

print(name.upper())

print(type(name))
print(dir(name))
print(help(str))
print(dir(__builtins__))
