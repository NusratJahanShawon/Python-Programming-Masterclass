age= 25
print(type(age))
age="25"
print(type(age)) 

my_list = [10, 20, 30]

# Get iterator
my_iter = iter(my_list)

# Use next() to manually get items
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30

