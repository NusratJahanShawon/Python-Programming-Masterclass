#using in for checking in python
parrot="noewegian Blue"

letter = input("enter a character:")

if letter in parrot:
    print( "{} is in {}". format(letter, parrot))
else:
    print("not matched")


#checking not in condition in python
activity=input("what would u like to do today?")

if "cinema" not in activity: # in this case if we use lower key in the cinema this will print the output to avoid it follow next part.
    print("I want to go to the cinema")

#to about same word bt will not be make differnce for upper or lower case.
if "cinema" not in activity.casefold():

    print("I want to got o the cinema.")