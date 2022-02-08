import os
import webbrowser
# Code that executes the subroutines one after the other.

exec(open("record.py").read())

exec(open("analyze.py").read())

current_dir = os.getcwd()

new = 2 # open in a new tab, if possible
url = current_dir + "/index.html"
webbrowser.open(url,new=new)