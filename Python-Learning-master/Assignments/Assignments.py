#string and list on 18/03
lis=["foo", "bar", "baz"]
lis.append("bar")
print(lis)
print(lis.index("bar"))
print("count of word bar:",lis.count("bar"))

s=[]
if len(s)==0 or not s:
    print(f"list is empty")
else:
    print("list is not empty")

x=lis.pop()
print(f"Last item of list : {x}")
print(f"Last item of list : {lis[-1]}")

lis_cop=lis.copy()
print(lis_cop,id(lis),id(lis_cop))

lis_cop=lis
print(lis_cop,id(lis),id(lis_cop))

l=["a","b","a","a","c","f","f"]
s="dar vin roy"
print(l.count("a"))
print("+".join(l))
print(s.split(" "))
l.remove("a")
print(f"print after removal :{l}")

buffer5 = [1,2,3,4,5]
print(len(buffer5))