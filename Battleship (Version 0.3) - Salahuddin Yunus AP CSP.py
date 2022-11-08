"""
================
Salahuddin Yunus
23 January 2022
================

Project: Create a program that replicates the famous board game, battleship.

"""

import time, random

def arenaSize(difficulty):
    difficultyScale = "abc"
    size = 5 + difficultyScale.find(difficulty)
    return size

def shipLocation(arena):
    location = arena*arena
    location = random.randrange(1, location + 1)
    return location

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
                print("0   ", end="")
            shotHitCount += 1
            shotMissCount += 1
        print()
    return

def shotCalculation(shotLocation):
    row = "ABCDEFG"
    shot = (row.find(shotLocation[0]) + 1)*(int(shotLocation[1]))
    return shot



#program starts and greets user, gives them short rundown and ability to ask for help if needed, otherwise must enter yes or no if they want to play
print('Welcome to Battleship!')
time.sleep(1.5)
print("In this game, you must shoot down the enemy ship within 8 tries.")
time.sleep(2.2)
print("If you fail to do so, they will shoot you down and you will lose.")
time.sleep(2.2)
print('Need help with how to play? (Enter "Help")')
time.sleep(1.5)
print('Do you wish to play? (Enter "Yes" or "No")')
userChoice = input("").lower()                                                                  #user can either enter help, y/yes, or n/no
yesChoice = "y", "yes"                                                                          #tuple to check user input if yes
noChoice = "n", "no"                                                                            #tuple to check user input if no

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



while userChoice in yesChoice:
    print("Pick a difficulty:\na. Easy\nb. Normal\nc. Hard")
    difficulty = input("").lower()
    #if user does not enter valid choice, will iterate until valid choice is entered
    while difficulty != "a" and difficulty != "b" and difficulty != "c":
        print("Invalid input entered. Please try again.\nPick a difficulty:\na. Easy\nb. Normal\nc. Hard")
        difficulty = input("").lower()

    if difficulty == "a":
        print("Difficulty: Easy")
        arena = arenaSize(difficulty)
        arenaGrid(arena)
        ship = shipLocation(arena)
        for i in range(8):
            shotHit = 0
            shotMiss = 0
            arenaGrid(arena)
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
    elif difficulty == "b":
        print("Difficulty: Normal")
    else:
        print("Difficulty: Hard")