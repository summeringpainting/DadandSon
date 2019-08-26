import random
from random import randint


def Beast(counter=0, counter1=1, luckvar=3, countup=2, level=1):
    print("You are on LVL " + str(level) + "! To win pick a number between 1 to " + str(luckvar) + " in " + str(countup) + " guesses")
    luck = random.randint(1, luckvar)
    print("The answer will be " + str(luck))
    loto = (int(input("Pick a number from 1 to " + str(luckvar) + ": ")))
    while luck != loto:

        if loto <= (luck + 3) and loto >= (luck - 3):
            counter += 1
            if counter > counter1:
                print("too many guesses")
                break
            else:
                print("closey")
                print(counter)
                loto = (int(input("Try again hotshot! Pick a number from 1 to " + str(luckvar) + ": ")))

        else:
            counter += 1
            if counter > counter1:
                print("too many guesses")
                break
            else:
                print("Not closey")
                loto = (int(input("NOOOOO Pick a number from 1 to " + str(luckvar) + ": ")))

    else:
        print("WINWINWINWIN")
        Beast(counter=0, counter1=counter1 + 1, luckvar=luckvar + 2, countup=countup + 1, level=level + 1)

Beast()
