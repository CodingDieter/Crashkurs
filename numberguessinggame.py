from random import randrange

"""small game"""
print("\n")
print("guess a number between 0 - 10")
guessedValue = int(input())
while 0 > guessedValue > 10:
    print("input wasn`t an number you stupid piece of shit.. \n")
    print("try again: ")
    guessedValue = int(input())


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





