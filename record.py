import pyaudio
import wave
import os

audio = pyaudio.PyAudio()

current_dir = os.getcwd()

# Define a "output" directory :
directory = "/output"

path = current_dir + directory

isExist = os.path.exists(path)      # Valeure booléenne

if not isExist:
    # Create the directory
    # 'result' in
    # current directory
    os.mkdir(directory)

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:           # Change this condition to stop the stream
    pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wave.open(current_dir + "/output/Mon_enregistrement.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()