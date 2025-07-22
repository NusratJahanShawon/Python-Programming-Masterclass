#using 'continue' in for loop

shopping_list = ["milk", "paste", "egg", "spam", "bread", "rice"]

for item in shopping_list:
    if item =="spam":
        continue # when its appers in a loop its case everything else in the loop to be ignored    
        print("im ignored!!")
    print("buy " + item) 

#using Break in for loop

for item in shopping_list:
    if item =="spam":
        break 
        print("im ignored!!")
    print("buy " + item) 

#   ---Search using break to find ----
shopping_list = ["milk", "paste", "egg", "spam", "bread", "rice"]
item_to_find="spam"
found_at= None 

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at= index
        break
print("item found at position {}".format(found_at))

#   ---Search using break to not find ----
shopping_list = ["milk", "paste", "egg", "spam", "bread", "rice"]
item_to_find="orange"
# found_at= None 

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at= index
#         break
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
if found_at is not None:
    print("item found at position {}".format(found_at))
else:
    print("{} not found.".format(item_to_find))