#using 'continue' in for loop

shopping_list = ["milk", "paste", "egg", "spam", "bread", "rice"]

for item in shopping_list:
    if item =="spam":
        continue # when its appers in a loop its case everything else in the loop to be ignored    
        print("im ignored!!")
    print("buy " + item) 