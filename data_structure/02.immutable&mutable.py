#immutable  objects means they cant be changed if u change the id will change with it
# like data type ----- int, float, bool, str, tuble, froxenset they cant be changed


#checking with bool if the id means value are unchangeable
# result=True
# another_result= result
# print(id(result))  # id () return the identity of the object
# print(id(another_result))
#-------
# result=False
# print(id(result))
#-------

# checking with str
# result="correct"
# another_result=result
# print(id(result))
# print(id(another_result))
#-------------------------------------------------
#mutable objects means they can be changeable 
#those are---- list, dict, set, bytearray

computer_parts=["computer",
                "monitor",
                "keyboard",
                "mouse",
                "mouse mat"]

another_list=computer_parts
print(id(computer_parts))
print(id(another_list))

computer_parts+= ["CPU"]
print(computer_parts)
print(id(computer_parts))
print(id(another_list))