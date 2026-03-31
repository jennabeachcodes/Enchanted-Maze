#map for gameFile.py

#game starts at coordinates 0,0
def ExistIn0_0():
    print()
    while True:
        movement = input("What would you like to do? ")

        if (movement == "1"):
            print()
            print("You find yourself in an enchanted forest.")
            print("The light streaming around you seems to lift your spirits.")
            print("You're ready to tackle the maze.")          
            ExistIn0_0()
            break

        elif (movement == "2"):
            #go to line 48
            nav0_0()
            break

        elif (movement == "3"):
            print()
            print("You spot a hollow tree.")

            import inventory          
            inventory.takeTreasure() #line 14         
            
            ExistIn0_0()
            break

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn0_0()
            break            

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn0_0()
            break

#move around 0,0
def nav0_0():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("Ouch! You encounter a rock wall. You cannot move north.")       
        ExistIn0_0()

    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("You walk along the eastern path.")
        print("Your current location on the map is 1,0")
        #go to line 148
        ExistIn1_0()

    elif (direction.upper() in ["SOUTH", "S"]):
        print()
        print("You travel along the southern road.")        
        print("Your current location on the map is 0,1")
        #go to line 86
        ExistIn0_1()

    elif (direction.upper() in ["WEST", "W"]):
        print()
        print("Ouch! You encounter a rock wall. You cannot move west.")     
        ExistIn0_0()
        
    elif (direction == "0"):
        ExistIn0_0()

    else:
        import directionsMenu
        directionsMenu.navMenu()
        nav0_0()
#[end code for 0,0]
        
#[code for 0,1]
def ExistIn0_1():
    print()
    while True:
        movement = input("What would you like to do? ")

        if (movement == "1"):
            print()
            print("You find yourself in a pitch-dark cave.")
            print("Your eyes are unable to adapt.")
            print("You cannot see anything.")
            ExistIn0_1()

        elif (movement == "2"):        
            nav0_1()            

        elif (movement == "3"):
            print()
            print("It is too dark to see anything.")            
            ExistIn0_1()

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn0_1()

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn0_1()
        break

#move around 0,1
def nav0_1():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("You travel back north.")
        print("You are at the start of the maze.")
        print("Your current location on the map is 0,0")        
        ExistIn0_0()          

    elif (direction.upper() in ["SOUTH", "S"]) or (direction.upper() in ["WEST", "W"]) or (direction.upper() in ["EAST", "E"]):
        print()
        print("You hear the low snarls of a large ornery creature.")
        print("If you move in this direction a voracious Gruethorn will devour you whole!")
        ExistIn0_1()
        
    elif (direction == "0"):
        ExistIn0_1()
    
    else:
        import directionsMenu
        directionsMenu.navMenu()
        nav0_1()
#[end code for 0,1]      

#[code for 1,0]
def ExistIn1_0():
    print()
    while True:
        movement = input("What would you like to do? ")

        if (movement == "1"):
            print()
            print("Around you are gently sloping grassy knolls.")
            print("There is a lovely cool breeze.")
            print("You are in the foothills of a mountain range.")            
            ExistIn1_0()

        elif (movement == "2"):            
            nav1_0()       
           
        elif (movement == "3"):

            print()                        
            import inventory          
            inventory.takeWatch() #line 32         
            
            ExistIn1_0()
            break
        
        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn1_0()
            break  

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn1_0()
        break

#move around 1,0
def nav1_0():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("The northern mountain range is impassable.")
        print("You hear a faint voice on the wind: You shall not pass.")
        ExistIn1_0()
        
    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("You kick off your shoes and start to swim into the setting sun...")
        print("You then change your mind and return to shore.")
        print("You put your shoes back on.")
        ExistIn1_0()
        
    elif (direction.upper() in ["WEST", "W"]):
        print()
        print("You travel back along the western path.")
        print("The map shows you are at the start of the maze.")
        print("Your current location on the map is 0,0")     
        ExistIn0_0()

    elif (direction.upper() in ["SOUTH", "S"]):
        print()
        print("You travel along the south road.")
        print("Your current location on the map is 1,1")
        #go to line 229
        ExistIn1_1()
        
    elif direction == "0":
        ExistIn1_0()

    else:
        import directionsMenu
        directionsMenu.navMenu()
        nav1_0()      
#[end code for 1,0]

#[code for 1,1]
def ExistIn1_1():
    print()
    while True:
        movement = input("What would you like to do? ")
        if (movement == "1"):
            print()
            print("You find yourself in the middle of a deep canyon.")
            print("All around you are steep vertical sides.")                      
            ExistIn1_1()

        elif (movement == "2"):            
            nav1_1()       
           
        elif (movement == "3"):
            print()
            import inventory          
            inventory.takeHat()#line 49 
            ExistIn1_1()
            break

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn1_1()
            break  

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn1_1()
        break
#move around 1,1
def nav1_1():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("You travel back north.")
        print("Your current location on the map is 1,0")
        #go to line 148
        ExistIn1_0()
        
    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("You travel along the path east.")
        print("Your current location on the map is 2,1")
        #go to line 396
        ExistIn2_1()
        
    elif (direction.upper() in ["WEST", "W"]):
        print()
        print("You cannot travel west.")    
        #go to line 229
        ExistIn1_1()

    elif direction.upper() in ["SOUTH", "S"]:
        print()
        print("You travel along the south path.")
        print("Your current location on the map is 1,2")
        #go to line 305
        ExistIn1_2()

    elif (direction == "0"):
        ExistIn1_1()

    else:
         import directionsMenu
         directionsMenu.navMenu()
         nav1_1()
#[end code for 1,1]
         
#[code for 1,2]
def ExistIn1_2():
    print()
    while True:
        movement = input("What would you like to do? ")
        if (movement == "1"):
            print()
            print("Ew! What is that smell?")
            print("You find yourself in a swamp.")            
            ExistIn1_2()

        elif (movement == "2"):            
            nav1_2()       
           
        elif (movement == "3"):
            print()
            import inventory          
            inventory.takeSkull()#line 68
            ExistIn1_2()
            break

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn1_2()
            break  

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn1_2()
        break
#move around 1,2
def nav1_2():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("You travel back north.")
        print("Your current location on the map is 1,1")
        #go to line 229
        ExistIn1_1()
        
    elif (direction.upper() in ["WEST", "W"]):
        print()
        print("There is a mysterious portal to the east.")
        #go to line 379
        portalChoice()         
                
    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("You travel along the eastern path.")
        print("Your current location on the map is 2,2")
        #go to line 473
        ExistIn2_2()

    elif (direction.upper() in ["SOUTH", "S"]):
        print()
        print("This seems to be the end of the world.")
        print("You cannot travel south.")    
        ExistIn1_2()

    elif (direction == "0"):
        ExistIn1_2()

    else:
         import directionsMenu
         directionsMenu.navMenu()
         nav1_2()

#[portal at 1,2]
def portalChoice():
    choice = input("Do you want to enter the portal? Y/N ")
    if (choice.upper() == "Y"):
        print()
        print("You enter the portal.")
        print("This place seems familiar.")
        #go to line 4
        ExistIn0_0()
    else:
        print()
        print("You back away from the eerie portal.")
        #go to line 305
        ExistIn1_2()
#[end code for 1,2]

#[code for 2,1]
def ExistIn2_1():
    print()
    while True:
        movement = input("What would you like to do? ")
        if (movement == "1"):
            print()
            print("Ash falls from the sky. It makes breathing difficult.")
            print("You find yourself in a volanic waste land")           
            ExistIn2_1()

        elif (movement == "2"):            
            nav2_1()       
           
        elif (movement == "3"):
            print()
            print("You encounter a large pile of ash.")
            print()
            import inventory          
            inventory.takeDiamond() #line 85
            ExistIn2_1()

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn2_1()
            break  

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn2_1()
        break
#move around 2,1
def nav2_1():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print()
        print("You encounter the ocean.")
        print("You see a sea serpent in the water.")
        print("You decide to stay on land.")
        ExistIn2_1()
        
    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("To the east is large snowy mountain range.")
        print("You forgot your skis.")
        print("You cannot travel east.")     
        ExistIn2_1()
        
    elif (direction.upper() in ["WEST", "W"]):
        print()
        print("You travel along the path west.")
        print("Your current location on the map is 1,1")
        #go to line 229
        ExistIn1_1()

    elif (direction.upper() in ["SOUTH", "S"]):
        print()
        print("You travel south along the path.")
        print("Your current location on the map is 2,2")
        #go to line 473
        ExistIn2_2()

    elif (direction == "0"):
        ExistIn2_1()

    else:
         import directionsMenu
         directionsMenu.navMenu()
         nav2_1()        
#[end code for 2,1]

#[code for 2,2]
def ExistIn2_2():
    print()
    while True:
        movement = input("What would you like to do? ")
        if (movement == "1"):
            print()
            print("You arrive at a pleasant grass plain.")
            print("The land is dotted with vibrant wildflowers.")
            ExistIn2_2()
            break

        elif (movement == "2"):            
            nav2_2()       
           
        elif (movement == "3"):
            print()
            print("You spot something shining in the grass.")
            print()
            
            import inventory          
            inventory.takeGold() #line 101
            
            ExistIn2_2()

        elif (movement == "4"):
            import directionsMenu
            directionsMenu.navMenu()
            ExistIn2_2()
            break  

        elif (movement == "0"):
            break

        else:
            import menu
            menu.menu()
            ExistIn2_2()
        break
def nav2_2():
    print()
    direction = input("In what direction would you like to move? ")

    if (direction.upper() in ["NORTH", "N"]):
        print("You travel north along the path.")
        print("Your current location on the map is 2,1")
        #go to line 395
        ExistIn2_1()
        
    elif (direction.upper() in ["EAST", "E"]):
        print()
        print("There is a deep chasm in the ground.")

        choice = input("Do you want to enter the chasm? Y/N ")
        
        if (choice.upper() == "Y"):
            print()
            print("You make a spectacular swan dive.")
            print("You vanish into a void, never to be seen again.")
            print("Game over.")
        else:
            print()
            print("You back away from the edge.")
            ExistIn2_2()       
                  
    elif (direction.upper() in ["WEST", "W"]):
        print("You travel along a path heading west.")
        print("Your current location on the map is 1,2")
        #go to line 305
        ExistIn1_2()

    elif (direction.upper() in ["SOUTH", "S"]):
        print()
        print("There is a glowing exit portal to the south.")
        print("You walk through the portal without delay.")

        import inventory
        inventory.endInv() #line 117     
        
    elif (direction == "0"):
        ExistIn2_2()

    else:
         import directionsMenu
         directionsMenu.navMenu()
         nav2_2()        
#[end code for 2,2]  
