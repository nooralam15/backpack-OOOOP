#OOP assignment

#initialize a packback class
class Packback: 
    #Initialize a constructor
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    #Create a method that'll control opening and closing 
    def openCloseBag(self, state):
        if state == "open" or state =="Open":
            self.open = True
            print("Packback is open")
        
        elif state == "close" or state == "Close":
            self.open = False
            print("PackBack closed")