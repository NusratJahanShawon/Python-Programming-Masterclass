
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

print("-------------------")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

title, artist, year= metallica
print(title)
print(artist)
print(year)

# here in tuple theres many data so unpacking is best way to keep track easily. 

table= ("Coffee table", 200,100,75, 50.0)
name,length,width,height,price=table
print(length*height)
