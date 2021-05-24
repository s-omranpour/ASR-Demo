import streamlit as st
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

from utils import display_spectrogram, display_waveplot, send
from record import Recorder

WAVE_OUTPUT_FILE = "data/rec.wav"

def main():
    st.title("ZLab ASR Demo")
    duration = st.slider('Duration', min_value=1, max_value=10)
    st.write('Press the record button and speak for', duration, 'seconds.\n Then press "transcribe" button to display the spoken text and its spectrogram plot!')
    
    recorder = Recorder(path=WAVE_OUTPUT_FILE)
    if st.button('Record'):
        with st.spinner(f'Recording for {duration} seconds ....'):
            recorder.record_n_save(duration)
        # st.success("Recording completed")

        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            display_waveplot(WAVE_OUTPUT_FILE)
            # display_spectrogram(WAVE_OUTPUT_FILE)
        except Exception as e:
            st.write('Error:', e)

    # if st.button('Transcribe'):
        with st.spinner("Transcribing the voice"):
            res = send(WAVE_OUTPUT_FILE)
        for k in res:
            st.write(k + ': ' + res[k])

        

if __name__ == '__main__':
    main()
