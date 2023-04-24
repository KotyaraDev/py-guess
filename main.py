import random
from time import sleep

number = random.randint(1, 100)
attempt = 5


print("|==========================================|")
print("| Welcome to Guess                         |")
print("| Rules of the game:                       |")
print("| 1. I make a number, you guess            |")
print("| 2. You have everything ", attempt, " попыток         |", sep="")
print("|==========================================|")
sleep(1)
print("Let's go!")


ask = input("\n\nWrite your answer:")

def check_number(ask):
    global attempt

    try:
        int(ask)
    except ValueError:
        print("Please, use number.")
        return False

    answer = int(ask)

    if attempt <= 1:
        print("The attempts are over..\nCorrect answer:", number, "\nThe game is finished ahead of schedule.")
        return True

    if answer != number:

        if answer < number:
            attempt -= 1
            print("The answer is false! Strive for more number.\nAttempts remains:", attempt)
            return False
        elif answer > number:
            attempt -= 1
            print("The answer is false! Strive for a smaller number.\nAttempts remains:", attempt)
            return False
    else:
        print("The answer is true! A guessed number:", number, "\nYou guessed for:", 5 - attempt, "attempts")
        return True

while not check_number(ask):
    ask = input("\n\nWrite your answer: ")