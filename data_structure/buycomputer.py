available_part=["computer",
                "monitor",
                "keyboard",
                "mouse",
                "mouse pad",
                "HDMI cable"]
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
        # for part in available_part:
        #     print("{0}: {1}".format(available_part.index(part)+1,part))

        for number, part in enumerate(available_part):   #enumerate (pair of values) returns with index number within. 
            print("{0}: {1}".format(number+1,part))

    current_choice=input()

print(computer_parts)