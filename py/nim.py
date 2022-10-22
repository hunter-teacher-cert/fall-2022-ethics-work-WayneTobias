# nim
# CSCI 77800
# consulted: ThinkPython
# Game of Nim
from random import random
stones = 12
stonesTaken = 0
# loop
while (stonesTaken < stones) :
    print("Number of stones to take: ")
    nStones = input()
    numStones = int(nStones)
    stonesTaken += numStones
    print("Number of stones remaining: " + str((stones - stonesTaken)))
    # check for win
    if (stonesTaken >= stones) :
        print("User wins!")
        break
    # machine turn
    #r =  java.util.Random()
    numStones = int(3 * random() + 1)
    print("Computer takes " + str(numStones) + " stones.")
    # calculate number of stones remaining
    stonesTaken += numStones
    print("Number of stones remaining: " + str((stones - stonesTaken)))
    # check for win
    if (stonesTaken >= stones) :
        print("Computer wins!")
        break
print("Game over!")