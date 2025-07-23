# to write list we use [ ]
# list is a sequence type
# list can be mutable , you can change the contents of a list
computer_parts=["computer",
                "monitor",
                "keyboard",
                "mouse",
                "mouse mat"]
for parts in computer_parts:
    print(parts)

#we can print by index number
print(computer_parts[2])

# also can use slicing in list
print(computer_parts[0:3])
print(computer_parts[-1])   # by slicing list itss also provid a list 

#adding items with .append()

current_choice="-"
computer_parts=[]

while current_choice !=0:
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
    else:
        print("Please add options from the list below:")
        print("1:computer")
        print("2:monitor")
        print("3:Keyborad")
        print("4:mouse")
        print("5:  mouse mat")
        print("0: to finish")