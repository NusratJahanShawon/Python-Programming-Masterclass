
# #here i is indecates index
# here is range if we want to print 1- 20 numbers index i will start with the starting bt will not include the last number
# to include the last number we can assign the last number + 1 to print out that number

for i in range(1,20):
    print("i is now {}".format(i))

#practice:

for i in range(0,10):
    print(i)

#note: if we put range( 10 ) i will start from 0 and end in 9 index
#note: range cant be like (10,2) the end value cant be smaller than the starting

# in range part (start, end, steps)

for i in range(0,10,2):
    print(i)

# range also can be impliment with negative steps
for i in range(10,0,-2):
    print("i is now {}".format(i))


# without using the 'or' 'and; condition we can use range in this as well 
age= int(input("how old are you?"))
# if age >=16 and age <= 65:
# if 16 <= age <=65:
# if age < 16 or age > 65:
if age in range(16,66):
        print("Have a good day at work")
else:
    print("enjoy ur free time.")

    print("-" * 80)
