#OOP assignment

#initialize a packback class
class Packback: 
    #Initialize a constructor
    def __init__(self, size, color):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
        print("a " + size + ' ' + color + ' packback')

    #Create a method that'll control opening and closing 
    def openCloseBag(self, state):
        if state == "open" or state =="Open":
            self.open = True
            print("Packback is open")
        
        elif state == "close" or state == "Close":
            self.open = False
            print("PackBack closed")
    
    #Create a method that'll put stuff into the Packback
    def putin(self, item):
        if self.open == True:
            self.items.append(item)
            print(item + " has been added to bag")
        
        else: 
            print("Can't add item because bag is closed")
    
    #Create a method that'll take stuff into the Packback
    def takeout(self, item):
        if self.open == True:
            if item in self.items:
                self.items.remove(item)
                print(item + " has been removed")
            else: 
                print(item + " isn't in bag")

        else: 
            print("Can't remove item cause packback is closed")


#running the packback class
packback1 = Packback("small", "blue")
packback2 = Packback("medium", "red")
packback3 = Packback("large", "green")

packback3.openCloseBag("Open")
packback3.putin("lunch")
packback3.putin("jacket")
packback3.openCloseBag("close")
packback3.openCloseBag("open")
packback3.takeout("jacket")
packback3.openCloseBag("close")