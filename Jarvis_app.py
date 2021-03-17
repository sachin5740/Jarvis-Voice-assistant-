import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as friday
import webbrowser as joker
import os 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishs():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("good morning sir")

    elif hour>=12 and hour<17:
        speak("good afternoon sir")

    else:
        speak("good evning sir")

    speak("i am Friday , please tell me what can i help you")

def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print(e)

        print("say that again please")
        speak("i can't understand, say that again")
        return "None"
    return query



    #speak("hello sachin")
while True:
    wishs()
    query=takecom().lower()
    if "who is" in query:
        speak("Searching .....")
        query = query.replace("who is", "")
        result=friday.summary(query,sentences=4)
        speak("Accoding to Wikipedia")
        print(result)
        speak(result)
        break
    elif "open youtube" in query:
        joker.open("youtube.com")
        break

    elif "open google" in query:
        joker.open("google.com")
        break
    elif "open stackoverflow" in query:
        joker.open("stackoverflow.com")
        break
    elif "search" in query:
        speak("Searching")
        result=query.replace("search", "")
        joker.open(f"https://www.google.com/search?q={result}&rlz=1C1CHBF_enIN872IN872&oq=god&aqs=chrome..69i57j0l7.1983j0j8&sourceid=chrome&ie=UTF-8")
    elif "play music" in query:
        Music_dir="address of directry"
        songs=os.listdir(Music_dir)
        os.startfile(os.path.join(Music_dir,songs[0]))
        break
    elif "time" in query:
        hour=datetime.datetime.now().time()
        print(f"time is: {hour}")
        speak(f"{hour}")

        break
    elif "vs code" in query:
        path="C:\\Users\\kapil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("Start visual studio code")
        os.startfile(path)
        break
    elif "who are you" in query:
        speak("i am your personal assistance Jarvis")
        break


        

