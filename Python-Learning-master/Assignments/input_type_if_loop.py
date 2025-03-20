#add two digits
x=input("enter two digit number:")
a,b=x
a=int(a)
b=int(b)
print( "addition is :" , (a+b))


#BMI calculation
x=float(input("enter weight in KG:"))
y=float(input("enter height in cm:"))
BMI = int(x / y ** 2)
print(f"BMI is {BMI}")

#age in days,weeks,months
age=int(input("enter your age:"))
total_days_left=(90-age)*365
weeks =int((90-age) * 52)
months = int((90-age) * 12)
print(f"you have {total_days_left} days, {weeks} weeks and {months} months left")

#BMI calculation and category
x=float(input("enter weight in KG:"))
y=float(input("enter height in cm:"))
BMI = int(x / y ** 2)
#print(f"BMI is {BMI}")

if BMI <= 18:
    print("\bYour BMI is 18, you are underweight.")
elif BMI <=22 and BMI > 18:
    print("\bYour BMI is 22, you have a normal weight." )
elif BMI <=28 and BMI > 22 :
    print("\bYour BMI is 28, you are slightly overweight." )
elif BMI<=33 and BMI > 28 :
    print("\bYour BMI is 33, you are obese.")
elif BMI > 33 :
    print("\bYour BMI is 40, you are clinically obese.")


#pizza order
x = input("enter ur pizza size(S=small,M=medium,L=large: ").upper()
y = input("enter Y or N for add_pepperoni: ").upper()
z = input("enter Y or N for extra_cheese: ").upper()

if x=='S':
    if (y=='Y') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15+2+1
        print(f"Your final bill is {bill} ")
    if (y=='Y') and (z=='N'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 2
        print(f"Your final bill is {bill} ")
    if (y=='N') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 1
        print(f"Your final bill is {bill} ")
if x=='M':
    if (y=='Y') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15+3+1
        print(f"Your final bill is {bill} ")
    if (y=='Y') and (z=='N'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 3
        print(f"Your final bill is {bill} ")
    if (y=='N') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 1
        print(f"Your final bill is {bill} ")
if x=='L':
    if (y=='Y') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15+3+1
        print(f"Your final bill is {bill} ")
    if (y=='Y') and (z=='N'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 3
        print(f"Your final bill is {bill} ")
    if (y=='N') and (z=='Y'):
        print(f"size =  {x} add_pepperoni = {y} extra_cheese = {z} ")
        bill = 15 + 1
        print(f"Your final bill is {bill} ")

print("Enjoy the Pizza Buddy")


#driver insured or not
ms = input("Enter marital status y or n :").upper()
if ms == "Y":
    print ("Driver need to be insured")
else:
    age= int(input("enter your age:"))
    if age > 25:
        sex=input("Enter your sex M or F :").upper()
        if (sex == "M" and age > 30) or (sex == "F" and age > 25):
            print("Driver need to be insured")
        else:
            print("Driver need NOT be insured ")
    else:
        print("Driver need NOT be insured")


#odd or even
number=int(input("Enter the number to know odd or even:"))
if number%2==0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")



#leap or not
number=int(input("Enter the number to know odd or even:"))
if (number%4 == 0):
    if (number % 100 == 0):
        if(number % 400 == 0):
            print(f"{number} is leap")
        else:
            print(f"{number} is not leap")
    else:
        print(f"{number} is leap")

else:
    print(f"{number} is not leap")


#by 7 but are not a multiple of 5
l=[]
for i in range(2000,32001):
    if (i % 7==0) and (i%5!=0):
        l.append(i)
        if i==3200:
            break
    else:
        continue
print(l)


#An input string is valid
s = "{[]}"
s=",".join(s)
lis=s.split(',')
print(lis)
print(lis[0],lis[1])
print(lis[-1])
if (lis[0]==lis[1]) or (lis[0]==lis[-1]):
    print(True)
else:
    print(False)


















