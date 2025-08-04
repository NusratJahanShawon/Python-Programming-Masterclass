def fizz_buzz(n: int) -> str:
    """
    Returns 'fizz' if n is divisible by 3,
    'buzz' if n is divisible by 5,
    'fizz buzz' if divisible by both 3 and 5,
    otherwise returns the number as a string.

    Parameters:
    n (int): The number to evaluate.

    Returns:
    str: The fizz buzz result.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

# Test the function from 1 to 100
for i in range(1, 101):
    print(fizz_buzz(i))
