import requests

r = requests.get("https://financialmodellingprep.com/developer/docs/pricing")
print(r.text)