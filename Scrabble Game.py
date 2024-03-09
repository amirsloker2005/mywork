# File: CS112_A2_T2_2_20230066
# Purpose: The player that has 3 numbers that add up to 15 first wins
# Author: Amir Abd El Wahed Abd El Hamid
# ID: 20230066
from itertools import combinations


def combsum(number):  # to find the possible sums of the selected numbers so far and see if they add up to 15
    if len(number) >= 3:
        for limit in range(3, len(number) + 1):
            for combination in combinations(number, limit):
                if sum(combination) == 15 and len(combination) == 3:
                    return 15

while True:
    scrabble = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # the list of numbers that the players will select from
    playerone = []  # a list that saves the numbers chosen by player 1
    playertwo = []  # a list that saves the numbers chosen by player 2
    print("***Scrabble Game***")
    while True:
        print("Player one choose a number from", scrabble, "the numbers you have chosen till now are", playerone)
        playeronemove = int(input(""))
        if playeronemove in scrabble:  # to check if the selected number is available in the list
            playerone.append(playeronemove)
            scrabble.remove(playeronemove)
            if combsum(playerone) == 15:
                print("Player one won with ", playerone, "\n\n\n")
                break
            elif len(scrabble) == 0:
                print("Draw")
                break
            else:
                print("Player two choose a number from", scrabble, "the numbers you have chosen till now are",
                      playertwo)
                playertwomove = int(input(""))
                while playertwomove not in scrabble:
                    print("The number", playertwomove, "is not within the allowed numbers", scrabble)
                    print("Choose a number from", scrabble, "the numbers you have chose are", playertwo)
                    playertwomove = int(input(""))
                playertwo.append(playertwomove)
                scrabble.remove(playertwomove)
                if combsum(playertwo) == 15:
                    print("Player two won with", playertwo, "\n\n\n")
                    break
                elif len(scrabble) == 0:
                    print("Draw")
                    break
                else:
                    continue

        else:
            print("the number", playeronemove, "is not within the allowed numbers", scrabble)
    continue
