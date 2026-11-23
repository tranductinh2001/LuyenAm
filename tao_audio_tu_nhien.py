# -*- coding: utf-8 -*-
import os
import asyncio
import edge_tts
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE_DIR, "BAI_NOP_HOAN_CHINH")
PUBLIC_DIR = r"C:\Users\X1\Desktop\tài liệu THCS Đắk Trôi\thaogiang\public\audio_generated"
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(PUBLIC_DIR, exist_ok=True)

SCRIPT_AUDIO_1_SPK1 = (
    "Hey Brad! Are you ready to leave? Did you peel the apples and put the peel in the bin? "
    "Oh no, stop it leaking! Do not just let the dog lick it! Take a pin or a peg to fix it. "
    "Wait, do we need bread or jam? Got it. Should I bring a pen to write down the bill, "
    "or maybe a cheque? Okay. By the way, where are we going to live during the trip? "
    "Near the sheep or near the big ship? Awesome! Ring the bell, mark an X on the map, and let us go!"
)

SCRIPT_AUDIO_1_SPK2 = (
    "Yes, I did. But look at the sink, it is starting to leak! Fixed! "
    "Now, what about the food? Should I pack this tin of beans? Both! "
    "Put the bread in a pan, and throw out that old bean in the bin. "
    "Just bring a pen. Oh, and do not forget to send a message to the men at the farm. "
    "Near the field. We can see the cute little chicks with yellow cheeks, a little pig, and maybe even a sheep."
)

async def synth_and_copy(text, voice, out_name):
    out_path = os.path.join(OUT_DIR, out_name)
    comm = edge_tts.Communicate(text, voice, rate="-3%")
    await comm.save(out_path)
    pub_path = os.path.join(PUBLIC_DIR, out_name)
    shutil.copy2(out_path, pub_path)
    print(f"OK: {out_name} ({os.path.getsize(out_path)} bytes)")

async def main():
    # 1. Brian (Nam - Cực kỳ tự nhiên, giọng ấm, đàm thoại mượt)
    await synth_and_copy(SCRIPT_AUDIO_1_SPK1, "en-US-BrianMultilingualNeural", "Audio_1_Spk1_Brian_TuNhien.mp3")
    await synth_and_copy(SCRIPT_AUDIO_1_SPK2, "en-US-BrianMultilingualNeural", "Audio_1_Spk2_Brian_TuNhien.mp3")
    
    # 2. Ava (Nữ - Trong trẻo, tự nhiên, nhả chữ hội thoại đời thực)
    await synth_and_copy(SCRIPT_AUDIO_1_SPK1, "en-US-AvaMultilingualNeural", "Audio_1_Spk1_Ava_NuTuNhien.mp3")
    await synth_and_copy(SCRIPT_AUDIO_1_SPK2, "en-US-AvaMultilingualNeural", "Audio_1_Spk2_Ava_NuTuNhien.mp3")
    
    # 3. Ryan (Nam - Giọng Anh-Anh rất cuốn, tự nhiên, không cứng nhắc)
    await synth_and_copy(SCRIPT_AUDIO_1_SPK1, "en-GB-RyanNeural", "Audio_1_Spk1_Ryan_GiongAnh.mp3")
    await synth_and_copy(SCRIPT_AUDIO_1_SPK2, "en-GB-RyanNeural", "Audio_1_Spk2_Ryan_GiongAnh.mp3")

if __name__ == "__main__":
    asyncio.run(main())
