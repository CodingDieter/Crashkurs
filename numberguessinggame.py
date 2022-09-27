from random import randrange

"""small game"""
print("\n")
print("guess a number between 0 - 10")

while True:
    try:
        guessedValue = int(input())
        if 0 <= guessedValue <= 10:
            break
        else:
            print("input wasn`t in the given range you stupid piece of shit \n")
    except:
        print("input wasn`t a number you stupid piece of shit.. \n")
        print("try again: ")

print("\n")

randomNumber = randrange(10)

print("you chose: ", guessedValue)
print("computer chose: ", randomNumber)
print("\n")

if randomNumber == guessedValue:
    print("you won... congrats:)")
else:
    print("loooooser :(")

print("\n")





