
#multipule variables bt same values
a=b=c=d=e=f=12
print(c)

x,y,z=1,2,72
print(x)
print(y)
print(z)

print("unpacking a tuple")

data=1,2,72
x,y,z=data
print(x)
print(y)
print(z)

print()

for t in enumerate("abcdefghi"):
    index, character = t
    print(index, character)

print("unpacking a list")
data_list=[1,23,45]
p,q,r=data_list
print(p)
print(q)
print(r)

