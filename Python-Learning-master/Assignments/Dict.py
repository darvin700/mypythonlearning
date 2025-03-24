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




