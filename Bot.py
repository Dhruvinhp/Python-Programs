import speech_recognition as sr
import pyttsx3
import wikipedia

def speak(string):
    engine=pyttsx3.init()
    engine.say(string)
    engine.runAndWait()

def userInput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query

def out():
    query = userInput().lower()
    print("User said: {query}")
    results = wikipedia.summary(query, sentences=3)
    print(results)
    speak("Wikipedia said: ")
    speak(results)
    speak("Hello sir, How can i help you?")
    speak("what you want to search on WikiPedia?")
