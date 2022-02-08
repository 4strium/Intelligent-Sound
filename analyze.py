import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

file = "Mon_enregistrement.wav"

# waveform :
signal, sample_rate = librosa.load(file, sr=22050) # sample rate * Time -> example -> 22050 * 30
librosa.display.waveshow(signal, sr=sample_rate)
plt.xlabel("Temps")                            # Nom de l'axe x
plt.ylabel("Amplitude")                        # Nom de l'axe y
plt.show()

#fft -> spectrum :
fft = np.fft.fft(signal)

magnitude = np.abs(fft)
frequency = np.linspace(0, sample_rate, len(magnitude))
plt.plot(frequency, magnitude)
plt.xlabel("Frequence")                            # Nom de l'axe x
plt.ylabel("Magnitude")                            # Nom de l'axe y
plt.show()

# stft -> spectrogram :

n_fft = 2048 
hop_length = 512

stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)
spectrogram = np.abs(stft)

log_spectrogram = librosa.amplitude_to_db(spectrogram)

librosa.display.specshow(log_spectrogram, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Temps")                            # Nom de l'axe x
plt.ylabel("Frequence")                        # Nom de l'axe y
plt.colorbar()
plt.show()

# MFFCs :
MFCCs = librosa.feature.mfcc(signal, sample_rate, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)
librosa.display.specshow(MFCCs, sr=sample_rate, hop_length=hop_length)
plt.xlabel("Temps")                            # Nom de l'axe x
plt.ylabel("MFCC")                             # Nom de l'axe y
plt.colorbar()
plt.show()