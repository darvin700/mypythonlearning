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




