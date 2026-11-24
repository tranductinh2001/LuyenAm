# LuyenAm - Bit1 AI English Voice Studio

Ứng dụng Luyện âm Tiếng Anh AI, Thu âm từng câu bằng giọng thật 100%, Đánh giá phát âm âm vị học tức thì (100% Không Cần Key AI), Nghe mẫu bản xứ lưu sẵn đa tốc độ (0.75x / 1.0x / 1.25x) và Tự động cắt ghép thành file MP3 hoàn chỉnh phục vụ môn Luyện âm căn bản (LACB - VB2 Ngôn ngữ Anh).

## 🌟 Tính Năng Chính
- ⚡ **100% Không Cần Key AI:** Hoạt động hoàn toàn độc lập, không yêu cầu Beekone hay bất kỳ API key nào. Mọi tính năng đánh giá âm vị và phát mẫu đều chạy mượt mà ngay lập tức.
- 🔊 **50 File Âm Thanh Mẫu Lưu Sẵn (Zero Latency):** Toàn bộ 50 câu thoại của 5 Audio (Speaker 1 Nam & Speaker 2 Nữ) đã được sinh sẵn và lưu trong thư mục `sample_audio/`. Bấm là phát ngay tức khắc (<10ms), không cần chờ tải mạng.
- 🎚️ **Tùy Chỉnh Tốc Độ Đọc Mẫu Linh Hoạt:**
  - 🐢 **0.75x (Chậm):** Dễ nghe chi tiết khẩu hình miệng, độ căng nguyên âm và âm đuôi để nhại theo (Shadowing).
  - 🎯 **1.0x (Chuẩn):** Tốc độ đàm thoại tự nhiên của người bản xứ.
  - ⚡ **1.25x (Nhanh):** Nâng cao khả năng phản xạ nghe nói.
- 🎙️ **Thu âm từng câu bằng giọng thật:** Phân tách kịch bản chi tiết 5 bài Audio (cả Speaker 1 và Speaker 2) thành từng câu độc lập kèm ký hiệu phiên âm IPA và bản dịch tiếng Việt.
- 🎯 **Đánh giá phát âm AI liền tay:** Chấm điểm ngay khi dừng thu âm theo thang điểm 100 (A+, A, B, C). Mã màu chi tiết từng từ:
  - 🟢 Xanh: Phát âm chuẩn xác.
  - 🟡 Vàng: Gần đúng, cần chú ý âm đuôi.
  - 🔴 Đỏ: Đọc nhầm sang từ đối lập trong cặp âm tối thiểu (Minimal Pairs) hoặc nuốt âm.
- 💡 **Góp ý khẩu hình âm học:** Hướng dẫn vị trí đặt lưỡi, độ mở của môi và độ dài nguyên âm.
- ✂️ **Công nghệ Ghép & Xử lý Âm thanh AI Thông minh (Smart AI Splicer):**
  - **FFT Room Denoiser:** Lọc tạp âm nền, tiếng quạt gió và tiếng rè mic tần số thấp (<80Hz) & tần số cao (>12kHz).
  - **Smart VAD Trimming:** Tự động phát hiện và cắt bỏ khoảng lặng thừa (dead-air), tiếng thở, tiếng click chuột ở đầu và cuối mỗi câu thu trước khi ghép.
  - **Dynamic Leveling & Loudness Normalization:** Tự động cân bằng độ to nhỏ giữa các câu và chuẩn hóa âm lượng theo chuẩn phát thanh quốc tế (-16 LUFS, True Peak -1.5dB).
  - **Anti-Click Micro-fades:** Chèn dải làm mượt 15ms ở các điểm nối câu, loại bỏ hoàn toàn hiện tượng nổ lách tách (click/pop) khi ghép.
- 🎧 **10 File âm thanh bài nộp hoàn chỉnh:** Tải về nhanh 5 Audio (Speaker 1 & 2) chuẩn đàm thoại tự nhiên.

## 🚀 Triển Khai
- **Trực tiếp trên Vercel:** Deploy nhanh dưới dạng Static Web App.
- **Chạy cục bộ:** Cổng 5180 (`python server_luyen_am.py` hoặc nhấp đúp `Chay_Studio_Cong_5180.bat`).

