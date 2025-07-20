# for i in range(1,13):
#     print("no. {} squared is {} and cubed is {:4}".format(i,i**2,i**3))
#     print("*" * 80)

#conditional logic

name=input("what is you name?")
age= int(input("how are you {0} ?" .format(name)))
print(age)

#condition if-else
# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print("please come back in {0} years.".format(18-age))


#elif  condition
if age < 18:
    print("please come back in {0} years.".format(18-age))
elif age==900:
    print("aren't you dead yet!!!")
else:
    print("You are old enough to vote.")

#==================



 