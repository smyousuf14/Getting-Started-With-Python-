class Car:
    
    # Default Constructor
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def toString(self):
        print("Name: " + self.name + " ID: " + str(self.ID))

honda = Car("Honda", 1)
Toyota = Car("Toyota", 2)

honda.toString()
Toyota.toString()
