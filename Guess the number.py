# put a number than ask user to guess it
# if it is less than the number than say the number is bigger than that
# Or less than and congratulate if they geet it right.
# user only has 9 turns if they don't make it in 9 turns say game over
import random

n = random.randint(1, 99)  # generates random number between 1 and 99
count = 0
print("==Number guessing game==")
print("**You have to guess the number between 1 to 99.**")
print("**You get only 9 turns\nIf you want to give up enter 100.**")
while True:
    count = count + 1
    unum = input("Guess a number: ")
    if unum.isnumeric():
        unum = int(unum)
        if 1 <= count < 9 and unum <= 99:
            a = 9 - count
            if n > unum:
                print("Opps! The number is greater than", unum)
                print("you tried", count, "times", "remaining no of turns is", a, "\n")
            elif n < unum:
                print("Opps! The number is less than", unum)
                print("you tried", count, "times", "remaining no of turns is", a, "\n")
            else:
                print("congratulations :) \n you have guessed the number correctly \n It was", unum)
                print("In", count, "turns.")
                print("Do you want to play next round ? yes or no")
                yn = input()
                yn = yn.upper()
                if yn == "YES":
                    count = 0
                    n = random.randint(0, 99)
                    continue
                else:
                    break
        elif unum == 100:
            print(":( You gave up. \n  Better luck next time.")
            print("If you want to try again type 'YES' else type 'exit' to quite")
            yn = input()
            yn = yn.upper()
            if yn == "YES":
                count = 0
                n = random.randint(0, 99)
                continue
            else:
                exit()
        elif unum > 100:
            print("Out of range try something between 1 and 99.\n")
            continue
        else:
            print("game over")
            print("If you want to try again\n type \"yes\"")
            yn = input()
            yn = yn.upper()
            if yn == "YES":
                count = 0
                n = random.randint(0, 99)
                continue
            else:
                break
    else:
        print("Opps :( that wasn't a number")
