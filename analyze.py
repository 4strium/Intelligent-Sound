import librosa, librosa.display
import matplotlib.pyplot as plt

file = "Mon_enregistrement.wav"

# waveform :
signal, sr = librosa.load(file, sr=22050) # sr * T -> 22050 * 30
librosa.display.waveshow(signal, sr=sr)
plt.xlabel("Temps")                            # Nom de l'axe x
plt.ylabel("Amplitude")                        # Nom de l'axe y
plt.show()