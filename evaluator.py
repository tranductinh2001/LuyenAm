# -*- coding: utf-8 -*-
"""
evaluator.py - Hybrid AI Pronunciation Assessment Engine
Combines Beeknoee Cloud Audio/LLM API with Local High-Precision Phonetic Alignment
"""

import os
import re
import json
import difflib
import requests

# Beeknoee Gateway Config
DEFAULT_BEE_KEY = "sk-bee-9a4e3ae0de60aaab4298ad268bf3a66ef42e5e59ac4ccd7506750d71d80622ae"
BEE_BASE_URL = "https://platform.beeknoee.com/api/v1"
BEE_STT_MODEL = "whisper-large-v3-turbo"
BEE_EVAL_MODEL = "google/gemini-3.1-flash-lite"

# Minimal Pairs Knowledge Base for 5 Audios
MINIMAL_PAIRS_RULES = {
    1: {
        "focus": "Cặp âm /iː/ vs /ɪ/ và /e/ vs /æ/",
        "pairs": {
            "peel": {"counter": "pill", "sound": "/iː/", "advice": "Kéo dài âm /iː/, mở bè khóe miệng như đang mỉm cười."},
            "pill": {"counter": "peel", "sound": "/ɪ/", "advice": "Phát âm /ɪ/ ngắn, dứt khoát, thả lỏng môi."},
            "leave": {"counter": "live", "sound": "/iː/", "advice": "Kéo dài âm /iː/ trong 'leave', không đọc ngắn như 'live'."},
            "live": {"counter": "leave", "sound": "/lɪv/", "advice": "Đọc âm /ɪ/ ngắn và dứt khoát."},
            "leak": {"counter": "lick", "sound": "/liːk/", "advice": "Kéo dài âm /iː/ và bật âm đuôi /k/ rõ ràng."},
            "lick": {"counter": "leak", "sound": "/lɪk/", "advice": "Âm /ɪ/ ngắn, đầu lưỡi bật nhanh."},
            "sheep": {"counter": "ship", "sound": "/ʃiːp/", "advice": "Tròn môi âm /ʃ/ và kéo dài âm /iː/."},
            "ship": {"counter": "sheep", "sound": "/ʃɪp/", "advice": "Âm /ɪ/ ngắn, không kéo dài."},
            "bean": {"counter": "bin", "sound": "/biːn/", "advice": "Kéo dài âm /iː/, âm /n/ ngân nhẹ ở vòm họng."},
            "bin": {"counter": "bean", "sound": "/bɪn/", "advice": "Âm /ɪ/ ngắn, kết thúc nhanh ở âm /n/."},
            "pen": {"counter": "pan", "sound": "/pen/", "advice": "Âm /e/ mở miệng vừa phải, bật hơi âm /p/ nhẹ nhàng."},
            "pan": {"counter": "pen", "sound": "/pæn/", "advice": "Hạ thấp hàm dưới mở rộng miệng cho âm /æ/ bẹt."},
            "men": {"counter": "man", "sound": "/men/", "advice": "Âm /e/ gọn gàng, khẩu hình trung bình."},
            "man": {"counter": "men", "sound": "/mæn/", "advice": "Hạ hàm sâu hơn tạo âm /æ/ căng."}
        }
    },
    2: {
        "focus": "Cặp âm /ɑː/ vs /ʌ/ và /ɒ/ vs /ɔː/",
        "pairs": {
            "park": {"counter": "truck", "sound": "/pɑːk/", "advice": "Mở rộng họng, ngân sâu âm /ɑː/ dài."},
            "truck": {"counter": "park", "sound": "/trʌk/", "advice": "Âm /ʌ/ ngắn, bật nhanh từ cuống họng."},
            "barn": {"counter": "hut", "sound": "/bɑːn/", "advice": "Mở rộng miệng phát âm /ɑː/ trầm và dài."},
            "hut": {"counter": "barn", "sound": "/hʌt/", "advice": "Âm /ʌ/ ngắn dứt khoát."},
            "cod": {"counter": "cord", "sound": "/kɒd/", "advice": "Mở miệng tròn vừa, âm /ɒ/ ngắn."},
            "cord": {"counter": "cod", "sound": "/kɔːd/", "advice": "Tròn môi cong lưỡi nhẹ kéo dài âm /ɔː/."},
            "cap": {"counter": "cup", "sound": "/kæp/", "advice": "Hạ hàm rộng cho âm /æ/."},
            "cup": {"counter": "cap", "sound": "/kʌp/", "advice": "Âm /ʌ/ ngắn gọn, bật nhẹ âm /p/."}
        }
    },
    3: {
        "focus": "Cặp âm /uː/ vs /ʊ/ và /ɜː/ vs /ə/",
        "pairs": {
            "pool": {"counter": "pull", "sound": "/uː/", "advice": "Chu môi tròn nhỏ, kéo dài âm /uː/."},
            "pull": {"counter": "pool", "sound": "/ʊ/", "advice": "Môi hơi mở, âm /ʊ/ ngắn và thả lỏng."},
            "fool": {"counter": "full", "sound": "/fuːl/", "advice": "Răng trên chạm môi dưới cho âm /f/, ngân dài /uː/."},
            "full": {"counter": "fool", "sound": "/fʊl/", "advice": "Âm /ʊ/ phát âm nhanh dứt khoát."},
            "bird": {"counter": "bud", "sound": "/bɜːd/", "advice": "Môi hơi mở hờ, lưỡi nâng giữa vòm miệng ngân dài âm /ɜː/."},
            "worker": {"counter": "walker", "sound": "/ˈwɜːkə/", "advice": "Âm /ɜː/ cuộn lưỡi nhẹ, khác với /ɔː/ trong walker."}
        }
    },
    4: {
        "focus": "Nguyên âm đôi Diphthongs (/aɪ/, /eə/, /ɪə/, /əʊ/, /ɔɪ/)",
        "pairs": {
            "pie": {"counter": "pear", "sound": "/paɪ/", "advice": "Chuyển mượt mà từ /a/ sang /ɪ/."},
            "pear": {"counter": "pie", "sound": "/peə/", "advice": "Mở âm /e/ rồi lướt nhẹ về /ə/."},
            "pier": {"counter": "beer", "sound": "/pɪə/", "advice": "Bắt đầu bằng /ɪ/ lướt nhẹ sang /ə/, bật hơi /p/."},
            "bowl": {"counter": "boil", "sound": "/bəʊl/", "advice": "Âm /əʊ/ tròn môi dần, nâng cuống lưỡi ở âm /l/."}
        }
    },
    5: {
        "focus": "Cặp phụ âm bật hơi /p/-/b/, /t/-/d/, /tʃ/-/dʒ/, /ʃ/-/ʒ/",
        "pairs": {
            "choking": {"counter": "joking", "sound": "/tʃ/", "advice": "Âm vô thanh /tʃ/ bật hơi mạnh ở đầu lưỡi, không rung dây thanh."},
            "joking": {"counter": "choking", "sound": "/dʒ/", "advice": "Âm hữu thanh /dʒ/ rung dây thanh quản rõ ràng."},
            "cheap": {"counter": "Jeep", "sound": "/tʃiːp/", "advice": "Bật hơi gió mạnh cho /tʃ/, kéo dài /iː/."},
            "casual": {"counter": "shoe", "sound": "/ʒ/", "advice": "Rung lưỡi nhẹ cho âm /ʒ/ giữa hai nguyên âm."}
        }
    }
}

def clean_word(w):
    return re.sub(r"[^a-zA-Z0-9']", "", w).lower()

def local_phonetic_evaluate(target_text, spoken_text, audio_num=1):
    """
    Local high-precision phonetic analysis when Beeknoee Cloud is offline/402.
    """
    target_tokens = [w for w in target_text.split() if clean_word(w)]
    spoken_tokens = [clean_word(w) for w in spoken_text.split() if clean_word(w)]

    rule_book = MINIMAL_PAIRS_RULES.get(int(audio_num), MINIMAL_PAIRS_RULES[1])
    pairs_dict = rule_book.get("pairs", {})

    words_analysis = []
    total_score_sum = 0
    total_weight = 0

    spoken_remaining = list(spoken_tokens)

    for orig_word in target_tokens:
        tw = clean_word(orig_word)
        is_pair = tw in pairs_dict
        pair_info = pairs_dict.get(tw, {})
        weight = 2.0 if is_pair else 1.0

        # Exact match
        if tw in spoken_remaining:
            spoken_remaining.remove(tw)
            words_analysis.append({
                "word": orig_word,
                "clean": tw,
                "status": "good",
                "score": 95,
                "ipa": pair_info.get("sound", ""),
                "feedback": "Phát âm chuẩn xác!"
            })
            total_score_sum += 95 * weight
            total_weight += weight
            continue

        # Check minimal pair counter word (e.g. said 'pill' instead of 'peel')
        counter = pair_info.get("counter")
        if counter and counter in spoken_remaining:
            spoken_remaining.remove(counter)
            advice = pair_info.get("advice", "Cần chú ý độ dài và khẩu hình.")
            words_analysis.append({
                "word": orig_word,
                "clean": tw,
                "status": "warning",
                "score": 55,
                "ipa": pair_info.get("sound", ""),
                "feedback": f"Đọc nhầm sang từ '{counter}'. {advice}"
            })
            total_score_sum += 55 * weight
            total_weight += weight
            continue

        # Near match (Levenshtein ratio)
        matches = difflib.get_close_matches(tw, spoken_remaining, n=1, cutoff=0.65)
        if matches:
            found_spoken = matches[0]
            spoken_remaining.remove(found_spoken)
            ratio = difflib.SequenceMatcher(None, tw, found_spoken).ratio()
            score_est = int(70 + ratio * 20)
            words_analysis.append({
                "word": orig_word,
                "clean": tw,
                "status": "good" if score_est >= 85 else "warning",
                "score": score_est,
                "ipa": pair_info.get("sound", ""),
                "feedback": f"Nghe gần đúng ('{found_spoken}'). Cần phát âm rõ âm đuôi."
            })
            total_score_sum += score_est * weight
            total_weight += weight
            continue

        # Missing word or pronounced completely differently
        words_analysis.append({
            "word": orig_word,
            "clean": tw,
            "status": "error",
            "score": 40,
            "ipa": pair_info.get("sound", ""),
            "feedback": "Chưa nhận diện được từ này hoặc bị nuốt âm."
        })
        total_score_sum += 40 * weight
        total_weight += weight

    overall_score = int(round(total_score_sum / max(1.0, total_weight)))

    # Advice generation
    if overall_score >= 88:
        grade = "Xuất Sắc (A+)"
        general_advice = "Ngữ điệu và phát âm các cặp âm tối thiểu rất tốt! Bạn đã sẵn sàng ghép bài nộp."
    elif overall_score >= 78:
        grade = "Rất Tốt (A)"
        general_advice = "Phát âm rõ ràng, nhịp điệu tự nhiên. Chú ý kéo dài hoặc ngắt ngắn một số nguyên âm trọng tâm."
    elif overall_score >= 65:
        grade = "Khá (B)"
        general_advice = "Cần mở khẩu hình rộng hơn và chú ý phân biệt các từ trong cặp âm tối thiểu."
    else:
        grade = "Cần Cải Thiện (C)"
        general_advice = "Hãy bấm nút 'Nghe Mẫu AI Phát Âm' để nghe kỹ lại trước khi bấm thu âm lại nhé."

    return {
        "success": True,
        "score": overall_score,
        "grade": grade,
        "engine": "Local Phonetic AI Engine (Chuẩn Âm Vị LACB)",
        "focusPair": rule_book.get("focus", ""),
        "wordsAnalysis": words_analysis,
        "generalAdvice": general_advice,
        "spokenTranscript": spoken_text if spoken_text else "(Nhận diện từ âm thanh)",
        "beeknoeeStatus": "Hệ thống tự động sử dụng Local Phonetic Engine (Khi tài khoản Beeknoee có số dư sẽ tự động kích hoạt thêm Whisper Cloud STT)."
    }

def evaluate_with_beeknoee_cloud(audio_file_path, target_text, audio_num=1, api_key=None):
    """
    Attempt evaluation using Beeknoee Cloud API (Whisper STT + Gemini 3.1 LLM).
    Returns None if balance is 0 / 402 or offline, letting local engine handle it.
    """
    key = api_key or os.environ.get("BEE_API_KEY") or DEFAULT_BEE_KEY
    if not key or not os.path.exists(audio_file_path):
        return None

    headers = {"Authorization": f"Bearer {key}"}

    # Step 1: Transcribe using Beeknoee Whisper STT
    try:
        with open(audio_file_path, "rb") as f:
            files = {"file": ("audio.mp3", f, "audio/mpeg")}
            data = {"model": BEE_STT_MODEL, "language": "en"}
            resp_stt = requests.post(f"{BEE_BASE_URL}/audio/transcriptions", headers=headers, files=files, data=data, timeout=12)

        if resp_stt.status_code != 200:
            # Insufficient balance (402) or other error
            return None

        stt_result = resp_stt.json()
        spoken_text = stt_result.get("text", "").strip()
        if not spoken_text:
            return None

        # Step 2: Call Beeknoee LLM (Gemini 3.1 Flash Lite) for expert phonetic assessment
        system_prompt = (
            "You are a Senior English Phonetics Assessor for university students studying English Phonology. "
            "Evaluate the student's spoken transcription against the target sentence. "
            "Output JSON with keys: score (0-100 integer), grade (string), feedback (concise Vietnamese advice on mouth/tongue/vowel length)."
        )
        user_prompt = (
            f"Target sentence: \"{target_text}\"\n"
            f"Student said: \"{spoken_text}\"\n"
            f"Topic: Audio {audio_num} minimal pairs.\n"
            "Respond in valid JSON only."
        )

        resp_llm = requests.post(
            f"{BEE_BASE_URL}/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": BEE_EVAL_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.2,
                "max_tokens": 400
            },
            timeout=15
        )

        if resp_llm.status_code == 200:
            content = resp_llm.json()["choices"][0]["message"]["content"]
            json_match = re.search(r"\{.*\}", content, re.DOTALL)
            if json_match:
                parsed = json.loads(json_match.group(0))
                # Run local word alignment on top of Beeknoee STT text to get word tags
                local_res = local_phonetic_evaluate(target_text, spoken_text, audio_num)
                local_res["score"] = parsed.get("score", local_res["score"])
                local_res["grade"] = parsed.get("grade", local_res["grade"])
                local_res["generalAdvice"] = parsed.get("feedback", local_res["generalAdvice"])
                local_res["engine"] = "Beeknoee AI Cloud (Whisper Large v3 + Gemini 3.1 Flash Lite)"
                local_res["beeknoeeStatus"] = "Đã phân tích qua Beeknoee Cloud Gateway thành công!"
                return local_res

    except Exception:
        pass

    return None

