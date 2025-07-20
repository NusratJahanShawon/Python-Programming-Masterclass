answer= 5

print("please guess number between 1 and 10:")
guess=int(input())

if guess < answer:
    print("please guess highter.")
    guess=int(input())
    if guess == answer:
        print("we done you guessed it.")
    else:
        print("sorry you have not guessed correctly")

elif guess > answer:
    print("Please guess lower")
    guess=int(input())
    if guess == answer:
        print("we done you guessed it.")
    else:
        print("sorry you have not guessed correctly")
else:
    print("you got it first time.") 

#==========================
if guess !=answer:
    if guess < answer:
        print("please guess highter.")
    else:
        print("please guess lower")
    guess=int(input())
    if guess == answer:
        print("we done you guessed it.")
    else:
        print("sorry you have not guessed correctly")
else:
    print("you got it first time.") 

#=================
if guess == answer:
    print("you got it first time.")
else:
    if guess < answer:
        print("please guess highter.")
    else:
        print("please guess lower")
    guess=int(input())
    if guess == answer:
        print("we done you guessed it.")
    else:
        print("sorry you have not guessed correctly")

    