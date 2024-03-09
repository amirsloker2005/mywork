''''
Program: each player chooses 2 squares that form a rectangle each round until there are no available rectangles to form, then the last player wins.
Author: Amir Abd El Wahid, S21,S22 ISA
ID: 20230066
Version: 1.0
Date: 2024/2/29
'''
from itertools import combinations
def winnercheck(list):  # this function checks if there are any rectangles available to use, because if there isn`t, the player who last played will win
    for combination in combinations(list, 2):
        if any(not str.isdigit(f"{index}") for index in combination): continue
        else:
            if combination[0] - combination[1] == 1 or combination[0] - combination[1] == -1 or combination[0] - combination[1] == 4 or combination[0] - combination[1] ==  -4: return False
            else: continue
    return True

def turncheck(move): # checks if the input is a valid number or not
    if len(move) == 2:
        if any(not index.isdigit() for index in move):
            return True
        else: return False
    else: return True
while True:
    squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # the numbers that we are going to use to record the used squares
    player = 1 # used for taking turns between players
    table = f"{squares[0]} | {squares[1]} | {squares[2]} | {squares[3]}\n---+---+---+---\n{squares[4]} | {squares[5]} | {squares[6]} | {squares[7]}\n---+---+---+---\n{squares[8]} | {squares[9]} | {squares[10]} | {squares[11]}\n---+---+---+---\n{squares[12]} | {squares[13]} | {squares[14]} | {squares[15]}"
    print(table)
    while True:
        table = f"{squares[0]} | {squares[1]} | {squares[2]} | {squares[3]}\n---+---+---+---\n{squares[4]} | {squares[5]} | {squares[6]} | {squares[7]}\n---+---+---+---\n{squares[8]} | {squares[9]} | {squares[10]} | {squares[11]}\n---+---+---+---\n{squares[12]} | {squares[13]} | {squares[14]} | {squares[15]}"
        turn = input(f"Player {player}`s turn, Choose two available Square Numbers (from 1 to 16) that are next to each other to form a rectangle.\n").split() # takes the two numbers as input from user and put them in list to use soon
        while turncheck(turn):
            turn = input("invalid input, Type two numbers (from 1 to 16) separated by a space to form a rectangle.\n").split()
        if (int(turn[0]) in squares and int(turn[1]) in squares) and (int(turn[0]) - int(turn[1]) == 4 or int(turn[0]) - int(turn[1]) == -4 or int(turn[0]) - int(turn[1]) == -1 or int(turn[0]) - int(turn[1]) == 1): #Checks if the two numbers are available in the table and if they can form a rectangle
            squares[int(turn[0])-1] = "X"
            squares[int(turn[1])-1] = "X"
            table = f"{squares[0]} | {squares[1]} | {squares[2]} | {squares[3]}\n---+---+---+---\n{squares[4]} | {squares[5]} | {squares[6]} | {squares[7]}\n---+---+---+---\n{squares[8]} | {squares[9]} | {squares[10]} | {squares[11]}\n---+---+---+---\n{squares[12]} | {squares[13]} | {squares[14]} | {squares[15]}"
            print(table)
            if winnercheck(squares):
                print(f"\nPlayer {player} has won!!\n")
                while True:
                    choice = input("Do you want to play again?\nA) Yes\nB) No\n").upper() #asks if the user wants to play again
                    if choice == "A": break
                    elif choice == "B": quit()
                    else: print("enter a valid choice")
                if choice == "A": break
            else:  #this is used to switch between players when there is no winner yet
                if player == 1: player = 2
                else: player = 1
        else: print("The two squares you chose cannot be formed into a rectangle.")