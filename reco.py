import speech_recognition as sr
import os

current_dir = os.getcwd()

filename = current_dir + "\output\Mon_enregistrement.wav"


r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)
    try:
        data = r.recognize_google(audio, language="fr-FR")
        print(data)
    except:
        print("Ressayez s'il vous plaît...")

file = open("robot.txt", "w")
file.write(data + "\n")

file.close()