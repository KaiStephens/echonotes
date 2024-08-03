import pyaudio
import wave
import threading
import io

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.is_recording = False
        self.frames = []

    def start_recording(self):
        self.is_recording = True
        self.frames = []
        
        def record():
            stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                     rate=RATE, input=True,
                                     frames_per_buffer=CHUNK)
            
            while self.is_recording:
                data = stream.read(CHUNK)
                self.frames.append(data)
            
            stream.stop_stream()
            stream.close()
        
        self.record_thread = threading.Thread(target=record)
        self.record_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_thread.join()
        self.audio.terminate()

    def get_wav_data(self):
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(self.frames))
        return wav_buffer.getvalue()
