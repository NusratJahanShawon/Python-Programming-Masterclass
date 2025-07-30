# using functions is a great way to avoid duplicating code
# also putting functions in code that allows us to use it over and over again in the code, without re-writing it

# A function that is bound to an instance of a class is called method
# def --- funtion defination start with the keyword 'def'
# then next we give name of the funcction , here we used 'multiply'
# () inside the perantheses we put our parameters. bt even if we dont have any perwameters we still will use the '( )'


def multiply():
    result = 10.5 * 4
    return result


answer=multiply()
print(answer)
# print(multiply())

# by puting perameters
# arguments are the values that will be used by formal parameters, when we call a function
# we need to put values to providing an argument in the functiom
# 
def multiply(x,y):
    result = x * y
    return result


answer=multiply(10, 3)
print(answer)

#-----------Palindrom checking with words-----------
def is_palindrom(string):
    backwards =string[: : -1].casefold()
    return backwards == string.casefold()


word= input("ENter a word to check: ")
if is_palindrom(word):
    print("'{}' is a palindrome.".format(word))
else: 
    print("Not")

# --------palindrom checking sentance-----