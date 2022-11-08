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

#function to determine location of enemy ship
def shipLocation(arena):                                                                       
    location = random.randrange(1, (arena*arena + 1))               #location variable takes a random integer from 1 to max capacity of arena
    return location                                                 #returns randomly selected location of enemy ship

#function to determine user inputted shot location (ex: A6)
def shotCalculation(arena, shotLocation):
    row = ["A", "B", "C", "D", "E", "F", "G"]                                               #row list variable
    shot = (row.index(shotLocation[0].upper()) + 1) + (arena*(int(shotLocation[1]) - 1))    #determines exact location of shot based on user input
    return shot                                                                             #returns shot location

#function to build arena, as well as to show where user has shot
def arenaGrid(arena, shotHit, shotMiss):
    shotHitCount = 1
    shotMissCount = 1
    for i1 in range(arena):
        for i2 in range(arena):
            if shotHitCount == shotHit:
                print("X   ", end="")
            elif shotMissCount == shotMiss:
                print("1   ", end="")
            else:
                print("~   ", end="")
            shotHitCount += 1
            shotMissCount += 1
        print()
    return





#program starts and greets user, gives them short rundown and ability to ask for help if needed, otherwise must enter yes or no if they want to play
print('Welcome to Battleship!')
time.sleep(1.5)
print("In this game, you must shoot down the enemy ship within a few number of tries.")
time.sleep(2.2)
print("If you fail to do so, they will shoot you down and you will lose.")
time.sleep(2.2)
print('Need help with how to play? (Enter "Help")')
time.sleep(1.5)
print('Do you wish to play? (Enter "Yes" or "No")')
userChoice = input("").lower()                                                              #user can either enter help, y/yes, or n/no
yesChoice = "y", "yes"                                                                      #tuple to check user input if yes
noChoice = "n", "no"                                                                        #tuple to check user input if no

#if user does not enter valid choice, will iterate until valid choice is entered
while userChoice not in yesChoice and userChoice not in noChoice and userChoice != "help":
    time.sleep(1)
    print('\nInvalid input entered. Please try again.')
    userChoice = input("").lower()

#if user asks for help, will explain and will show example, then will ask again if user wishes to play
if userChoice == "help":
    time.sleep(1)
    print("\nTo play this game, you must enter the letter corresponding to the column AND one of the numbers corresponding to the row, that you wish to attack (example: A3, B2, F5, etc.).")
    time.sleep(3.5)
    print('Want to play? (Enter "Yes" or "No")')
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
        print("We are in the middle of battle with an enemy ship but we do not have a clear view on the location of the enemy!")
        time.sleep(2.2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!")
        time.sleep(2.2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call                                               
        ship = shipLocation(arena)                                                      #shipLocation function call

        #user can play game for a total of 8 shots
        for shotCount in range(8, -1, -1):
            print("\nYou have a total of", shotCount, "shots remaining.")
            shotHit = 0                                                                 #variable for shots that have hit
            shotMiss = 0                                                                #variable for shots that have missed
            arenaGrid(arena, shotHit, shotMiss)
            shotLocation = input("Enter the area you would like to shoot:\n")
            userShot = shotCalculation(arena, shotLocation)
            if userShot != ship:
                shotMiss += userShot
            elif userShot == ship:
                shotHit += userShot
            elif userShot > arena*arena:
                while userShot > arena*arena or userShot < arena*arena:
                    print("Invalid input entered.\nDo not forget, you must enter one of letters corresponding to the column AND one of the numbers corresponding to the row that you wish to attack (example: A3).")
                    shotLocation = input("Enter the area you would like to shoot:\n")

    #if user chooses b/Normal, will start game in Normal mode
    elif difficulty == "b":
        #exposition
        time.sleep(1)
        print("\nDifficulty: Normal")
        time.sleep(1)
        print("\nWelcome to the battlefield soldier!")
        time.sleep(1.5)
        print("We are in the middle of battle with an enemy ship but we do not have a clear view on the location of the enemy!")
        time.sleep(2.2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!")
        time.sleep(2.2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call                                               
        ship = shipLocation(arena)                                                      #shipLocation function call

        #user can play game for a total of 10 shots
        for shotCount in range(10, -1, -1):
            print("\nYou have a total of", shotCount, "shots remaining.")
            shotHit = 0
            shotMiss = 0
            arenaGrid(arena, shotHit, shotMiss)
            shotLocation = input("Enter the area you would like to shoot:\n")
            userShot = shotCalculation(shotLocation)
            if userShot != ship:
                shotMiss += userShot
            elif userShot == ship:
                shotHit += userShot
            elif userShot > arena*arena:
                while userShot > arena*arena or userShot < arena*arena:
                    print("Invalid input entered.\nDo not forget, you must enter one of letters corresponding to the column AND one of the numbers corresponding to the row that you wish to attack (example: A3).")
                    shotLocation = input("Enter the area you would like to shoot:\n")

    #if user chooses c/Hard, will start game in Hard mode
    else:
        #exposition
        time.sleep(1)
        print("\nDifficulty: Hard")
        time.sleep(1)
        print("\nWelcome to the battlefield soldier!")
        time.sleep(1.5)
        print("We are in the middle of battle with an enemy ship but we do not have a clear view on the location of the enemy!")
        time.sleep(2.2)
        print("Here's a map of enemy waters, the darned ship is somewhere in this area and we are leaving it to you to take the shots, Don't let me down soldier!")
        time.sleep(2.2)

        arena = arenaSize(difficulty)                                                   #arenaSize function call                                               
        ship = shipLocation(arena)                                                      #shipLocation function call

        #user can play game for a total of 12 shots
        for shotCount in range(12, -1, -1):
            print("\nYou have a total of", shotCount, "shots remaining.")
            shotHit = 0
            shotMiss = 0
            arenaGrid(arena, shotHit, shotMiss)
            shotLocation = input("Enter the area you would like to shoot:\n")
            userShot = shotCalculation(shotLocation)
            if userShot != ship:
                shotMiss += userShot
            elif userShot == ship:
                shotHit += userShot
            elif userShot > arena*arena:
                while userShot > arena*arena or userShot < arena*arena:
                    print("Invalid input entered.\nDo not forget, you must enter one of letters corresponding to the column AND one of the numbers corresponding to the row that you wish to attack (example: A3).")
                    shotLocation = input("Enter the area you would like to shoot:\n")