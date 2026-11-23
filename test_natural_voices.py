# -*- coding: utf-8 -*-
import asyncio
import edge_tts
import os

TEXT = "Hey Brad! Are you ready to leave? Did you peel the apples and put the peel in the bin? Oh no, stop it leaking! Do not just let the dog lick it."

async def main():
    voices = {
        "andrew": "en-US-AndrewMultilingualNeural",
        "brian": "en-US-BrianMultilingualNeural",
        "ava": "en-US-AvaMultilingualNeural",
        "ryan": "en-GB-RyanNeural"
    }
    for name, voice in voices.items():
        out = f"test_{name}.mp3"
        print(f"Synthesizing with {name} ({voice})...")
        comm = edge_tts.Communicate(TEXT, voice=voice, rate="-3%")
        await comm.save(out)
        print(f"Saved {out} (size: {os.path.getsize(out)} bytes)")

if __name__ == "__main__":
    asyncio.run(main())

