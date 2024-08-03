from audioRecorder import AudioRecorder
from speechToText import transcribe_audio
from aiSummarizer import summarizeText
import os
from datetime import datetime

file_content = ""
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M")

recorder = AudioRecorder()
print("Recording... Press Enter to stop.")
recorder.start_recording()
input()  # Wait for Enter key
recorder.stop_recording()
    
print("Processing audio...")
audio_data = recorder.get_wav_data()
utterances = transcribe_audio(audio_data)
    
for utterance in utterances:
    file_content += (f"Speaker {utterance.speaker}: {utterance.text}")

summary = summarizeText(file_content)

print(summary)

with open(current_time, "w") as f:
    f.write("[Summary]\n \n" + str(summary) + "\n \n[Transcript] \n \n" + file_content)
