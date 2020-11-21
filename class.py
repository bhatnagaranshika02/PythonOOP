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
print(Demo.i)
print(d.i)
print(d.personal())
print(Demo.personal())
print(d.display())
        
