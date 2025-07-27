# here we will see the join() method to use in iterable 

flowers=[
    "daffodil",
    "Evening primrose",
    "Hyfrangea",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]
# for flower in flowers:
#     print(flower)

seperator=" | "
output=seperator.join(flowers)
print(output)

seperator=" * "
output=seperator.join(flowers)
print(output)

print(",".join(flowers))