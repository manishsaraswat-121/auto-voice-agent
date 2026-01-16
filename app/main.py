from fastapi import FastAPI, UploadFile, File
from app.services.stt import speech_to_text
from app.services.tts import text_to_speech
from app.graph.workflow import workflow

app = FastAPI(title="Auto Dealership Voice Agent")


@app.post("/voice")
async def voice_agent(audio: UploadFile = File(...)):
    audio_bytes = await audio.read()
    user_text = speech_to_text(audio_bytes)

    result = workflow.invoke({"user_text": user_text})

    response_text = (
        f"Your test drive for {result['booking']['model']} "
        f"is scheduled on {result['booking']['date']} at {result['booking']['time']}."
    )

    return {
    "user_text": user_text,
    "response": response_text,
    "audio_file": text_to_speech(response_text)
    }

