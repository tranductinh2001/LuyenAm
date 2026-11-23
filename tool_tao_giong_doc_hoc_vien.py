# -*- coding: utf-8 -*-
"""
TOOL GIẢ LẬP GIỌNG ĐỌC CỦA CHÍNH BẠN (VOICE CLONING TỪ VIDEO/AUDIO MẪU)
Đọc bài tập tiếng Anh ~85% chuẩn, ngữ điệu học viên Việt Nam tự nhiên
"""

import os
import sys
import re
import json
import tempfile
import subprocess
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import docx
import requests
from gtts import gTTS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def parse_docx_audio(file_path):
    """Trích xuất danh sách câu thoại theo Speaker từ file Word kịch bản"""
    dialogue = []
    if not os.path.exists(file_path):
        return dialogue
    doc = docx.Document(file_path)
    for p in doc.paragraphs:
        txt = p.text.strip()
        if not txt:
            continue
        if txt.startswith('/') and txt.endswith('/'):
            continue
        if any(txt.startswith(prefix) for prefix in ['Này ', 'Tớ ', 'Ôi không', 'Được rồi', 'Chờ đã', 'Tuyệt ', 'Rõ rồi', 'Ý kiến', 'Chà', 'Viết ', 'Bình tĩnh', 'Xong rồi', 'Mới ơn', 'Không khí', 'Ghi nhớ', 'Đừng lo', 'Cậu đang']):
            continue
        
        m = re.match(r'^(Speaker\s+[12](?:\s*\([^)]+\))?):\s*(.+)$', txt, re.IGNORECASE)
        if m:
            spk_label = m.group(1)
            content = m.group(2).strip()
            current_spk = 'Speaker 1' if '1' in spk_label else 'Speaker 2'
            dialogue.append({'speaker': current_spk, 'label': spk_label, 'text': content})
    return dialogue

def simulate_learner_text(text):
    """
    Biến đổi văn bản tiếng Anh thành phong cách đọc của học viên Việt Nam:
    - Tách từ viết tắt để đọc từng từ (không lướt âm như Tây).
    - Thêm ngắt nhịp nhẹ để nhịp điệu phẳng (syllable-timed), đạt khoảng 85% chuẩn.
    """
    t = text
    contractions = {
        r"\bdon't\b": "do not",
        r"\bdid't\b": "did not",
        r"\bdidn't\b": "did not",
        r"\bcan't\b": "can not",
        r"\bwon't\b": "will not",
        r"\bit's\b": "it is",
        r"\bthat's\b": "that is",
        r"\bthere's\b": "there is",
        r"\bwhat's\b": "what is",
        r"\blet's\b": "let us",
        r"\bi'm\b": "I am",
        r"\byou're\b": "you are",
        r"\bwe're\b": "we are",
        r"\bthey're\b": "they are",
        r"\bi've\b": "I have",
        r"\bi'll\b": "I will",
        r"\byou'll\b": "you will",
    }
    for pat, rep in contractions.items():
        t = re.sub(pat, rep, t, flags=re.IGNORECASE)

    t = re.sub(r',\s*', ', ... ', t)
    t = re.sub(r'\b(and|but|or|because|so)\b', r'... \1', t, flags=re.IGNORECASE)
    t = re.sub(r'\?\s*', '? ... ', t)
    return t.strip()

def extract_audio_from_video(video_path, output_wav):
    """Trích xuất âm thanh từ video MP4/MKV và chuẩn hóa 24kHz mono WAV sạch tiếng"""
    cmd = [
        "ffmpeg", "-y", "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "24000",
        "-ac", "1",
        output_wav
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def get_audio_duration(file_path):
    """Lấy thời lượng âm thanh tính bằng giây"""
    try:
        out = subprocess.check_output([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", file_path
        ]).decode().strip()
        return float(out)
    except:
        return 0.0

def process_learner_audio_with_ffmpeg(input_mp3, output_mp3, speed=0.90, mic_simulate=True):
    speed_factor = max(0.7, min(1.2, float(speed)))
    if mic_simulate:
        audio_filter = f"atempo={speed_factor},highpass=f=100,lowpass=f=7000,volume=1.05"
    else:
        audio_filter = f"atempo={speed_factor}"

    cmd = [
        "ffmpeg", "-y", "-i", input_mp3,
        "-filter:a", audio_filter,
        "-q:a", "3",
        output_mp3
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)

def clone_and_generate_elevenlabs(api_key, voice_sample_path, text, output_mp3, stability=0.88):
    """
    Sử dụng API ElevenLabs để:
    1. Upload file mẫu giọng của bạn để tạo Cloned Voice tức thì.
    2. Tổng hợp bài đọc bằng chính giọng bạn với tham số Stability cao (ngữ điệu đơ kiểu học viên).
    """
    headers = {"xi-api-key": api_key.strip()}

    # 1. Tạo Instant Voice Clone
    add_voice_url = "https://api.elevenlabs.io/v1/voices/add"
    with open(voice_sample_path, "rb") as f:
        files = {"files": (os.path.basename(voice_sample_path), f, "audio/wav")}
        data = {
            "name": f"HocVien_Voice_{os.path.splitext(os.path.basename(voice_sample_path))[0]}",
            "description": "Cloned voice for student pronunciation assignment"
        }
        res = requests.post(add_voice_url, headers=headers, data=data, files=files, timeout=60)

    if res.status_code != 200:
        raise Exception(f"Lỗi tạo giọng ElevenLabs: {res.text}")

    voice_id = res.json().get("voice_id")
    if not voice_id:
        raise Exception("Không nhận được voice_id từ ElevenLabs.")

    # 2. Sinh giọng đọc
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    tts_data = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": float(stability),       # Cao (~0.88 - 0.90): giọng phẳng, đơ tự nhiên, không luyến láy
            "similarity_boost": 0.80,            # Rất giống giọng mẫu
            "style": 0.0,                        # Tắt hoàn toàn phong cách biểu cảm Tây
            "use_speaker_boost": True
        }
    }
    tts_res = requests.post(tts_url, headers=headers, json=tts_data, timeout=120)
    if tts_res.status_code != 200:
        raise Exception(f"Lỗi tạo audio: {tts_res.text}")

    with open(output_mp3, "wb") as f:
        f.write(tts_res.content)

class MainVoiceClonerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Công Cụ Fake Giọng Đọc Chính Bạn (~85% Chuẩn) - Luyện Âm VB2")
        self.root.geometry("860x730")
        self.root.minsize(820, 680)

        self.voice_sample_file = None
        self.extracted_wav_file = None
        self.current_generated_file = None
        self.current_dialogue = []

        self.setup_ui()
        self.load_audio_list()

    def setup_ui(self):
        # Tiêu đề
        title_frame = tk.Frame(self.root, bg="#1a365d", pady=10)
        title_frame.pack(fill=tk.X)
        lbl_title = tk.Label(
            title_frame,
            text="HỆ THỐNG CLONE GIỌNG CHÍNH BẠN ĐỌC BÀI TẬP TIẾNG ANH",
            font=("Segoe UI", 13, "bold"),
            fg="white", bg="#1a365d"
        )
        lbl_title.pack()
        lbl_sub = tk.Label(
            title_frame,
            text="Đầu vào: Video/Audio của bạn | Đầu ra: Đọc đúng giọng bạn với ngữ điệu học viên (~85% chuẩn)",
            font=("Segoe UI", 9, "italic"),
            fg="#90cdf4", bg="#1a365d"
        )
        lbl_sub.pack()

        # Phần 1: Chọn video / voice mẫu của bạn
        frame_sample = ttk.LabelFrame(self.root, text=" BƯỚC 1: Chọn Video hoặc Audio nói giọng của bạn ", padding=10)
        frame_sample.pack(fill=tk.X, padx=15, pady=6)

        row_s1 = ttk.Frame(frame_sample)
        row_s1.pack(fill=tk.X, pady=3)
        self.btn_browse = ttk.Button(row_s1, text="📁 Chọn Video / Audio mẫu...", command=self.browse_sample_file)
        self.btn_browse.pack(side=tk.LEFT, padx=5)
        self.lbl_sample_path = ttk.Label(row_s1, text="Chưa chọn file mẫu nào (Hỗ trợ .mp4, .m4a, .wav, .mp3)", foreground="#718096")
        self.lbl_sample_path.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        row_s2 = ttk.Frame(frame_sample)
        row_s2.pack(fill=tk.X, pady=3)
        self.lbl_sample_info = ttk.Label(
            row_s2,
            text="💡 Khuyên dùng: Video/Audio dài từ 1 đến 3 phút (tối thiểu 30s), nói rõ tiếng, không có nhạc nền.",
            font=("Segoe UI", 8, "italic"),
            foreground="#2b6cb0"
        )
        self.lbl_sample_info.pack(side=tk.LEFT, padx=5)

        # Phần 2: Chọn bài tập cần đọc
        frame_exercise = ttk.LabelFrame(self.root, text=" BƯỚC 2: Chọn đoạn kịch bản cần đọc ", padding=10)
        frame_exercise.pack(fill=tk.X, padx=15, pady=6)

        row_e1 = ttk.Frame(frame_exercise)
        row_e1.pack(fill=tk.X, pady=3)
        ttk.Label(row_e1, text="Chọn bài môn Luyện âm:").pack(side=tk.LEFT, padx=5)
        self.cbo_audio = ttk.Combobox(row_e1, width=35, state="readonly")
        self.cbo_audio.pack(side=tk.LEFT, padx=5)
        self.cbo_audio.bind("<<ComboboxSelected>>", self.on_audio_selected)

        ttk.Label(row_e1, text="Vai đọc:").pack(side=tk.LEFT, padx=15)
        self.var_speaker = tk.StringVar(value="Speaker 1")
        ttk.Radiobutton(row_e1, text="Speaker 1", variable=self.var_speaker, value="Speaker 1", command=self.update_editor_text).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(row_e1, text="Speaker 2", variable=self.var_speaker, value="Speaker 2", command=self.update_editor_text).pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(row_e1, text="Cả 2 người", variable=self.var_speaker, value="Both", command=self.update_editor_text).pack(side=tk.LEFT, padx=5)

        # Phần 3: Chọn công nghệ Clone & Điều chỉnh ngữ điệu
        frame_mode = ttk.LabelFrame(self.root, text=" BƯỚC 3: Chọn phương thức Clone & Chỉnh ngữ điệu ~85% ", padding=10)
        frame_mode.pack(fill=tk.X, padx=15, pady=6)

        self.tab_ctrl = ttk.Notebook(frame_mode)
        self.tab_ctrl.pack(fill=tk.X, expand=True)

        # Tab A: ElevenLabs API (Chất lượng cao nhất, giọng thật 95%)
        tab_eleven = ttk.Frame(self.tab_ctrl, padding=8)
        self.tab_ctrl.add(tab_eleven, text=" ⭐ Cách 1: Clone Giọng Mẫu (ElevenLabs - Giống giọng 95%) ")
        
        row_el1 = ttk.Frame(tab_eleven)
        row_el1.pack(fill=tk.X, pady=2)
        ttk.Label(row_el1, text="ElevenLabs API Key:").pack(side=tk.LEFT, padx=5)
        self.txt_api_key = ttk.Entry(row_el1, width=42, show="*")
        self.txt_api_key.pack(side=tk.LEFT, padx=5)
        ttk.Label(row_el1, text="(Nhập API Key cá nhân để clone giọng tức thì)", font=("Segoe UI", 8), foreground="#718096").pack(side=tk.LEFT, padx=5)

        row_el2 = ttk.Frame(tab_eleven)
        row_el2.pack(fill=tk.X, pady=4)
        ttk.Label(row_el2, text="Độ phẳng ngữ điệu (Stability):").pack(side=tk.LEFT, padx=5)
        self.scale_stab = ttk.Scale(row_el2, from_=0.5, to=0.98, value=0.88)
        self.scale_stab.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Label(row_el2, text="0.88 (Ngữ điệu phẳng học viên, tránh bị luyến láy như Tây)").pack(side=tk.LEFT, padx=5)

        # Tab B: Chế độ Miễn Phí qua Google Colab (Mô hình F5-TTS)
        tab_colab = ttk.Frame(self.tab_ctrl, padding=8)
        self.tab_ctrl.add(tab_colab, text=" 🚀 Cách 2: Miễn Phí 100% bằng Google Colab (F5-TTS) ")
        lbl_colab_info = ttk.Label(
            tab_colab,
            text="Đã chuẩn bị sẵn file sổ tay Google Colab (`.ipynb`) dùng GPU T4 miễn phí của Google.\nBạn chỉ việc tải file video mẫu của bạn lên Colab rồi bấm chạy để lấy file nộp bài!",
            font=("Segoe UI", 9),
            foreground="#2d3748"
        )
        lbl_colab_info.pack(side=tk.LEFT, padx=5)
        btn_open_colab_file = ttk.Button(tab_colab, text="Mở thư mục chứa file Colab", command=self.open_colab_folder)
        btn_open_colab_file.pack(side=tk.RIGHT, padx=5)

        # Tab C: Giả lập nhanh trên máy (Dùng ngay, không cần API)
        tab_local = ttk.Frame(self.tab_ctrl, padding=8)
        self.tab_ctrl.add(tab_local, text=" ⚡ Cách 3: Giả Lập Nhanh Trực Tiếp Trên Máy ")
        ttk.Label(tab_local, text="Tạo âm thanh học viên nhanh bằng engine máy tính + bộ lọc micro tự nhiên.").pack(side=tk.LEFT, padx=5)

        # Phần 4: Khung văn bản đọc
        frame_text = ttk.LabelFrame(self.root, text=" BƯỚC 4: Văn bản kịch bản sẽ đọc (Đã tự động ngắt nhịp học viên) ", padding=8)
        frame_text.pack(fill=tk.BOTH, expand=True, padx=15, pady=6)

        self.txt_content = tk.Text(frame_text, wrap=tk.WORD, height=6, font=("Consolas", 10))
        self.txt_content.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
        scrollbar = ttk.Scrollbar(frame_text, command=self.txt_content.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.txt_content.config(yscrollcommand=scrollbar.set)

        # Phần Nút thực hiện
        frame_action = ttk.Frame(self.root, padding=8)
        frame_action.pack(fill=tk.X, padx=15, pady=4)

        self.btn_run = tk.Button(
            frame_action,
            text="TẠO BÀI NỘP BẰNG GIỌNG BẠN (.MP3)",
            font=("Segoe UI", 11, "bold"),
            bg="#2b6cb0", fg="white",
            padx=15, pady=8,
            command=self.execute_generation
        )
        self.btn_run.pack(side=tk.RIGHT, padx=5)

        self.btn_play = tk.Button(
            frame_action,
            text="▶ Nghe thử file vừa tạo",
            font=("Segoe UI", 10),
            bg="#4a5568", fg="white",
            padx=10, pady=8,
            state=tk.DISABLED,
            command=self.play_audio_clicked
        )
        self.btn_play.pack(side=tk.RIGHT, padx=5)

        self.lbl_status = ttk.Label(frame_action, text="Sẵn sàng.", font=("Segoe UI", 9, "italic"))
        self.lbl_status.pack(side=tk.LEFT, padx=5)

    def browse_sample_file(self):
        f = filedialog.askopenfilename(
            title="Chọn Video hoặc Audio giọng mẫu của bạn",
            filetypes=[
                ("Video & Audio Files", "*.mp4;*.m4a;*.wav;*.mp3;*.mov;*.mkv"),
                ("All Files", "*.*")
            ]
        )
        if f:
            self.voice_sample_file = f
            self.lbl_sample_path.config(text=f, foreground="#2d3748")
            # Trích xuất và kiểm tra thời lượng
            threading.Thread(target=self._process_sample_input, args=(f,), daemon=True).start()

    def _process_sample_input(self, f):
        self.lbl_status.config(text="Đang phân tích và trích xuất giọng nói từ file mẫu...")
        ext = os.path.splitext(f)[1].lower()
        wav_target = os.path.join(BASE_DIR, "Giong_Mau_Chuan_Hoa.wav")
        try:
            if ext in ['.mp4', '.mov', '.mkv', '.m4a', '.mp3']:
                extract_audio_from_video(f, wav_target)
            else:
                wav_target = f
            dur = get_audio_duration(wav_target)
            self.extracted_wav_file = wav_target
            self.lbl_status.config(text=f"Đã nạp file mẫu thành công! (Thời lượng: {dur:.1f} giây)")
        except Exception as e:
            self.lbl_status.config(text=f"Lỗi đọc file: {e}")

    def load_audio_list(self):
        items = []
        for i in range(1, 6):
            fn = f"VB2_LACB_Audio {i}.docx"
            if os.path.exists(os.path.join(BASE_DIR, fn)):
                items.append(f"Audio {i}: {fn}")
        items.append("Nhập văn bản tự do")
        self.cbo_audio['values'] = items
        if items:
            self.cbo_audio.current(0)
            self.on_audio_selected(None)

    def on_audio_selected(self, event):
        sel = self.cbo_audio.get()
        if "Audio " in sel:
            idx = sel.split(":")[0].replace("Audio ", "").strip()
            fn = os.path.join(BASE_DIR, f"VB2_LACB_Audio {idx}.docx")
            self.current_dialogue = parse_docx_audio(fn)
        else:
            self.current_dialogue = []
        self.update_editor_text()

    def update_editor_text(self):
        spk_choice = self.var_speaker.get()
        if not self.current_dialogue:
            return

        lines = []
        for item in self.current_dialogue:
            if spk_choice == "Both" or item['speaker'] == spk_choice:
                txt = simulate_learner_text(item['text'])
                if spk_choice == "Both":
                    lines.append(f"{item['speaker']}: {txt}")
                else:
                    lines.append(txt)

        self.txt_content.delete("1.0", tk.END)
        self.txt_content.insert(tk.END, "\n\n".join(lines))

    def open_colab_folder(self):
        try:
            os.startfile(BASE_DIR)
        except Exception as e:
            messagebox.showinfo("Thư mục", f"Đường dẫn: {BASE_DIR}")

    def execute_generation(self):
        text = self.txt_content.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập nội dung cần đọc!")
            return

        active_tab_idx = self.tab_ctrl.index(self.tab_ctrl.select())

        sel_name = self.cbo_audio.get().split(":")[0].replace(" ", "_")
        spk = self.var_speaker.get().replace(" ", "_")
        default_out = f"Bai_Nop_Giong_That_{sel_name}_{spk}.mp3"

        out_path = filedialog.asksaveasfilename(
            initialdir=BASE_DIR,
            initialfile=default_out,
            defaultextension=".mp3",
            filetypes=[("MP3 Audio", "*.mp3")]
        )
        if not out_path:
            return

        self.btn_run.config(state=tk.DISABLED)

        if active_tab_idx == 0:  # ElevenLabs Voice Clone
            api_key = self.txt_api_key.get().strip()
            if not api_key:
                messagebox.showwarning("Thiếu API Key", "Vui lòng nhập ElevenLabs API Key ở mục Cách 1 để thực hiện Clone giọng!")
                self.btn_run.config(state=tk.NORMAL)
                return
            if not self.extracted_wav_file or not os.path.exists(self.extracted_wav_file):
                messagebox.showwarning("Chưa có file mẫu", "Vui lòng chọn file Video hoặc Audio nói giọng của bạn ở Bước 1 trước!")
                self.btn_run.config(state=tk.NORMAL)
                return

            self.lbl_status.config(text="Đang gửi mẫu giọng lên AI để clone và đọc bài...")
            stab = float(self.scale_stab.get())
            threading.Thread(target=self._run_elevenlabs, args=(api_key, self.extracted_wav_file, text, out_path, stab), daemon=True).start()

        elif active_tab_idx == 1:  # Google Colab
            self.lbl_status.config(text="Đang xuất kịch bản và dữ liệu cho Google Colab...")
            # Lưu text ra file để sẵn sàng tải lên Colab
            colab_txt = os.path.join(BASE_DIR, "kich_ban_doc_colab.txt")
            with open(colab_txt, "w", encoding="utf-8") as f:
                f.write(text)
            self.btn_run.config(state=tk.NORMAL)
            messagebox.showinfo("Google Colab", f"Đã lưu văn bản vào: {colab_txt}\n\nBạn hãy mở file 'Clone_Giong_Colab.ipynb' trong thư mục để chạy GPU miễn phí!")

        else:  # Giả lập nhanh Offline
            self.lbl_status.config(text="Đang tạo audio học viên offline...")
            threading.Thread(target=self._run_local_generation, args=(text, out_path), daemon=True).start()

    def _run_elevenlabs(self, api_key, sample_wav, text, out_path, stab):
        try:
            # Làm sạch text khỏi nhãn Speaker
            clean_lines = [re.sub(r'^Speaker\s+[12]:\s*', '', l.strip()) for l in text.split("\n") if l.strip()]
            full_text = " ... ".join(clean_lines)

            clone_and_generate_elevenlabs(api_key, sample_wav, full_text, out_path, stability=stab)
            self.current_generated_file = out_path
            self.root.after(0, self._on_success, out_path, "Clone thành công bằng giọng thật của bạn qua ElevenLabs!")
        except Exception as e:
            self.root.after(0, self._on_error, str(e))

    def _run_local_generation(self, raw_text, out_path):
        try:
            clean_lines = [re.sub(r'^Speaker\s+[12]:\s*', '', l.strip()) for l in raw_text.split("\n") if l.strip()]
            full_text = " ... ".join(clean_lines)

            temp_mp3 = os.path.join(tempfile.gettempdir(), "temp_local_voice.mp3")
            tts = gTTS(text=full_text, lang='en', tld='com.vn', slow=False)
            tts.save(temp_mp3)

            process_learner_audio_with_ffmpeg(temp_mp3, out_path, speed=0.90, mic_simulate=True)
            if os.path.exists(temp_mp3):
                os.remove(temp_mp3)

            self.current_generated_file = out_path
            self.root.after(0, self._on_success, out_path, "Đã tạo file audio học viên thành công!")
        except Exception as e:
            self.root.after(0, self._on_error, str(e))

    def _on_success(self, out_path, msg):
        self.btn_run.config(state=tk.NORMAL)
        self.btn_play.config(state=tk.NORMAL)
        self.lbl_status.config(text=f"Hoàn thành: {os.path.basename(out_path)}")
        messagebox.showinfo("Thành công", f"{msg}\n\nĐã lưu: {out_path}")

    def _on_error(self, err_msg):
        self.btn_run.config(state=tk.NORMAL)
        self.lbl_status.config(text="Có lỗi xảy ra.")
        messagebox.showerror("Lỗi", f"Chi tiết lỗi:\n{err_msg}")

    def play_audio_clicked(self):
        if self.current_generated_file and os.path.exists(self.current_generated_file):
            try:
                os.startfile(self.current_generated_file)
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể mở file audio:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainVoiceClonerApp(root)
    root.mainloop()
