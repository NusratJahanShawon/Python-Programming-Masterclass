
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
# [
#   {"name": "A", "age": 32, "country": "Bangladesh"},
#   {"name": "B", "age": 25, "country": "India"},
#   {"name": "C", "age": 35, "country": "Bangladesh"}
# ]

# 1. result = []

# 2. for user in users:
#      if user.age > 30 and user.country == "Bangladesh":
#          result.append(user)

# 3. return result

#==========================
# counting words
#  


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

