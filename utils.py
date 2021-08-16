import numpy as np
import requests
import librosa, librosa.display
import streamlit as st
import matplotlib.pyplot as plt
import json

def send(wav_file, password = None):
    url = "http://asr.fanaplab.com:5000/transcribe"
    rec, _ = librosa.load(wav_file, sr=16000)
    files = {"file" : rec.tobytes()}
    resp = requests.post(url, files=files, params={'password': password})
    return json.loads(resp.text)

def display_waveplot(wav_file):
    y, sr = librosa.load(wav_file, sr=16000)
    fig = plt.figure(figsize=(10, 4))
    librosa.display.waveplot(y,x_axis='time')
    plt.title('Voice wave plot')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=True)
    

def display_spectrogram(wav_file):
    y, sr = librosa.load(wav_file, sr=16000)
    spec = librosa.amplitude_to_db(librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128))
    fig = plt.figure(figsize=(10, 4))
    librosa.display.specshow(spec, y_axis='mel', x_axis='time')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    st.pyplot(fig, clear_figure=False)
