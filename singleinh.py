class vehicle:
    def __init__ (self,color):
        self.color = color

    def display(self):
        print('vehicle: ',self.color)

class TwoWheeler(vehicle):
    def __init__ (self,number,color):
        #vehicle.__init__(self,color)
        super()

        self.number = number
        self.color = color

        

    def printing(self):
        print(self.color ,'and', self.number)


obj1 = TwoWheeler(24,'pink')
obj1.display()

obj1.printing()
