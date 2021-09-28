import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if 4<=hour<12:
        speak("Good Morning!")
    elif 12<=hour<=18:
        speak("Good Afternoon!")
    elif 18<hour<=21:
        speak("Good Evening!")
    else:
        speak("Good night!")

    speak("Hello, I'm JARVIS sir. Please tell me How may i help you?")

def takeCommand():
    '''
    Its takes microphone input from the user and return string output
    '''
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    
    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Hopeplateform@gmail.com", "Hope@plateform")
    server.sendmail("Hopeplateform@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    # takeCommand()
    while True:
        query = takeCommand().lower()
        if 'open Wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia") 
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("Stackoverflow.com")

        elif 'play music' in query:
            musicdir = "U:\\Music\\Songs\\English"
            songs = os.listdir(musicdir)
            print(songs)
            os.startfile(os.path.join(musicdir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir Time is {strTime}")
        
        elif "open code" in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "what's my name" in query:
            speak("Your name is Dhruvin")

        elif "Send email to Dhruvin" in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "dhruvinhprajapati@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("sorry my dear i'm unbale to send this email")