# -*- coding: utf-8 -*-
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_documents():
    doc = docx.Document()

    # Set Margins
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Title
    title_p = doc.add_paragraph()
    title_run = title_p.add_run("KỊCH BẢN THU ÂM MẪU GIỌNG ĐỂ CLONE AI CHUẨN XÁC NHẤT\n(PHỤC VỤ 5 BÀI TẬP MÔN LUYỆN ÂM CĂN BẢN - VB2)")
    title_run.font.name = "Arial"
    title_run.font.size = Pt(15)
    title_run.font.bold = True
    title_run.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Intro
    p_intro = doc.add_paragraph()
    p_intro.paragraph_format.space_before = Pt(4)
    p_intro.paragraph_format.space_after = Pt(12)
    r_intro = p_intro.add_run(
        "Mục đích: Bài đọc này được thiết kế cô đọng, lồng ghép 100% các cặp âm trọng tâm (Minimal Pairs) "
        "từ Audio 1 đến Audio 5 (nguyên âm ngắn/dài, nguyên âm đôi, và các cặp phụ âm bật hơi). "
        "Khi lấy mẫu bằng bài này, mô hình AI (F5-TTS hoặc ElevenLabs) sẽ nhận diện đúng khẩu hình và ngữ điệu tự nhiên của bạn nhất."
    )
    r_intro.font.name = "Arial"
    r_intro.font.size = Pt(10)
    r_intro.font.italic = True
    r_intro.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    def add_heading(text, level=1):
        h = doc.add_paragraph()
        h.paragraph_format.space_before = Pt(12)
        h.paragraph_format.space_after = Pt(4)
        r = h.add_run(text)
        r.font.name = "Arial"
        r.font.bold = True
        if level == 1:
            r.font.size = Pt(12.5)
            r.font.color.rgb = RGBColor(0x0C, 0x4A, 0x6E)
        else:
            r.font.size = Pt(11)
            r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        return h

    def add_box(text, bg_hex="F0FDF4", border_hex="86EFAC"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_ALIGN_PARAGRAPH.CENTER
        table.autofit = False
        table.columns[0].width = Inches(6.8)
        cell = table.cell(0, 0)
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hex}"/>')
        tcPr.append(shd)

        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/>'
            f'<w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>'
        )
        tcPr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    # --- PHẦN 1 ---
    add_heading("PHẦN 1: DÀNH CHO GOOGLE COLAB (F5-TTS) — CHỈ CẦN ĐỌC 1 CÂU (8 – 12 GIÂY)")
    p1 = doc.add_paragraph("👉 F5-TTS chỉ cần đoạn mẫu ngắn 8 - 12 giây. Hãy chọn duy nhất 1 trong 3 câu dưới đây để ghi âm:")
    p1.runs[0].font.name = "Arial"
    p1.runs[0].font.size = Pt(10)

    add_heading("• Câu lựa chọn 1 (Khuyên dùng - Bao quát Audio 1, 2 và 4):", level=2)
    add_box(
        '"Hey Brad, are you ready to leave? Did you pack the bread, the fresh bun, and put the peel in the bin near the old park?"',
        "F0F9FF", "0284C7"
    )

    add_heading("• Câu lựa chọn 2 (Bao quát Audio 3 và 4 - Âm u/oo, ơ và nguyên âm đôi):", level=2)
    add_box(
        '"Look at that bird near the pool! The warm soup is ready, so take a seat by the pier and enjoy a taste of the pie."',
        "F8FAFC", "64748B"
    )

    add_heading("• Câu lựa chọn 3 (Bao quát Audio 5 - Phụ âm bật hơi ch/j, sh/s, p/b):", level=2)
    add_box(
        '"Poppy and Ben are joking near the shoe shop, checking the cheap green Jeep and sipping a cup of hot tea."',
        "F8FAFC", "64748B"
    )

    # --- PHẦN 2 ---
    add_heading("PHẦN 2: DÀNH CHO ELEVENLABS HOẶC CLONE TOÀN DIỆN (1.5 – 2 PHÚT)")
    p2 = doc.add_paragraph(
        "👉 Nếu dùng ElevenLabs (trong tool desktop), hãy đọc trọn vẹn đoạn văn dưới đây với giọng đều, thong thả (mất khoảng 1m30s - 2m):"
    )
    p2.runs[0].font.name = "Arial"
    p2.runs[0].font.size = Pt(10)

    full_story = (
        '"Hey Brad and Jane, are you ready to leave for our trip? Remember to park the truck near the old barn, '
        'not near the small hut. Did you peel the fresh apples, pack the bread in a pan, and put the peel in the bin? '
        'Look at the cute little chicks with yellow cheeks near the pool! The weather is warm, but do not let the dog lick the hot soup.\n\n'
        'Roy brought some fried cod, a fresh bun, and a cup of tea. We can sit by the pier, drink a cold beer, '
        'and watch the wooden boat float on the water. Be careful not to step on that worm near the rock, or a bird might fly down from the tree.\n\n'
        'Poppy and Ben are still checking that cheap green Jeep near the shoe shop. What a funny day! '
        'Let us measure our time, sew a letter on the jacket, ring the bell, and mark an X on the map to start our journey."'
    )
    add_box(full_story, "F0FDF4", "16A34A")

    # --- PHẦN 3 ---
    add_heading("PHẦN 3: HƯỚNG DẪN KỸ THUẬT THU ÂM ĐỂ GIỐNG NHẤT")
    tips = [
        ("1. Âm lượng & Tông giọng:", "Đọc đúng cao độ giọng nói hàng ngày (không thì thầm, không gồng quá trầm hoặc quá cao). Đọc rõ các phụ âm cuối (ending sounds như /t/, /d/, /k/, /s/, /z/)."),
        ("2. Nhịp ngắt nghỉ:", "Dừng khoảng 0.5 giây ở dấu phẩy (,) và 1 giây ở dấu chấm (.). Không cần đọc vội hay lướt âm quá nhanh."),
        ("3. Vị trí Micro:", "Đặt mic (tai nghe hoặc điện thoại) cách miệng 15 - 20 cm, hơi nghiêng chếch một bên để tránh tiếng gió hơi thở phả vào mic."),
        ("4. Xử lý sau thu âm:", "Lưu file với tên 'my_voice.mp3' hoặc 'my_voice.wav'. Dùng phần mềm cắt bỏ 1 giây im lặng lúc bấm nút ở đầu và cuối.")
    ]
    for title, desc in tips:
        tp = doc.add_paragraph()
        tp.paragraph_format.space_before = Pt(2)
        tp.paragraph_format.space_after = Pt(2)
        r1 = tp.add_run(f"• {title} ")
        r1.font.name = "Arial"
        r1.font.bold = True
        r1.font.size = Pt(10)
        r2 = tp.add_run(desc)
        r2.font.name = "Arial"
        r2.font.size = Pt(10)

    output_docx = "Doc_Thu_Am_Mau_Giong_LACB.docx"
    doc.save(output_docx)
    print(f"Generated: {output_docx}")

    # Generate companion TXT
    txt_content = f"""================================================================================
KỊCH BẢN THU ÂM MẪU GIỌNG ĐỂ CLONE AI CHUẨN XÁC NHẤT
(PHỤC VỤ 5 BÀI TẬP MÔN LUYỆN ÂM CĂN BẢN - VB2)
================================================================================

Tài liệu này được thiết kế bao phủ 100% các cặp âm trọng tâm (Minimal Pairs) 
từ Audio 1 đến Audio 5. Giúp AI nhận diện đúng khẩu hình và ngữ điệu tự nhiên của bạn.

--------------------------------------------------------------------------------
PHẦN 1: DÀNH CHO GOOGLE COLAB (F5-TTS) — CHỈ CẦN 1 CÂU (8 – 12 GIÂY)
--------------------------------------------------------------------------------
(Chỉ cần chọn đọc DUY NHẤT 1 trong 3 câu sau):

[LỰA CHỌN 1 - KHUYÊN DÙNG (Bao quát Audio 1, 2 & 4)]:
"Hey Brad, are you ready to leave? Did you pack the bread, the fresh bun, and put the peel in the bin near the old park?"

[LỰA CHỌN 2 (Bao quát Audio 3 & 4 - Âm u/oo, ơ và nguyên âm đôi)]:
"Look at that bird near the pool! The warm soup is ready, so take a seat by the pier and enjoy a taste of the pie."

[LỰA CHỌN 3 (Bao quát Audio 5 - Phụ âm bật hơi ch/j, sh/s, p/b)]:
"Poppy and Ben are joking near the shoe shop, checking the cheap green Jeep and sipping a cup of hot tea."


--------------------------------------------------------------------------------
PHẦN 2: DÀNH CHO ELEVENLABS HOẶC CLONE TOÀN DIỆN (1.5 – 2 PHÚT)
--------------------------------------------------------------------------------
(Đọc toàn bộ đoạn văn liền mạch dưới đây với nhịp độ thong thả, tự nhiên):

"Hey Brad and Jane, are you ready to leave for our trip? Remember to park the truck near the old barn, not near the small hut. Did you peel the fresh apples, pack the bread in a pan, and put the peel in the bin? Look at the cute little chicks with yellow cheeks near the pool! The weather is warm, but do not let the dog lick the hot soup.

Roy brought some fried cod, a fresh bun, and a cup of tea. We can sit by the pier, drink a cold beer, and watch the wooden boat float on the water. Be careful not to step on that worm near the rock, or a bird might fly down from the tree.

Poppy and Ben are still checking that cheap green Jeep near the shoe shop. What a funny day! Let us measure our time, sew a letter on the jacket, ring the bell, and mark an X on the map to start our journey."


--------------------------------------------------------------------------------
PHẦN 3: KỸ THUẬT THU ÂM ĐỂ GIỐNG NHẤT
--------------------------------------------------------------------------------
1. Âm lượng & Tông giọng: 
   - Đọc bằng đúng giọng nói hàng ngày của bạn. 
   - Chú ý đọc rõ các âm đuôi (ending sounds: t, d, k, p, s, z).
2. Nhịp ngắt nghỉ:
   - Dấu phẩy (,) ngắt nghỉ ~0.5 giây.
   - Dấu chấm (.) ngắt nghỉ ~1.0 giây.
3. Micro:
   - Đặt mic cách miệng 15-20 cm, hơi lệch 45 độ để tránh tiếng phả hơi thở.
4. Tên file:
   - Đổi tên file thu âm thành "my_voice.mp3" hoặc "my_voice.wav" để đưa vào tool/Colab.
================================================================================
"""
    with open("Doc_Thu_Am_Mau_Giong_LACB.txt", "w", encoding="utf-8") as f:
        f.write(txt_content)
    print("Generated: Doc_Thu_Am_Mau_Giong_LACB.txt")

if __name__ == "__main__":
    create_documents()

