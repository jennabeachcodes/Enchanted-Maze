#inventory

treasure = "Treasure"
watch = "Watch"
topHat = "Hat"
skull = "Jeweled skull"
diamond = "Diamond"
gold = "Pot of Gold"

worldItems = [treasure, topHat, watch, skull, diamond, gold]
userInv = []

#[treasure at 0,0]
def takeTreasure():
    print()
    decision = input("Do you want to reach inside? Y/N ")
    if (decision.upper() == "Y"):
        # Check if the item is present in worldItems
        if (treasure in worldItems):
            worldItems.remove(treasure)
            userInv.append(treasure)
            print()
            print("You have added treasure to your inventory!")        
        else:
            print()
            print("There is nothing else to take.")
    else:
        print()
        print("You leave without searching the tree.")

#[watch at 1,0]    
def takeWatch():
    decision = input("Do you want to search the area? Y/N ")
    if (decision.upper() == "Y"):
        # Check if the item is present in worldItems
        if (watch in worldItems):
            worldItems.remove(watch)
            userInv.append(watch)
            print()
            print("You have added a watch to your inventory!")     
        else:
            print()
            print("There is nothing else to take.")
    else:
        print()
        print("You leave without searching.")
   
#[top at 1,1]
def takeHat():
    decision = input("Do you want to search the area? Y/N ")
    if (decision.upper() == "Y"):
        if (topHat in worldItems):
            worldItems.remove(topHat)
            userInv.append(topHat)
            print()
            print("You find a large golden top hat.")
            print("It appears to have once belonged to Abe Lincoln.")
            print("You add the top hat to your inventory.")            
       
        else:
            print()
            print("There is nothing else to take.")
    else:
        print()
        print("You leave without searching.")
        
#[skull at 1,2]
def takeSkull():
    decision = input("Do you want to search the area? Y/N ")
    if (decision.upper() == "Y"):
        if (skull in worldItems):
            worldItems.remove(skull)
            userInv.append(skull)
            print()
            print("You find a bejeweled skull.")          
            print("You add the skull to your inventory.")           
        else:
            print()
            print("There is nothing else to take.")
    else:
        print()
        print("You leave without searching.")
      
#[diamond at 2,1]
def takeDiamond():
    decision = input("Do you want to search the pile of ash? Y/N ")
    if (decision.upper() == "Y"):
        if (diamond in worldItems):
            worldItems.remove(diamond)
            userInv.append(diamond)
            print()         
            print("You add a diamond to your inventory.")           
        else:
            print()
            print("There is nothing else to take.")
    else:
        print()
        print("You leave without searching.")    
    
#[gold at 2,2]
def takeGold():
    decision = input("Do you want to the grass? Y/N ")
    if (decision.upper() == "Y"):        
        if (gold in worldItems):
            worldItems.remove(gold)
            userInv.append(gold)
            print()         
            print("You add a pot of gold to your inventory.")         
        else:
            print()
            print("Shining in the sun is a piece of useless metal.")
    else:
        print()
        print("You leave without searching the grass.")       

#[user's end inventory]
def endInv():
    print()
    print("You end the game with the following items:")
    if (treasure in userInv):
        print(treasure)
    if (watch in userInv):
        print(watch)
    if (topHat in userInv):
        print(topHat)
    if (skull in userInv):
        print(skull)
    if (diamond in userInv):
        print(diamond)
    if (gold in userInv):
        print(gold)
    else:
        print("None. Try again next time.")
    
    print()
    print("The following items remain in the world: " + str(worldItems))
