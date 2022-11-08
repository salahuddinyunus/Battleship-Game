"""
================
Salahuddin Yunus
23 January 2022
================

Project: Create a program that replicates the famous board game, battleship.

"""

import time, random

print('Welcome to Battleship!\nDo you wish to play? (Enter "Yes" or "No")')
play = input("").upper()

#if user does not enter valid choice, will iterate until valid choice is entered
while play != "YES" and play != "Y" and play != "N" and play != "NO":
    print('Invalid input entered. Please try again.\nDo you wish to play? (Enter "Yes" or "No")')
    play = input("").upper()



while play == "YES" or play == "Y":
    print("Pick a difficulty:\na. Easy\nb. Normal\nc. Hard")
    difficulty = input("").lower()

    #if user does not enter valid choice, will iterate until valid choice is entered
    while difficulty != "a" and difficulty != "b" and difficulty != "c":
        print("Invalid input entered. Please try again.\nPick a difficulty:\na. Easy\nb. Normal\nc. Hard")
        difficulty = input("").lower()
