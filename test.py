age= 25
print(type(age))
age="25"
print(type(age)) 

my_list = [10, 20, 30]

# Get iterator
my_iter = iter(my_list)

# Use next() to manually get items
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30

# String + Array Manipulation
# for i in range(1,13):
text = "Hello world Python is fun"
print(text)
result = text.split()
print(result)

# ----
data = "apple,banana,cherry"
result = data.split(",")
print(result)

# ------
date = "2025-07-16"
result = date.split("-")
print(result)

#===
emails = ["alice@abc.com", "bob@company.org", "charlie@xyz.net"]

results = []
for email in emails:
    name, domain = email.split('@', 1)
    results.append([name, '@' + domain])

print(results)
#-------
# emails = input_string.split(",")
# company_emails = []

# for email in emails:
#     if email.endswith("@company.com"):
#         company_emails.append(email)
        
#     return company_emails


#==========================================
# Object Filtering
#You have a list of users with age and country.
# Return all users above 30 and from Bangladesh.
[
  {"name": "A", "age": 32, "country": "Bangladesh"},
  {"name": "B", "age": 25, "country": "India"},
  {"name": "C", "age": 35, "country": "Bangladesh"}
]

# 1. result = []

# 2. for user in users:
#      if user.age > 30 and user.country == "Bangladesh":
#          result.append(user)

# 3. return result

#==========================
# counting words
#  


