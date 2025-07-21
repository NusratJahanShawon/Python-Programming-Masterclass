# Find and Print Capital Letters: Python String Manipulation Exercise
# Write a program to print out the capital letters in the string
# "Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order,
#  Irrigation, Roads, the Fresh-Water System, and Public Health, what have the Romans ever done for us?"
# Check out the string methods for one way to test if a character is in uppercase.

string="""Alright, but apart from the Sanitation, the Medicine, Education, Wine, 
Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, 
what have the Romans ever done for us?"""


for letter in string:
    if letter.isupper():
        print(letter)


#if i take a empty array and put the    

empty_array=[]    
for letter in string:
    if letter.isupper():
        empty_array.append(letter)

print(empty_array)