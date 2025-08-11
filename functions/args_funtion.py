# * used for unpacking iterables

numbers= (0,1,2,3,4,5,6,7,8,9)

print(numbers)
print(*numbers)# its unpacking the tuple
print(*numbers, sep='-') # unpacking with a custom separator

def  test_sequence(*args):
    print(args)
    for i in args:
        print(i)

test_sequence(0,1,2,3,4,5,6,7,8,9)
print()
test_sequence()
