import pydub
import os

current_dir = os.getcwd()

song = pydub.AudioSegment.from_wav(current_dir + "\output\Mon_enregistrement.wav")
pydub.play(song)