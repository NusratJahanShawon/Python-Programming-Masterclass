#A nested for loop means a for loop inside another for loop.
# The inner loop runs completely every time the outer loop runs once.

for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is {2}".format(j,i,i*j))
    print("-----------------------------")

#
# Exercise 1: Print a Rectangle of Stars

for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

# Exercise 2: Multiplication Table

for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
    print()

# Write a program to print a right-angle triangle of * based on user input n.

n = 4  
for i in range(1, n + 1):    
    for j in range(i):          
        print("*", end="")
    print()                     
