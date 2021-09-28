mobile={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
phone=input(">Phone: ")
out=""
for ch in phone:
    out+=mobile.get(ch,"!") + " "
print(out)

def emojis(message):
    words= message.split(" ")
    emojis={
        ":)":"😃",
        ":(":"😢"
    }
    out=""
    for word in words:
        out+=emojis.get(word,word)
    return out
message=input(">")
result=emojis(message)
print(result)