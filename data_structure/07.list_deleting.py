data=[4, 5, 104, 105, 110, 120, 130, 130, 150, 
      160, 170, 183, 180, 187, 188, 192, 350, 360]

del data[0:2] # started from zero bt deleted up to 2 but as always 2 is not included 
print(data)

del data[14:]
print(data)

#safely remove values from list
#deleting min value
min_valid=100
max_valid=200

stop=0
for index, value in enumerate(data):
    if value >= min_valid:
        stop =index
        break
print(stop)
del data[:stop]
print(data) 

#process the high values
start=0
# for index in range(len(data) -1,-1,-1):
#     print(index)
for index, value in enumerate(data):
    if value <= max_valid:
        stop =index+1
        break
print(stop)
del data[start:]
print(data) 