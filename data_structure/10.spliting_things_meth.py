# split()method can be used in string sepation
# if we split the string its tranfer into single words and into a list


program=" the quick brown fox jumps over the lazy dog"

#if we write our sting in different formate this will give the same output
# program= """the quick brown 
# fox jumps \tover 
# the lazy dog"""

words= program.split()
print(words)

numbers= "9,223,378,556,324,435" # we also can split sting seperated with ',' 
print(numbers.split(","))

generated__list=['9','',
                 '2','2','3', ' ',
                 '2','2','3', ' ',
                 '2','2','3', ' ',
                 '2','2','3', ' ',
                 '7','8','5']

values= "".join(generated__list) #here we r doing the separtion bt using the .join method 
print(values)

values_list = values.split()
print(values_list)

# use a for loop to produce a list of ints, rather than strings


#replace the values in place
for index in range(len(values_list)):
    values_list[index] =int(values_list[index])
print(values_list)

#creating into new list

nums=['2','4','5']

for index in range(len(nums)):
    nums[index] =int(nums[index])
print(nums)

empty_list=[]
for num in nums:
    empty_list.append(int(num))
print(empty_list)