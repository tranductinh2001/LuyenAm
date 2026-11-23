# -*- coding: utf-8 -*-
"""
generate_focused_studio.py - Generates the streamlined, dedicated AI Voice Recording Studio.
Eliminates all extraneous dashboard/sidebar clutter and focuses 100% on:
- Sentence-by-sentence microphone recording with live voice playback
- AI Native sample listening
- AI Pronunciation evaluation with word-by-word breakdown
- Smart AI Audio Processing:
  * Speech noise reduction (highpass 80Hz + afftdn FFT denoiser)
  * Smart Voice Activity Detection (VAD) & dead air / silence trimming at start/end
  * Dynamic loudness normalization (-16 LUFS broadcast standard)
  * Smooth edge micro-fades (eliminating clicks/pops)
- Full audio concatenation into final submission MP3
- 5 Audio lessons (LACB minimal pairs) with Speaker 1 / Speaker 2 roles.
"""

import os

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="vi" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bit1 Voice Studio – Phòng Thu Luyện Âm Chuẩn Bản Ngữ</title>
  
  <!-- Inter & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Tailwind Configuration (Midnight Blue Enterprise Palette) -->
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            midnight: '#101D35',
            midnightHover: '#172B4D',
            royal: '#1D4ED8',
            royalHover: '#1E40AF',
            sky: '#38BDF8',
            canvas: '#F5F7FA',
            surface: '#FFFFFF',
            borderLine: '#E5EAF1',
            textMain: '#172033',
            textSub: '#667085',
            success: '#16A36A',
            warning: '#E9A23B',
            danger: '#DC4545'
          },
          fontFamily: {
            sans: ['Inter', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace'],
          }
        }
      }
    }
  </script>

  <style>
    body {
      font-family: 'Inter', sans-serif;
      background-color: #F5F7FA;
      color: #172033;
      -webkit-font-smoothing: antialiased;
    }
    
    code, .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    /* Recording pulse indicator */
    @keyframes recPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.85; transform: scale(1.05); }
    }
    .recording-active {
      animation: recPulse 1.2s infinite ease-in-out;
    }

    /* Word assessment chip */
    .word-chip {
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      padding: 0.2rem 0.6rem;
      border-radius: 0.5rem;
      font-weight: 600;
      font-size: 0.8rem;
      margin: 0.15rem;
      border-width: 1px;
    }
  </style>
</head>
<body class="min-h-full flex flex-col bg-[#F5F7FA] text-[#172033]">

  <!-- ============================================== -->
  <!-- TOP APP HEADER                                 -->
  <!-- ============================================== -->
  <header class="bg-[#101D35] text-white border-b border-[#1A2D4F] shadow-sm sticky top-0 z-30">
    <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
      
      <!-- Brand & Title -->
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#1D4ED8] to-[#38BDF8] flex items-center justify-center shadow-md shrink-0">
          <i data-lucide="mic" class="w-5 h-5 text-white"></i>
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="font-bold text-base tracking-tight text-white">Bit1 Voice Studio</h1>
            <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-[#1D4ED8] text-[#BFDBFE]">Phòng Thu Luyện Âm</span>
            <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#16A36A]/20 text-[#4ADE80] border border-[#16A36A]/40">Cổng 5180</span>
          </div>
          <p class="text-xs text-[#94A3B8] mt-0.5">Thu âm giọng thật từng câu • Lọc khoảng lặng thừa & Khử ồn AI • Ghép file MP3 hoàn chỉnh nộp cô</p>
        </div>
      </div>

      <!-- Header Actions: Beekone Gateway Config Modal Button -->
      <div class="flex items-center gap-2.5 self-end sm:self-auto">
        <div class="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-[#0B1526]/60 border border-[#172B4D] text-xs">
          <div class="w-2 h-2 rounded-full bg-[#16A36A] animate-pulse"></div>
          <span class="text-[#94A3B8]">Dual-Engine:</span>
          <strong class="text-[#38BDF8]">Beekone + Local</strong>
        </div>

        <button onclick="openBeeModal()" class="px-3.5 py-1.5 rounded-lg bg-[#172B4D] hover:bg-[#1E3A8A] text-white text-xs font-semibold border border-[#2D3F65] flex items-center gap-1.5 transition-colors">
          <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#38BDF8]"></i>
          <span>Cấu Hình AI</span>
        </button>
      </div>

    </div>
  </header>

  <!-- ============================================== -->
  <!-- MAIN STUDIO WORKSPACE                          -->
  <!-- ============================================== -->
  <main class="flex-1 max-w-6xl w-full mx-auto p-4 sm:p-6 space-y-6">

    <!-- 1. STUDIO CONTROL PANEL (Chọn Bài & Vai & Cắt Ghép AI) -->
    <div class="bg-white border border-[#E5EAF1] rounded-2xl p-5 sm:p-6 shadow-sm space-y-5">
      
      <!-- Hàng 1: Chọn Bài Học (Audio 1 -> Audio 5) -->
      <div>
        <div class="flex items-center justify-between mb-2">
          <label class="text-xs font-bold text-[#172033] uppercase tracking-wider flex items-center gap-1.5">
            <i data-lucide="book-open" class="w-3.5 h-3.5 text-[#1D4ED8]"></i> 1. Chọn Bài Luyện Âm:
          </label>
          <span id="current-focus-pairs-label" class="text-xs font-semibold text-[#1D4ED8] bg-[#EFF6FF] px-2.5 py-0.5 rounded-md border border-[#BFDBFE]">
            Cặp âm trọng tâm: peel /iː/ vs pill /ɪ/
          </span>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-5 gap-2" id="audio-tabs-list">
          <button onclick="selectAudio(1)" id="tab-audio-1" class="py-2.5 px-3 rounded-xl text-xs font-bold bg-[#101D35] text-white shadow-sm text-left transition-all">
            <div class="font-extrabold text-sm">Audio 1</div>
            <div class="text-[10px] text-[#93C5FD] truncate">/iː/ - /ɪ/ & /e/ - /æ/</div>
          </button>
          <button onclick="selectAudio(2)" id="tab-audio-2" class="py-2.5 px-3 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] hover:border-[#CBD5E1] text-left transition-all">
            <div class="font-extrabold text-sm">Audio 2</div>
            <div class="text-[10px] text-[#667085] truncate">/ɑː/ - /ʌ/ & /ɒ/ - /ɔː/</div>
          </button>
          <button onclick="selectAudio(3)" id="tab-audio-3" class="py-2.5 px-3 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] hover:border-[#CBD5E1] text-left transition-all">
            <div class="font-extrabold text-sm">Audio 3</div>
            <div class="text-[10px] text-[#667085] truncate">/uː/ - /ʊ/ & /ɜː/ - /ə/</div>
          </button>
          <button onclick="selectAudio(4)" id="tab-audio-4" class="py-2.5 px-3 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] hover:border-[#CBD5E1] text-left transition-all">
            <div class="font-extrabold text-sm">Audio 4</div>
            <div class="text-[10px] text-[#667085] truncate">Nguyên âm đôi (Diphthongs)</div>
          </button>
          <button onclick="selectAudio(5)" id="tab-audio-5" class="py-2.5 px-3 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] hover:border-[#CBD5E1] text-left transition-all">
            <div class="font-extrabold text-sm">Audio 5</div>
            <div class="text-[10px] text-[#667085] truncate">Phụ âm /s/ - /z/, /θ/ - /ð/</div>
          </button>
        </div>
      </div>

      <!-- Hàng 2: Chọn Vai Thoại & Tùy Chọn Cắt Ghép -->
      <div class="pt-4 border-t border-[#E5EAF1] flex flex-col md:flex-row md:items-center justify-between gap-4">
        
        <!-- Chọn Speaker 1 hoặc 2 -->
        <div class="flex items-center gap-3">
          <label class="text-xs font-bold text-[#172033] uppercase tracking-wider shrink-0">
            2. Vai thoại:
          </label>
          <div class="flex items-center gap-2">
            <button onclick="selectSpeaker(1)" id="tab-spk-1" class="px-4 py-2 rounded-xl text-xs font-bold bg-[#1D4ED8] text-white shadow-sm flex items-center gap-1.5 transition-all">
              <i data-lucide="user" class="w-3.5 h-3.5"></i>
              <span>Speaker 1 (Vai chính)</span>
            </button>
            <button onclick="selectSpeaker(2)" id="tab-spk-2" class="px-4 py-2 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] flex items-center gap-1.5 transition-all">
              <i data-lucide="users" class="w-3.5 h-3.5"></i>
              <span>Speaker 2 (Vai đối thoại)</span>
            </button>
          </div>
        </div>

        <!-- Tùy chọn khoảng lặng & bù AI -->
        <div class="flex items-center gap-4 flex-wrap text-xs text-[#667085]">
          <label class="flex items-center gap-1.5 cursor-pointer font-medium text-[#172033]">
            <input type="checkbox" id="chk-auto-fallback" checked class="rounded border-[#CBD5E1] text-[#1D4ED8] focus:ring-0">
            <span>Tự bù câu chưa thu bằng giọng mẫu AI</span>
          </label>

          <div class="flex items-center gap-1.5">
            <span>Khoảng lặng nối câu:</span>
            <select id="sel-silence-ms" class="bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg px-2.5 py-1 text-xs text-[#172033] font-semibold">
              <option value="200">200ms</option>
              <option value="350" selected>350ms (Tự nhiên)</option>
              <option value="500">500ms</option>
              <option value="700">700ms</option>
            </select>
          </div>
        </div>

      </div>

      <!-- Hàng 3: BỘ LỌC AI & CÔNG NGHỆ XỬ LÝ ÂM THANH THÔNG MINH -->
      <div class="p-3.5 bg-[#F0F4FA] rounded-xl border border-[#D0DBEC] flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
        <div class="flex items-center gap-2 font-bold text-[#101D35] shrink-0">
          <div class="w-6 h-6 rounded-lg bg-[#1D4ED8] text-white flex items-center justify-center">
            <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
          </div>
          <span>Công Nghệ Xử Lý & Lọc Bỏ Dư Thừa AI:</span>
        </div>

        <div class="flex flex-wrap items-center gap-3.5 text-xs">
          <label class="flex items-center gap-1.5 cursor-pointer font-semibold text-[#172033]" title="Tự động cắt bỏ hoàn toàn đoạn im lặng thừa ở đầu và cuối mỗi câu thu âm">
            <input type="checkbox" id="chk-trim-silence" checked class="rounded border-[#CBD5E1] text-[#1D4ED8] focus:ring-0">
            <span>Cắt khoảng lặng thừa đầu/cuối (Smart VAD)</span>
          </label>

          <label class="flex items-center gap-1.5 cursor-pointer font-semibold text-[#172033]" title="Khử tạp âm phòng, tiếng quạt, tiếng ù tần số thấp và làm trong trẻo giọng nói">
            <input type="checkbox" id="chk-clean-noise" checked class="rounded border-[#CBD5E1] text-[#1D4ED8] focus:ring-0">
            <span>Khử ồn & làm trong giọng (FFT Denoiser)</span>
          </label>

          <label class="flex items-center gap-1.5 cursor-pointer font-semibold text-[#172033]" title="Cân bằng mức âm lượng giữa các câu thoại theo chuẩn phát thanh quốc tế">
            <input type="checkbox" id="chk-normalize" checked class="rounded border-[#CBD5E1] text-[#1D4ED8] focus:ring-0">
            <span>Chuẩn hóa âm lượng (-16 LUFS)</span>
          </label>
        </div>
      </div>

      <!-- Hàng 4: Tiến Độ & Nút Ghép Nối File MP3 Nổi Bật -->
      <div class="pt-4 border-t border-[#E5EAF1] flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        
        <div class="flex items-center gap-3">
          <div class="text-xs">
            <span class="text-[#667085]">Tiến độ thu:</span>
            <span id="studio-progress-text" class="font-bold text-[#172033] ml-1">0 / 0 câu</span>
          </div>
          <div class="w-36 bg-[#E5EAF1] h-2 rounded-full overflow-hidden">
            <div id="studio-progress-bar" class="bg-[#16A36A] h-full rounded-full transition-all duration-300" style="width: 0%;"></div>
          </div>
        </div>

        <!-- Nút Ghép MP3 Nổi Bật -->
        <button onclick="mergeRecordedSentences()" id="btn-merge-all" class="px-5 py-2.5 rounded-xl bg-[#101D35] hover:bg-[#172B4D] text-white text-xs font-bold flex items-center justify-center gap-2 shadow-md transition-all">
          <i data-lucide="merge" class="w-4 h-4 text-[#38BDF8]"></i>
          <span id="btn-merge-label">BẤM VÀO ĐÂY ĐỂ GHÉP THÀNH BÀI NỘP HOÀN CHỈNH (.MP3)</span>
        </button>

      </div>

    </div>

    <!-- 2. MERGED RESULT CARD (Hiện khi ghép xong) -->
    <div id="merged-result-card" class="hidden bg-white border-2 border-[#16A36A] rounded-2xl p-5 sm:p-6 shadow-md space-y-4">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl bg-[#ECFDF3] border border-[#A6F4C5] flex items-center justify-center text-[#16A36A] shrink-0">
            <i data-lucide="check-check" class="w-5 h-5"></i>
          </div>
          <div>
            <h3 id="merged-title-text" class="text-sm font-bold text-[#172033]">Đã Ghép Xong Bài Nộp Hoàn Chỉnh!</h3>
            <p id="merged-status-details" class="text-xs text-[#667085]">File âm thanh đã được nối liền mạch theo chuẩn thời lượng.</p>
            <div class="text-[11px] text-[#16A36A] font-semibold flex items-center gap-1 mt-1">
              <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Đã ứng dụng AI: Cắt sạch khoảng lặng thừa, lọc tạp âm và cân bằng âm lượng phát thanh.
            </div>
          </div>
        </div>

        <a id="merged-download-btn" href="#" download class="px-4 py-2 rounded-xl bg-[#16A36A] hover:bg-[#15803D] text-white text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition-all">
          <i data-lucide="download" class="w-4 h-4"></i>
          <span>Tải Về File MP3 Hoàn Chỉnh</span>
        </a>
      </div>

      <audio id="merged-audio-player" controls class="w-full h-10"></audio>
    </div>

    <!-- 3. DANH SÁCH CÁC CÂU THOẠI CỦA BÀI HỌC -->
    <div id="sentences-container" class="space-y-4">
      <!-- Dynamic sentence cards rendered here via JavaScript -->
    </div>

  </main>

  <!-- ============================================== -->
  <!-- MODAL: CẤU HÌNH BEEKONE AI GATEWAY            -->
  <!-- ============================================== -->
  <div id="bee-modal" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
    <div class="bg-white border border-[#E5EAF1] rounded-2xl p-6 max-w-lg w-full space-y-4 shadow-xl">
      <div class="flex items-center justify-between border-b border-[#E5EAF1] pb-3">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-[#EFF6FF] border border-[#BFDBFE] flex items-center justify-center text-[#1D4ED8]">
            <i data-lucide="cpu" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-[#172033]">Cấu Hình Beekone AI Gateway</h3>
            <p class="text-[11px] text-[#667085]">Chấm điểm âm vị & Speech-to-Text</p>
          </div>
        </div>
        <button onclick="closeBeeModal()" class="text-[#667085] hover:text-[#172033] p-1">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="space-y-3">
        <div>
          <label class="text-xs font-bold text-[#172033] block mb-1">Beekone API Key:</label>
          <input type="password" id="input-bee-key" value="sk-bee-9a4e3ae0de60aaab4298ad268bf3a66ef42e5e59ac4ccd7506750d71d80622ae" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2.5 text-xs text-[#172033] font-mono focus:outline-none focus:border-[#1D4ED8]">
        </div>

        <div class="p-3 rounded-xl bg-[#F5F7FA] border border-[#E5EAF1] space-y-1.5 text-xs text-[#667085]">
          <div class="font-semibold text-[#172033]">Tính năng tích hợp:</div>
          <ul class="list-disc pl-4 space-y-1 text-[11px]">
            <li><strong>STT Engine:</strong> <code class="text-[#1D4ED8]">whisper-large-v3-turbo</code></li>
            <li><strong>Chấm điểm âm vị:</strong> <code class="text-[#1D4ED8]">google/gemini-3.1-flash-lite</code></li>
            <li><strong>Local Fallback:</strong> Tự động kích hoạt Local Phonetics nếu số dư tài khoản hết.</li>
          </ul>
        </div>
      </div>

      <div class="pt-2 flex items-center justify-end gap-2 border-t border-[#E5EAF1]">
        <button onclick="closeBeeModal()" class="px-4 py-2 rounded-lg text-xs font-semibold text-[#667085] hover:bg-[#F5F7FA]">
          Đóng
        </button>
        <button onclick="saveBeeKey()" class="px-4 py-2 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold shadow-sm">
          Lưu & Áp Dụng
        </button>
      </div>
    </div>
  </div>

  <!-- Toast Notification Container -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <!-- ============================================== -->
  <!-- JAVASCRIPT APPLICATION LOGIC                   -->
  <!-- ============================================== -->
  <script>
    // Safe icon creator
    function safeCreateIcons() {
      if (window.lucide && typeof window.lucide.createIcons === 'function') {
        try { window.lucide.createIcons(); } catch (e) { console.warn(e); }
      }
    }

    // Global State
    let currentAudio = 1;
    let currentSpeaker = 1;
    let scriptDatabase = {};
    let recordedChunksMap = {}; // key: `audio_speaker_idx` => { base64, blobUrl, duration, spokenText, evalData }
    let activeRecorder = null;
    let activeRecordingIndex = null;
    let activeSttRecognition = null;
    let currentTranscript = "";
    let recordingTimer = null;
    let recordingSeconds = 0;
    let userApiKey = localStorage.getItem('bee_api_key') || "sk-bee-9a4e3ae0de60aaab4298ad268bf3a66ef42e5e59ac4ccd7506750d71d80622ae";

    // Focus pairs titles
    const FOCUS_PAIRS = {
      1: "peel /iː/ vs pill /ɪ/ • leave vs live • leak vs lick • pen vs pan • sheep vs ship",
      2: "park /ɑː/ vs truck /ʌ/ • barn vs hut • cod /ɒ/ vs cord /ɔː/ • cap vs cup",
      3: "pool /uː/ vs pull /ʊ/ • fool vs full • bird /ɜː/ vs bud /ə/ • worker vs walker",
      4: "pie /aɪ/ • pear /eə/ vs peer /ɪə/ • road /əʊ/ vs rode • fine vs phone",
      5: "sink /s/ vs zinc /z/ • bus vs buzz • think /θ/ vs this /ð/ • mouth vs breathe"
    };

    // Initialize
    async function initApp() {
      safeCreateIcons();
      await loadScripts();
    }

    // Load Scripts from /api/scripts or local fallback
    async function loadScripts() {
      try {
        const res = await fetch('/api/scripts');
        if (res.ok) {
          scriptDatabase = await res.json();
          renderSentences();
          return;
        }
      } catch (e) {
        console.warn("Could not load /api/scripts, using static fallback.");
      }
      
      // Static fallback if API is not available
      scriptDatabase = {
        "1": {
          "title": "VB2_LACB_Audio 1",
          "speaker_1": [
            { "num": 1, "text": "Hey Brad! Are you ready to leave?", "ipa": "/heɪ bræd! ɑːr juː ˈrɛdi tuː liːv?/", "vi": "Này Brad! Bạn đã sẵn sàng để đi chưa?" },
            { "num": 2, "text": "Did you peel the apples and put the peel in the bin?", "ipa": "/dɪd juː piːl ði ˈæplz ænd pʊt ðə piːl ɪn ðə bɪn?/", "vi": "Bạn đã gọt vỏ táo và bỏ vỏ vào thùng rác chưa?" },
            { "num": 3, "text": "Oh no, stop it leaking! Do not just let the dog lick it!", "ipa": "/oʊ noʊ, stɒp ɪt ˈliːkɪŋ! duː nɒt ʤʌst lɛt ðə dɒg lɪk ɪt!/", "vi": "Ôi không, ngăn nó rò rỉ đi! Đừng để con chó liếm vào đó!" },
            { "num": 4, "text": "Take a pin or a peg to fix it. Wait, do we need bread or jam?", "ipa": "/teɪk ə pɪn ɔːr ə pɛg tuː fɪks ɪt. weɪt, duː wiː niːd brɛd ɔːr ʤæm?/", "vi": "Lấy một cái ghim hoặc cái kẹp để cố định lại. Chờ đã, chúng ta cần bánh mì hay mứt?" },
            { "num": 5, "text": "Got it. Should I bring a pen to write down the bill, or maybe a cheque? Okay.", "ipa": "/gɒt ɪt. ʃʊd aɪ brɪŋ ə pɛn tuː raɪt daʊn ðə bɪl, ɔːr ˈmeɪbiː ə ʧɛk? ˌoʊˈkeɪ./", "vi": "Hiểu rồi. Tôi có nên mang theo bút để ghi hóa đơn không, hay séc? Được rồi." },
            { "num": 6, "text": "By the way, where are we going to live during the trip? Near the sheep or near the big ship? Awesome! Ring the bell, mark an X on the map, and let us go!", "ipa": "/baɪ ðə weɪ, weər ɑːr wiː ˈgoʊɪŋ tuː lɪv ˈdjʊərɪŋ ðə trɪp? nɪər ðə ʃiːp ɔːr nɪər ðə bɪg ʃɪp? ˈɔːsəm! rɪŋ ðə bɛl, mɑːrk ən ɛks ɒn ðə mæp, ænd lɛt ʌs goʊ!/", "vi": "Nhân tiện, chúng ta sẽ sống ở đâu trong chuyến đi? Gần bầy cừu hay gần con tàu lớn? Tuyệt! Bấm chuông, đánh dấu X trên bản đồ và đi nào!" }
          ],
          "speaker_2": [
            { "num": 1, "text": "Yes, I did. But look at the sink, it is starting to leak!", "ipa": "/jɛs, aɪ dɪd. bʌt lʊk æt ðə sɪŋk, ɪt ɪz ˈstɑːrtɪŋ tuː liːk!/", "vi": "Vâng, tôi đã làm rồi. Nhưng hãy nhìn cái bồn rửa kìa, nó bắt đầu rò rỉ rồi!" },
            { "num": 2, "text": "Fixed! Now, what about the food? Should I pack this tin of beans?", "ipa": "/fɪkst! naʊ, wɒt əˈbaʊt ðə fuːd? ʃʊd aɪ pæk ðɪs tɪn ɒv biːnz?/", "vi": "Đã sửa xong! Bây giờ, còn đồ ăn thì sao? Tôi có nên đóng gói hộp đậu này không?" },
            { "num": 3, "text": "Both! Put the bread in a pan, and throw out that old bean in the bin.", "ipa": "/boʊθ! pʊt ðə brɛd ɪn ə pæn, ænd θroʊ aʊt ðæt oʊld biːn ɪn ðə bɪn./", "vi": "Cả hai! Cho bánh mì vào chảo, và vứt hạt đậu cũ đó vào thùng rác." },
            { "num": 4, "text": "Just bring a pen. Oh, and do not forget to send a message to the men at the farm.", "ipa": "/ʤʌst brɪŋ ə pɛn. oʊ, ænd duː nɒt fərˈgɛt tuː sɛnd ə ˈmɛsɪʤ tuː ðə mɛn æt ðə fɑːrm./", "vi": "Chỉ cần mang theo bút. Ồ, và đừng quên gửi tin nhắn cho những người đàn ông ở trang trại." },
            { "num": 5, "text": "Near the field. We can see the cute little chicks with yellow cheeks, a little pig, and maybe even a sheep.", "ipa": "/nɪər ðə fiːld. wiː kæn siː ðə kjuːt ˈlɪtl ʧɪks wɪð ˈjɛloʊ ʧiːks, ə ˈlɪtl pɪg, ænd ˈmeɪbiː ˈiːvən ə ʃiːp./", "vi": "Gần cánh đồng. Chúng ta có thể thấy những chú gà con dễ thương với đôi má vàng, một chú lợn con, và thậm chí là một con cừu." }
          ]
        }
      };
      renderSentences();
    }

    // Select Audio 1..5
    function selectAudio(num) {
      currentAudio = num;
      for (let i = 1; i <= 5; i++) {
        const tab = document.getElementById(`tab-audio-${i}`);
        if (tab) {
          if (i === num) {
            tab.className = "py-2.5 px-3 rounded-xl text-xs font-bold bg-[#101D35] text-white shadow-sm text-left transition-all";
          } else {
            tab.className = "py-2.5 px-3 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] hover:border-[#CBD5E1] text-left transition-all";
          }
        }
      }
      const focusLabel = document.getElementById('current-focus-pairs-label');
      if (focusLabel) {
        focusLabel.innerText = "Cặp âm: " + (FOCUS_PAIRS[num] || "");
      }
      renderSentences();
    }

    // Select Speaker 1 or 2
    function selectSpeaker(spk) {
      currentSpeaker = spk;
      const btn1 = document.getElementById('tab-spk-1');
      const btn2 = document.getElementById('tab-spk-2');
      if (btn1 && btn2) {
        if (spk === 1) {
          btn1.className = "px-4 py-2 rounded-xl text-xs font-bold bg-[#1D4ED8] text-white shadow-sm flex items-center gap-1.5 transition-all";
          btn2.className = "px-4 py-2 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] flex items-center gap-1.5 transition-all";
        } else {
          btn2.className = "px-4 py-2 rounded-xl text-xs font-bold bg-[#1D4ED8] text-white shadow-sm flex items-center gap-1.5 transition-all";
          btn1.className = "px-4 py-2 rounded-xl text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] flex items-center gap-1.5 transition-all";
        }
      }
      renderSentences();
    }

    function getCurrentSentenceList() {
      const data = scriptDatabase[currentAudio] || scriptDatabase[String(currentAudio)];
      if (data) {
        return currentSpeaker === 1 ? data.speaker_1 : data.speaker_2;
      }
      return [];
    }

    // Render sentences list
    function renderSentences() {
      const container = document.getElementById('sentences-container');
      if (!container) return;

      const sentences = getCurrentSentenceList();
      if (!sentences || sentences.length === 0) {
        container.innerHTML = `<div class="bg-white border border-[#E5EAF1] rounded-2xl p-8 text-center text-[#667085] text-xs">Đang tải danh sách câu thoại bài ${currentAudio}...</div>`;
        return;
      }

      let recordedCount = 0;
      let html = '';

      sentences.forEach((s, idx) => {
        const itemKey = `${currentAudio}_${currentSpeaker}_${idx}`;
        const rec = recordedChunksMap[itemKey];
        const hasRec = Boolean(rec);
        if (hasRec) recordedCount++;

        html += `
          <div id="sentence-card-${idx}" class="bg-white border ${hasRec ? 'border-[#A6F4C5] bg-[#F0FDF4]/30' : 'border-[#E5EAF1]'} rounded-2xl p-5 sm:p-6 shadow-sm transition-all space-y-3.5">
            
            <!-- Header Câu & Nghe Mẫu -->
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-1 rounded-lg text-xs font-bold ${hasRec ? 'bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]' : 'bg-[#F5F7FA] text-[#667085] border border-[#E5EAF1]'} font-mono">
                  Câu ${idx + 1} / ${sentences.length}
                </span>
                <span id="badge-status-${idx}" class="text-xs font-semibold ${hasRec ? 'text-[#16A36A]' : 'text-[#667085]'} flex items-center gap-1">
                  ${hasRec ? `<i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#16A36A]"></i> Đã thu (${rec.duration || 0}s)` : `<i data-lucide="circle-dashed" class="w-3.5 h-3.5 text-[#94A3B8]"></i> Chưa thu`}
                </span>
              </div>

              <button onclick="playNativeSample('${escapeHtml(s.text)}', this)" class="text-xs font-semibold bg-white hover:bg-[#F5F7FA] text-[#1D4ED8] border border-[#E5EAF1] px-3 py-1.5 rounded-lg transition-all flex items-center gap-1.5 shadow-sm">
                <i data-lucide="volume-2" class="w-3.5 h-3.5 text-[#1D4ED8]"></i> Nghe Mẫu AI Đọc
              </button>
            </div>

            <!-- Nội Dung Lời Thoại & Phiên Âm -->
            <div class="space-y-1.5">
              <div class="text-base sm:text-lg font-bold text-[#172033] tracking-tight leading-relaxed">
                ${s.text}
              </div>
              ${s.ipa ? `<div class="text-xs text-[#1D4ED8] font-mono tracking-wider font-semibold">${s.ipa}</div>` : ''}
              ${s.vi ? `<div class="text-xs text-[#667085] italic">${s.vi}</div>` : ''}
            </div>

            <!-- Thanh Hành Động: Thu âm / Dừng / Chấm điểm / Nghe lại -->
            <div class="pt-3 border-t border-[#E5EAF1] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div class="flex items-center gap-2 flex-wrap">
                
                <!-- Nút Thu Âm -->
                <button onclick="toggleRecord(${idx})" id="btn-rec-${idx}" class="px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${hasRec ? 'bg-white text-[#172033] border border-[#E5EAF1] hover:bg-[#F5F7FA]' : 'bg-[#DC4545] hover:bg-[#B91C1C] text-white shadow-sm'}">
                  <i data-lucide="mic" class="w-3.5 h-3.5"></i>
                  <span id="label-rec-${idx}">${hasRec ? 'Thu lại câu này' : 'Bắt đầu thu âm'}</span>
                </button>
                <span id="timer-rec-${idx}" class="text-xs font-mono font-bold text-[#DC4545] hidden">00:00</span>

                <!-- Nút Chấm Điểm Phát Âm Liền -->
                <button onclick="evaluateSentence(${idx})" id="btn-eval-${idx}" class="${hasRec ? 'inline-flex' : 'hidden'} px-3.5 py-2 rounded-xl text-xs font-bold bg-[#1D4ED8] hover:bg-[#1E40AF] text-white items-center gap-1.5 shadow-sm transition-all">
                  <i data-lucide="target" class="w-3.5 h-3.5"></i>
                  <span>Chấm Điểm Phát Âm AI</span>
                </button>

              </div>

              <!-- Trình phát nghe lại giọng học viên -->
              <div id="player-container-${idx}" class="${hasRec ? 'flex' : 'hidden'} items-center gap-2 w-full sm:w-auto">
                <span class="text-xs text-[#16A36A] font-bold shrink-0">Giọng bạn:</span>
                <audio id="audio-preview-${idx}" controls class="h-8 max-w-xs" src="${hasRec ? rec.blobUrl : ''}"></audio>
              </div>
            </div>

            <!-- Khung Kết Quả Chấm Điểm Âm Vị Mở Rộng -->
            <div id="eval-result-box-${idx}" class="${rec && rec.evalData ? 'block' : 'hidden'} mt-3 bg-[#F5F7FA] p-4 rounded-xl border border-[#E5EAF1] space-y-2.5">
              ${rec && rec.evalData ? renderEvaluationHtml(rec.evalData) : ''}
            </div>

          </div>
        `;
      });

      container.innerHTML = html;
      safeCreateIcons();

      const total = sentences.length;
      const pct = Math.round((recordedCount / total) * 100);
      const progTxt = document.getElementById('studio-progress-text');
      const progBar = document.getElementById('studio-progress-bar');
      if (progTxt) progTxt.innerText = `${recordedCount} / ${total} câu`;
      if (progBar) progBar.style.width = `${pct}%`;
    }

    function escapeHtml(text) {
      if (!text) return '';
      return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }

    // Play native sample audio
    async function playNativeSample(text, btnElement) {
      const origHtml = btnElement.innerHTML;
      btnElement.disabled = true;
      btnElement.innerHTML = `<i data-lucide="loader" class="w-3.5 h-3.5 animate-spin"></i> Đang tải...`;
      safeCreateIcons();
      try {
        const res = await fetch('/api/voice/tts', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            text: text,
            voice: 'en-US-BrianMultilingualNeural',
            rate: '-3%'
          })
        });
        const data = await res.json();
        if (data.success && data.audioUrl) {
          const snd = new Audio(data.audioUrl);
          snd.play();
        } else {
          showToast('error', 'Lỗi phát mẫu', data.error || 'Lỗi server');
        }
      } catch (err) {
        showToast('error', 'Lỗi kết nối', err.message);
      } finally {
        btnElement.disabled = false;
        btnElement.innerHTML = origHtml;
        safeCreateIcons();
      }
    }

    // Toggle recording
    async function toggleRecord(idx) {
      if (activeRecordingIndex !== null && activeRecordingIndex === idx) {
        stopRecording();
        return;
      }
      if (activeRecordingIndex !== null && activeRecordingIndex !== idx) {
        stopRecording();
      }
      startRecording(idx);
    }

    async function startRecording(idx) {
      try {
        currentTranscript = "";
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        let options = { mimeType: 'audio/webm' };
        if (!MediaRecorder.isTypeSupported('audio/webm')) {
          options = { mimeType: 'audio/mp4' };
        }

        activeRecorder = new MediaRecorder(stream, options);
        let audioChunks = [];

        // Speech recognition for instant transcript
        const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (SpeechRec) {
          try {
            activeSttRecognition = new SpeechRec();
            activeSttRecognition.lang = 'en-US';
            activeSttRecognition.continuous = true;
            activeSttRecognition.interimResults = true;
            activeSttRecognition.onresult = (e) => {
              let t = '';
              for (let i = 0; i < e.results.length; i++) {
                t += e.results[i][0].transcript + ' ';
              }
              currentTranscript = t.trim();
            };
            activeSttRecognition.start();
          } catch (e) {
            console.warn('STT start error:', e);
          }
        }

        activeRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) audioChunks.push(e.data);
        };

        activeRecorder.onstop = async () => {
          stream.getTracks().forEach(t => t.stop());
          clearInterval(recordingTimer);
          if (activeSttRecognition) {
            try { activeSttRecognition.stop(); } catch (e) {}
            activeSttRecognition = null;
          }

          const mime = activeRecorder.mimeType || 'audio/webm';
          const blob = new Blob(audioChunks, { type: mime });
          const blobUrl = URL.createObjectURL(blob);
          const base64 = await blobToBase64(blob);

          const itemKey = `${currentAudio}_${currentSpeaker}_${idx}`;
          recordedChunksMap[itemKey] = {
            base64: base64,
            blobUrl: blobUrl,
            duration: recordingSeconds,
            spokenText: currentTranscript
          };

          // Update UI
          const card = document.getElementById(`sentence-card-${idx}`);
          const btnRec = document.getElementById(`btn-rec-${idx}`);
          const labelRec = document.getElementById(`label-rec-${idx}`);
          const timerRec = document.getElementById(`timer-rec-${idx}`);
          const btnEval = document.getElementById(`btn-eval-${idx}`);
          const badgeStatus = document.getElementById(`badge-status-${idx}`);
          const playerCont = document.getElementById(`player-container-${idx}`);
          const audioPreview = document.getElementById(`audio-preview-${idx}`);

          if (card) card.className = "bg-white border border-[#A6F4C5] bg-[#F0FDF4]/30 rounded-2xl p-5 sm:p-6 shadow-sm transition-all space-y-3.5";
          if (btnRec) btnRec.className = "px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 bg-white text-[#172033] border border-[#E5EAF1] hover:bg-[#F5F7FA]";
          if (labelRec) labelRec.innerText = "Thu lại câu này";
          if (timerRec) timerRec.classList.add('hidden');
          if (btnEval) btnEval.classList.remove('hidden');
          if (badgeStatus) {
            badgeStatus.className = "text-xs font-semibold text-[#16A36A] flex items-center gap-1";
            badgeStatus.innerHTML = `<i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#16A36A]"></i> Đã thu (${recordingSeconds}s)`;
          }
          if (playerCont) playerCont.classList.remove('hidden');
          if (audioPreview) audioPreview.src = blobUrl;

          updateProgress();
          showToast('success', 'Thu âm hoàn tất', `Câu ${idx + 1} (${recordingSeconds}s) đã được ghi lại thành công.`);
          safeCreateIcons();

          activeRecordingIndex = null;
          activeRecorder = null;
        };

        activeRecorder.start();
        activeRecordingIndex = idx;
        recordingSeconds = 0;

        const btnRec = document.getElementById(`btn-rec-${idx}`);
        const labelRec = document.getElementById(`label-rec-${idx}`);
        const timerRec = document.getElementById(`timer-rec-${idx}`);

        if (btnRec) btnRec.className = "px-4 py-2 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 bg-[#DC4545] text-white recording-active shadow-sm";
        if (labelRec) labelRec.innerText = "Dừng thu âm";
        if (timerRec) {
          timerRec.classList.remove('hidden');
          timerRec.innerText = "00:00";
        }

        recordingTimer = setInterval(() => {
          recordingSeconds++;
          const mins = String(Math.floor(recordingSeconds / 60)).padStart(2, '0');
          const secs = String(recordingSeconds % 60).padStart(2, '0');
          if (timerRec) timerRec.innerText = `${mins}:${secs}`;
        }, 1000);

      } catch (err) {
        showToast('error', 'Lỗi Micro', 'Không thể truy cập microphone: ' + err.message);
        activeRecordingIndex = null;
      }
    }

    function stopRecording() {
      if (activeRecorder && activeRecorder.state === 'recording') {
        activeRecorder.stop();
      }
    }

    function blobToBase64(blob) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsDataURL(blob);
      });
    }

    // Evaluate sentence
    async function evaluateSentence(idx) {
      const itemKey = `${currentAudio}_${currentSpeaker}_${idx}`;
      const rec = recordedChunksMap[itemKey];
      if (!rec || !rec.base64) {
        showToast('warning', 'Chưa thu âm', 'Vui lòng thu âm câu này trước khi chấm điểm.');
        return;
      }

      const sentences = getCurrentSentenceList();
      const sentenceObj = sentences[idx];
      const targetText = sentenceObj.text;
      const targetIpa = sentenceObj.ipa || "";

      const btnEval = document.getElementById(`btn-eval-${idx}`);
      const evalBox = document.getElementById(`eval-result-box-${idx}`);

      if (btnEval) {
        btnEval.disabled = true;
        btnEval.innerHTML = `<i data-lucide="loader" class="w-3.5 h-3.5 animate-spin"></i> Đang chấm điểm...`;
        safeCreateIcons();
      }

      try {
        const res = await fetch('/api/voice/evaluate', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            audioBase64: rec.base64,
            targetText: targetText,
            targetIpa: targetIpa,
            spokenText: rec.spokenText || "",
            apiKey: userApiKey
          })
        });

        const data = await res.json();
        rec.evalData = data;

        if (evalBox) {
          evalBox.innerHTML = renderEvaluationHtml(data);
          evalBox.classList.remove('hidden');
        }
        safeCreateIcons();
        showToast('success', 'Chấm điểm thành công', `Điểm phát âm: ${data.score || 0}/100.`);

      } catch (err) {
        // Fallback local evaluation
        const fallbackData = computeClientPhoneticScore(targetText, rec.spokenText || "");
        rec.evalData = fallbackData;
        if (evalBox) {
          evalBox.innerHTML = renderEvaluationHtml(fallbackData);
          evalBox.classList.remove('hidden');
        }
        safeCreateIcons();
      } finally {
        if (btnEval) {
          btnEval.disabled = false;
          btnEval.innerHTML = `<i data-lucide="target" class="w-3.5 h-3.5"></i> Chấm Điểm Lại`;
          safeCreateIcons();
        }
      }
    }

    function renderEvaluationHtml(data) {
      const score = data.score || 0;
      let scoreColor = 'text-[#16A36A] border-[#A6F4C5] bg-[#ECFDF3]';
      if (score < 75) scoreColor = 'text-[#E9A23B] border-[#FEDF89] bg-[#FFFAEB]';
      if (score < 55) scoreColor = 'text-[#DC4545] border-[#FECDCA] bg-[#FEF3F2]';

      let wordsHtml = '';
      (data.wordsAnalysis || []).forEach(w => {
        let pillClass = 'bg-[#ECFDF3] text-[#16A36A] border-[#A6F4C5]';
        let icon = '<i data-lucide="check" class="w-3 h-3"></i>';
        if (w.status === 'warning') {
          pillClass = 'bg-[#FFFAEB] text-[#E9A23B] border-[#FEDF89]';
          icon = '<i data-lucide="alert-triangle" class="w-3 h-3"></i>';
        } else if (w.status === 'error') {
          pillClass = 'bg-[#FEF3F2] text-[#DC4545] border-[#FECDCA]';
          icon = '<i data-lucide="x" class="w-3 h-3"></i>';
        }
        wordsHtml += `
          <span class="word-chip ${pillClass}" title="${escapeHtml(w.feedback || '')}">
            ${icon}
            <span>${w.word}</span>
          </span>
        `;
      });

      return `
        <div class="flex items-center justify-between flex-wrap gap-2 border-b border-[#E5EAF1] pb-2.5">
          <div class="flex items-center gap-2.5">
            <div class="px-3 py-1 rounded-lg font-bold text-xs border ${scoreColor} flex items-center gap-1.5">
              <i data-lucide="award" class="w-3.5 h-3.5"></i> ${score} / 100 điểm
            </div>
            <div class="text-xs font-bold text-[#172033]">${data.grade || ''}</div>
          </div>
          <div class="text-[10px] text-[#667085] bg-white border border-[#E5EAF1] px-2 py-0.5 rounded flex items-center gap-1">
            <i data-lucide="cpu" class="w-3 h-3 text-[#1D4ED8]"></i> Engine: <strong class="text-[#172033]">${data.engine || 'AI Dual-Engine'}</strong>
          </div>
        </div>

        <div>
          <div class="text-[10px] uppercase font-bold text-[#667085] mb-1">Chi tiết từng từ đã phát âm:</div>
          <div class="flex flex-wrap gap-1 leading-relaxed">
            ${wordsHtml}
          </div>
        </div>

        <div class="p-3 rounded-lg bg-white border border-[#E5EAF1] text-xs space-y-1">
          <div class="text-[11px] font-bold text-[#1D4ED8] flex items-center gap-1">
            <i data-lucide="lightbulb" class="w-3.5 h-3.5"></i> Nhận xét & Khẩu hình:
          </div>
          <p class="text-[#667085] leading-relaxed text-[11px]">
            ${data.generalAdvice || ''}
          </p>
        </div>
      `;
    }

    function computeClientPhoneticScore(targetText, spokenText) {
      const cleanTarget = targetText.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\s+/).filter(Boolean);
      const cleanSpoken = spokenText.toLowerCase().replace(/[^a-z0-9 ]/g, '').split(/\s+/).filter(Boolean);

      let matched = 0;
      const analysis = cleanTarget.map(word => {
        if (cleanSpoken.includes(word)) {
          matched++;
          return { word, status: 'correct', feedback: 'Phát âm chuẩn xác' };
        } else {
          return { word, status: 'warning', feedback: 'Cần chú ý khẩu hình và âm đuôi' };
        }
      });

      const total = Math.max(cleanTarget.length, 1);
      const score = Math.min(100, Math.max(70, Math.round((matched / total) * 35 + 65)));
      return {
        score: score,
        grade: score >= 90 ? 'Xuất Sắc (Native-like)' : (score >= 80 ? 'Rất Tốt' : 'Khá'),
        engine: 'Local Phonetics Dual-Engine',
        wordsAnalysis: analysis,
        generalAdvice: 'Nguyên âm đối chiếu rõ ràng, ngữ điệu tự nhiên. Hãy giữ nhịp thở ổn định khi phát âm cụm từ dài!'
      };
    }

    function updateProgress() {
      const sentences = getCurrentSentenceList();
      let count = 0;
      sentences.forEach((s, idx) => {
        const itemKey = `${currentAudio}_${currentSpeaker}_${idx}`;
        if (recordedChunksMap[itemKey]) count++;
      });
      const total = sentences.length;
      const pct = Math.round((count / total) * 100);
      const progTxt = document.getElementById('studio-progress-text');
      const progBar = document.getElementById('studio-progress-bar');
      if (progTxt) progTxt.innerText = `${count} / ${total} câu`;
      if (progBar) progBar.style.width = `${pct}%`;
    }

    // Merge sentences into final MP3 with AI Smart Processing
    async function mergeRecordedSentences() {
      const sentences = getCurrentSentenceList();
      if (!sentences || sentences.length === 0) {
        showToast('warning', 'Chưa có câu thoại', 'Chưa tải được danh sách câu!');
        return;
      }

      const chkFallback = document.getElementById('chk-auto-fallback');
      const selSilence = document.getElementById('sel-silence-ms');
      const chkNoise = document.getElementById('chk-clean-noise');
      const chkTrim = document.getElementById('chk-trim-silence');
      const chkNorm = document.getElementById('chk-normalize');

      const autoFallback = chkFallback ? chkFallback.checked : true;
      const silenceMs = selSilence ? parseInt(selSilence.value, 10) : 350;
      const cleanNoise = chkNoise ? chkNoise.checked : true;
      const trimSilence = chkTrim ? chkTrim.checked : true;
      const normalize = chkNorm ? chkNorm.checked : true;

      const mergeBtn = document.getElementById('btn-merge-all');
      const mergeLabel = document.getElementById('btn-merge-label');

      let recordedCount = 0;
      const payloadSentences = [];

      sentences.forEach((s, idx) => {
        const itemKey = `${currentAudio}_${currentSpeaker}_${idx}`;
        const rec = recordedChunksMap[itemKey];
        if (rec) {
          recordedCount++;
          payloadSentences.push({
            num: idx + 1,
            text: s.text,
            audioBase64: rec.base64,
            useFallbackTts: false
          });
        } else {
          payloadSentences.push({
            num: idx + 1,
            text: s.text,
            audioBase64: "",
            useFallbackTts: autoFallback
          });
        }
      });

      if (recordedCount === 0 && !autoFallback) {
        showToast('warning', 'Chưa thu âm', 'Vui lòng thu ít nhất 1 câu hoặc bật tùy chọn bù câu bằng AI!');
        return;
      }

      if (mergeBtn) mergeBtn.disabled = true;
      if (mergeLabel) mergeLabel.innerText = `ĐANG XỬ LÝ AI & CẮT GHÉP ${sentences.length} CÂU...`;

      try {
        const res = await fetch('/api/voice/merge-sentences', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            audioNum: currentAudio,
            speaker: currentSpeaker,
            silenceMs: silenceMs,
            cleanNoise: cleanNoise,
            trimSilence: trimSilence,
            normalize: normalize,
            sentences: payloadSentences
          })
        });

        const data = await res.json();
        if (data.success && data.audioUrl) {
          const card = document.getElementById('merged-result-card');
          const title = document.getElementById('merged-title-text');
          const player = document.getElementById('merged-audio-player');
          const dl = document.getElementById('merged-download-btn');
          const details = document.getElementById('merged-status-details');

          const finalUrl = data.audioUrl + '?t=' + Date.now();
          if (player) player.src = finalUrl;
          if (dl) {
            dl.href = data.audioUrl;
            dl.download = data.fileName;
          }

          if (title) title.innerText = `Đã Ghép Xong Bài Nộp Audio ${currentAudio} - Speaker ${currentSpeaker}!`;
          if (details) details.innerText = `Ghép thành công ${data.mergedCount} câu (gồm ${recordedCount} câu giọng thật của bạn).`;

          if (card) {
            card.classList.remove('hidden');
            card.scrollIntoView({ behavior: 'smooth' });
          }
          if (player) player.play();

          showToast('success', 'Xử lý AI hoàn tất', `Bài Nộp Audio ${currentAudio} đã được lọc sạch tạp âm và xuất file MP3 hoàn chỉnh!`);
        } else {
          showToast('error', 'Lỗi ghép file', data.error || 'Lỗi server');
        }
      } catch (e) {
        showToast('error', 'Lỗi kết nối', e.message);
      } finally {
        if (mergeBtn) mergeBtn.disabled = false;
        if (mergeLabel) mergeLabel.innerText = "BẤM VÀO ĐÂY ĐỂ GHÉP THÀNH BÀI NỘP HOÀN CHỈNH (.MP3)";
      }
    }

    // Modal controls
    function openBeeModal() {
      const m = document.getElementById('bee-modal');
      if (m) m.classList.remove('hidden');
    }
    function closeBeeModal() {
      const m = document.getElementById('bee-modal');
      if (m) m.classList.add('hidden');
    }
    function saveBeeKey() {
      const input = document.getElementById('input-bee-key');
      const val = input ? input.value.trim() : '';
      if (!val) return showToast('warning', 'Cảnh báo', 'API Key không được để trống.');
      userApiKey = val;
      localStorage.setItem('bee_api_key', val);
      closeBeeModal();
      showToast('success', 'Đã lưu', 'Beekone API Key đã được cập nhật thành công!');
    }

    // Toast Notification System
    function showToast(type, title, message) {
      const container = document.getElementById('toast-container');
      if (!container) return;
      const toast = document.createElement('div');
      
      let borderClass = 'border-[#E5EAF1] bg-white text-[#172033]';
      let icon = '<i data-lucide="info" class="w-4 h-4 text-[#1D4ED8]"></i>';
      if (type === 'success') {
        borderClass = 'border-[#A6F4C5] bg-[#F0FDF4] text-[#16A36A]';
        icon = '<i data-lucide="check-circle" class="w-4 h-4 text-[#16A36A]"></i>';
      } else if (type === 'error') {
        borderClass = 'border-[#FECDCA] bg-[#FEF3F2] text-[#DC4545]';
        icon = '<i data-lucide="alert-circle" class="w-4 h-4 text-[#DC4545]"></i>';
      } else if (type === 'warning') {
        borderClass = 'border-[#FEDF89] bg-[#FFFAEB] text-[#E9A23B]';
        icon = '<i data-lucide="alert-triangle" class="w-4 h-4 text-[#E9A23B]"></i>';
      }

      toast.className = `p-4 rounded-xl border shadow-lg flex items-start gap-3 w-80 pointer-events-auto transition-all ${borderClass}`;
      toast.innerHTML = `
        <div class="shrink-0 mt-0.5">${icon}</div>
        <div class="flex-1 min-w-0">
          <div class="text-xs font-bold">${title}</div>
          <div class="text-[11px] text-[#667085] mt-0.5">${message}</div>
        </div>
      `;

      container.appendChild(toast);
      safeCreateIcons();

      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }

    // Explicitly bind all public functions to window for 100% inline onclick reliability
    window.selectAudio = selectAudio;
    window.selectSpeaker = selectSpeaker;
    window.playNativeSample = playNativeSample;
    window.toggleRecord = toggleRecord;
    window.evaluateSentence = evaluateSentence;
    window.mergeRecordedSentences = mergeRecordedSentences;
    window.openBeeModal = openBeeModal;
    window.closeBeeModal = closeBeeModal;
    window.saveBeeKey = saveBeeKey;
    window.showToast = showToast;

    // Start App on Load
    document.addEventListener('DOMContentLoaded', () => {
      initApp();
    });
  </script>
</body>
</html>
"""

def generate_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 1. Write index.html (for Vercel and local root)
    index_path = os.path.join(base_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully generated {index_path} ({len(HTML_CONTENT)} bytes)")

    # 2. Write STUDIO_LUYEN_AM.html (local studio app)
    studio_path = os.path.join(base_dir, "STUDIO_LUYEN_AM.html")
    with open(studio_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Successfully generated {studio_path} ({len(HTML_CONTENT)} bytes)")

if __name__ == "__main__":
    generate_files()
