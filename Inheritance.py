class Animal:
    age = None
    
    def __init__(self, age):
        self.age = age
    def toString(self):
        print("Age: " + str(self.age))

class Cat(Animal):
    
    def __init__(self, age, colour):
        super().__init__(age)
        self.colour = colour

don = Animal(10)
Joe = Cat(12, "blue")
don.toString()
Joe.toString()
