day= "monday"
temp=30
raining = False

if (day == "saturday" and temp >27) or not raining:
    print("Go swimming")

else:
    print("learn python")


# exploring truthy and falsy value
#zero (0) is always represent false in boolean 

if 0:
    print("True")
else:
    print("False")

# also empty space is also known as false

name= input("please enter your  name:")
if name:
    print("hello , {}".format(name))
else:
    print("are you the man with no name?")

# another way
name= input("please enter your  name:")
if name != " ":
    print("hello , { }".format(name))
else:
    print("are you the man with no name?")

