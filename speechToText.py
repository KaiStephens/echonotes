import assemblyai as aai
import io

from apiInputs import assemAPIKey

aai.settings.api_key = assemAPIKey

def transcribe_audio(audio_data):
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(speaker_labels=True)
    
    # Create a file-like object from the audio data
    audio_file = io.BytesIO(audio_data)
    
    transcript = transcriber.transcribe(
        audio_file,
        config=config
    )
    
    return transcript.utterances
