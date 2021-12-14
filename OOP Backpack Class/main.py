# Object Orientated Programing Backpack Class by Elijah

# Backpack Class
class Backpack():
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.items = []
        self.open = False
    
    def openBag(self): # open bag
        if self.open == True: # checks to see if its already open
            pass
        else:
            self.open = True
            print("The backpack has been opened!")
    
    def closeBag(self): # close bag
        if self.open == False: # checks to see if its already closed
            pass
        else:
            self.open = False
            print("The backpack has been closed!")
    
    def putin(self, item): # add an item to the backpack
        if self.open == True: # only if its open
            self.items.append(item)
            print("The backpack has been tampered with! An item was added!")
    
    def takeout(self, item): # remove an item from the backpack
        if self.open == True and item in self.items: # only if its open and the item is in the backpack
            self.items.remove(item)
            print("The package was removed!")

# backpacks
smallBlueBackpack = Backpack("blue", "small")
mediumRedBackpack = Backpack("red", "medium")
largeGreenBackpack = Backpack("green", "large")

# backpack method call
largeGreenBackpack.openBag()
largeGreenBackpack.putin("lunch")
largeGreenBackpack.putin("jacket")
largeGreenBackpack.closeBag()
largeGreenBackpack.openBag()
largeGreenBackpack.takeout("jacket")
largeGreenBackpack.closeBag()