# LuyenAm - Bit1 AI English Voice Studio

Ứng dụng Luyện âm Tiếng Anh AI, Thu âm từng câu bằng giọng thật 100%, Đánh giá phát âm âm vị học tức thì (Beeknoee AI / Local Phonetics) và Tự động cắt ghép thành file MP3 hoàn chỉnh phục vụ môn Luyện âm căn bản (LACB - VB2 Ngôn ngữ Anh).

## 🌟 Tính Năng Chính
- 🎙️ **Thu âm từng câu bằng giọng thật:** Phân tách kịch bản chi tiết 5 bài Audio (cả Speaker 1 và Speaker 2) thành từng câu độc lập kèm ký hiệu phiên âm IPA và bản dịch tiếng Việt.
- 🎯 **Đánh giá phát âm AI liền tay:** Chấm điểm ngay khi dừng thu âm theo thang điểm 100 (A+, A, B, C). Mã màu chi tiết từng từ:
  - 🟢 Xanh: Phát âm chuẩn xác.
  - 🟡 Vàng: Gần đúng, cần chú ý âm đuôi.
  - 🔴 Đỏ: Đọc nhầm sang từ đối lập trong cặp âm tối thiểu (Minimal Pairs) hoặc nuốt âm.
- 💡 **Góp ý khẩu hình âm học:** Hướng dẫn vị trí đặt lưỡi, độ mở của môi và độ dài nguyên âm.
- ✂️ **Tự động ghép bài nộp bằng FFmpeg / Web Audio:** Tự động nối các câu đã thu thành 1 file MP3 192kbps liền mạch có khoảng ngắt nghỉ 350ms tự nhiên.
- 🎧 **10 File âm thanh bài nộp hoàn chỉnh:** Tải về nhanh 5 Audio (Speaker 1 & 2) chuẩn đàm thoại tự nhiên.
- 🗣️ **Text to Speech & STT:** Luyện tập phát âm tự do với các giọng đọc bản xứ (`Brian`, `Ava`, `Ryan`).

## 🚀 Triển Khai
- **Trực tiếp trên Vercel:** Deploy nhanh dưới dạng Static Web App.
- **Chạy cục bộ:** Cổng 5180 (`python server_luyen_am.py` hoặc nhấp đúp `Chay_Studio_Cong_5180.bat`).
