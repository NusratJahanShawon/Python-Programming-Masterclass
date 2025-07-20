answer= 5

print("please guess number between 1 and 10:")
guess=int(input())

if guess < answer:
    print("please guess highter.")
elif guess > answer:
    print("Please guess lower")
else:
    print("you got it first time.")