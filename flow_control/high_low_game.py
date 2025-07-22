
low=1
high=1000

print("please think of a number between {} and {}".format(low,high))
input("press ENter to start")

guesses=1

while True:
    print("\t guessing in th range of {} to {}".format(low , high))
    guess=low+(high-low)//2
    high_low= input("my guess is {}.should i guess high or lower? or c if my guess was correct ".format(guess)).casefold()

    if high_low=="h":
        low=guess+1
        #guess higher. the low end of the range becomes 1 greater than the guess.
    elif high_low =="l":
        high= guess-1
        #guess lower. the high end of the range becomes one less than the guess
    elif high_low=="c":
    
        print("i got it in {} guesseds!".format(guesses))
    else:
        print("please enter h,l or c")
    # guesses= guesses+1
    guesses +=1