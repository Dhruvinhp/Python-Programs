from win32com.client import Dispatch
import requests
import json

def speak(str):
    speak=Dispatch("SAPI.spVoice")
    speak.Speak(str)

if __name__ == '__main__':
    url = ('https://newsapi.org/v2/top-headlines?'
           'sources=bbc-sport&'
           'apiKey=d311100c6c7144948c3be2b97313b654')

    rs = requests.get(url)
    text = rs.text
    my_json = json.loads(text)
    for i in range(0, 11):
        speak(my_json['articles'][i]['title'])