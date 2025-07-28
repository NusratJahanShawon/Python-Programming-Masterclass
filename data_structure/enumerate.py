#enumerate() helps you loop through a list (or string, etc.) and gives you both the item and its position (index) at the same time.

for index, char in enumerate("asdfghj"):
    print(index, char)


#another way
for t in enumerate("abcdefghi"):
    print(t)