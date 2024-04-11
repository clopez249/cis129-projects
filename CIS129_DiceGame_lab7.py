# Author: Chris Lopez
# Title: Dice Game
# Date: April 10th, 2024
#     This code is a program for a dice game in python.

import random  

# the main function
def main():
    endProgram = 'no'  # initialize variable
    playerOne = 'NO NAME'  # initialize playerOne
    playerTwo = 'NO NAME'  # initialize playerTwo

    # call to inputNames
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == 'no':
        winnerName = 'NO NAME'  # populate variable
        p1number = p2number = 0  # populate variables

        # call to rollDice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo, winnerName)

        # call to displayInfo
        displayInfo(winnerName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets the players names
def inputNames(playerOne, playerTwo):
    playerOne = input("Enter Player One's name: ")
    playerTwo = input("Enter Player Two's name: ")
    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo, winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    
    if p1number > p2number:
        winnerName = playerOne
    elif p2number > p1number:
        winnerName = playerTwo
    else:
        winnerName = "TIE"
    
    return winnerName

# this function displays the winner
def displayInfo(winnerName):
    print("The winner is:", winnerName)

# calls main
main()
