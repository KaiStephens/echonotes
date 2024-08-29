from audioRecorder import AudioRecorder
from speechToText import transcribe_audio
from aiSummarizer import summarizeText
from datetime import datetime

# Initialize variables
file_content = ""
current_time = datetime.now().strftime("%Y-%m-%d-%H-%M")

# Start recording
recorder = AudioRecorder()
print("Recording... Press Enter to stop.")
recorder.start_recording()
input()  # Wait for Enter key to stop
recorder.stop_recording()

# Process the recorded audio
print("Processing audio...")
audio_data = recorder.get_mp3_data()
transcription = transcribe_audio(audio_data)

# Since Whisper likely returns a single string:
if isinstance(transcription, str):
    file_content += transcription
elif isinstance(transcription, list):
    for utterance in transcription:
        file_content += f"{utterance}\n"

# Summarize the transcription
summary = summarizeText(file_content)
print(summary)

# Save the summary and transcript to a file
with open(f"{current_time}.txt", "w") as f:
    f.write("[Summary]\n\n" + summary + "\n\n[Transcript]\n\n" + file_content)
