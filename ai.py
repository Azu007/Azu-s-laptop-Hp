import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime


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
        print(f"user said:,{query}\n") 
    
    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query                
        
if __name__ == "__main__":
    # wishME()
    takeCommand()
