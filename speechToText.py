import os
from openai import OpenAI
from apiInputs import openAPIKey
import io

os.environ["OPENAI_API_KEY"] = openAPIKey

client = OpenAI()

def transcribe_audio(audio_data):
    audio_file = io.BytesIO(audio_data)
    
    audio_file.name = "audio.wav"

    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

    return transcription.text

if __name__ == "__main__":
    audio_data = b"..." 

    transcript = transcribe_audio(audio_data)
    print(transcript)
