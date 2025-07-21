#python provides several ways to repeat a block of code ---
# for loops
# while loops


name= "nustrat shawon"

for character in name:  # character is a variable name , which can be anything
    print(character)


#-------------------
nums="9,223,354,545,676,234,565"
seperators= " "

for char in nums:
    if not char.isnumeric():
        seperators= seperators+char
print(seperators)

value= "".join(char if char not in seperators else " " for char in nums).split()
print([int(val) for val in value])

#---------------------

nums=input("please enter a series of numbers, using any separator you like:")
seperators= " "

for char in nums:
    if not char.isnumeric():
        seperators= seperators+char
print(seperators)

value= "".join(char if char not in seperators else " " for char in nums).split()
print([int(val) for val in value])

# ---------------------------
