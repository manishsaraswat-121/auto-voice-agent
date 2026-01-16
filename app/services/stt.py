'''import whisper
model = whisper.load_model("base")

def speech_to_text(audio_path):
    return model.transcribe(audio_path)["text"]'''
    
def speech_to_text(audio_path: str):
    # Temporary fallback for Windows environments
    return "I want to book a test drive for an SUV tomorrow at 11 AM"

