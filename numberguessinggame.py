from random import randrange

"""small game"""


def numberguessinggame():
    print()
    print("guess a number between 0 - 10")

    while True:
        try:
            guessedvalue = int(input())
            if 0 <= guessedvalue <= 10:
                break
            else:
                print("input wasn`t in the given range you stupid piece of shit \n")

        except:
            print("input wasn`t a number you stupid piece of shit.. \n")
            print("try again: ")

    print("\n")

    randomnumber = randrange(10)

    print("you chose: ", guessedvalue)
    print("computer chose: ", randomnumber)
    print("\n")

    if randomnumber == guessedvalue:
        print("you won... congrats:)")
    else:
        print("loooooser :(")