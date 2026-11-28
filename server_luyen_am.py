# -*- coding: utf-8 -*-
"""
server_luyen_am.py - Dedicated Standalone Server for Bit1 English Voice Studio
Runs on Port 5180 (No conflicts with port 5173 or other projects)
Includes Sentence-by-Sentence Recording Merge API, Script Database & AI Evaluation (Beeknoee Cloud + Local Fallback)
"""

import os
import sys
import json
import asyncio
import hashlib
import urllib.parse
import base64
import tempfile
import subprocess
import shutil
from http.server import HTTPServer, SimpleHTTPRequestHandler
import edge_tts
import evaluator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "BAI_NOP_HOAN_CHINH")
SCRIPTS_FILE = os.path.join(BASE_DIR, "audio_scripts_data.json")
os.makedirs(AUDIO_DIR, exist_ok=True)
PORT = 5180

def get_hash(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()[:10]

async def synth_voice(text, voice="en-US-BrianMultilingualNeural", rate="-3%"):
    clean_text = text.replace("...", ",").strip()
    h = get_hash(f"{clean_text}_{voice}_{rate}")
    out_name = f"gen_{h}.mp3"
    out_path = os.path.join(AUDIO_DIR, out_name)
    if not os.path.exists(out_path) or os.path.getsize(out_path) < 100:
        comm = edge_tts.Communicate(clean_text, voice=voice, rate=rate)
        await comm.save(out_path)
    return out_name

def merge_audio_chunks(sentences, audio_num, speaker_id, silence_ms=350, clean_noise=True, trim_silence=True, normalize=True):
    """
    Concatenate recorded base64 audio chunks (and/or fallback TTS) using FFmpeg with AI smart audio processing:
    - Smart Voice Activity Detection (VAD) & dead air / silence trimming at start and end
    - Speech noise reduction (highpass 80Hz + afftdn FFT room denoiser)
    - Dynamic speech volume leveling (dynaudnorm)
    - Smooth edge micro-fades (eliminating clicks/pops)
    - Calibrated acoustic gap insertion between sentences
    - Broadcast-grade mastering with EBU R128 Loudness Normalization (-16 LUFS)
    """
    temp_dir = tempfile.mkdtemp(prefix=f"merge_{audio_num}_{speaker_id}_")
    try:
        silence_sec = max(0.1, silence_ms / 1000.0)
        silence_wav = os.path.join(temp_dir, "silence.wav")
        # Generate silence
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi",
            "-i", "anullsrc=r=44100:cl=stereo",
            "-t", str(silence_sec),
            silence_wav
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Build filter chain for cleaning and trimming each recorded chunk
        chunk_filters = []
        if clean_noise:
            chunk_filters.extend(["highpass=f=80", "lowpass=f=12000", "afftdn=nf=-25"])
        if trim_silence:
            # Smart silence trim: trims dead air at start (>80ms below -38dB) and end (>150ms below -38dB)
            chunk_filters.append("silenceremove=start_periods=1:start_duration=0.08:start_threshold=-38dB:detection=rms:stop_periods=1:stop_duration=0.15:stop_threshold=-38dB")
        if normalize:
            # Speech leveling
            chunk_filters.append("dynaudnorm=f=150:g=15:m=10.0:r=0.9:b=1")
        # Micro fade-in to prevent click/pop at boundary
        chunk_filters.append("afade=t=in:ss=0:d=0.015")
        
        filter_str = ",".join(chunk_filters) if chunk_filters else "anull"

        valid_chunks = []
        for item in sentences:
            num = item.get("num", 1)
            b64_data = item.get("audioBase64", "")
            use_fallback = item.get("useFallbackTts", False)
            text = item.get("text", "")

            chunk_wav = os.path.join(temp_dir, f"chunk_{num}.wav")

            if b64_data and len(b64_data) > 100:
                # User recorded audio
                if "," in b64_data:
                    b64_data = b64_data.split(",", 1)[1]
                raw_bytes = base64.b64decode(b64_data)
                raw_path = os.path.join(temp_dir, f"raw_{num}.bin")
                with open(raw_path, "wb") as f:
                    f.write(raw_bytes)

                # Process with Smart AI Filters (Noise gate + Silence trim + Normalization)
                res = subprocess.run([
                    "ffmpeg", "-y", "-i", raw_path,
                    "-af", filter_str,
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
                    chunk_wav
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                # Fallback to simple conversion if silence removal trimmed completely (too aggressive)
                if res.returncode != 0 or not os.path.exists(chunk_wav) or os.path.getsize(chunk_wav) < 1000:
                    subprocess.run([
                        "ffmpeg", "-y", "-i", raw_path,
                        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
                        chunk_wav
                    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                if os.path.exists(chunk_wav) and os.path.getsize(chunk_wav) > 1000:
                    valid_chunks.append(chunk_wav)
                    continue

            # Fallback to TTS if user didn't record or chunk was invalid
            if use_fallback and text:
                tts_mp3 = os.path.join(temp_dir, f"tts_{num}.mp3")
                sent_spk = s.get("speaker", speaker_id)
                fallback_voice = "en-US-AvaMultilingualNeural" if str(sent_spk) == "2" else "en-US-BrianMultilingualNeural"
                asyncio.run(edge_tts.Communicate(text, voice=fallback_voice, rate="-4%").save(tts_mp3))
                subprocess.run([
                    "ffmpeg", "-y", "-i", tts_mp3,
                    "-af", "dynaudnorm=f=150:g=15:m=10.0:r=0.9:b=1,afade=t=in:ss=0:d=0.015",
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
                    chunk_wav
                ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if os.path.exists(chunk_wav) and os.path.getsize(chunk_wav) > 1000:
                    valid_chunks.append(chunk_wav)

        if not valid_chunks:
            raise ValueError("Không có đoạn ghi âm hợp lệ nào để ghép.")

        # Create concat list file
        concat_txt = os.path.join(temp_dir, "concat.txt")
        with open(concat_txt, "w", encoding="utf-8") as f:
            for idx, c_path in enumerate(valid_chunks):
                # Escape backslashes for FFmpeg
                norm_c = c_path.replace("\\", "/")
                f.write(f"file '{norm_c}'\n")
                if idx < len(valid_chunks) - 1:
                    norm_s = silence_wav.replace("\\", "/")
                    f.write(f"file '{norm_s}'\n")

        # Output MP3 filename
        role_suffix = "Full" if str(speaker_id) == "all" else f"Speaker_{speaker_id}"
        out_filename = f"Bai_Ghi_Am_That_Audio_{audio_num}_{role_suffix}.mp3"
        out_path = os.path.join(AUDIO_DIR, out_filename)

        # Concatenate and Master with EBU R128 loudness normalization
        master_res = subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", concat_txt,
            "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
            "-c:a", "libmp3lame", "-b:a", "192k",
            out_path
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if master_res.returncode != 0 or not os.path.exists(out_path) or os.path.getsize(out_path) < 1000:
            # Fallback to standard concat without loudnorm if needed
            subprocess.run([
                "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                "-i", concat_txt,
                "-c:a", "libmp3lame", "-b:a", "192k",
                out_path
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        return out_filename, len(valid_chunks)

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

class VoiceStudioHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path in ["/", "/index.html"]:
            self.path = "/STUDIO_LUYEN_AM.html"
            return super().do_GET()

        if path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            data = {
                "status": "online",
                "port": PORT,
                "project": "Bit1 AI English Voice Studio",
                "features": [
                    "sentence_recorder_splicer",
                    "instant_ai_pronunciation_evaluation",
                    "beeknoee_cloud_whisper",
                    "local_phonetic_fallback",
                    "natural_conversational_tts",
                    "prompt_custom_voice",
                    "stt_practice"
                ]
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))
            return

        if path == "/api/scripts":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            if os.path.exists(SCRIPTS_FILE):
                with open(SCRIPTS_FILE, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(b"{}")
            return

        if path == "/api/voice/beeknoee-info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            info = {
                "provider": "Beeknoee AI Platform",
                "baseUrl": evaluator.BEE_BASE_URL,
                "sttModel": evaluator.BEE_STT_MODEL,
                "evalModel": evaluator.BEE_EVAL_MODEL,
                "billingUrl": "https://platform.beeknoee.com/billing",
                "status": "integrated_with_auto_fallback"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))
            return

        return super().do_GET()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len).decode("utf-8")
        try:
            req_data = json.loads(body) if body else {}
        except Exception:
            req_data = {}

        if path in ["/api/voice/clone", "/api/voice/tts"]:
            text = req_data.get("text", "").strip()
            voice = req_data.get("voice", "en-US-BrianMultilingualNeural")
            level = str(req_data.get("level", "82"))
            prompt = req_data.get("prompt", "").lower()

            if not text:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Văn bản không được để trống"}).encode("utf-8"))
                return

            rate = "-4%"
            speed_val = req_data.get("speed")
            if speed_val is not None:
                try:
                    s = float(speed_val)
                    if s <= 0.8:
                        rate = "-25%"
                    elif s >= 1.2:
                        rate = "+25%"
                    else:
                        rate = "-2%"
                except Exception:
                    pass
            elif "chậm" in prompt or level == "75":
                rate = "-15%"
            elif "nhanh" in prompt or level == "88":
                rate = "+15%"

            try:
                out_name = asyncio.run(synth_voice(text, voice, rate=rate))
                audio_url = f"/BAI_NOP_HOAN_CHINH/{out_name}"
                res = {
                    "success": True,
                    "audioUrl": audio_url,
                    "voice": voice,
                    "rate": rate,
                    "level": level
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(res).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        if path == "/api/voice/merge-sentences":
            audio_num = req_data.get("audioNum", 1)
            speaker_id = req_data.get("speaker", 1)
            silence_ms = int(req_data.get("silenceMs", 350))
            clean_noise = bool(req_data.get("cleanNoise", True))
            trim_silence = bool(req_data.get("trimSilence", True))
            normalize = bool(req_data.get("normalize", True))
            sentences = req_data.get("sentences", [])

            if not sentences:
                self.send_response(400)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Danh sách câu rỗng"}).encode("utf-8"))
                return

            try:
                out_filename, merged_count = merge_audio_chunks(
                    sentences, audio_num, speaker_id, silence_ms,
                    clean_noise=clean_noise, trim_silence=trim_silence, normalize=normalize
                )
                res = {
                    "success": True,
                    "audioUrl": f"/BAI_NOP_HOAN_CHINH/{out_filename}",
                    "fileName": out_filename,
                    "mergedCount": merged_count
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps(res).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Lỗi ghép âm thanh: {str(e)}"}).encode("utf-8"))
            return

        if path in ["/api/voice/evaluate", "/api/voice/evaluate-sentence"]:
            target_text = req_data.get("targetText", "").strip()
            spoken_text = req_data.get("spokenText", "").strip()
            audio_num = int(req_data.get("audioNum", 1))

            if not target_text:
                self.send_response(400)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Thiếu câu văn bản mục tiêu"}).encode("utf-8"))
                return

            # Pure local phonetic evaluation - ZERO API key required, 100% offline & fast!
            final_res = evaluator.local_phonetic_evaluate(target_text, spoken_text, audio_num)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(final_res, ensure_ascii=False).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

def run():
    server = HTTPServer(("0.0.0.0", PORT), VoiceStudioHandler)
    print(f"🚀 Bit1 English Voice Studio running at: http://localhost:{PORT}")
    print(f"   Dedicated port {PORT} - 100% separate from thaogiang (5173)")
    server.serve_forever()

if __name__ == "__main__":
    run()
