"""
================
Salahuddin Yunus
23 January 2022
================

Project: Create a program that replicates the famous board game, battleship.

"""

import time, random

"""
def shipSize(difficulty):
    ship =
"""

print('Welcome to Battleship!\nIn this game, you must shoot down the enemy ship within 8 tries.\nIf you fail to do so, they will shoot you down and you will lose.\nNeed help with playing? Enter ("Help")\nDo you wish to play? (Enter "Yes" or "No")')
userChoice = input("").lower()
noChoice = "n", "no"
yesChoice = "y", "yes"

#if user does not enter valid choice, will iterate until valid choice is entered
while userChoice not in yesChoice and userChoice not in noChoice and userChoice != "help":
    print('Invalid input entered. Please try again.\n')
    userChoice = input("").lower()



if userChoice == "help":
    print("To play this game, you must enter one of letters corresponding to the column AND one of the numbers corresponding to the row that you wish to attack.")
    print('Do you wish to play? (Enter "Yes" or "No")')
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
    elif difficulty == "b":
        print("Difficulty: Normal")
    else:
        print("Difficulty: Hard")
