

import random

highest=10
answer= random.randint(1,highest)
print(answer)
guess=0   # any number which is not qual to answer
print("please guess number between 1 and {}:".format(highest))

while guess !=  answer:
    guess=int(input())
    if guess==0:
        break
    if guess == answer:
        print("we done you guessed it.")
        break
    else:
        if guess < answer:
            print("please guess highter.")
        else:
            print("please guess lower")
        # guess=int(input())
        # if guess == answer:
        #     print("we done you guessed it.")
        # else:
        #     print("sorry you have not guessed correctly")

