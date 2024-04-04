# Author: Chris Lopez
# April 3rd, 2024
# CIS 129 Lab 06
#   This program is a conversion of pseudocode of a Hot Dog Calculator 


import math

def main():
    # Get the total number of hot dogs needed.
    total = getTotalHotDogs()

    # Named constants for the package sizes
    DOGS = 10  # Hot dogs in a package
    BUNS = 8   # Hot dog buns in a package

    # Calculate the number of left over hot dogs.
    dogsLeft = (DOGS - total % DOGS) % DOGS

    # Calculate the minimum number of packages of hot dogs.
    minDogs = math.ceil(total / DOGS)

    # Calculate the number of left over hot dog buns.
    bunsLeft = (BUNS - total % BUNS) % BUNS

    # Calculate the minimum number of packages of hot dogs buns.
    minBuns = math.ceil(total / BUNS)

    # Display the results.
    showResults(dogsLeft, minDogs, bunsLeft, minBuns)

def getTotalHotDogs():
    # Get the number of people attending the cookout.
    people = int(input("Enter the number of people attending the cookout: "))

    # Get the number of hot dogs each person will be given.
    hotDogs = int(input("Enter the number of hot dogs for each person: "))

    # Calculate the total number of hot dogs needed.
    total = people * hotDogs
    return total

def showResults(dogsLeft, minDogs, bunsLeft, minBuns):
    # Display the minimum packages of hot dogs needed.
    print("Minimum packages of hot dogs needed:", minDogs)

    # Display the minimum packages of buns needed.
    print("Minimum packages of hot dog buns needed:", minBuns)

    # Display the number of hot dogs left over.
    print("Hot dogs left over:", dogsLeft)

    # Display the number of hot dog buns left over.
    print("Hot dog buns left over:", bunsLeft)

if __name__ == "__main__":
    main()
