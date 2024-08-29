from audioRecorder import AudioRecorder
from speechToText import transcribe_audio
from aiSummarizer import summarizeText
from datetime import datetime

file_content = ""
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M")

recorder = AudioRecorder()
print("Recording... Press Enter to stop.")
recorder.start_recording()
input() 
recorder.stop_recording()

print("Processing audio...")
audio_data = recorder.get_mp3_data()
transcription = transcribe_audio(audio_data)

if isinstance(transcription, str):
    file_content += transcription
elif isinstance(transcription, list):
    for utterance in transcription:
        file_content += f"{utterance}\n"

summary = summarizeText(file_content)
print(summary)

with open(f"recordings/{current_time}.txt", "w") as f:
    f.write("[Summary]\n\n" + summary + "\n\n[Transcript]\n\n" + file_content)
