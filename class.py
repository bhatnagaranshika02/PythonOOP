class Demo:
    i = 10

    @classmethod
    def personal(cls):
        Demo.i +=1

    def __init__ (self,l,b):
        self.l = l
        self.b = b
        print(Demo.i)

    def display(self):
        return self.l * self.b


d= Demo(10,20)
d1 = Demo(30,40)
print(Demo.i)
print(d.i)
print(d.personal())
print(Demo.personal())
print(d.display())
d=d1
print(d.display())
print(d1.display())
print(Demo.__dict__)
print(Demo.__name__)
print(Demo.__base__)
print(Demo.__doc__)
        
