import speech_recognition as sr
import os
from deep_translator import GoogleTranslator
from gtts import gTTS
import vlc

current_dir = os.getcwd()

filename = current_dir + "\output\Mon_enregistrement.wav"


r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)
    try:
        datafr = r.recognize_google(audio, language="fr-FR")
    except:
        print("Ressayez s'il vous plaît...")

file = open("rapport.txt", "w")
file.write("J'ai compris cette phrase : " + datafr + 2*"\n")

dataen = GoogleTranslator(source='fr', target='en').translate(datafr)
file.write("Je l'ai traduit en anglais : " + dataen + 2*"\n")

dataes = GoogleTranslator(source='fr', target='es').translate(datafr)
file.write("Je l'ai traduit en espagnol : " + dataes + 2*"\n")

datade = GoogleTranslator(source='fr', target='de').translate(datafr)
file.write("Je l'ai traduit en allemand : " + datade + 2*"\n")

datait = GoogleTranslator(source='fr', target='it').translate(datafr)
file.write("Je l'ai traduit en italien : " + datait + 2*"\n")

datasq = GoogleTranslator(source='fr', target='sq').translate(datafr)
file.write("Je l'ai traduit en albanais : " + datasq + 2*"\n")

dataeu = GoogleTranslator(source='fr', target='eu').translate(datafr)
file.write("Je l'ai traduit en basque : " + dataeu + 2*"\n")

dataca = GoogleTranslator(source='fr', target='ca').translate(datafr)
file.write("Je l'ai traduit en catalan : " + dataca + 2*"\n")

file.close()

langue = 'fr'

myobj = gTTS(text=datafr, lang=langue, slow=False)

myobj.save("speech.mp3")

p = vlc.MediaPlayer( current_dir + "/speech.mp3")

command = str(input("Voulez-vous lire la phrase reconnue ? \n"))

if command == 'oui' :
    p.play()