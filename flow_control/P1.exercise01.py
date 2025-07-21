name=input("What is you name?")
age=int(input("How old are you {0}".format(name)))

if age >= 18 and age < 31:
    print("Welcome to the Holiday!, {0}".format(name))
else:
    print("Sorry! come again later.")