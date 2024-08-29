import pyaudio
import wave
import threading
import io
from pydub import AudioSegment

FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 22050 
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
            default_device_index = self.audio.get_default_input_device_info()['index']
            stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                     rate=RATE, input=True,
                                     frames_per_buffer=CHUNK,
                                     input_device_index=default_device_index)
            
            while self.is_recording:
                data = stream.read(CHUNK, exception_on_overflow=False)
                self.frames.append(data)
            
            stream.stop_stream()
            stream.close()

        self.record_thread = threading.Thread(target=record)
        self.record_thread.start()

    def stop_recording(self):
        self.is_recording = False
        self.record_thread.join()
        self.audio.terminate()

    def get_mp3_data(self):
        wav_buffer = io.BytesIO()
        with wave.open(wav_buffer, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(self.frames))
        
        wav_buffer.seek(0)
        audio = AudioSegment.from_wav(wav_buffer)
        audio = audio.compress_dynamic_range()
        
        mp3_buffer = io.BytesIO()
        audio.export(mp3_buffer, format="mp3", bitrate="64k")
        
        return mp3_buffer.getvalue()

if __name__ == "__main__":
    recorder = AudioRecorder()
    print("Recording... Press Enter to stop.")
    recorder.start_recording()
    input()  
    recorder.stop_recording()
    
    mp3_data = recorder.get_mp3_data()
    print(f"MP3 data length: {len(mp3_data)} bytes")
