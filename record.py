import pyaudio
import numpy as np
import wave

class Recorder:
    def __init__(self, rate=16000, path='data/rec.wav', chunk_size=1024):
        self.audio = pyaudio.PyAudio()
        self.rate = rate
        self.path = path
        self.chunk_size = chunk_size 
    
    def record_n_save(self, duration):
        frames = []
        stream = self.audio.open(format=pyaudio.paInt16, 
                            channels=1,
                            rate=self.rate, 
                            input=True,
                            frames_per_buffer=self.chunk_size)

        for i in range(0, int(self.rate / self.chunk_size * duration)):
            frames.append(stream.read(self.chunk_size))
        stream.stop_stream()
        stream.close()
        # audio.terminate()

        waveFile = wave.open(self.path, 'wb')
        waveFile.setnchannels(1)
        waveFile.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        waveFile.setframerate(self.rate)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()




