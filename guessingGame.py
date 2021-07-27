import random

number = random.randint(1,10)
chance = 5

while chance > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    chance = chance-1
    if chance>=1:
        if guess==number:
            print("Yay you got it")
            number = random.randint(1,10)
        else:
            print("Wrong number")
            print("Chances Remaining:")
            print(chance)
    elif chance == 0:
        print("Game Over")