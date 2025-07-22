#and truth table
#              true            False
#   ------------------------------------------
# true --------true            false
# false        false           false

# Or Truth Table
#              true            False
#   ------------------------------------------
# true --------true            true
# false        true            false


age= int(input("how old are you?"))

# if age >=16 and age <= 65:
if 16 <= age <=65:
    print("Have a good day at work")
else:
    print("enjoy ur free time.")

print("-" * 80)

if age < 16 or age > 65:
    print("enjoy ur free time")

