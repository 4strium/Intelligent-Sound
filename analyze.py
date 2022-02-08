import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

FIG_SIZE = (15,10)

current_dir = os.getcwd()

file = current_dir + "\output\Mon_enregistrement.wav"

# Define a "result" directory :
directory = "/result"

path = current_dir + directory
print(path)

isExist = os.path.exists(path)      # Valeure booléenne

if not isExist:
    # Create the directory
    # 'result' in
    # current directory
    os.mkdir(directory)


signal, sample_rate = librosa.load(file, sr=22050) # sample rate * Time -> example -> 22050 * 30

# waveform :
plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(signal, sr=sample_rate, alpha=0.6)
plt.xlabel("Temps (en secondes)")                            # Nom de l'axe x
plt.ylabel("Amplitude")                        # Nom de l'axe y
plt.title("Ondes")
plt.savefig(current_dir + '/result/ondes.png', bbox_inches='tight')

#fft -> spectrum :
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sample_rate, len(magnitude))
plt.figure(figsize=FIG_SIZE)
plt.plot(frequency, magnitude)
plt.xlabel("Frequence")                            # Nom de l'axe x
plt.ylabel("Magnitude")                            # Nom de l'axe y
plt.title("Spectre Audio")
plt.savefig(current_dir + '/result/spectre_audio.png', bbox_inches='tight')

# stft -> spectrogram :

n_fft = 2048 
hop_length = 512

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)
spectrogram = np.abs(stft)

log_spectrogram = librosa.amplitude_to_db(spectrogram)

plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(log_spectrogram, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Temps")                            # Nom de l'axe x
plt.ylabel("Frequence")                        # Nom de l'axe y
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram (DeciBel)")
plt.savefig(current_dir + '/result/spectrogram.png', bbox_inches='tight')

# MFCCs :
MFCCs = librosa.feature.mfcc(y=signal, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(MFCCs, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC coefficients")
plt.colorbar()
plt.title("Spectre de puissance à court terme d'un son")
plt.savefig(current_dir + '/result/MFCC.png', bbox_inches='tight')
