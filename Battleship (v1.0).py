"""
================
Salahuddin Yunus
23 January 2022
================

Project: Create a program that replicates the famous board game, battleship.

"""

import time, random

#function to determine size of arena based on difficulty
def arenaSize(difficulty):
    difficultyScale = "abc"                                         #difficulty scale based on index
    arena = 6 + difficultyScale.find(difficulty)                    #easy arena = 6x6, normal arena = 7x7, hard arena = 8x8 
    return arena                                                    #returns size of arena (easy = 6, normal = 7, hard = 8)


#function to determine location and dimensions of enemy ship, ship length = # of locations that the ship is taking up, ship direction = vertical or horizontal
def shipLocation(arena):
    location = []                                                               #ship location list variable
    initialLoc = random.randrange(1, (arena*arena + 1))                         #location variable takes a random integer from 1 to max capacity of arena
    location.append(initialLoc)                                                 #appends the initial location of ship determined, guaranteed to be length of 1 with additional pieces/locations to add on
    shipLength = random.randrange(1, 4)                                         #will take a random # between 1 and 3 to add on additionally to the length of the ship
    shipDirection = random.randrange(2)                                         #will take a random # between 0 and 1 as the direction, 0 is vertical, 1 is horizontal
    #if ship is vertical
    if shipDirection == 0:                                                                              
        if (initialLoc + arena) in range(1, (arena*arena + 1)):             #checks to make sure spot ahead is on grid
            additionalLoc = initialLoc + arena                              #assigns another location to variable    
            location.append(additionalLoc)                                  #appends new location to ship location list variable
            shipLength -= 1                                                 #if ship length = 1, will end here       
            if shipLength != 0:                                             #if ship length = 2, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc + arena) in range(1, (arena*arena +1)):
                    additionalLoc = additionalLoc + arena
                    location.append(additionalLoc)
                    shipLength -= 1
                else:
                    additionalLoc = initialLoc - arena
                    location.append(additionalLoc)
                    shipLength -= 1
            if shipLength != 0:                                             #if ship length = 3, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc + arena) in range(1, (arena*arena +1)) and location.count((additionalLoc + arena)) != 1:
                    additionalLoc = additionalLoc + arena
                    location.append(additionalLoc)
                elif (additionalLoc - arena) >= 1:
                    additionalLoc = additionalLoc - arena
                    location.append(additionalLoc)
        else:                                                               #if spot not on grid, goes the opposite direction
            additionalLoc = initialLoc - arena                              #assigns another location to variable
            location.append(additionalLoc)                                  #appends new location to ship location list variable 
            shipLength -= 1                                                 #if ship length = 1, will end here
            if shipLength != 0:                                             #if ship length = 2, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc - arena) in range(1, (arena*arena +1)):
                    additionalLoc = additionalLoc - arena
                    location.append(additionalLoc)
                    shipLength -= 1
                else:
                    additionalLoc = initialLoc + arena
                    location.append(additionalLoc)
                    shipLength -= 1
            if shipLength != 0:                                             #if ship length = 3, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc - arena) in range(1, (arena*arena +1)) and location.count((additionalLoc - arena)) != 1:
                    additionalLoc = additionalLoc - arena
                    location.append(additionalLoc)
                elif (additionalLoc + arena) >= 1:
                    additionalLoc = additionalLoc + arena
                    location.append(additionalLoc)
        return location                                                     #returns vertical ship's locations
    #if ship is horizontal
    elif shipDirection == 1:
        if (initialLoc + 1) in range(1, (arena*arena + 1)) and (initialLoc % arena) != 0:                 #checks to make sure spot ahead is on grid
            additionalLoc = initialLoc + 1                                  #assigns another location to variable
            location.append(additionalLoc)                                  #appends new location to ship location list variable
            shipLength -= 1                                                 #if ship length = 1, will end here
            if shipLength != 0:                                             #if ship length = 2, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc + 1) in range(1, (arena*arena + 1)) and (additionalLoc % arena) != 0:
                    additionalLoc = additionalLoc + 1
                    location.append(additionalLoc)
                    shipLength -= 1
                else:
                    additionalLoc = initialLoc - 1
                    location.append(additionalLoc)
                    shipLength -= 1
            if shipLength != 0:                                             #if ship length = 3, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc + 1) in range(1, (arena*arena + 1)) and location.count((additionalLoc + arena)) != 1:
                    additionalLoc = additionalLoc + 1
                    location.append(additionalLoc)
                else:
                    additionalLoc = additionalLoc - 1
                    location.append(additionalLoc)
        else:                                                               #if spot not on grid, goes the opposite direction
            additionalLoc = initialLoc - 1                                  #assigns another location to variable
            location.append(additionalLoc)                                  #appends new location to ship location list variable
            shipLength -= 1                                                 #if ship length = 1, will end here
            if shipLength != 0:                                             #if ship length = 2, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc - 1) in range(1, (arena*arena + 1)) and (additionalLoc % arena) != 0:
                    additionalLoc = additionalLoc - 1
                    location.append(additionalLoc)
                    shipLength -= 1
                else:
                    additionalLoc = initialLoc + 1
                    location.append(additionalLoc)
                    shipLength -= 1
            if shipLength != 0:                                             #if ship length = 3, will repeat the process to find additional place on grid for last piece of ship
                if (additionalLoc - 1) in range(1, (arena*arena + 1)) and location.count((additionalLoc - arena)) != 1:
                    additionalLoc = additionalLoc - 1
                    location.append(additionalLoc)
                else:
                    additionalLoc = additionalLoc + 1
                    location.append(additionalLoc)
        return location                                                     #returns horizontal ship's locations
    

#function to determine user inputted shot location (ex: A6)
def shotCalculation(arena, shotLocation):
    row = ["A", "B", "C", "D", "E", "F", "G", "H"]                                          #row list variable
    shot = (row.index(shotLocation[0].upper()) + 1) + (arena*(int(shotLocation[1]) - 1))    #determines exact location of shot based on user input
    return shot                                                                             #returns shot location


#function to build arena, as well as to show where user has shot
def arenaGrid(arena, shotHit, shotMiss):
    shotCount = 1                                                                        
    columnNumbers = 1
    print("    ", end="")                                              #add little bit of space because of the extra column of numbers
    for i1 in range(arena):                                            #for loop to create row of letters
        row = ["A", "B", "C", "D", "E", "F", "G", "H"]                 
        print(row[i1], "  ", end="")
    print()
    for i2 in range(arena):                                            #for loop with nested for loop to build arena
        print(columnNumbers, "  ", end="")                             #creates numbered column as grid builds
        columnNumbers += 1
        for i3 in range(arena):                                        #nested for loop that accounts for places that have been shot at by user
            if shotHit.count(shotCount) == 1:                          #if user shot in this are of grid and it hit, prints X
                print("X   ", end="")                                  
            elif shotMiss.count(shotCount) == 1:                       #if user shot in this are of grid and it miss, prints O     
                print("O   ", end="")                                  
            else:                                                      #user has not shot in this area, prints ~
                print("~   ", end="")
            shotCount += 1
        print()
    return





#program starts and greets user, gives them short rundown and ability to ask for help if needed, otherwise must enter yes or no if they want to play
print('Welcome to Battleship!')
time.sleep(1)
print("In this game, you must shoot down the enemy ship within a few number of tries.")
time.sleep(1.5)
print("If you fail to do so, they will shoot you down and you will lose.")
time.sleep(1.5)
print('Need help with learning to play? (Enter "Help")')
time.sleep(1)
print('Do you wish to play? (Enter "Yes" or "No")')
userChoice = input("").lower()                                                              #user can either enter help, y/yes, or n/no
yesChoice = "y", "yes"                                                                      #tuple to check user input if yes
noChoice = "n", "no"                                                                        #tuple to check user input if no

#if user does not enter valid choice, will iterate until valid choice is entered
while userChoice not in yesChoice and userChoice not in noChoice and userChoice != "help":
    time.sleep(1)
    print('\nInvalid input entered. Please try again.')
    time.sleep(1)
    print('Do you wish to play? (Enter "Yes" or "No")')
    userChoice = input("").lower()

#if user asks for help, will explain and will show example, then will ask again if user wishes to play
if userChoice == "help":
    time.sleep(1)
    print("\nTo play this game, you must enter the letter corresponding to the column AND one of the numbers corresponding to the row, that you wish to attack (example: A3, B2, F5, etc.).")
    time.sleep(2.5)
    print('If a shot misses, an "O" will appear in the area that you shot. However, if it hit the enemy ship, an "X" will appear.')
    time.sleep(1.5)
    print("The number of shots/tries that you get depend on the difficulty you choose. However, you only lose a shot/try if you miss.")
    time.sleep(1.5)
    print('\nWant to play? (Enter "Yes" or "No")')
    userChoice = input("").lower()
    while userChoice not in yesChoice and userChoice not in noChoice and userChoice != "help":
        time.sleep(1)
        print('\nInvalid input entered. Please try again.')
        time.sleep(1)
        print('Do you wish to play? (Enter "Yes" or "No")')
        userChoice = input("").lower()



#if user chooses to play
while userChoice in yesChoice:
    #user can choose a difficulty, difficulty affects arena size and shot count, easy = 6x6 arena and 8 shots, normal = 7x7 arena and 10 shots, hard = 8x8 arena and 12 shots
    time.sleep(1)
    print("\nPick a difficulty (Enter Letter):\na. Easy\nb. Normal\nc. Hard")                                                         
    difficulty = input("").lower()

    #if user does not enter valid difficulty, will iterate until valid difficulty is entered                        
    while difficulty != "a" and difficulty != "b" and difficulty != "c":
        time.sleep(1)
        print("\nInvalid input entered. Please try again.\nPick a difficulty:\na. Easy\nb. Normal\nc. Hard")
        difficulty = input("").lower()

    #if user chooses a/Easy, will start game in Easy mode
    if difficulty == "a":
        #exposition
        time.sleep(1)
        print("\nDifficulty: Easy")
        time.sleep(1)
        print("\nWelcome to the battlefield soldier!")
        time.sleep(1.5)
        print("We are in the middle of battle with an enemy ship that we do not have a clear view on!")
        time.sleep(2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!\n")
        time.sleep(2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call, determines size of arena                                            
        ship = shipLocation(arena)                                                      #shipLocation function call, determines location, direction, and size of enemy ship, returns location(s)
        shotHit = []                                                                    #list variable for shots that have hit
        shotMiss = []                                                                   #list variable for shots that have missed
        shotCount = 10                                                                  #user can play game for a total of 10 shots
        rowA = ["A", "B", "C", "D", "E", "F"]                                           #only used if player uses letter outside of row
        #game begins
        while shotCount != 0:
            if len(ship) != 0:                                          
                arenaGrid(arena, shotHit, shotMiss)                                     #arenaGrid function call, builds arena/grid
                time.sleep(1)
                print("\nYou have a total of", shotCount, "shots remaining.")
                time.sleep(1)
                shotLocation = input("Enter the area you would like to shoot:\n")       #user inputs location of area they would like to shoot
                time.sleep(1)
                #if user enters a value that does not follow the format of letter-number (ex: B5, A3, C6, etc.) or user tries to shoot in place they have already shot, will iterate until valid entry is given
                while len(shotLocation) != 2 or shotLocation[0].isalpha() != True or shotLocation[1].isnumeric() != True or shotHit.count(shotCalculation(arena, shotLocation)) == 1 or shotMiss.count(shotCalculation(arena, shotLocation)) or rowA.count(shotLocation[0].upper()) != 1:
                    print("\nInvalid input entered.\nDo not forget, you must enter the letter corresponding to the column AND one of the numbers corresponding to the row, that you wish to attack (example: A3, B2, F5, etc.).")
                    time.sleep(1.5)
                    shotLocation = input("Enter the area you would like to shoot:\n")
                #shotCalculation function call, determines location of user inputted shot in grid
                userShot = shotCalculation(arena, shotLocation)                             
                if ship.count(userShot) == 1:                                           #if the user's shot hit the ship
                    shotHit.append(userShot)                                            #adds user's shot to shot thats hit list
                    ship.remove(userShot)                                               #removes location of ship from ships locations list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" HIT!")
                    time.sleep(1.5)
                    print("You hit the ship so you do not lose a shot!\n")
                else:                                                                   #if the user's shot missed the ship, adds location of missed shot to shots that missed list variable
                    shotMiss.append(userShot)                                           #adds user's shot to shot thats missed list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" missed.\n")
                    time.sleep(1.5)
                    shotCount -= 1                                                      #shotCount goes down if user misses
            else:
                time.sleep(1.5)
                arenaGrid(arena, shotHit, shotMiss)
                time.sleep(1.5)
                print("\nYou successfully destroyed the enemy ship! The enemy is now fleeing and we have won the battle!")
                time.sleep(2)
                print("You deserve a promotion. Congratulations soldier and well done!")
                shotCount = 0

        if len(ship) == 0:
            print('\nYou have won! Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()
        else:
            time.sleep(1.5)
            arenaGrid(arena, shotHit, shotMiss)
            time.sleep(1.5)
            print("\nWe have lost soldier...")
            time.sleep(1)
            print("The enemy may have won but it was still a pleasure to fight alongside you.")
            time.sleep(2)
            print("It seems this is the end of the line...")
            time.sleep(1.5)
            print('\nYou have lost. Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()


    #if user chooses b/Normal, will start game in Normal mode
    elif difficulty == "b":
        #exposition
        time.sleep(1)
        print("\nDifficulty: Normal")
        time.sleep(1)
        print("\nWelcome to the battlefield soldier!")
        time.sleep(1.5)
        print("We are in the middle of battle with an enemy ship that we do not have a clear view on!")
        time.sleep(2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!\n")
        time.sleep(2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call, determines size of arena                                            
        ship = shipLocation(arena)                                                      #shipLocation function call, determines location, direction, and size of enemy ship, returns location(s)
        shotHit = []                                                                    #list variable for shots that have hit
        shotMiss = []                                                                   #list variable for shots that have missed
        shotCount = 12                                                                  #user can play game for a total of 12 shots
        rowB = ["A", "B", "C", "D", "E", "F", "G"]                                      #only used if player uses letter outside of row
        #game begins
        while shotCount != 0:
            if len(ship) != 0:                                          
                arenaGrid(arena, shotHit, shotMiss)                                     #arenaGrid function call, builds arena/grid
                time.sleep(1)
                print("\nYou have a total of", shotCount, "shots remaining.")
                time.sleep(1)
                shotLocation = input("Enter the area you would like to shoot:\n")       #user inputs location of area they would like to shoot
                time.sleep(1)
                #if user enters a value that does not follow the format of letter-number (ex: B5, A3, C6, etc.) or user tries to shoot in place they have already shot, will iterate until valid entry is given
                while len(shotLocation) != 2 or shotLocation[0].isalpha() != True or shotLocation[1].isnumeric() != True or shotHit.count(shotCalculation(arena, shotLocation)) == 1 or shotMiss.count(shotCalculation(arena, shotLocation)) or rowB.count(shotLocation[0].upper()) != 1:
                    print("\nInvalid input entered.\nDo not forget, you must enter the letter corresponding to the column AND one of the numbers corresponding to the row, that you wish to attack (example: A3, B2, F5, etc.).")
                    time.sleep(1.5)
                    shotLocation = input("Enter the area you would like to shoot:\n")
                #shotCalculation function call, determines location of user inputted shot in grid
                userShot = shotCalculation(arena, shotLocation)                             
                if ship.count(userShot) == 1:                                           #if the user's shot hit the ship
                    shotHit.append(userShot)                                            #adds user's shot to shot thats hit list
                    ship.remove(userShot)                                               #removes location of ship from ships locations list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" HIT!")
                    time.sleep(1.5)
                    print("You hit the ship so you do not lose a shot!\n")
                else:                                                                   #if the user's shot missed the ship, adds location of missed shot to shots that missed list variable
                    shotMiss.append(userShot)                                           #adds user's shot to shot thats missed list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" missed.\n")
                    time.sleep(1.5)
                    shotCount -= 1                                                      #shotCount goes down if user misses
            else:
                time.sleep(1.5)
                arenaGrid(arena, shotHit, shotMiss)
                time.sleep(1.5)
                print("\nYou successfully destroyed the enemy ship! The enemy is now fleeing and we have won the battle!")
                time.sleep(2)
                print("You deserve a promotion. Congratulations soldier and well done!")
                shotCount = 0

        if len(ship) == 0:
            print('\nYou have won! Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()
        else:
            time.sleep(1.5)
            arenaGrid(arena, shotHit, shotMiss)
            time.sleep(1.5)
            print("\nWe have lost soldier...")
            time.sleep(1)
            print("The enemy may have won but it was still a pleasure to fight alongside you.")
            time.sleep(2)
            print("It seems this is the end of the line...")
            time.sleep(1.5)
            print('\nYou have lost. Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()


    #if user chooses c/Hard, will start game in Hard mode
    else:
        #exposition
        time.sleep(1)
        print("\nDifficulty: Hard")
        time.sleep(1)
        print("\nWelcome to the battlefield soldier!")
        time.sleep(1.5)
        print("We are in the middle of battle with an enemy ship that we do not have a clear view on!")
        time.sleep(2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!\n")
        time.sleep(2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call, determines size of arena                                            
        ship = shipLocation(arena)                                                      #shipLocation function call, determines location, direction, and size of enemy ship, returns location(s)
        shotHit = []                                                                    #list variable for shots that have hit
        shotMiss = []                                                                   #list variable for shots that have missed
        shotCount = 14                                                                  #user can play game for a total of 14 shots
        rowC = ["A", "B", "C", "D", "E", "F", "G", "H"]                                 #only used if player uses letter outside of row
        #game begins
        while shotCount != 0:
            if len(ship) != 0:                                          
                arenaGrid(arena, shotHit, shotMiss)                                     #arenaGrid function call, builds arena/grid
                time.sleep(1)
                print("\nYou have a total of", shotCount, "shots remaining.")
                time.sleep(1)
                shotLocation = input("Enter the area you would like to shoot:\n")       #user inputs location of area they would like to shoot
                time.sleep(1)
                #if user enters a value that does not follow the format of letter-number (ex: B5, A3, C6, etc.) or user tries to shoot in place they have already shot, will iterate until valid entry is given
                while len(shotLocation) != 2 or shotLocation[0].isalpha() != True or shotLocation[1].isnumeric() != True or shotHit.count(shotCalculation(arena, shotLocation)) == 1 or shotMiss.count(shotCalculation(arena, shotLocation)) or rowC.count(shotLocation[0].upper()) != 1:
                    print("\nInvalid input entered.\nDo not forget, you must enter the letter corresponding to the column AND one of the numbers corresponding to the row, that you wish to attack (example: A3, B2, F5, etc.).")
                    time.sleep(1.5)
                    shotLocation = input("Enter the area you would like to shoot:\n")
                #shotCalculation function call, determines location of user inputted shot in grid
                userShot = shotCalculation(arena, shotLocation)                             
                if ship.count(userShot) == 1:                                           #if the user's shot hit the ship
                    shotHit.append(userShot)                                            #adds user's shot to shot thats hit list
                    ship.remove(userShot)                                               #removes location of ship from ships locations list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" HIT!")
                    time.sleep(1.5)
                    print("You hit the ship so you do not lose a shot!\n")
                else:                                                                   #if the user's shot missed the ship, adds location of missed shot to shots that missed list variable
                    shotMiss.append(userShot)                                           #adds user's shot to shot thats missed list
                    print("That shot....", end="")
                    time.sleep(1.5)
                    print(" missed.\n")
                    time.sleep(1.5)
                    shotCount -= 1                                                      #shotCount goes down if user misses
            else:
                time.sleep(1.5)
                arenaGrid(arena, shotHit, shotMiss) 
                time.sleep(1.5)
                print("\nYou successfully destroyed the enemy ship! The enemy is now fleeing and we have won the battle!")
                time.sleep(2)
                print("You deserve a promotion. Congratulations soldier and well done!")
                shotCount = 0

        if len(ship) == 0:
            print('\nYou have won! Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()
        else:
            time.sleep(1.5)
            arenaGrid(arena, shotHit, shotMiss)
            time.sleep(1.5)
            print("\nWe have lost soldier...")
            time.sleep(1)
            print("The enemy may have won but it was still a pleasure to fight alongside you.")
            time.sleep(2)
            print("It seems this is the end of the line...")
            time.sleep(1.5)
            print('\nYou have lost. Do you wish to play again? (Enter "Yes" or "No")')
            userChoice = input("").lower()                                              #user can either enter help, y/yes, or n/no
            #if user does not enter valid choice, will iterate until valid choice is entered
            while userChoice not in yesChoice and userChoice not in noChoice:
                time.sleep(1)
                print('\nInvalid input entered. Please try again.')
                userChoice = input("").lower()
time.sleep(1.5)
print("\nHave a great day and I hope to see you in the battlefield once more soldier!")       #if user does not wish to play, will end program
