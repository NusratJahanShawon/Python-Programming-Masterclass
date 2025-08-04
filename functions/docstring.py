# allowing you to document your code for better readability, understanding, and maintainability.
#They are string literals used to describe the purpose, functionality, and behavior of modules, classes, methods, and functions.

# places we can use Docstrings:

# 1. Module Docstrings: At the top of a Python file, explaining what the module does.
# 2. Class Docstrings: Just below the class definition, explaining the class and its attributes.
# 3. Function and Method Docstrings: Right after the def keyword, explaining what the function or method does.

def multiply(x, y):
    """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result
 
 
def is_palindrome(string):
    """
    Check if a string is a palindrome.
 
    A palindrome is a string that reads the same forwards as backwards.
 
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()
 
 
def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)
