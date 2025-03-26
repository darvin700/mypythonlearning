class name:
    def __init__(self,a):
        print("First class")
        self.a=a
    def prin(self):
        print(self.a ,"whats my name")
    def __str__(self):
        print("+++++")
        return self.a + "whahts my name"


objj=name("roy")
print(objj.a)
objj.a="darvin"
print(objj.a)
objj.prin()
occ=name(objj.a)

print(occ.a)
print(occ)

class circle:
    def __init__(self,radius):
        self.pi=3.14
        self.radius=radius

    def __str__(self):
        return f"{self.pi * self.radius **2}"

area=circle(35)
print(area)

class List:
    def __init__(self):
        self.data = []

    def append(self, element):
        """Adds an element to the list."""
        self.data.append(element)
        print(f"{element} added successfully!")

    def delete(self, element):

        if element in self.data:
            self.data.remove(element)
            print(f"{element} removed successfully!")
        else:
            print(f"{element} not found in the list.")

    def display(self):

        if self.data:
            print("Current List:", self.data)
        else:
            print("The list is empty.")


a = List()


a.append(10)
a.append(20)
a.append(30)
a.display()
a.delete(20)
a.display()
a.append(40)
a.display()

class stud_record:
    def __init__(self,name,mark,mark2,roll):
        self.name = name
        self.mark = mark
        self.mark2= mark2
        self.roll = roll

    def get_name(self):
        print(f"roll number is {self.roll}","From Parant")

    def display(self):
        total= self.mark+self.mark2
        print(f" {self.name} total mark is {total}","from parant")

    def __str__(self):
        return f"{self.name} is added and mark is {self.mark} , {self.mark2} " + "from parant"

class xam_result(stud_record):
    def __init_(self,name,mark,mark2):
        stud_record.__init__(self,name,mark,mark2,roll)
        self.roll= 25

    def dis(self):
        print("child display====",self.name,"from child")
        print("I am child")


#stud1=stud_record("darvin",65,78,21)
#print(stud1)

'''stud2= stud_record("kemi",98,92)
print(stud2)
stud2.display()
stud1.display())
stud1.name="roy"
print(stud1.name)
#print(stud1)'''

ch=xam_result("rrr",1,1,22)
#ch.name="ttt"
print(ch.roll)


print(help(xam_result))




