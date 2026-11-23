# -*- coding: utf-8 -*-
import docx
import re
import os

base_dir = r"c:\Users\X1\Desktop\VB2\kì 1\luyện âm"

def parse_and_clean(idx):
    fn = os.path.join(base_dir, f"VB2_LACB_Audio {idx}.docx")
    if not os.path.exists(fn):
        return [], [], []
    doc = docx.Document(fn)
    spk1_lines = []
    spk2_lines = []
    full_dialogue = []
    
    for p in doc.paragraphs:
        txt = p.text.strip()
        if not txt or (txt.startswith('/') and txt.endswith('/')):
            continue
        m = re.match(r'^(Speaker\s+[12](?:\s*\([^)]+\))?):\s*(.+)$', txt, re.IGNORECASE)
        if m:
            label = m.group(1)
            content = m.group(2).strip()
            
            clean_txt = content
            contractions = {
                r"\bdon't\b": "do not", r"\bdid't\b": "did not", r"\bdidn't\b": "did not",
                r"\bcan't\b": "can not", r"\bwon't\b": "will not", r"\bit's\b": "it is",
                r"\bthat's\b": "that is", r"\bthere's\b": "there is", r"\bwhat's\b": "what is",
                r"\blet's\b": "let us", r"\bi'm\b": "I am", r"\byou're\b": "you are",
                r"\bwe're\b": "we are", r"\bthey're\b": "they are", r"\bi've\b": "I have",
                r"\bi'll\b": "I will", r"\byou'll\b": "you will"
            }
            for pat, rep in contractions.items():
                clean_txt = re.sub(pat, rep, clean_txt, flags=re.IGNORECASE)
            clean_txt = re.sub(r',\s*', ', ... ', clean_txt)
            clean_txt = re.sub(r'\b(and|but|or|because|so)\b', r'... \1', clean_txt, flags=re.IGNORECASE)
            clean_txt = re.sub(r'\?\s*', '? ... ', clean_txt)
            
            full_dialogue.append(f"{label}: {clean_txt}")
            if '1' in label:
                spk1_lines.append(clean_txt)
            else:
                spk2_lines.append(clean_txt)
    return spk1_lines, spk2_lines, full_dialogue

out_path = os.path.join(base_dir, "Kich_Ban_Doc_Theo_Tung_Audio.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("="*70 + "\n")
    f.write("TỔNG HỢP KỊCH BẢN 5 BÀI LUYỆN ÂM (ĐÃ TỐI ƯU HÓA NGỮ ĐIỆU HỌC VIÊN ~85%)\n")
    f.write("Dùng để copy trực tiếp vào ElevenLabs hoặc Google Colab để Clone giọng\n")
    f.write("="*70 + "\n\n")
    
    for i in range(1, 6):
        s1, s2, full = parse_and_clean(i)
        f.write(f"{'#'*25} AUDIO {i} {'#'*25}\n\n")
        f.write(f"--- [AUDIO {i} - VAI SPEAKER 1] ---\n")
        f.write("\n".join(s1) + "\n\n")
        
        f.write(f"--- [AUDIO {i} - VAI SPEAKER 2] ---\n")
        f.write("\n".join(s2) + "\n\n")
        
        f.write(f"--- [AUDIO {i} - TOÀN BỘ ĐỐI THOẠI (CẢ 2 VAI)] ---\n")
        f.write("\n".join(full) + "\n\n\n")

print("Created Kich_Ban_Doc_Theo_Tung_Audio.txt successfully!")

