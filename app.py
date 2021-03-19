import streamlit as st
import numpy as np
import librosa, librosa.display
import matplotlib.pyplot as plt

from utils import display_spectrogram, display_waveplot, record, send

WAVE_OUTPUT_FILE = "data/recorded.wav"

def main():
    st.title("ZLab ASR Demo")
    DURATION = st.slider('Duration', min_value=1, max_value=10)
    st.write('Press the record button and speak for', DURATION, 'seconds.\n Then press "transcribe" button to display the spoken text and its spectrogram plot!')
    
    if st.button('Record'):
        with st.spinner(f'Recording for {DURATION} seconds ....'):
            record(DURATION, WAVE_OUTPUT_FILE)
        st.success("Recording completed")

    if st.button('Play'):
        try:
            audio_file = open(WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
            display_waveplot(WAVE_OUTPUT_FILE)
            # display_spectrogram(WAVE_OUTPUT_FILE)
        except:
            st.write("Please record sound first")

    if st.button('Transcribe'):
        with st.spinner("Transcribing the voice"):
            text = 'salam'#send(WAVE_OUTPUT_FILE)
        st.write("Text:", text)
        st.write("\n")

        

if __name__ == '__main__':
    main()
