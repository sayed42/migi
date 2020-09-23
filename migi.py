import pyttsx3 
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import smtplib
engine  =  pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice','english+f3')
engine.setProperty('rate',150)
#print(voices[16].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


print("What's the matter?")
speak("What's the matter?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("I didn't get you , Say that again clearly or fuck off...")
        speak("I didn't get you , Say that again clearly or fuck off...")
        
        return "None"
    return query
if __name__=="__main__":
    takeCommand()
    while True:
        query= takeCommand().lower()
        if 'who is' in query:
            print("Yeah , I know something about that human....")
            speak("Yeah , I know something about that human....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences= 2)
            print(results)
            speak(results)
            
        elif 'what is' in query:
            print("Yeah , I know something about that stuff....")
            speak("Yeah , I know something about that stuff....")
            
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open youtube' in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            
            webbrowser.open("https://www.youtube.com")
        elif 'open instagram' in query:
            print("Opening Instagram...")
            speak("Opening Instagram...")
            webbrowser.open("https://www.instagram.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"It's already{strTime}")
            speak(f"it's already{strTime}")
            
        elif 'are you' in query:
            print("My name is migi , one of the closest friend of Sayed and my task is to do stuff for him which he always gets bored to do ...also I have the entire data of wikipedia which helps me to share knowledge which you don't know about")
            speak("My name is migi , one of the closest friend of Sayed and my task is to do stuff for him which he always gets bored to do ...also I have the entire data of wikipedia which helps me to share knowledge which you don't know about")
        elif 'sleep' in query:
            print("ok so goodbye for now...")
            speak("Ok! so goodbye for now...")
            break

        


