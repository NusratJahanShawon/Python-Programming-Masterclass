# print("Please choose your option from the list below:")
# print("1. Learn Python")
# print("2. Learn Java")
# print("3. Go swimming")
# print("4. Have dinner")
# print("5. Go to Bed")
# print("0. Exit")
# while True:
#     num=input("ENTER YOUR CHOICE: ")
#     if num == "0":
#         break
#     elif num in "12345":
#         print("you chose {}".format(num))
#     else:
#         print("Please choose your option from the list below:")
#         print("1. Learn Python")
#         print("2. Learn Java")
#         print("3. Go swimming")
#         print("4. Have dinner")
#         print("5. Go to Bed")
#         print("0. Exit")



num="-"
while num !="0":
    if num in "12345":
        print("you chose {}".format(num))
    else:
        print("Please choose your option from the list below:")
        print("1. Learn Python")
        print("2. Learn Java")
        print("3. Go swimming")
        print("4. Have dinner")
        print("5. Go to Bed")
        print("0. Exit")
    num=input("ENTER YOUR CHOICE: ")