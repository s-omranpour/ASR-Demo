import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import librosa, librosa.display
import matplotlib.pyplot as plt

def record(duration, path):
    rec = sd.rec(int(duration * 16000), samplerate=16000, channels=1)
    sd.wait()
    print(rec.shape, np.sum(rec))
    write(path, 16000, rec.astype(np.int16))

def send(wav_file):
    url = "http://localhost:8090/speech/predict"
    rec, _ = librosa.load(wav_file, sr=16000)
    resp = requests.post(url, files={"file": rec.tobytes()})
    return json.loads(resp.text)

def display_waveplot(wav_file):
    y, sr = librosa.load(wav_file, sr=16000)
    fig = plt.figure(figsize=(10, 4))
    librosa.display.waveplot(y,x_axis='time')
    plt.title('Voice wave plot')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=False)
    

def display_spectrogram(wav_file):
    y, sr = librosa.load(wav_file, sr=16000)
    spec = librosa.amplitude_to_db(librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128))
    fig = plt.figure(figsize=(10, 4))
    librosa.display.specshow(spec, y_axis='mel', x_axis='time')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=False)
