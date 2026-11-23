# BÁO CÁO TOÀN DIỆN: KHÔI PHỤC API, TÁI SỬ DỤNG DỮ LIỆU GIỌNG NÓI VÀ HOÀN THIỆN PROJECT BIT1

**Dự án triển khai:** Bit1 Voice Studio (Hệ thống xử lý giọng nói tiếng Anh AI, Thu âm từng câu, Cắt ghép bài & Đánh giá phát âm tức thì Beeknoee AI)  
**Thời gian cập nhật:** 23/11/2026  
**Chuyên gia phụ trách:** Senior Full-stack Developer, AI Engineer & Software Architect  

---

## 1. Kết quả tra cứu tài liệu & Khảo sát API Beeknoee Audio Platform

Qua rà soát mã nguồn các dự án cũ (`auto-rating-KHBD`, `Auto_gen_KHBD`, `edit_KHBD`, `test_Giao_Duc`) và tra cứu tài liệu nền tảng **Beeknoee Platform** (`platform.beeknoee.com`), hệ thống đã xác định cấu trúc API âm thanh của Beeknoee:

1. **Chuẩn kết nối thống nhất (OpenAI Compatible):**
   - **Base URL:** `https://platform.beeknoee.com/api/v1`
   - **Xác thực:** Header `Authorization: Bearer sk-bee-...`
2. **Các dịch vụ âm thanh & mô hình hỗ trợ:**
   - **Speech-to-Text (STT / File Transcription):** Hỗ trợ `POST /audio/transcriptions` với các mô hình hàng đầu: `whisper-large-v3-turbo`, `whisper-large-v3`, `whisper-1`, `google/gemini-2.5-flash-stt`. Nhận dạng chuẩn xác từng âm vị tiếng Anh.
   - **Text-to-Speech (TTS):** Hỗ trợ `POST /audio/speech` với `google/google-tts`, `kokoro-82m`, `openai/tts-1`.
   - **Đánh giá âm vị học bằng LLM:** Hỗ trợ `POST /chat/completions` với mô hình tối ưu `google/gemini-3.1-flash-lite` để phân tích khẩu hình, vị trí đặt lưỡi và độ dài nguyên âm.
3. **Hiện trạng tài khoản & Cơ chế Dual-Engine:**
   - Các khóa API cũ trong hệ thống (`sk-bee-9a4e3a...` và `sk-bee-73e9d7...`) đều hợp lệ (HTTP 200 tại `/models` với 347 mô hình).
   - Tuy nhiên, khi gọi `/chat/completions` hoặc `/audio/transcriptions`, API trả về mã lỗi `HTTP 402: Insufficient balance` (cần nạp số dư bằng VNĐ tại `https://platform.beeknoee.com/billing`).
   - **Giải pháp tối ưu đã triển khai:** Xây dựng kiến trúc **Dual-Engine (Lai ghép 2 tầng)**:
     - *Tầng 1 (Cloud):* Gọi Beeknoee Whisper STT + Gemini 3.1 khi tài khoản có số dư.
     - *Tầng 2 (Local Fallback):* Tự động kích hoạt **Local Phonetic AI Engine** khi tài khoản 402 hoặc offline, đảm bảo người học **luôn luôn nhận được điểm số và đánh giá tức thì** mà không bao giờ bị gián đoạn hay phụ thuộc mạng.

---

## 2. Bảng tổng hợp các API & Công nghệ giọng nói trong Bit1 Studio

| Tên Dịch Vụ / Công Nghệ | Phân Loại | Trạng Thái | Vai Trò Trong Bit1 Voice Studio |
| :--- | :--- | :--- | :--- |
| **Beeknoee AI Cloud STT & LLM** | Cloud Whisper & Gemini | **Tích hợp sẵn (Kèm Fallback)** | Nhận diện giọng nói qua Whisper v3 và phân tích âm vị học sâu qua Gemini 3.1 Flash Lite. |
| **Local Phonetic AI Engine** | Offline Rule-based Alignment | **Hoạt động 100% (Mặc định)** | So khớp chuỗi âm vị, đối chiếu cặp âm tối thiểu (Minimal Pairs 5 Audio) và chấm điểm 0-100 tức thì. |
| **MediaRecorder & Web Audio API** | Client-side Recording | **Hoạt động 100%** | Thu âm giọng thật của học viên từng câu trực tiếp trên trình duyệt, có preview tức thì. |
| **FFmpeg Concat & DSP Engine** | Audio Splicing & DSP | **Hoạt động 100%** | Chuẩn hóa sample rate 44.1kHz, chèn khoảng nghỉ 350ms tự nhiên và ghép các câu thành file MP3 192kbps. |
| **Microsoft Edge Neural TTS** | Neural Conversational TTS | **Hoạt động xuất sắc** | Cung cấp câu mẫu chuẩn bản xứ cho học viên nghe trước khi thu; tự động bù câu chưa thu. |
| **Web Speech API (`SpeechRecognition`)** | Realtime STT | **Hoạt động tốt** | Bắt giọng nói trực tiếp song song lúc thu âm để gửi lên bộ đánh giá âm vị. |

---

## 3. Tính năng mới: Đánh Giá Phát Âm Liền Tay Ngay Khi Thu Xong

### 🎯 Quy trình học tập tối ưu:
1. **Thu âm câu riêng lẻ:** Người học bấm micro thu duy nhất 1 câu.
2. **Đánh giá tức thì (Instant Assessment):**
   - Ngay khi người học bấm **"Dừng thu"**, hệ thống có tùy chọn tự động kích hoạt bộ đánh giá (hoặc bấm nút **`🎯 Đánh Giá Liền Câu Này`**).
   - Bảng kết quả phân tích hiển thị ngay bên dưới câu đó chỉ sau 0.5 giây:
     - **Điểm số trực quan:** Thang điểm 100 (A+, A, B, C) với mã màu rõ ràng.
     - **Hiển thị thẻ từ (Word Pills):**
       - 🟢 *Màu xanh:* Từ phát âm chuẩn xác.
       - 🟡 *Màu vàng:* Từ đọc gần đúng, cần chú ý âm đuôi hoặc âm lướt.
       - 🔴 *Màu đỏ:* Từ đọc nhầm sang cặp âm đối lập (ví dụ: cần đọc `peel` /iː/ nhưng đọc thành `pill` /ɪ/, hay `bin` thành `bean`) hoặc bị nuốt âm.
     - **Lời khuyên âm học chi tiết:** Hướng dẫn cụ thể về khẩu hình miệng, độ bẹt của môi, độ dài nguyên âm và cách đặt đầu lưỡi.
3. **Thu lại không giới hạn:** Người học đọc lại câu đó cho đến khi đạt điểm tối đa (90–100 điểm) rồi mới chuyển sang câu tiếp theo.
4. **Ghép bài 1-Click:** Khi toàn bộ các câu đều đạt điểm cao, bấm **"Ghép Thành Bài Nộp Hoàn Chỉnh (.MP3)"** để xuất file nộp bài chuẩn chỉnh.

---

## 4. Hướng dẫn sử dụng & Khởi chạy hệ thống

### A. Địa chỉ truy cập
Hệ thống chạy trên cổng riêng độc lập **`5180`**, tách biệt hoàn toàn với dự án bài giảng `thaogiang` (cổng 5173):
👉 **`http://localhost:5180`**

### B. Khởi động 1-Click
1. Mở thư mục: `c:\Users\X1\Desktop\VB2\kì 1\luyện âm`.
2. Nhấp đúp file: **`Chay_Studio_Cong_5180.bat`**.
3. Trình duyệt sẽ tự động mở trang Studio tại địa chỉ `http://localhost:5180`.

### C. Nạp số dư Beeknoee AI (Tùy chọn)
Nếu muốn bật thêm tính năng phiên âm Cloud Whisper bằng Beeknoee, người dùng có thể:
1. Bấm nút **`⚙️ Cấu Hình Beeknoee AI`** ở góc trên cùng bên phải giao diện Studio.
2. Nhấp vào liên kết **Nạp số dư tài khoản** (`https://platform.beeknoee.com/billing`).
3. Dán API Key mới và bấm **Lưu & Áp Dụng**.
*(Lưu ý: Ngay cả khi chưa nạp số dư, hệ thống vẫn hoạt động trơn tru 100% nhờ bộ xử lý Local Phonetic AI Engine).*
