import re

mystr = '''
Good morning sir/ma'am
Thank you for giving me this opportunity
My self Dhruvin Prajapati
Im from Ahmedabad, Gujarat
I study Information technology from Government Engineering College Modasa
Im creative, optimistic and determined person
My hobbies are Drawing, Traveling
My strength is I'm self motivated and hardworker and always carries a positive attitude
My weakness is I trust people easily and I cannot say no if someone asks for help
My short term goals are to get a job in a reputed company like yours and improve my knowledge and skills
My long term goal is to achieve a good position where I can build my career
Thats all about me 
Thank you.
mobile numbers: +91-7600704046, +91-9723886255, 8563355371, +91-7056856571

'''

# searching techniques:
#findall, search, split, sub, finditer

# Meta character:

# pt = re.compile(r'My') # r for ignore inline commands like \n
# pt1 = re.compile(r'.') # . for search all character
# pt2 = re.compile(r'.ing')#  for search End character with front character
# pt3 = re.compile(r'^My') # ^ for search staring character with
# pt = re.compile(r'ing$') # $ for search ending with words
# pt = re.compile(r'my*') # * for 0 or more Ending y character with m
# pt = re.compile(r'my+') # + for 1 or more ending y character with m
# pt = re.compile(r'Th{1}') # {} for search many ending h character with T
# pt = re.compile(r'(my){1}') # () for group search, not only ending but all group
# pt = re.compile(r'my|go') # | for either or, either my or go

# Special sequences:
# pt = re.compile(r'\AGo') # \A returns a match if specified characters are at the beginning of the string
# pt = re.compile(r'\bmy') # \b returns a match if specified characters are at the beginning or at the enging of the word
# pt = re.compile(r'ed\b')
pt = re.compile(r'\d{10}')  # \d for search integer values


matches = pt.finditer(mystr)  # finditer function
for match in matches:
    print(match)
