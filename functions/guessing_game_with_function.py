import random

# here this function does is , if its gets a non integer value as input it doesnt crash 
def get_integer(promt):
    while True:
        temp=input(promt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("ERROR")


highest = 1000
answer = random.randint(1, highest)
print(answer)  
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(highest))
 
while guess != answer:
    guess = get_integer(":")
    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
