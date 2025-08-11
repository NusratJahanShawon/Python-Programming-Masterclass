# This code demonstrates the use of positional, arbitrary positional, keyword, and arbitrary keyword arguments in a function.
def func(p1,p2,*arge, k, **kwargs):
    print("positional arguments:....{}".format (p1, p2))
    print("arbitrary positional arguments:.....{}".format (arge))
    print("arbitrary positional arguments:.....{}".format (*arge))
    print("keyword argument:....{}".format (k))
    print("arbitrary keyword arguments:....{}".format (kwargs))

func(2, 3, 4, 5, 6, k=7, key1=8, key2=9)

