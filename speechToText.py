import os
from openai import OpenAI
from apiInputs import openAPIKey
import io

# Set your API key as an environment variable
os.environ["OPENAI_API_KEY"] = openAPIKey

# Initialize the client
client = OpenAI()

def transcribe_audio(audio_data):
    # Create a file-like object from the audio data
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
