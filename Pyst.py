# This is Pyst code
# Welcome to create a better version of yourself
# All the lines that start with '#' are comments, this is to describe the code so it is better for you to understand.


#First we need to install and import some libraries, if you are not familiar with python please check the file Learnpython.txt there is beginners youtube tutorials in English, Spanish and Japanese


#Import Libraries
import speech_recognition as  sr #this will recognize your speech
import pyttsx3 #This is a library that convert text to speech
import calendar
import time
import csv #librarie to write, read, open and save csv files

r = sr.Recognizer()

while True:
    
    try:
        
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            
            print("Ok, you said: " + r.recognize_google(audio, language="es-ES"))
    
    except sr.UnknownValueError:
        r = sr.Recognizer()
        continue
