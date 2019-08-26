import random
from random import randint


def Beast(counter=0, counter1=1, luckvar=3, countup=2, level=1):
    print("You are on LVL " + str(level) + "! To win pick a number between 1 to " + str(luckvar) + " in " + str(countup) + " guesses")
    luck = random.randint(1, luckvar)
    print("The answer will be " + str(luck))
    loto = (int(input("Pick a number from 1 to " + str(luckvar) + ": ")))
    while luck != loto:

        if 0 < loto < 4:
            counter += 1
            print("closey")
            print(counter)
            if counter > counter1:
                print("too many guesses")
                break
            loto = (
                int(input("Pick a number from 1 to " + str(luckvar) + " in " + str(countup) + " guesses: ")))
        elif loto <= 0 or loto > 3:
            print("Not closey")
            loto = (int(input("NOOOOO Pick a number from 1 to 3: ")))


    else:
        print("WINWINWINWIN")
        Beast(counter=0, counter1=counter1 + 1, luckvar=luckvar + 2, countup=countup + 1, level=level + 1)

Beast()
