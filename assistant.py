import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#ptint(voices[1].id)
engine.setProperty('voices',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme(datetime): 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hey subagayathri,your assistant is here let me know how can I help you")
def takecommand():
    # it take a microphone input from the user returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.print_threahold =1
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print("user said",query)
    except Exception as e:
        print(e)
        speak("say that again please.....")    
        return "none"
    return query
if __name__ == '__main__':
    #speak("subagayathri is a good girl")
    wishme(datetime)
    #while True:
    if 1:
        query= takecommand().lower()
        
        if 'wikipedia' in query:
            speak("searching wikipedia.....please wait for a while")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak=("according to wikipedia") 
            print("results")             
            # speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube")
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open notepad' in query:
            npath='C:\\Users\\ELCOT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
            os.startfile(npath) 
        elif 'open calendar' in query:
            webbrowser.open("calendar.com")
        elif 'open code' in query:
            codepath='C:\python'
            os.startfile(codepath)
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%h:%m:%S")
            speak(f"mam the time is{strTime}")
        elif 'no thanks' in query:
            speak("thank you mam for using me. have a great day ahead")
sys.exit()            
                
                                   
        