# -*- coding: utf-8 -*-
"""
tao_audio_bai_nop_5_bai.py
Tự động xuất 5 bài tập âm thanh hoàn chỉnh (Audio 1 đến Audio 5) 
sử dụng mô hình giả lập ngữ điệu học viên tự nhiên (~85% chuẩn) 
kèm bộ lọc âm học micro tai nghe phòng học để nộp bài cho giảng viên.
"""

import os
import sys
import re
import asyncio
import subprocess
import edge_tts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "BAI_NOP_HOAN_CHINH")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Đọc kịch bản 5 bài đã tách sẵn
SCRIPT_FILE = os.path.join(BASE_DIR, "Kich_Ban_Doc_Theo_Tung_Audio.txt")

def parse_scripts():
    with open(SCRIPT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    audios = re.split(r'#{10,}\s*AUDIO\s*(\d+)\s*#{10,}', content)
    results = {}
    for i in range(1, len(audios), 2):
        audio_num = int(audios[i])
        body = audios[i + 1]
        results[audio_num] = {}
        for m in re.finditer(r'---\s*\[(.*?)\]\s*---\s*\n(.*?)(?=\n---|---|\Z)', body, re.DOTALL):
            title = m.group(1).strip()
            txt = m.group(2).strip()
            if "SPEAKER 1" in title:
                results[audio_num]["speaker1"] = txt
            elif "SPEAKER 2" in title:
                results[audio_num]["speaker2"] = txt
            elif "CẢ 2 VAI" in title:
                results[audio_num]["both"] = txt
    return results

def apply_student_mic_filter(in_file, out_file, speed=0.88):
    cmd = [
        "ffmpeg", "-y", "-i", in_file,
        "-filter:a", f"atempo={speed},highpass=f=110,lowpass=f=7000,volume=1.08",
        "-q:a", "3",
        out_file
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

async def generate_all_assignments():
    data = parse_scripts()
    print("=" * 65)
    print("🚀 BẮT ĐẦU TẠO 5 BÀI TẬP ÂM THANH HOÀN CHỈNH CHO MÔN LUYỆN ÂM VB2")
    print("   Phong cách: Giả lập học viên Việt Nam tự nhiên (~85% chuẩn)")
    print("=" * 65)

    voice_male = "en-US-GuyNeural"
    voice_female = "en-US-JennyNeural"

    generated_files = []

    for num in range(1, 6):
        script_data = data.get(num, {})
        # 1. Xuất file Speaker 1 (thường là vai chính của học viên)
        spk1_text = script_data.get("speaker1", "")
        if spk1_text:
            raw_tmp = os.path.join(OUTPUT_DIR, f"temp_raw_audio_{num}_spk1.mp3")
            final_mp3 = os.path.join(OUTPUT_DIR, f"Bai_Nop_Audio_{num}_Speaker_1.mp3")
            comm = edge_tts.Communicate(spk1_text, voice=voice_male, rate="+0%", pitch="-1Hz")
            await comm.save(raw_tmp)
            apply_student_mic_filter(raw_tmp, final_mp3, speed=0.88)
            if os.path.exists(raw_tmp):
                os.remove(raw_tmp)
            dur = subprocess.check_output([
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", final_mp3
            ]).decode().strip()
            print(f"✅ Audio {num} [Speaker 1]: {os.path.basename(final_mp3)} ({float(dur):.1f}s)")
            generated_files.append(final_mp3)

        # 2. Xuất file Speaker 2 (nếu bài yêu cầu nộp vai 2)
        spk2_text = script_data.get("speaker2", "")
        if spk2_text:
            raw_tmp = os.path.join(OUTPUT_DIR, f"temp_raw_audio_{num}_spk2.mp3")
            final_mp3 = os.path.join(OUTPUT_DIR, f"Bai_Nop_Audio_{num}_Speaker_2.mp3")
            comm = edge_tts.Communicate(spk2_text, voice=voice_male, rate="+0%", pitch="-1Hz")
            await comm.save(raw_tmp)
            apply_student_mic_filter(raw_tmp, final_mp3, speed=0.88)
            if os.path.exists(raw_tmp):
                os.remove(raw_tmp)
            dur = subprocess.check_output([
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", final_mp3
            ]).decode().strip()
            print(f"✅ Audio {num} [Speaker 2]: {os.path.basename(final_mp3)} ({float(dur):.1f}s)")
            generated_files.append(final_mp3)

    print("\n🎉 ĐÃ TẠO TOÀN BỘ 5 BÀI TẬP THÀNH CÔNG TẠI THƯ MỤC:")
    print(f"👉 {OUTPUT_DIR}")

if __name__ == "__main__":
    asyncio.run(generate_all_assignments())

