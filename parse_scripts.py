# -*- coding: utf-8 -*-
import docx
import json
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
all_audios = {}

for num in range(1, 6):
    file_path = os.path.join(BASE_DIR, f"VB2_LACB_Audio {num}.docx")
    doc = docx.Document(file_path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    
    title = paras[0]
    content = paras[1:]
    
    spk1_sentences = []
    spk2_sentences = []
    
    i = 0
    while i < len(content):
        line = content[i]
        if line.startswith("Speaker 1") or "Speaker 1" in line:
            text = re.sub(r"^Speaker 1[^:]*:\s*", "", line).strip()
            ipa = ""
            vi = ""
            if i + 1 < len(content) and content[i+1].startswith("/"):
                ipa = content[i+1]
                if i + 2 < len(content) and not content[i+2].startswith("Speaker") and not content[i+2].startswith("/"):
                    vi = content[i+2]
                    i += 3
                else:
                    i += 2
            else:
                if i + 1 < len(content) and not content[i+1].startswith("Speaker") and not content[i+1].startswith("/"):
                    vi = content[i+1]
                    i += 2
                else:
                    i += 1
            spk1_sentences.append({
                "sentence_num": len(spk1_sentences) + 1,
                "speaker": 1,
                "text": text,
                "ipa": ipa,
                "vi": vi
            })
        elif line.startswith("Speaker 2") or "Speaker 2" in line:
            text = re.sub(r"^Speaker 2[^:]*:\s*", "", line).strip()
            ipa = ""
            vi = ""
            if i + 1 < len(content) and content[i+1].startswith("/"):
                ipa = content[i+1]
                if i + 2 < len(content) and not content[i+2].startswith("Speaker") and not content[i+2].startswith("/"):
                    vi = content[i+2]
                    i += 3
                else:
                    i += 2
            else:
                if i + 1 < len(content) and not content[i+1].startswith("Speaker") and not content[i+1].startswith("/"):
                    vi = content[i+1]
                    i += 2
                else:
                    i += 1
            spk2_sentences.append({
                "sentence_num": len(spk2_sentences) + 1,
                "speaker": 2,
                "text": text,
                "ipa": ipa,
                "vi": vi
            })
        else:
            i += 1

    all_audios[num] = {
        "audio_num": num,
        "title": title,
        "speaker_1": spk1_sentences,
        "speaker_2": spk2_sentences
    }

out_json = os.path.join(BASE_DIR, "audio_scripts_data.json")
with open(out_json, "w", encoding="utf-8") as f:
    json.dump(all_audios, f, ensure_ascii=False, indent=2)

print("Parsed successfully!")
for num, d in all_audios.items():
    print(f"Audio {num}: Speaker 1 has {len(d['speaker_1'])} sentences, Speaker 2 has {len(d['speaker_2'])} sentences.")

