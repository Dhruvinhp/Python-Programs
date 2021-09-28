import json

data = '{"Name":"Dhruvin", "Erno":"18"}'
print(data[0])

# parsed = json.loads(data)
# parsed2 = json.load(data)
# print(parsed, parsed2)

data2 = {
    "name":"Dhruvin",
    "cars":['bmw','audi','ferrari'],
    "fridge":('roti',460),
    "isbad":False
} 

jscom = json.dumps(data2)
print(jscom)