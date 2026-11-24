import os
import json
import asyncio
import edge_tts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DIR = os.path.join(BASE_DIR, "sample_audio")
SCRIPTS_FILE = os.path.join(BASE_DIR, "audio_scripts_data.json")

os.makedirs(SAMPLE_DIR, exist_ok=True)

# Speaker voices
VOICE_SPK1 = "en-US-BrianMultilingualNeural"   # Natural expressive male voice
VOICE_SPK2 = "en-US-AvaMultilingualNeural"     # Natural expressive female voice

async def generate_sentence_audio(text, voice, out_path):
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        print(f"Skipping existing: {os.path.basename(out_path)}")
        return
    try:
        comm = edge_tts.Communicate(text, voice=voice, rate="-2%")
        await comm.save(out_path)
        print(f"Generated: {os.path.basename(out_path)} ({os.path.getsize(out_path)} bytes)")
    except Exception as e:
        print(f"Error generating {os.path.basename(out_path)}: {e}")

async def main():
    with open(SCRIPTS_FILE, "r", encoding="utf-8") as f:
        scripts = json.load(f)
    
    tasks = []
    # Semi-parallel to avoid rate limits (batches of 5)
    for audio_id in ["1", "2", "3", "4", "5"]:
        audio_data = scripts.get(audio_id, {})
        for spk_key, voice, spk_num in [("speaker_1", VOICE_SPK1, 1), ("speaker_2", VOICE_SPK2, 2)]:
            sentences = audio_data.get(spk_key, [])
            for idx, s in enumerate(sentences):
                text = s.get("text", "").strip()
                if not text:
                    continue
                out_name = f"audio_{audio_id}_spk_{spk_num}_sent_{idx}.mp3"
                out_path = os.path.join(SAMPLE_DIR, out_name)
                tasks.append(generate_sentence_audio(text, voice, out_path))
    
    print(f"Total sentences to generate: {len(tasks)}")
    
    # Run in batches of 6
    batch_size = 6
    for i in range(0, len(tasks), batch_size):
        batch = tasks[i:i+batch_size]
        await asyncio.gather(*batch)
        await asyncio.sleep(0.5)

    print("All sample audio generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
