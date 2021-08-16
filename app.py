import streamlit as st
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write, read

from utils import display_spectrogram, display_waveplot, send

WAVE_OUTPUT_FILE = "data/rec.wav"

def main():
    st.title("ZLab ASR Demo")
    password = st.text_input("Enter password:", "")

    duration = st.slider('Duration', min_value=1, max_value=10)
    st.write('Press the record button and speak for', duration, 'seconds.\n Then press "transcribe" button to display the spoken text and its spectrogram plot!')
    
    if st.button('Record'):
        with st.spinner(f'Recording for {duration} seconds ....'):
            rec = sd.rec(duration*16000, samplerate=16000, channels=1)
            sd.wait()
            write(WAVE_OUTPUT_FILE, 16000, rec)

        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            display_waveplot(WAVE_OUTPUT_FILE)
        except Exception as e:
            st.write('Error:', e)

        with st.spinner("Transcribing the voice"):
            res = send(WAVE_OUTPUT_FILE, password)
        st.write('Text:\n' + res)

        

if __name__ == '__main__':
    main()
