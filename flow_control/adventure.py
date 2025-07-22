
available_exits=["north", "south", "east","west"]

chosen_exit= ""

while chosen_exit not in available_exits:
    chosen_exit= input("please choose a direction: ")
print("aren't you glad you got out of there")


#another way
available_exits=["north", "south", "east","west"]

chosen_exit= ""

while chosen_exit not in available_exits:
    chosen_exit= input("please choose a direction: ")
    if chosen_exit.casefold() == "quite":
        print("Game over.")
        break

print("aren't you glad you got out of there")