from random import randint

def rollDice():
    broj = 0
    broj = randint(0,6)
    return broj


for i in range(0,15):
    print("Broj je: ", rollDice())

