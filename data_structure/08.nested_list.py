
empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,7,9]

number= [even , odd] # this will provide lists within list, the items itself are list in this format
print(number)

# outer Loop
for number_list in number:
    print(number_list)

    for value in number_list:
        print(value)

#-------------------------------------------
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}".format(meal,meal.count("spam")))



#--- removing the spam from the list and then print the list----

# for meal in menu:
#     new_meal = [item for item in meal if item != "spam"]
#     print(new_meal)

# -----another approch-----
for meal in menu:
    for index in range(len(meal)-1, - 1, -1):
        if meal[index] == "spam":
            del meal[index]
    print(meal)

print()

#--- another approch---
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()