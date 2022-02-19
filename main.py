import os
import shutil
import time
import webbrowser
# Code that executes the subroutines one after the other.

exec(open("record.py").read())

exec(open("analyze.py").read())

current_dir = os.getcwd()

target = current_dir + "\\public\image"

original1 = current_dir + "\\result\ondes.png"
shutil.copy(original1, target)

original2 = current_dir + "\\result\spectre_audio.png"
shutil.copy(original2, target)

original3 = current_dir + "\\result\spectrogram.png"
shutil.copy(original3, target)

original4 = current_dir + "\\result\MFCC.png"
shutil.copy(original4, target)

exec(open("reconnaissance.py").read())

time.sleep(5)

new = 2 # open in a new tab, if possible
url = current_dir + "/index.html"
webbrowser.open(url,new=new)

webbrowser.open("rapport.txt")