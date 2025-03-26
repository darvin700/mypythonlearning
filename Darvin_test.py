


class SomeBaseClass:
    def __init__(self):
        print("Constructor of SomeBaseClass is called")

    def printhello(self):
        print("helloworld")


class UnsuperChild(SomeBaseClass):
    def __init__(self):
        print("Constructor of UnsuperChild is called")
        super(UnsuperChild, self).__init__()


class SuperChild(UnsuperChild):
    def __init__(self):
        print("Constructor of SuperChild is called")
        super(SuperChild, self).__init__()


#         super().__init__()
#         super(SomeBaseClass,self).__init__()
#         super(UnsuperChild,self).__init__()

# a=SomeBaseClass()
# b=UnsuperChild()
c = SuperChild()  # str1="python"