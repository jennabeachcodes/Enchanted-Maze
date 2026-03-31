#Jenna Beach
#Assignment 1 - Python
#November 21, 2023

gameName = "Enchanted Maze"

#Create function runGame
def runGame():
    print()
    charName=input("What is your character's name? ")
    
    print()
    print("Welcome " + charName + " to the " + gameName + " adventure game.")  

    #import menu
    import menu
    menu.menu()

    print()
    print("Your map shows your current location as: 0,0")    
   
    #import map
    import map    
    map.ExistIn0_0()

#call runGame funtion
runGame()

print()
print("Thank you for playing " + gameName)
    
