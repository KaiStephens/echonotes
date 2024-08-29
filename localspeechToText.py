import whisper
import tempfile
import os

def transcribe_audio(audio_data, model_name="base"):
    """
    Transcribe audio using the local Whisper model.
    
    :param audio_data: bytes object containing the MP3 audio data
    :param model_name: name of the Whisper model to use (default: "base")
    :return: transcribed text
    """
    model = whisper.load_model(model_name)
    
    # Create a temporary file to store the MP3 data
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        temp_file.write(audio_data)
        temp_file_path = temp_file.name

    try:
        result = model.transcribe(temp_file_path)
        return result["text"]
    finally:
        os.unlink(temp_file_path)

if __name__ == "__main__":
    from audioRecorder import AudioRecorder
    
    recorder = AudioRecorder()
    print("Recording... Press Enter to stop.")
    recorder.start_recording()
    input()
    recorder.stop_recording()
    
    audio_data = recorder.get_mp3_data()
    transcript = transcribe_audio(audio_data)
    print("Transcript:", transcript)