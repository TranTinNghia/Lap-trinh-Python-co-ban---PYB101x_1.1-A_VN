class Bike:
    def __init__(self, colour, price):
        self.colour = colour
        self.price = price
    def __str__(self):
        return "{0} {1}".format(self.colour, self.price)
testOne = Bike("Blue",89.99)
testTwo = Bike("Purple",25.0)
print(testOne)
print(testTwo)