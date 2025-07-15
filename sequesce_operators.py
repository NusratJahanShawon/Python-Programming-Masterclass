# A sequence is defined as an ordered set of items

# 5 type of sequences build-in:
# the string type
# list
# tuple
# range
# bytes and bytearray

str1= "Do "
str2="you "
str3="think "
str4="coding "
str5="fun "

print(str1 + str2 + str3 + str4 + str5)
# but working with string can be printed more easily in python'
print("Do " "you " "think " "coding " "fun") 

# when using arethmathic operators with str that will not work, bt will do repeat the str in the calculate numbers
print("hello" * 5)

# print("hello" * 5+4)   this will give u a error
print("hello" * (5+4))
print("hello" * 5 + "4")

#checking if the sequence is present in the str

today="Friday"

print("day" in today)
print("Fri" in today)
print("sam" in today)
print("shawon" in "sabbir")