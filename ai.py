# from lib2to3.pytree import _Results
# from unittest import result
import glob
import time
import sys
import webbrowser
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import random



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishME():
     hour=int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning")
     elif hour>=12 and hour>18:
         speak("Good Afternoon")
     else:
         speak("Good Evening")
         
speak("I am afreen Sir. Please tell me how may I help you")             
     
     
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listining....")
        r.pause_threshold =1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n") 
    
    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query                
        
if __name__ == "__main__":
    wishME()
    takeCommand()
    # while True:
    if 2:
        query = takeCommand().lower()



        if 'Wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
           

            music_dir = 'C:\\Users\\Md-Azmat\\Desktop\\SnapTube'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice (songs))) 


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")              
        
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Md-Azmat\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
