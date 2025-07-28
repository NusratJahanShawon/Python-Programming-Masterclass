# its a mathematical name for an ordered set of data.
# tuples are different than list because they are immutable. means they cant be changed after they are ccreated.

t=( "a","b","c")
print(t)

# TO make a normal str to a tuple, we will put extra parantheses around the print function

name="sam"
age=26

print(name, age, "python" ,2020)
print((name, age, "python" ,2020))

#-----understanding immutability of tuples------
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)

# metallica[0]="Master of pupptes" # this line will give and error as we cant change it

# to change in a tuple we can first make it list

metallica2=list(metallica)
print(metallica2)

#changing
metallica2[0]="Master of puppets"
print(metallica2)

