# defineing a class
class Test:
    # data initialize
    # self == instance
    # __init__ == constructor
    def __init__(self, name, position, location): 
        self.name = name
        self.position = position
        self.location = location
        
    def NameAndPosition(self):
        print(self.name + ' is a ' + self.position + ' at ' + self.location +'.')
    
# call class        
a = Test('A', 'Programmer', 'Google')
b = Test('B', 'Artist', 'PIXAR')
a.NameAndPosition() # calling method
b.NameAndPosition()