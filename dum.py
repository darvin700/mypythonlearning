class par:
    num=10
    def __init__(self,b):
        #self.num=10
        self.b=b
    def sum(self):
        return self.num+self.b

class chil(par):
    num1=15
    def __init__(self,c):
        super().__init__(c)
        #self.num1=15
        self.z=c

    def sum1(self,p):
        l=p
        print(self.z,self.b,self.num,self.num1,l)
        return self.z+self.b+self.num+self.num1+self.sum()
#parr=par(50)
#print(f"parant b {parr.b}")
chill=chil(10)
print(chill.sum1(1000))