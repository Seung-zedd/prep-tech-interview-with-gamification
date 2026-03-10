import sys
import os
import asyncio
import edge_tts
import re
# Suppress pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time

# Use ko-KR-InJoonNeural with senior-like adjustments
VOICE = "ko-KR-InJoonNeural"
RATE = "-10%"       # Slightly slower
PITCH = "-10Hz"     # Deeper voice

# Technical term translation map for natural senior pronunciation
TECH_TERMS = {
    "3-way handshake": "쓰리웨이 핸드쉐이크",
    "4-way handshake": "포웨이 핸드쉐이크",
    "TCP": "티씨피",
    "UDP": "유디피",
    "IP": "아이피",
    "DNS": "디엔에스",
    "HTTP": "에이치티티피",
    "HTTPS": "에이치티티피에스",
    "SYN": "씬",
    "ACK": "액",
    "FIN": "핀",
    "TIME_WAIT": "타임 웨이트",
    "handshake": "핸드쉐이크"
}

def preprocess_text(text):
    # Sort terms by length descending to avoid partial matches
    sorted_terms = sorted(TECH_TERMS.keys(), key=len, reverse=True)
    for term in sorted_terms:
        # Case insensitive replacement
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        text = pattern.sub(TECH_TERMS[term], text)
    return text

async def generate_tts(text, output_file):
    processed_text = preprocess_text(text)
    communicate = edge_tts.Communicate(processed_text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(output_file)

def speak(text):
    try:
        # Save session audio in a hidden dir
        audio_dir = os.path.join(os.getcwd(), '.session_audio')
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)
            
        temp_file = os.path.join(audio_dir, 'speech.mp3')
        
        # Generate high quality neural TTS
        asyncio.run(generate_tts(text, temp_file))
        
        # Play using pygame
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
            
        pygame.mixer.quit()
        
    except Exception as e:
        print(f"TTS ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_to_speak = " ".join(sys.argv[1:])
        speak(text_to_speak)
