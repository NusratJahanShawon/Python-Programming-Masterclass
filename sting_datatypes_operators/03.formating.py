for i in range(1,13):
    print("NO. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))


print()

# alliged in left
for i in range(1,13):
    print("NO. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))

# in middle 
for i in range(1,13):
    print("NO. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

print()

for i in range(1,13):
    print("NO. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))

print()

print("pi is approximately {0:12}".format(22/7))
print("pi is approximately {0:12f}".format(22/7))
print("pi is approximately {0:12.50f}".format(22/7))
print("pi is approximately {0:52.50f}".format(22/7))
print("pi is approximately {0:62.50f}".format(22/7))
print("pi is approximately {0:<72.50f}".format(22/7))
print("pi is approximately {0:<72.54f}".format(22/7))

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])