#slicing [start : end : range]
#the end number is not upto bt not including

name="Norwegian Blue"

print(name[0:6])
print(name[3:5])
print(name[0:9])

#if we keep empty the first stating entry its start from the index no 0
print(name[ :6])
#if we keep empty the last entry its print till the last indexx number
print(name[10: ])
#or we can wrtie the +1 after the index number we have
print(name[10:14]) 


print(name[ : ])
print(name[:6] + name[6:])

#--------advance-------
# slicing with negative indexing number 

name="Norwegian Blue"
print(name[-4:-2]) #Bl
print(name[-4:12]) # will print the same as the upper one.

print(name[ 0:6 ])  #Norweg
print(name[-14:-8]) # same as [0:6] bt with negative indexing

#------step slicing--------

name="Norwegian Blue"
print(name[0:6:2])
print(name[0:6:3])

nums="9,223,354,545,676,234,565"
# print(nums[1: :4])

seperators= nums[1::4]
print(seperators)

value= "".join(char if char not in seperators else " " for char in nums).split()
print([int(val) for val in value])

#--- slicing backwards----
letters="abcdefghijklmnopqrstuvwxyz"
backward=letters[25:0:-1] # this wont print the a in the str becaze of the not cincluding the end slising number
print(backward)

#practice:

letters="abcdefghijklmnopqrstuvwxyz"
# create a slice that produce the characters qpo
print(letters[16:13:-1])
  
#print edcba
print(letters[4 : : -1])

#last 8 chaaracter in reverse order
print(letters[ : -9:-1 ])

 
