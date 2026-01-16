import pyttsx3
import uuid
import os

OUTPUT_DIR = "app/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

engine = pyttsx3.init()

def text_to_speech(text: str) -> str:
    file_name = f"{uuid.uuid4()}.wav"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    engine.save_to_file(text, file_path)
    engine.runAndWait()

    return file_path
