#A while loop in Python is used to repeatedly execute a block of code as long as 
# a given condition is True.
#Infinite loop: If the condition never becomes False, the loop will continue forever.


i= 0
while i<10:
    print("i is not {}".format(i))
    i+=1

# using break in while loop for easy end task

available_exits=["north", "south", "east","west"]

chosen_exit= ""

while chosen_exit not in available_exits:
    chosen_exit= input("please choose a direction: ")
    if chosen_exit.casefold() == "quite":
        print("Game over.")
        break

print("aren't you glad you got out of there")