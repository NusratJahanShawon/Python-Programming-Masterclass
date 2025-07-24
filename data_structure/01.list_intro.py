# to write list we use [ ]
# list is a sequence type
# list can be mutable , you can change the contents of a list
# computer_parts=["computer",
#                 "monitor",
#                 "keyboard",
#                 "mouse",
#                 "mouse mat"]
# for parts in computer_parts:
#     print(parts)

#we can print by index number
# print(computer_parts[2])

# also can use slicing in list
# print(computer_parts[0:3])
# print(computer_parts[-1])   # by slicing list itss also provid a list 

#adding items with .append()

current_choice="-"
computer_parts=[]

while current_choice != '0':
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("keyboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("Mouse pad")
        elif current_choice == '6':
            computer_parts.append("HDMI cable")
    else:
        print("Please add options from the list below:")
        print("1:computer")
        print("2:monitor")
        print("3:Keyborad")
        print("4:mouse")
        print("5: mouse mat")
        print("6. HDMI able")
        print("0: to finish")

    current_choice=input()

print(computer_parts)

#------------------
