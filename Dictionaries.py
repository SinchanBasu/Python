# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:59:49 2021

@author: SINCHAN BASU
"""

import speech_recognition as sr
AUDIO_FILE=("sample_sinchan.wav")
# use auio file as a source

r=sr.Recognizer() #initialise the recogniser

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
#reads the audio file

try:
    print("audio file contains" + r.recognize_google(audio))
except sr.UnknownValueError :
      print("Google Speech Recognition could not understand audio")
except sr.RequestError :
     print ("couldn't get the results from Google Speech Recognition")      