even=[2,4,6,8]
odd=[1,3,5,7,9]

#using .extend() function where i will combine both variable values
even.extend(odd)
print(even)

#normal sort() function 
even.sort()
print(even)

# sorting list with also reversing the values
even.sort(reverse=True)
print(even)

#--------------
# sorting sting
message="How are you doing to day in this hot ?"

letter= sorted(message)
print(letter)

numbers= [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
print(numbers)
sorted_numbers=sorted(numbers)
print(sorted_numbers)

#--------------
# case insensitive sorting in str use key=str.casefold
message_in =sorted("How are you doing to day in this hot and Sunny day ?", key=str.casefold)
print(message_in)

#ase insensitive sorting in list use key=str.casefold

name=["Shawon",
      "Nusrat",
      "Rafi",
      "orni",
      "Sabbir"]
name.sort(key=str.casefold)
print(name)