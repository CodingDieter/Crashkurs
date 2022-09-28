"""main brain   author: Christian"""

from numberguessinggame import numberguessinggame
from class_player import Player

while True:
    print("type in player name: ")
    player1 = Player(input())

    print("Which game do you like to play?")
    print()
    print("1. guess the number")
    print("2. not available")
    print("3. not available")
    print()
    print("select option: ")

    while True:
        try:
            selectedOption = int(input())
            if 1 <= selectedOption <= 3:
                break
            else:
                print("there is no game listed with that number you stupid piece of shit \n")
        except:
            print("input wasn`t even a number you stupid piece of shit.. \n")
            print("try again: ")

    if selectedOption == 1:
        result = numberguessinggame()
        if result:
            player1.addpoints(50)
        elif not result:
            player1.subpoints(5)

    print("Player result: ", player1.points)