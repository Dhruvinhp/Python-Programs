import requests

r =  requests.get("https://financialmodelingprep.com/developer/docs/")
# print(r.text)
print(r.status_code)

url = "http://www.google.com"
data = {
        "p1":4,
        "p2":8
}

r2 = requests.post(url=url, data = data)
print(r2)