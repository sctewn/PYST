# This is Pyst code
# Welcome to create a better version of yourself
# All the lines that start with '#' are comments, this is to describe the code so it is better for you to understand.


#First we need to install and import some libraries, if you are not familiar with python please check the file Learnpython.txt there is beginners youtube tutorials in English, Spanish and Japanese
#this are the libraries for installation pip or pip3 on your command terminal:
#pip install speechrecognition
#pip install pyttsx3
#pip install pyaudio
#pip install playsound==1.2.2
#pip install pandas

#Import Libraries
import speech_recognition as  sr #this will recognize your speech
import pyttsx3 #This is a library that convert text to speech
import calendar
import time
import csv #librarie to write, read, open and save csv files
from playsound import playsound
import pandas as pd

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def answerAnalyser(text):
    
    answer = pd.read_csv("habitAnswer.csv")
     
    for i in range(1, len(answer)):
        
        if text in answer['Answer'][i] and answer['Category'][i] == 'no': 
            filename = random.choice(os.listdir(r"Sounds/Bad"))
            print(filename)
            sound = 'Sounds/Bad/'+filename
            playsound(sound)
            engine.say("Seriously Bro?, can't believe it")
            engine.runAndWait()
        elif text in answer['Answer'][i] and answer['Category'][i] == 'waiting': 
            filename = random.choice(os.listdir(r"Sounds/Waiting"))
            print(filename)
            sound = 'Sounds/Waiting/'+filename
            playsound(sound) 
            engine.say("come on, how many days you need to do this?.")
            engine.runAndWait()
        elif text in answer['Answer'][i] and answer['Category'][i] == 'yes': 
            filename = random.choice(os.listdir(r"Sounds/Good"))
            print(filename)
            sound = 'Sounds/Good/'+filename
            playsound(sound) 
            engine.say("Here is your star for job done!")
            engine.runAndWait()
        else:
            print("i Didn't get it, please repeat it")



            

#Whit this code you can talk and will see on your terminal what have you said.
while True:
    
    try:
        engine.say("have you finish your task?") #will repeat with the loop, so try the answers.
        engine.runAndWait()
        
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
            print("Ok, you said: "+r.recognize_google(audio, language="en-EN"))
            
            answerAnalyser(r.recognize_google(audio, language="en-EN"))

    
    except sr.UnknownValueError:
        r = sr.Recognizer()
        continue
