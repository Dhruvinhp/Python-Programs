dic={
    "name":"Dhruvin Prajapati",
    "age":19,
    "is_available":True
}
print(dic["name"])
print(dic.get("BirthDate"))
print(dic.get("BirthDate","5th Oct 2000"))
dic["name"]="CEO"
print(dic["name"])