# === mock_voice.py ===

import asyncio
import edge_tts
import os
import uuid
import glob

VOICE = "th-TH-PremwadeeNeural"


async def speak(text):
    output = f"voice_{uuid.uuid4().hex}.mp3"  # ชื่อไฟล์ไม่ซ้ำกันทุกครั้ง

    tts = edge_tts.Communicate(text, VOICE)
    await tts.save(output)

    os.startfile(output)

    
    for f in glob.glob("voice_*.mp3"):
        if f != output:
            try:
                os.remove(f)
            except PermissionError:
                pass 


def simple():
    asyncio.run(speak("ระวังข้างหน้า"))


def near():
    asyncio.run(speak("มีสิ่งกีดขวางอยู่ใกล้"))


def danger():
    asyncio.run(speak("อันตราย กรุณาหยุด"))


if __name__ == "__main__":
    simple()