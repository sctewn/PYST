# This is Pyst code
# Welcome to create a better version of yourself
# All the lines that start with '#' are comments, this is to describe the code so it is better for you to understand.


#First we need to install and import some libraries, if you are not familiar with python please check the file Learnpython.txt there is beginners youtube tutorials in English, Spanish and Japanese
#this are the libraries for installation pip or pip3 on your command terminal:
#pip install speechrecognition
#pip install pyttsx3
#pip install pyaudio
#pip install playsound==1.2.2

#Import Libraries
import speech_recognition as  sr #this will recognize your speech
import pyttsx3 #This is a library that convert text to speech
import calendar
import time
import csv #librarie to write, read, open and save csv files
from playsound import playsound

r = sr.Recognizer()

#Whit this code you can talk and will see on your terminal what have you said.
while True:
    
    try:
        
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
            if 'no' in r.recognize_google(audio, language="en-EN"): 
                a = random.choice(os.listdir(r"Sounds/Bad"))
                print(a)
                sound = 'Sounds/Bad/'+a
                playsound(sound)
            elif 'i will do it' in r.recognize_google(audio, language="en-EN"): 
                b = random.choice(os.listdir(r"Sounds/Waiting"))
                print(b)
                sound = 'Sounds/Waiting/'+b
                playsound(sound) 
            elif 'yes i will' in r.recognize_google(audio, language="en-EN"): 
                c = random.choice(os.listdir(r"Sounds/Waiting"))
                print(c)
                sound = 'Sounds/Waiting/'+c
                playsound(sound) 
            elif 'wait' in r.recognize_google(audio, language="en-EN"): 
                d = random.choice(os.listdir(r"Sounds/Waiting"))
                print(d)
                sound = 'Sounds/Waiting/'+d
                playsound(sound) 
            elif 'hold on' in r.recognize_google(audio, language="en-EN"): 
                e = random.choice(os.listdir(r"Sounds/Waiting"))
                print(e)
                sound = 'Sounds/Waiting/'+e
                playsound(sound)     
            elif 'done' in r.recognize_google(audio, language="en-EN"): 
                f = random.choice(os.listdir(r"Sounds/Good"))
                print(f)
                sound = 'Sounds/Good/'+f
                playsound(sound) 
            elif 'yes' in r.recognize_google(audio, language="en-EN"): 
                g = random.choice(os.listdir(r"Sounds/Good"))
                print(g)
                sound = 'Sounds/Good/'+g
                playsound(sound)     
            else:
                print("i Didn't get it, please repeat it")

    
    except sr.UnknownValueError:
        r = sr.Recognizer()
        continue
