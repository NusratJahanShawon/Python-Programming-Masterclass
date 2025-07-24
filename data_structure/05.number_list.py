
empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,7,9]

number=even + odd
print(number)

# note: if u want to sort a list without creating a new list we can use .sort() function
# note: if u wnat to sort a list in a new list we can use sorted() like the example shown here
sorted_number=sorted(number)
print(sorted_number)
print(number) 

digit=list("234355632")
digit=sorted("234355632")
print(digit)

#to check if they are same list
more_number=list(number) # way of copy a list
print(more_number)
# copy a list using slice
new_list=number[:]  # dont use this method much

#most use method in python 3 is this one for copy a list 
newest_list= number.copy()

print(number is more_number) # if they are same list or not
print(number == more_number) # if the values are the same in both list or not
