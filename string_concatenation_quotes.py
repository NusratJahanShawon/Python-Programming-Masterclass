# Quoates using on string
print("Hello World!") # you can use " " for stiring declaration

print('how are you doing today?') # you can use ' ' for stiring declaration

print("I'm doing 'fine', thank you.") # if you are quoting another word inside string you will have to use the different pairs of quotation.

print('you simplly can "quote" using differnt pairs of quotation.')


#Concatenation in python
# Concatenation in Python refers to the process of joining two or more strings, 
# or other iterable objects like lists or tuples, into a single, combined object.

# 01. Using the + Operator:
print("cats" + " and" + " Dogs") #Special note: if you write "dog" rather than " dog" (space after first quotation) you will not recieve space between words 

#02. as variables and + oprator:
greetings="hello"
name="sam"
print(greetings + ' ' + name)

#03. Using f-Strings:
name= "Alice"
age= 30
message= f"My name is {name} and I am {age} years old."
print(message)

#04: Using join() method:
# we use list for joining stings
words=["Is" , "it", "raining", "outside","?"]
sentence= " ".join(words) # we will need to use a space inside the quotation " " Or, there will be no space between the words.
print(sentence)


#05: % operators for string formatting: (similar to printf in C)
item = "apple"
price = 1.50
message = "The %s costs $%.2f." % (item, price)
print(message)  

#06. format() Method: 
product = "laptop"
cost = 1200
info = "The {} costs ${}.".format(product, cost)
print(info) 
