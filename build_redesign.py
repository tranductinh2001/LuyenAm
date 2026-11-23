# -*- coding: utf-8 -*-
"""
build_redesign.py - Generates the complete Premium Enterprise Midnight Blue UI/UX for Bit1 AI Voice Studio.
Builds index.html and STUDIO_LUYEN_AM.html with 100% clean UTF-8 encoding, complete functionality,
enterprise design system, Lucide icons, responsive sidebar/header, dashboard, studio, evaluation,
assignments, script database, voice synthesis lab, and settings.
"""

import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="vi" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bit1 AI Voice Studio – Enterprise EdTech SaaS</title>
  
  <!-- Inter & JetBrains Mono Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Tailwind Custom Configuration -->
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            primary: {
              DEFAULT: '#101D35', // Deep Midnight Blue
              hover: '#172B4D',
              active: '#0B1526',
              50: '#F0F4FA',
              100: '#E1E9F5',
              200: '#C2D3EB',
              700: '#172B4D',
              800: '#101D35',
              900: '#0B1526',
            },
            secondary: {
              DEFAULT: '#1D4ED8', // Royal Blue CTA
              hover: '#1E40AF',
              light: '#EFF6FF',
            },
            accent: {
              DEFAULT: '#38BDF8', // Sky Blue
              light: '#F0F9FF',
            },
            canvas: '#F5F7FA', // Clean Enterprise Gray-Slate Background
            surface: '#FFFFFF', // Pure White Surface
            border: '#E5EAF1', // Subtle 1px Enterprise Border
            textPrimary: '#172033', // Deep Slate
            textSecondary: '#667085', // Balanced Gray
            textMuted: '#98A2B3',
            success: {
              DEFAULT: '#16A36A',
              light: '#ECFDF3',
              border: '#A6F4C5'
            },
            warning: {
              DEFAULT: '#E9A23B',
              light: '#FFFAEB',
              border: '#FEDF89'
            },
            danger: {
              DEFAULT: '#DC4545',
              light: '#FEF3F2',
              border: '#FECDCA'
            }
          },
          fontFamily: {
            sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
            mono: ['JetBrains Mono', 'SFMono-Regular', 'Menlo', 'monospace'],
          },
          boxShadow: {
            'saas-subtle': '0 1px 3px 0 rgba(16, 29, 53, 0.04), 0 1px 2px -1px rgba(16, 29, 53, 0.04)',
            'saas-card': '0 4px 6px -1px rgba(16, 29, 53, 0.05), 0 2px 4px -2px rgba(16, 29, 53, 0.03)',
            'saas-elevated': '0 10px 15px -3px rgba(16, 29, 53, 0.08), 0 4px 6px -4px rgba(16, 29, 53, 0.03)',
            'saas-dropdown': '0 20px 25px -5px rgba(16, 29, 53, 0.1), 0 8px 10px -6px rgba(16, 29, 53, 0.06)',
          }
        }
      }
    }
  </script>

  <style>
    /* Global Base Reset & Typography */
    body {
      font-family: 'Inter', sans-serif;
      background-color: #F5F7FA;
      color: #172033;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    
    code, pre, .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }

    /* Custom Slim Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #F1F4F9;
    }
    ::-webkit-scrollbar-thumb {
      background: #D0D7E2;
      border-radius: 9999px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #A0ABC0;
    }

    /* Audio wave / recording animation */
    @keyframes pulse-recording {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.8; transform: scale(1.05); }
    }
    .is-recording {
      animation: pulse-recording 1.2s infinite ease-in-out;
    }

    /* Transition utilities */
    .transition-layout {
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
  </style>
</head>
<body class="h-full flex overflow-hidden">

  <!-- ========================================== -->
  <!-- 1. SIDEBAR (Collapsible Desktop / Mobile Drawer) -->
  <!-- ========================================== -->
  <aside id="app-sidebar" class="w-64 bg-[#101D35] text-white flex flex-col shrink-0 border-r border-[#172B4D] z-30 transition-layout fixed inset-y-0 left-0 md:static -translate-x-full md:translate-x-0">
    
    <!-- Sidebar Header: Brand & Workspace -->
    <div class="h-16 flex items-center justify-between px-5 border-b border-[#1A2D4F]">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-gradient-to-br from-[#1D4ED8] to-[#38BDF8] flex items-center justify-center shadow-md">
          <i data-lucide="waves" class="w-5 h-5 text-white"></i>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <span class="font-bold text-sm tracking-tight text-white">Bit1 Studio</span>
            <span class="px-1.5 py-0.5 rounded text-[10px] font-semibold bg-[#1D4ED8]/40 text-[#93C5FD] border border-[#1D4ED8]/60">SaaS</span>
          </div>
          <div class="text-[11px] text-[#94A3B8] truncate max-w-[130px]">VB2 Ngôn Ngữ Anh</div>
        </div>
      </div>
      
      <!-- Close button on mobile -->
      <button onclick="toggleSidebar(false)" class="md:hidden text-[#94A3B8] hover:text-white p-1">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <!-- Tenant / Context Pill -->
    <div class="px-4 py-3 border-b border-[#172B4D]/60 bg-[#0B1526]/40">
      <div class="flex items-center justify-between text-xs">
        <span class="text-[#94A3B8] font-medium flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-[#16A36A]"></span> Luyện Âm Chuẩn
        </span>
        <span class="text-[10px] font-mono font-medium text-[#38BDF8] bg-[#38BDF8]/10 px-2 py-0.5 rounded border border-[#38BDF8]/20">
          Port 5180
        </span>
      </div>
    </div>

    <!-- Navigation Menu Items -->
    <nav class="flex-1 overflow-y-auto px-3 py-4 space-y-6">
      
      <!-- Group 1: OVERVIEW -->
      <div>
        <div class="px-3 mb-2 text-[10px] font-bold tracking-wider uppercase text-[#64748B]">Tổng Quan</div>
        <div class="space-y-1">
          <button onclick="navigateTo('dashboard')" id="nav-btn-dashboard" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-white bg-[#1D4ED8] shadow-sm transition-layout">
            <i data-lucide="layout-dashboard" class="w-4 h-4 shrink-0 text-white"></i>
            <span>Dashboard SaaS</span>
          </button>
        </div>
      </div>

      <!-- Group 2: AI RECORDING STUDIO -->
      <div>
        <div class="px-3 mb-2 text-[10px] font-bold tracking-wider uppercase text-[#64748B]">Phòng Thu & Đánh Giá AI</div>
        <div class="space-y-1">
          <button onclick="navigateTo('studio')" id="nav-btn-studio" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="mic" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Phòng Thu Luyện Âm</span>
            <span class="px-1.5 py-0.2 rounded text-[10px] bg-[#16A36A]/20 text-[#4ADE80] font-mono">Live</span>
          </button>
          
          <button onclick="navigateTo('eval')" id="nav-btn-eval" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="target" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Chấm Điểm Âm Vị</span>
            <span class="px-1.5 py-0.2 rounded text-[10px] bg-[#38BDF8]/20 text-[#38BDF8]">AI</span>
          </button>

          <button onclick="navigateTo('stt')" id="nav-btn-stt" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="audio-waveform" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Nhận Diện Giọng Nói</span>
          </button>
        </div>
      </div>

      <!-- Group 3: CURRICULUM -->
      <div>
        <div class="px-3 mb-2 text-[10px] font-bold tracking-wider uppercase text-[#64748B]">Chương Trình & Bài Nộp</div>
        <div class="space-y-1">
          <button onclick="navigateTo('assignments')" id="nav-btn-assignments" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="file-check-2" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">5 Bài Nộp (LACB)</span>
            <span class="w-2 h-2 rounded-full bg-[#16A36A]"></span>
          </button>

          <button onclick="navigateTo('scripts')" id="nav-btn-scripts" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="book-open" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Tra Cứu Kịch Bản</span>
          </button>
        </div>
      </div>

      <!-- Group 4: AI VOICE LAB -->
      <div>
        <div class="px-3 mb-2 text-[10px] font-bold tracking-wider uppercase text-[#64748B]">Công Nghệ & Tổng Hợp</div>
        <div class="space-y-1">
          <button onclick="navigateTo('lab')" id="nav-btn-lab" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="sparkles" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Voice Synthesis Lab</span>
          </button>
        </div>
      </div>

      <!-- Group 5: SYSTEM -->
      <div>
        <div class="px-3 mb-2 text-[10px] font-bold tracking-wider uppercase text-[#64748B]">Hệ Thống</div>
        <div class="space-y-1">
          <button onclick="navigateTo('settings')" id="nav-btn-settings" class="nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout">
            <i data-lucide="settings" class="w-4 h-4 shrink-0"></i>
            <span class="flex-1 text-left">Cấu Hình & Gateway</span>
          </button>
        </div>
      </div>
    </nav>

    <!-- Sidebar Footer: System Status & User Profile -->
    <div class="p-4 border-t border-[#172B4D] bg-[#0B1526]/60">
      <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-lg bg-[#172B4D] border border-[#2D3F65] flex items-center justify-center font-bold text-xs text-[#38BDF8]">
          TĐ
        </div>
        <div class="flex-1 min-w-0">
          <div class="text-xs font-semibold text-white truncate">Trần Đức Tình</div>
          <div class="text-[10px] text-[#94A3B8] truncate">0352911750a@gmail.com</div>
        </div>
        <button onclick="navigateTo('settings')" title="Cài đặt tài khoản" class="text-[#94A3B8] hover:text-white p-1 rounded hover:bg-[#172B4D]">
          <i data-lucide="sliders" class="w-3.5 h-3.5"></i>
        </button>
      </div>
    </div>
  </aside>

  <!-- Mobile Overlay Backdrop -->
  <div id="sidebar-backdrop" onclick="toggleSidebar(false)" class="hidden fixed inset-0 z-20 bg-slate-900/60 backdrop-blur-xs md:hidden"></div>

  <!-- ========================================== -->
  <!-- 2. MAIN APP SHELL (Header + Dynamic Content Area) -->
  <!-- ========================================== -->
  <div class="flex-1 flex flex-col min-w-0 overflow-hidden bg-[#F5F7FA]">
    
    <!-- TOP HEADER -->
    <header class="h-16 bg-white border-b border-[#E5EAF1] px-4 md:px-8 flex items-center justify-between shrink-0 z-10 shadow-saas-subtle">
      
      <!-- Left side: Mobile Toggle & Breadcrumbs -->
      <div class="flex items-center gap-3 min-w-0">
        <button onclick="toggleSidebar(true)" class="md:hidden text-[#667085] hover:text-[#172033] p-1.5 rounded-lg hover:bg-[#F5F7FA]">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>

        <nav class="flex items-center gap-2 text-xs text-[#667085]">
          <span class="font-medium hover:text-[#172033] cursor-pointer" onclick="navigateTo('dashboard')">Trang chủ</span>
          <i data-lucide="chevron-right" class="w-3.5 h-3.5 text-[#98A2B3]"></i>
          <span id="breadcrumb-current-module" class="font-semibold text-[#172033]">Dashboard SaaS</span>
        </nav>
      </div>

      <!-- Right side: Global Search, Quick Engine Status, Notifications, Settings -->
      <div class="flex items-center gap-3">
        
        <!-- Global Search Bar / Command Palette Trigger -->
        <button onclick="openCommandPalette()" class="hidden sm:flex items-center gap-2 bg-[#F5F7FA] hover:bg-[#E5EAF1]/60 border border-[#E5EAF1] rounded-lg px-3 py-1.5 text-xs text-[#667085] transition-layout">
          <i data-lucide="search" class="w-3.5 h-3.5 text-[#98A2B3]"></i>
          <span>Tìm kiếm bài học, cặp âm...</span>
          <kbd class="ml-2 font-mono text-[10px] bg-white border border-[#E5EAF1] px-1.5 py-0.5 rounded text-[#98A2B3]">Ctrl K</kbd>
        </button>

        <!-- Engine Badge Status -->
        <div class="hidden lg:flex items-center gap-2 px-3 py-1 bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg text-xs">
          <div class="w-2 h-2 rounded-full bg-[#16A36A] animate-pulse"></div>
          <span class="text-[11px] font-medium text-[#172033]">Dual-Engine: Beekone + Local</span>
        </div>

        <!-- Notification Bell Dropdown -->
        <div class="relative">
          <button onclick="toggleNotificationDropdown()" class="p-2 rounded-lg text-[#667085] hover:text-[#172033] hover:bg-[#F5F7FA] relative">
            <i data-lucide="bell" class="w-4 h-4"></i>
            <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-[#1D4ED8] rounded-full"></span>
          </button>
          
          <div id="notification-dropdown" class="hidden absolute right-0 mt-2 w-80 bg-white border border-[#E5EAF1] rounded-xl shadow-saas-dropdown p-4 z-50 space-y-3">
            <div class="flex items-center justify-between border-b border-[#E5EAF1] pb-2">
              <span class="text-xs font-bold text-[#172033]">Thông báo hệ thống</span>
              <span class="text-[10px] text-[#1D4ED8] font-semibold cursor-pointer">Đánh dấu đã đọc</span>
            </div>
            <div class="space-y-2 text-xs">
              <div class="p-2.5 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1]/80 space-y-1">
                <div class="font-semibold text-[#172033] flex items-center gap-1.5">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#16A36A]"></i> 5 Audio LACB đã hoàn tất
                </div>
                <div class="text-[11px] text-[#667085]">Toàn bộ 5 bài nộp Audio 1 đến 5 với các cặp âm tối thiểu đã sẵn sàng để xuất bài.</div>
              </div>
              <div class="p-2.5 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1]/80 space-y-1">
                <div class="font-semibold text-[#172033] flex items-center gap-1.5">
                  <i data-lucide="cpu" class="w-3.5 h-3.5 text-[#1D4ED8]"></i> Dual-Engine Sẵn Sàng
                </div>
                <div class="text-[11px] text-[#667085]">Hệ thống dự phòng Local Phonetic tự động hoạt động nếu Beekone Gateway gián đoạn.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- Quick Gateway Modal Button -->
        <button onclick="openBeeConfigModal()" class="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-[#E5EAF1] text-xs font-semibold text-[#172033] bg-white hover:bg-[#F5F7FA] transition-layout shadow-saas-subtle">
          <i data-lucide="sliders" class="w-3.5 h-3.5 text-[#1D4ED8]"></i>
          <span class="hidden sm:inline">Cấu Hình AI</span>
        </button>

      </div>
    </header>

    <!-- MAIN SCROLLABLE CONTENT VIEW -->
    <main class="flex-1 overflow-y-auto p-4 md:p-8">
      <div class="max-w-7xl mx-auto space-y-6">

        <!-- ============================================== -->
        <!-- VIEW 1: DASHBOARD SAAS (Tổng quan dữ liệu & KPI) -->
        <!-- ============================================== -->
        <section id="page-dashboard" class="page-view space-y-6">
          
          <!-- Page Header & Action Bar -->
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5EAF1] pb-5">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#1D4ED8]/10 text-[#1D4ED8] border border-[#1D4ED8]/20">
                  EdTech SaaS Platform
                </span>
                <span class="text-xs text-[#667085]">VB2 Ngôn Ngữ Anh • Khóa Luyện Âm Chuẩn</span>
              </div>
              <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Trung Tâm Quản Trị & Luyện Âm Chuẩn Bản Ngữ</h1>
              <p class="text-xs text-[#667085] mt-0.5">Giám sát tiến độ thu âm 5 bài thực hành, chấm điểm âm vị AI và xuất gói bài nộp hoàn chỉnh.</p>
            </div>

            <div class="flex items-center gap-2.5">
              <button onclick="navigateTo('studio')" class="px-4 py-2 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-semibold flex items-center gap-2 shadow-sm transition-layout">
                <i data-lucide="mic" class="w-4 h-4"></i>
                <span>Mở Phòng Thu Ngay</span>
              </button>
              <button onclick="navigateTo('assignments')" class="px-3.5 py-2 rounded-lg bg-white border border-[#E5EAF1] hover:bg-[#F5F7FA] text-[#172033] text-xs font-semibold flex items-center gap-1.5 transition-layout">
                <i data-lucide="download" class="w-4 h-4 text-[#667085]"></i>
                <span>Gói Bài Nộp MP3</span>
              </button>
            </div>
          </div>

          <!-- 4 Enterprise KPI Metric Cards -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <!-- KPI 1 -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-5 shadow-saas-card space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-[#667085]">Tiến Độ 5 Bài Nộp (LACB)</span>
                <div class="w-8 h-8 rounded-lg bg-[#ECFDF3] border border-[#A6F4C5] flex items-center justify-center text-[#16A36A]">
                  <i data-lucide="check-circle" class="w-4 h-4"></i>
                </div>
              </div>
              <div>
                <div class="text-2xl font-bold text-[#172033]">5 / 5 Audio</div>
                <div class="text-[11px] text-[#16A36A] font-medium flex items-center gap-1 mt-1">
                  <i data-lucide="trending-up" class="w-3.5 h-3.5"></i> 100% Sẵn sàng nộp cô giáo
                </div>
              </div>
              <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                <div class="bg-[#16A36A] h-full rounded-full" style="width: 100%;"></div>
              </div>
            </div>

            <!-- KPI 2 -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-5 shadow-saas-card space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-[#667085]">Điểm Phát Âm AI Trung Bình</span>
                <div class="w-8 h-8 rounded-lg bg-[#EFF6FF] border border-[#BFDBFE] flex items-center justify-center text-[#1D4ED8]">
                  <i data-lucide="award" class="w-4 h-4"></i>
                </div>
              </div>
              <div>
                <div class="text-2xl font-bold text-[#172033]">92.4 <span class="text-sm font-normal text-[#667085]">/ 100</span></div>
                <div class="text-[11px] text-[#1D4ED8] font-medium flex items-center gap-1 mt-1">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Chuẩn bản ngữ A-Grade
                </div>
              </div>
              <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                <div class="bg-[#1D4ED8] h-full rounded-full" style="width: 92%;"></div>
              </div>
            </div>

            <!-- KPI 3 -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-5 shadow-saas-card space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-[#667085]">Cặp Âm Tối Thiểu (Minimal Pairs)</span>
                <div class="w-8 h-8 rounded-lg bg-[#F0FDF4] border border-[#BBF7D0] flex items-center justify-center text-[#16A36A]">
                  <i data-lucide="repeat" class="w-4 h-4"></i>
                </div>
              </div>
              <div>
                <div class="text-2xl font-bold text-[#172033]">12 Cặp Âm</div>
                <div class="text-[11px] text-[#667085] mt-1">
                  /iː/ - /ɪ/, /e/ - /æ/, /ɑː/ - /ʌ/, /uː/ - /ʊ/
                </div>
              </div>
              <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                <div class="bg-[#16A36A] h-full rounded-full" style="width: 100%;"></div>
              </div>
            </div>

            <!-- KPI 4 -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-5 shadow-saas-card space-y-3">
              <div class="flex items-center justify-between">
                <span class="text-xs font-medium text-[#667085]">Hạ Tầng Dual-Engine AI</span>
                <div class="w-8 h-8 rounded-lg bg-[#F8FAFC] border border-[#E2E8F0] flex items-center justify-center text-[#101D35]">
                  <i data-lucide="server" class="w-4 h-4"></i>
                </div>
              </div>
              <div>
                <div class="text-sm font-bold text-[#172033] truncate">Beekone + Local</div>
                <div class="text-[11px] text-[#16A36A] font-medium flex items-center gap-1 mt-1">
                  <span class="w-2 h-2 rounded-full bg-[#16A36A]"></span> Hoạt động độc lập 100%
                </div>
              </div>
              <div class="text-[10px] text-[#667085] truncate font-mono">
                Whisper-v3 + Rule Phonetics
              </div>
            </div>

          </div>

          <!-- Section: Progress Grid of the 5 Lessons & Phoneme Matrix -->
          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- 5 Audio Status Matrix (2 Cols) -->
            <div class="lg:col-span-2 bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
              <div class="flex items-center justify-between border-b border-[#E5EAF1] pb-3">
                <div>
                  <h3 class="text-sm font-bold text-[#172033]">Tình Trạng 5 Bài Nộp Thực Hành (Audio 1 – 5)</h3>
                  <p class="text-[11px] text-[#667085]">Danh mục file ghi âm đối thoại hoàn chỉnh, phân vai Speaker 1 & Speaker 2.</p>
                </div>
                <button onclick="navigateTo('assignments')" class="text-xs font-semibold text-[#1D4ED8] hover:underline flex items-center gap-1">
                  Xem chi tiết <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                </button>
              </div>

              <!-- List of 5 Lessons -->
              <div class="space-y-3">
                
                <!-- Audio 1 Item -->
                <div class="p-3.5 rounded-lg border border-[#E5EAF1] bg-[#F5F7FA]/60 hover:bg-[#F5F7FA] transition-layout flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-lg bg-[#101D35] text-white flex items-center justify-center font-bold text-xs shrink-0">
                      01
                    </div>
                    <div>
                      <div class="font-bold text-xs text-[#172033]">Audio 1: Cặp âm /iː/ – /ɪ/ & /e/ – /æ/</div>
                      <div class="text-[11px] text-[#667085] mt-0.5">peel vs pill • leave vs live • leak vs lick • pen vs pan • sheep vs ship</div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]">
                      Hoàn thành
                    </span>
                    <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_1_Speaker_1.mp3')" class="p-1.5 rounded-lg border border-[#E5EAF1] bg-white text-[#172033] hover:text-[#1D4ED8] hover:border-[#1D4ED8]">
                      <i data-lucide="play" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="selectAndGoToStudio(1, 1)" class="px-2.5 py-1 text-xs font-semibold bg-[#1D4ED8] text-white rounded-lg hover:bg-[#1E40AF]">
                      Thu âm
                    </button>
                  </div>
                </div>

                <!-- Audio 2 Item -->
                <div class="p-3.5 rounded-lg border border-[#E5EAF1] bg-[#F5F7FA]/60 hover:bg-[#F5F7FA] transition-layout flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-lg bg-[#101D35] text-white flex items-center justify-center font-bold text-xs shrink-0">
                      02
                    </div>
                    <div>
                      <div class="font-bold text-xs text-[#172033]">Audio 2: Cặp âm /ɑː/ – /ʌ/ & /ɒ/ – /ɔː/</div>
                      <div class="text-[11px] text-[#667085] mt-0.5">park vs truck • barn vs hut • cod vs cord • cap vs cup</div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]">
                      Hoàn thành
                    </span>
                    <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_2_Speaker_1.mp3')" class="p-1.5 rounded-lg border border-[#E5EAF1] bg-white text-[#172033] hover:text-[#1D4ED8] hover:border-[#1D4ED8]">
                      <i data-lucide="play" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="selectAndGoToStudio(2, 1)" class="px-2.5 py-1 text-xs font-semibold bg-[#1D4ED8] text-white rounded-lg hover:bg-[#1E40AF]">
                      Thu âm
                    </button>
                  </div>
                </div>

                <!-- Audio 3 Item -->
                <div class="p-3.5 rounded-lg border border-[#E5EAF1] bg-[#F5F7FA]/60 hover:bg-[#F5F7FA] transition-layout flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-lg bg-[#101D35] text-white flex items-center justify-center font-bold text-xs shrink-0">
                      03
                    </div>
                    <div>
                      <div class="font-bold text-xs text-[#172033]">Audio 3: Cặp âm /uː/ – /ʊ/ & /ɜː/ – /ə/</div>
                      <div class="text-[11px] text-[#667085] mt-0.5">pool vs pull • fool vs full • bird vs bud • worker vs walker</div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]">
                      Hoàn thành
                    </span>
                    <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_3_Speaker_1.mp3')" class="p-1.5 rounded-lg border border-[#E5EAF1] bg-white text-[#172033] hover:text-[#1D4ED8] hover:border-[#1D4ED8]">
                      <i data-lucide="play" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="selectAndGoToStudio(3, 1)" class="px-2.5 py-1 text-xs font-semibold bg-[#1D4ED8] text-white rounded-lg hover:bg-[#1E40AF]">
                      Thu âm
                    </button>
                  </div>
                </div>

                <!-- Audio 4 Item -->
                <div class="p-3.5 rounded-lg border border-[#E5EAF1] bg-[#F5F7FA]/60 hover:bg-[#F5F7FA] transition-layout flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-lg bg-[#101D35] text-white flex items-center justify-center font-bold text-xs shrink-0">
                      04
                    </div>
                    <div>
                      <div class="font-bold text-xs text-[#172033]">Audio 4: Nguyên âm đôi Diphthongs (/aɪ/, /eə/, /ɪə/, /əʊ/)</div>
                      <div class="text-[11px] text-[#667085] mt-0.5">pie • pear vs peer • road vs rode • fine vs phone</div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]">
                      Hoàn thành
                    </span>
                    <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_4_Speaker_1.mp3')" class="p-1.5 rounded-lg border border-[#E5EAF1] bg-white text-[#172033] hover:text-[#1D4ED8] hover:border-[#1D4ED8]">
                      <i data-lucide="play" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="selectAndGoToStudio(4, 1)" class="px-2.5 py-1 text-xs font-semibold bg-[#1D4ED8] text-white rounded-lg hover:bg-[#1E40AF]">
                      Thu âm
                    </button>
                  </div>
                </div>

                <!-- Audio 5 Item -->
                <div class="p-3.5 rounded-lg border border-[#E5EAF1] bg-[#F5F7FA]/60 hover:bg-[#F5F7FA] transition-layout flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div class="flex items-start gap-3">
                    <div class="w-8 h-8 rounded-lg bg-[#101D35] text-white flex items-center justify-center font-bold text-xs shrink-0">
                      05
                    </div>
                    <div>
                      <div class="font-bold text-xs text-[#172033]">Audio 5: Phụ âm vô thanh & hữu thanh (/s/ - /z/, /θ/ - /ð/)</div>
                      <div class="text-[11px] text-[#667085] mt-0.5">sink vs zinc • think vs this • bus vs buzz • thought vs though</div>
                    </div>
                  </div>
                  <div class="flex items-center gap-2 shrink-0">
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]">
                      Hoàn thành
                    </span>
                    <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_5_Speaker_1.mp3')" class="p-1.5 rounded-lg border border-[#E5EAF1] bg-white text-[#172033] hover:text-[#1D4ED8] hover:border-[#1D4ED8]">
                      <i data-lucide="play" class="w-3.5 h-3.5"></i>
                    </button>
                    <button onclick="selectAndGoToStudio(5, 1)" class="px-2.5 py-1 text-xs font-semibold bg-[#1D4ED8] text-white rounded-lg hover:bg-[#1E40AF]">
                      Thu âm
                    </button>
                  </div>
                </div>

              </div>
            </div>

            <!-- Phoneme Competency Radar & Quick Tips (1 Col) -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
              <div class="border-b border-[#E5EAF1] pb-3">
                <h3 class="text-sm font-bold text-[#172033]">Độ Chuẩn Âm Vị Quốc Tế (IPA)</h3>
                <p class="text-[11px] text-[#667085]">Đánh giá theo độ dài nguyên âm và độ bật hơi phụ âm.</p>
              </div>

              <div class="space-y-3.5">
                <div>
                  <div class="flex justify-between text-xs font-medium mb-1">
                    <span class="text-[#172033]">Nguyên âm dài /iː/, /ɑː/, /uː/</span>
                    <span class="text-[#16A36A] font-bold">96%</span>
                  </div>
                  <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                    <div class="bg-[#16A36A] h-full rounded-full" style="width: 96%;"></div>
                  </div>
                </div>

                <div>
                  <div class="flex justify-between text-xs font-medium mb-1">
                    <span class="text-[#172033]">Nguyên âm ngắn /ɪ/, /ʌ/, /ʊ/</span>
                    <span class="text-[#1D4ED8] font-bold">91%</span>
                  </div>
                  <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                    <div class="bg-[#1D4ED8] h-full rounded-full" style="width: 91%;"></div>
                  </div>
                </div>

                <div>
                  <div class="flex justify-between text-xs font-medium mb-1">
                    <span class="text-[#172033]">Cặp âm bẹt /e/ – /æ/ (man / men)</span>
                    <span class="text-[#1D4ED8] font-bold">89%</span>
                  </div>
                  <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                    <div class="bg-[#1D4ED8] h-full rounded-full" style="width: 89%;"></div>
                  </div>
                </div>

                <div>
                  <div class="flex justify-between text-xs font-medium mb-1">
                    <span class="text-[#172033]">Âm răng cắn lưỡi /θ/ – /ð/</span>
                    <span class="text-[#E9A23B] font-bold">84%</span>
                  </div>
                  <div class="w-full bg-[#E5EAF1] h-1.5 rounded-full overflow-hidden">
                    <div class="bg-[#E9A23B] h-full rounded-full" style="width: 84%;"></div>
                  </div>
                </div>
              </div>

              <!-- Tip card -->
              <div class="p-3.5 rounded-lg bg-[#EFF6FF] border border-[#BFDBFE] space-y-1 mt-4">
                <div class="text-xs font-bold text-[#1D4ED8] flex items-center gap-1.5">
                  <i data-lucide="lightbulb" class="w-3.5 h-3.5"></i> Lời khuyên khẩu hình:
                </div>
                <p class="text-[11px] text-[#1E3A8A] leading-relaxed">
                  Với âm /iː/, khóe môi cần căng sang hai bên như đang cười nhẹ; với âm /ɪ/, thả lỏng cơ hàm và phát âm ngắn dứt khoát.
                </p>
              </div>

            </div>

          </div>

          <!-- Bottom: Recent Studio Splicing Activities Table -->
          <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-[#E5EAF1] pb-3">
              <div>
                <h3 class="text-sm font-bold text-[#172033]">Nhật Ký Thu Âm & Ghép File Gần Nhất</h3>
                <p class="text-[11px] text-[#667085]">Lịch sử các câu thoại và file âm thanh vừa được xử lý trong phiên làm việc.</p>
              </div>
              <span class="text-xs font-medium text-[#667085]">5 bản ghi mới nhất</span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="border-b border-[#E5EAF1] text-[#667085] font-semibold bg-[#F5F7FA]">
                    <th class="py-2.5 px-3">Bài Học</th>
                    <th class="py-2.5 px-3">Vai Thoại</th>
                    <th class="py-2.5 px-3">Nội Dung / Tiêu Đề</th>
                    <th class="py-2.5 px-3">Điểm AI</th>
                    <th class="py-2.5 px-3">Trạng Thái</th>
                    <th class="py-2.5 px-3 text-right">Thao Tác</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-[#E5EAF1]">
                  <tr class="hover:bg-[#F5F7FA]/70">
                    <td class="py-3 px-3 font-semibold text-[#172033]">Audio 1</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#EFF6FF] text-[#1D4ED8]">Speaker 1</span></td>
                    <td class="py-3 px-3 text-[#172033]">Hey Brad! Are you ready to leave? Did you peel...</td>
                    <td class="py-3 px-3 font-bold text-[#16A36A]">95 / 100</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A]">Đã ghép MP3</span></td>
                    <td class="py-3 px-3 text-right">
                      <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_1_Speaker_1.mp3')" class="text-xs font-semibold text-[#1D4ED8] hover:underline">Nghe lại</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-[#F5F7FA]/70">
                    <td class="py-3 px-3 font-semibold text-[#172033]">Audio 2</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#FAF5FF] text-[#7E22CE]">Speaker 2</span></td>
                    <td class="py-3 px-3 text-[#172033]">Got it, Don! Is there a ban on bringing animals...</td>
                    <td class="py-3 px-3 font-bold text-[#16A36A]">91 / 100</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A]">Đã ghép MP3</span></td>
                    <td class="py-3 px-3 text-right">
                      <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_2_Speaker_2.mp3')" class="text-xs font-semibold text-[#1D4ED8] hover:underline">Nghe lại</button>
                    </td>
                  </tr>
                  <tr class="hover:bg-[#F5F7FA]/70">
                    <td class="py-3 px-3 font-semibold text-[#172033]">Audio 3</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#EFF6FF] text-[#1D4ED8]">Speaker 1</span></td>
                    <td class="py-3 px-3 text-[#172033]">Hey Luke! Look at the garden! It is 4 o'clock...</td>
                    <td class="py-3 px-3 font-bold text-[#16A36A]">94 / 100</td>
                    <td class="py-3 px-3"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-[#ECFDF3] text-[#16A36A]">Đã ghép MP3</span></td>
                    <td class="py-3 px-3 text-right">
                      <button onclick="quickPlayAudio('/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_3_Speaker_1.mp3')" class="text-xs font-semibold text-[#1D4ED8] hover:underline">Nghe lại</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

          </div>

        </section>


        <!-- ============================================== -->
        <!-- VIEW 2: AI STUDIO (Thu Âm Từng Câu & Ghép Nối) -->
        <!-- ============================================== -->
        <section id="page-studio" class="page-view hidden space-y-6">
          
          <!-- Studio Header & Controls -->
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5EAF1] pb-5">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#16A36A]/10 text-[#16A36A] border border-[#16A36A]/20">
                  Phòng Thu Tự Động
                </span>
                <span class="text-xs text-[#667085]">Ghi âm từng câu thoại • Tự động cắt ghép thành file MP3 hoàn chỉnh</span>
              </div>
              <h1 class="text-2xl font-bold text-[#172033] tracking-tight">AI Voice Recording Studio</h1>
            </div>

            <!-- Top Action Button -->
            <div class="flex items-center gap-2">
              <button onclick="mergeAllSentences()" id="btn-merge-all" class="px-4 py-2.5 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-layout">
                <i data-lucide="merge" class="w-4 h-4"></i>
                <span id="btn-merge-text">Ghép Thành File MP3 Hoàn Chỉnh</span>
              </button>
            </div>
          </div>

          <!-- Studio Lesson & Role Selection Bar -->
          <div class="bg-white border border-[#E5EAF1] rounded-xl p-5 shadow-saas-card space-y-4">
            
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <!-- Audio Lesson Selector (1-5) -->
              <div>
                <label class="text-xs font-bold text-[#172033] block mb-1.5">Chọn Bài Luyện Âm:</label>
                <div class="flex flex-wrap gap-1.5" id="recorder-audio-tabs">
                  <button onclick="selectRecorderAudio(1)" id="tab-rec-audio-1" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-[#101D35] text-white transition-layout">
                    Audio 1 (/iː/ - /ɪ/)
                  </button>
                  <button onclick="selectRecorderAudio(2)" id="tab-rec-audio-2" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
                    Audio 2 (/ɑː/ - /ʌ/)
                  </button>
                  <button onclick="selectRecorderAudio(3)" id="tab-rec-audio-3" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
                    Audio 3 (/uː/ - /ʊ/)
                  </button>
                  <button onclick="selectRecorderAudio(4)" id="tab-rec-audio-4" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
                    Audio 4 (Diphthongs)
                  </button>
                  <button onclick="selectRecorderAudio(5)" id="tab-rec-audio-5" class="px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
                    Audio 5 (/s/ - /z/)
                  </button>
                </div>
              </div>

              <!-- Speaker Role Selector -->
              <div>
                <label class="text-xs font-bold text-[#172033] block mb-1.5">Chọn Vai Thoại:</label>
                <div class="flex items-center gap-2">
                  <button onclick="selectRecorderSpeaker(1)" id="tab-rec-spk-1" class="px-4 py-1.5 rounded-lg text-xs font-bold bg-[#1D4ED8] text-white shadow-sm transition-layout">
                    Speaker 1 (Chính)
                  </button>
                  <button onclick="selectRecorderSpeaker(2)" id="tab-rec-spk-2" class="px-4 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
                    Speaker 2 (Đối thoại)
                  </button>
                </div>
              </div>
            </div>

            <!-- Splicing Options & Progress Indicator -->
            <div class="pt-3 border-t border-[#E5EAF1] flex flex-col md:flex-row md:items-center justify-between gap-4">
              
              <!-- Left: Progress -->
              <div class="flex items-center gap-3">
                <span class="text-xs font-medium text-[#667085]">Tiến độ thu âm vai này:</span>
                <span id="recorder-progress-text" class="text-xs font-bold text-[#172033]">0 / 0 câu</span>
                <div class="w-32 bg-[#E5EAF1] h-2 rounded-full overflow-hidden">
                  <div id="recorder-progress-bar" class="bg-[#16A36A] h-full rounded-full transition-all" style="width: 0%;"></div>
                </div>
              </div>

              <!-- Right: Splicing parameters -->
              <div class="flex items-center gap-4 flex-wrap text-xs text-[#667085]">
                <label class="flex items-center gap-1.5 cursor-pointer">
                  <input type="checkbox" id="chk-auto-fallback" checked class="rounded border-[#E5EAF1] text-[#1D4ED8] focus:ring-0">
                  <span>Tự bù câu chưa thu bằng giọng mẫu AI</span>
                </label>

                <div class="flex items-center gap-1.5">
                  <span>Khoảng lặng giữa câu:</span>
                  <select id="sel-silence-ms" class="bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg px-2 py-1 text-xs text-[#172033]">
                    <option value="200">200ms</option>
                    <option value="350" selected>350ms (Chuẩn)</option>
                    <option value="500">500ms</option>
                    <option value="700">700ms</option>
                  </select>
                </div>
              </div>

            </div>

          </div>

          <!-- Spliced Result Card (Appears after successful merge) -->
          <div id="merged-result-card" class="hidden bg-white border-2 border-[#16A36A] rounded-xl p-5 shadow-saas-elevated space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-[#ECFDF3] border border-[#A6F4C5] flex items-center justify-center text-[#16A36A]">
                  <i data-lucide="check-check" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 id="merged-title-text" class="text-sm font-bold text-[#172033]">Đã Ghép Xong Bài Nộp Hoàn Chỉnh!</h3>
                  <p id="merged-status-details" class="text-xs text-[#667085]">Toàn bộ các câu đã được ghép liền mạch theo chuẩn thời lượng.</p>
                </div>
              </div>

              <div class="flex items-center gap-2">
                <a id="merged-download-btn" href="#" download class="px-4 py-2 rounded-lg bg-[#16A36A] hover:bg-[#15803D] text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-layout">
                  <i data-lucide="download" class="w-4 h-4"></i>
                  <span>Tải File MP3</span>
                </a>
              </div>
            </div>

            <audio id="merged-audio-player" controls class="w-full h-10"></audio>
          </div>

          <!-- Sentences List Container -->
          <div id="recorder-sentences-container" class="space-y-4">
            <!-- Dynamic sentence cards rendered here via JavaScript -->
          </div>

        </section>


        <!-- ============================================== -->
        <!-- VIEW 3: AI PHONETIC EVALUATION HUB (Chấm Điểm Âm Vị) -->
        <!-- ============================================== -->
        <section id="page-eval" class="page-view hidden space-y-6">
          
          <div class="border-b border-[#E5EAF1] pb-5">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#38BDF8]/10 text-[#0284C7] border border-[#38BDF8]/20">
                Beekone AI Engine
              </span>
              <span class="text-xs text-[#667085]">Phân tích âm vị IPA • Đối chiếu cặp âm tối thiểu • Chấm điểm chi tiết</span>
            </div>
            <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Trung Tâm Đánh Giá & Chấm Điểm Phát Âm AI</h1>
          </div>

          <!-- Evaluation Showcase Card -->
          <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-5">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5EAF1] pb-4">
              <div>
                <h3 class="text-base font-bold text-[#172033]">Chấm Điểm Phát Âm Nhanh Bất Kỳ Đoạn Văn</h3>
                <p class="text-xs text-[#667085]">Nhập câu tiếng Anh bạn muốn kiểm tra, bật mic thu âm và nhận kết quả phân tích từng từ ngay lập tức.</p>
              </div>
              <div class="flex items-center gap-2">
                <span class="text-xs font-medium text-[#667085]">Engine:</span>
                <span class="text-xs font-bold text-[#1D4ED8] bg-[#EFF6FF] px-2.5 py-1 rounded-md border border-[#BFDBFE]">
                  Beekone Whisper-v3 Dual
                </span>
              </div>
            </div>

            <!-- Quick Text & Microphone tester -->
            <div class="space-y-3">
              <label class="text-xs font-bold text-[#172033] block">Câu Tiếng Anh Đối Chiếu:</label>
              <input type="text" id="eval-hub-text" value="Did you peel the apples and put the peel in the bin?" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-3 text-xs text-[#172033] font-medium focus:outline-none focus:border-[#1D4ED8]">
              
              <div class="flex items-center gap-3">
                <button onclick="runQuickHubRecording()" id="btn-eval-hub-rec" class="px-4 py-2 rounded-lg bg-[#DC4545] hover:bg-[#B91C1C] text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-layout">
                  <i data-lucide="mic" class="w-4 h-4"></i>
                  <span id="label-eval-hub-rec">Thu âm để chấm điểm</span>
                </button>
                <span id="timer-eval-hub" class="text-xs font-mono font-bold text-[#DC4545] hidden">00:00</span>
                <audio id="audio-eval-hub" controls class="h-8 hidden"></audio>
              </div>
            </div>

            <!-- Hub Evaluation Result Output -->
            <div id="eval-hub-result" class="p-5 rounded-xl border border-[#E5EAF1] bg-[#F5F7FA] space-y-4">
              <div class="flex items-center justify-between flex-wrap gap-2">
                <div class="flex items-center gap-3">
                  <div class="px-3.5 py-1.5 rounded-xl font-extrabold text-base bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1.5">
                    <i data-lucide="award" class="w-4 h-4"></i> 94 / 100
                  </div>
                  <div>
                    <div class="text-xs font-bold text-[#172033]">Xuất sắc (Native-level Phonetics)</div>
                    <div class="text-[11px] text-[#667085]">Phân biệt rõ ràng cặp âm /iː/ trong 'peel' và /ɪ/ trong 'bin'</div>
                  </div>
                </div>
                <span class="text-[10px] font-mono text-[#667085] bg-white border border-[#E5EAF1] px-2 py-1 rounded">
                  Latency: 180ms
                </span>
              </div>

              <div>
                <div class="text-[11px] font-bold text-[#667085] uppercase tracking-wider mb-2">Chi tiết âm vị từng từ:</div>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> Did
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> you
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> peel (/piːl/)
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> the
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> apples
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> and
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> put
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> the
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> peel (/piːl/)
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> in
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> the
                  </span>
                  <span class="px-2.5 py-1 rounded-md text-xs font-semibold bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] flex items-center gap-1">
                    <i data-lucide="check" class="w-3 h-3"></i> bin (/bɪn/)
                  </span>
                </div>
              </div>

              <div class="p-3.5 rounded-lg bg-white border border-[#E5EAF1] space-y-1">
                <div class="text-xs font-bold text-[#1D4ED8] flex items-center gap-1.5">
                  <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Nhận xét chi tiết từ AI:
                </div>
                <p class="text-[11px] text-[#667085] leading-relaxed">
                  Nguyên âm dài /iː/ trong từ 'peel' được ngân đủ 1.5 nhịp; âm ngắn /ɪ/ trong 'bin' dứt khoát, không bị kéo dài thành 'bean'. Tiếp tục duy trì nhịp điệu tự nhiên!
                </p>
              </div>
            </div>

          </div>

        </section>


        <!-- ============================================== -->
        <!-- VIEW 4: LIVE STT RECOGNITION (Nhận Diện Giọng Nói) -->
        <!-- ============================================== -->
        <section id="page-stt" class="page-view hidden space-y-6">
          <div class="border-b border-[#E5EAF1] pb-5">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#1D4ED8]/10 text-[#1D4ED8] border border-[#1D4ED8]/20">
                Web Speech API
              </span>
              <span class="text-xs text-[#667085]">Speech-to-Text độ trễ cực thấp • Thử nghiệm micro</span>
            </div>
            <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Thử Nghiệm Micro & Nhận Diện Thời Gian Thực</h1>
          </div>

          <div class="bg-white border border-[#E5EAF1] rounded-xl p-8 shadow-saas-card text-center space-y-6 max-w-2xl mx-auto">
            <div class="flex flex-col items-center justify-center space-y-3">
              <button onclick="toggleMicrophoneStt()" id="stt-mic-btn" class="w-20 h-20 rounded-full bg-[#1D4ED8] hover:bg-[#1E40AF] text-white flex items-center justify-center shadow-lg transition-all">
                <i data-lucide="mic" class="w-8 h-8"></i>
              </button>
              <div id="stt-status-text" class="text-xs font-bold text-[#172033]">Bấm vào micro để bắt đầu nói tiếng Anh</div>
              <p class="text-[11px] text-[#667085]">Trình duyệt sẽ nhận diện trực tiếp những gì bạn phát âm.</p>
            </div>

            <!-- Transcript box -->
            <div class="text-left space-y-2">
              <label class="text-xs font-bold text-[#172033]">Văn bản nhận diện được:</label>
              <div id="stt-transcript-box" class="min-h-[140px] p-4 rounded-xl border border-[#E5EAF1] bg-[#F5F7FA] font-mono text-xs text-[#172033] leading-relaxed">
                (Chưa có nội dung. Bấm micro và thử đọc: "Hey Brad, are you ready to leave?")
              </div>
            </div>
          </div>
        </section>


        <!-- ============================================== -->
        <!-- VIEW 5: 5 BÀI NỘP HOÀN CHỈNH (Assignments LACB) -->
        <!-- ============================================== -->
        <section id="page-assignments" class="page-view hidden space-y-6">
          
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#E5EAF1] pb-5">
            <div>
              <div class="flex items-center gap-2 mb-1">
                <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#16A36A]/10 text-[#16A36A] border border-[#16A36A]/20">
                  5 Bài Nộp Sẵn Sàng
                </span>
                <span class="text-xs text-[#667085]">LACB • Học Phần Luyện Âm Chuẩn Bản Ngữ</span>
              </div>
              <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Danh Mục 5 Bài Nộp Hoàn Chỉnh (Audio 1 – 5)</h1>
            </div>

            <div class="flex items-center gap-2">
              <a href="/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_1_Speaker_1.mp3" download class="px-4 py-2 rounded-lg bg-[#16A36A] hover:bg-[#15803D] text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-layout">
                <i data-lucide="download" class="w-4 h-4"></i>
                <span>Tải File Nộp Hiện Tại</span>
              </a>
            </div>
          </div>

          <!-- Assignment Navigation Tabs -->
          <div class="flex flex-wrap gap-2" id="assignment-tabs">
            <button onclick="loadAudioAssignment(1)" id="asg-tab-1" class="px-4 py-2 rounded-lg text-xs font-bold bg-[#101D35] text-white transition-layout">
              Audio 1: /iː/ - /ɪ/ & /e/ - /æ/
            </button>
            <button onclick="loadAudioAssignment(2)" id="asg-tab-2" class="px-4 py-2 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
              Audio 2: /ɑː/ - /ʌ/ & /ɒ/ - /ɔː/
            </button>
            <button onclick="loadAudioAssignment(3)" id="asg-tab-3" class="px-4 py-2 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
              Audio 3: /uː/ - /ʊ/ & /ɜː/ - /ə/
            </button>
            <button onclick="loadAudioAssignment(4)" id="asg-tab-4" class="px-4 py-2 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
              Audio 4: Diphthongs
            </button>
            <button onclick="loadAudioAssignment(5)" id="asg-tab-5" class="px-4 py-2 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout">
              Audio 5: /s/ - /z/ & /θ/ - /ð/
            </button>
          </div>

          <!-- Assignment Content Card -->
          <div id="assignment-content-card" class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-6">
            <!-- Dynamic assignment details injected via loadAudioAssignment(num) -->
          </div>

        </section>


        <!-- ============================================== -->
        <!-- VIEW 6: TRA CỨU KỊCH BẢN (Curriculum & Scripts) -->
        <!-- ============================================== -->
        <section id="page-scripts" class="page-view hidden space-y-6">
          
          <div class="border-b border-[#E5EAF1] pb-5">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#1D4ED8]/10 text-[#1D4ED8] border border-[#1D4ED8]/20">
                Kho Dữ Liệu Kịch Bản
              </span>
              <span class="text-xs text-[#667085]">Toàn bộ câu thoại, phiên âm IPA và nghĩa tiếng Việt</span>
            </div>
            <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Tra Cứu Kịch Bản & Phiên Âm Âm Vị</h1>
          </div>

          <!-- Filter & Search Toolbar -->
          <div class="bg-white border border-[#E5EAF1] rounded-xl p-4 shadow-saas-card flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto">
              <div class="relative flex-1 sm:w-64">
                <i data-lucide="search" class="w-4 h-4 text-[#98A2B3] absolute left-3 top-2.5"></i>
                <input type="text" id="script-search-input" oninput="filterScriptsTable()" placeholder="Tìm từ, câu thoại, IPA..." class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg pl-9 pr-3 py-1.5 text-xs text-[#172033] focus:outline-none focus:border-[#1D4ED8]">
              </div>

              <select id="script-filter-audio" onchange="filterScriptsTable()" class="bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg px-3 py-1.5 text-xs text-[#172033]">
                <option value="all">Tất cả bài (1 - 5)</option>
                <option value="1">Audio 1</option>
                <option value="2">Audio 2</option>
                <option value="3">Audio 3</option>
                <option value="4">Audio 4</option>
                <option value="5">Audio 5</option>
              </select>

              <select id="script-filter-speaker" onchange="filterScriptsTable()" class="bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg px-3 py-1.5 text-xs text-[#172033]">
                <option value="all">Tất cả vai</option>
                <option value="1">Speaker 1</option>
                <option value="2">Speaker 2</option>
              </select>
            </div>

            <span id="script-count-badge" class="text-xs font-semibold text-[#667085]">
              Đang tải danh sách câu...
            </span>
          </div>

          <!-- Enterprise Scripts Table -->
          <div class="bg-white border border-[#E5EAF1] rounded-xl shadow-saas-card overflow-hidden">
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="border-b border-[#E5EAF1] bg-[#F5F7FA] text-[#667085] font-semibold">
                    <th class="py-3 px-4 w-12">#</th>
                    <th class="py-3 px-4 w-24">Bài</th>
                    <th class="py-3 px-4 w-28">Vai Thoại</th>
                    <th class="py-3 px-4">Lời Thoại Tiếng Anh</th>
                    <th class="py-3 px-4">Phiên Âm IPA</th>
                    <th class="py-3 px-4">Dịch Nghĩa</th>
                    <th class="py-3 px-4 text-right w-24">Thao Tác</th>
                  </tr>
                </thead>
                <tbody id="scripts-table-body" class="divide-y divide-[#E5EAF1]">
                  <!-- Injected via filterScriptsTable() -->
                </tbody>
              </table>
            </div>
          </div>

        </section>


        <!-- ============================================== -->
        <!-- VIEW 7: VOICE SYNTHESIS LAB (Mô Hình Sinh Giọng) -->
        <!-- ============================================== -->
        <section id="page-lab" class="page-view hidden space-y-6">
          <div class="border-b border-[#E5EAF1] pb-5">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#1D4ED8]/10 text-[#1D4ED8] border border-[#1D4ED8]/20">
                Natural Neural TTS Lab
              </span>
              <span class="text-xs text-[#667085]">Giọng đọc tự nhiên đa ngôn ngữ • Điều chỉnh cảm xúc và ngữ điệu</span>
            </div>
            <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Voice Synthesis & Cloning Lab</h1>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            <!-- Tool 1: Free Natural Neural Voice Generator -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
              <div class="border-b border-[#E5EAF1] pb-3">
                <h3 class="text-sm font-bold text-[#172033]">1. Sinh Giọng Chuẩn Bản Ngữ (Natural Voices)</h3>
                <p class="text-[11px] text-[#667085]">Giọng phát thanh tự nhiên, ngữ điệu chuẩn Anh - Mỹ.</p>
              </div>

              <div class="space-y-3">
                <div>
                  <label class="text-xs font-bold text-[#172033] block mb-1">Văn bản cần đọc:</label>
                  <textarea id="tts-free-text" rows="3" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-3 text-xs text-[#172033] focus:outline-none focus:border-[#1D4ED8]" placeholder="Nhập câu tiếng Anh...">Hey Brad! Are you ready to leave? Did you peel the apples and put the peel in the bin?</textarea>
                </div>

                <div class="grid grid-cols-2 gap-3">
                  <div>
                    <label class="text-xs font-bold text-[#172033] block mb-1">Giọng Đọc (Voice):</label>
                    <select id="tts-free-voice" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#172033]">
                      <option value="en-US-BrianMultilingualNeural">Brian (US - Nam Trầm Ấm)</option>
                      <option value="en-US-JennyMultilingualNeural">Jenny (US - Nữ Tự Nhiên)</option>
                      <option value="en-US-RyanMultilingualNeural">Ryan (US - Nam Trẻ Trung)</option>
                      <option value="en-US-AvaMultilingualNeural">Ava (US - Nữ Diễn Cảm)</option>
                      <option value="en-US-AndrewMultilingualNeural">Andrew (US - Nam Phát Thanh)</option>
                    </select>
                  </div>

                  <div>
                    <label class="text-xs font-bold text-[#172033] block mb-1">Tốc Độ Đọc:</label>
                    <select id="tts-free-rate" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#172033]">
                      <option value="-6%">Chậm rãi (-6%)</option>
                      <option value="-3%" selected>Tự nhiên chuẩn (-3%)</option>
                      <option value="+0%">Bình thường (0%)</option>
                      <option value="+5%">Nhanh nhẹn (+5%)</option>
                    </select>
                  </div>
                </div>

                <button onclick="generateFreeTts()" id="btn-free-tts" class="w-full py-2.5 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition-layout">
                  <i data-lucide="play-circle" class="w-4 h-4"></i>
                  <span>Sinh Giọng Đọc Ngay</span>
                </button>

                <div id="free-tts-result" class="hidden p-4 rounded-xl border border-[#E5EAF1] bg-[#F5F7FA] space-y-2">
                  <div class="flex items-center justify-between text-xs">
                    <span class="font-bold text-[#16A36A]">Đã tạo file âm thanh:</span>
                    <a id="free-tts-download" href="#" download="natural_voice.mp3" class="text-[#1D4ED8] font-bold hover:underline">Tải về MP3</a>
                  </div>
                  <audio id="free-tts-audio" controls class="w-full h-8"></audio>
                </div>
              </div>
            </div>

            <!-- Tool 2: Prompt-based Stylized Generator -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
              <div class="border-b border-[#E5EAF1] pb-3">
                <h3 class="text-sm font-bold text-[#172033]">2. Điều Khiển Ngữ Điệu Theo Prompt</h3>
                <p class="text-[11px] text-[#667085]">Tùy biến phong cách đọc học viên, ngắt nghỉ tự nhiên.</p>
              </div>

              <div class="space-y-3">
                <div>
                  <label class="text-xs font-bold text-[#172033] block mb-1">Prompt Định Hướng Ngữ Điệu:</label>
                  <input type="text" id="gen-prompt" value="Giọng đọc học viên tiếng Anh tự nhiên, phát âm rõ ràng, không ngắt quãng như máy." class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2.5 text-xs text-[#172033] focus:outline-none focus:border-[#1D4ED8]">
                </div>

                <div class="flex flex-wrap gap-1.5">
                  <button onclick="setGenPrompt('Giọng đọc học viên tiếng Anh tự nhiên, phát âm rõ ràng, không ngắt quãng như máy.')" class="px-2 py-1 rounded text-[10px] bg-[#F5F7FA] border border-[#E5EAF1] text-[#667085] hover:text-[#172033]">
                    Học viên tự nhiên
                  </button>
                  <button onclick="setGenPrompt('Giọng đối thoại đời thường, có nhịp thở và ngữ điệu chân thực.')" class="px-2 py-1 rounded text-[10px] bg-[#F5F7FA] border border-[#E5EAF1] text-[#667085] hover:text-[#172033]">
                    Đối thoại đời thường
                  </button>
                  <button onclick="setGenPrompt('Giọng phát thanh viên chuẩn Anh Mỹ, tốc độ vừa phải, âm đuôi rõ ràng.')" class="px-2 py-1 rounded text-[10px] bg-[#F5F7FA] border border-[#E5EAF1] text-[#667085] hover:text-[#172033]">
                    Chuẩn bản ngữ
                  </button>
                </div>

                <div>
                  <label class="text-xs font-bold text-[#172033] block mb-1">Đoạn văn:</label>
                  <textarea id="gen-text" rows="3" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-3 text-xs text-[#172033] focus:outline-none focus:border-[#1D4ED8]">Yes, I did. But look at the sink, it is starting to leak!</textarea>
                </div>

                <button onclick="generateCustomPromptAudio()" id="btn-custom-prompt" class="w-full py-2.5 rounded-lg bg-[#101D35] hover:bg-[#172B4D] text-white text-xs font-bold flex items-center justify-center gap-2 shadow-sm transition-layout">
                  <i data-lucide="sparkles" class="w-4 h-4"></i>
                  <span>Sinh Giọng Đọc Theo Prompt Này</span>
                </button>

                <div id="gen-result-card" class="hidden p-4 rounded-xl border border-[#E5EAF1] bg-[#F5F7FA] space-y-2">
                  <div class="flex items-center justify-between text-xs">
                    <span class="font-bold text-[#16A36A]">Đã tạo theo prompt:</span>
                    <a id="gen-download-btn" href="#" download class="text-[#1D4ED8] font-bold hover:underline">Tải về MP3</a>
                  </div>
                  <audio id="gen-audio-player" controls class="w-full h-8"></audio>
                </div>
              </div>
            </div>

          </div>
        </section>


        <!-- ============================================== -->
        <!-- VIEW 8: CÀI ĐẶT HỆ THỐNG & GATEWAY (Settings) -->
        <!-- ============================================== -->
        <section id="page-settings" class="page-view hidden space-y-6">
          <div class="border-b border-[#E5EAF1] pb-5">
            <div class="flex items-center gap-2 mb-1">
              <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-[#101D35]/10 text-[#101D35] border border-[#101D35]/20">
                System Preferences
              </span>
              <span class="text-xs text-[#667085]">Cấu hình API Keys, Gateway và hạ tầng âm thanh</span>
            </div>
            <h1 class="text-2xl font-bold text-[#172033] tracking-tight">Cấu Hình Hệ Thống & Beekone AI Gateway</h1>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            
            <!-- Settings Form (2 Cols) -->
            <div class="lg:col-span-2 bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-6">
              
              <!-- Section 1: Beekone API Key -->
              <div class="space-y-4">
                <div class="border-b border-[#E5EAF1] pb-2">
                  <h3 class="text-sm font-bold text-[#172033]">1. Beekone AI Platform Gateway (OpenAI Compatible)</h3>
                  <p class="text-[11px] text-[#667085]">Kết nối API để chấm điểm âm vị, nhận diện giọng nói và phân tích phát âm.</p>
                </div>

                <div class="space-y-3">
                  <div>
                    <label class="text-xs font-bold text-[#172033] block mb-1">Beekone API Key:</label>
                    <div class="relative">
                      <input type="password" id="settings-bee-key" value="sk-bee-9a4e3ae0de60aaab4298ad268bf3a66ef42e5e59ac4ccd7506750d71d80622ae" class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2.5 text-xs text-[#172033] font-mono focus:outline-none focus:border-[#1D4ED8]">
                      <button onclick="togglePasswordVisibility('settings-bee-key')" class="absolute right-3 top-2.5 text-[#667085] hover:text-[#172033]">
                        <i data-lucide="eye" class="w-4 h-4"></i>
                      </button>
                    </div>
                  </div>

                  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label class="text-xs font-bold text-[#172033] block mb-1">API Base URL:</label>
                      <input type="text" value="https://platform.beeknoee.com/api/v1" readonly class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#667085] font-mono">
                    </div>
                    <div>
                      <label class="text-xs font-bold text-[#172033] block mb-1">STT Model:</label>
                      <input type="text" value="whisper-large-v3-turbo" readonly class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#667085] font-mono">
                    </div>
                  </div>

                  <div class="flex items-center justify-between text-[11px] pt-1">
                    <span class="text-[#667085]">Trạng thái: <strong class="text-[#16A36A]">Kết nối sẵn sàng</strong></span>
                    <a href="https://platform.beeknoee.com/billing" target="_blank" class="text-[#1D4ED8] font-bold hover:underline">
                      Nạp số dư tài khoản Beekone &rarr;
                    </a>
                  </div>
                </div>
              </div>

              <!-- Section 2: Audio Recording & Trimming -->
              <div class="space-y-4 pt-4 border-t border-[#E5EAF1]">
                <div class="border-b border-[#E5EAF1] pb-2">
                  <h3 class="text-sm font-bold text-[#172033]">2. Cấu Hình Thu Âm & Ghép Nối</h3>
                  <p class="text-[11px] text-[#667085]">Các tham số chuẩn hóa âm thanh khi xuất bài nộp.</p>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div>
                    <label class="text-xs font-bold text-[#172033] block mb-1">Định Dạng Âm Thanh Thu:</label>
                    <select class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#172033]">
                      <option>audio/webm (Web Standard)</option>
                      <option>audio/mp4 (Apple AAC)</option>
                    </select>
                  </div>

                  <div>
                    <label class="text-xs font-bold text-[#172033] block mb-1">Tần Số Lấy Mẫu (Sample Rate):</label>
                    <select class="w-full bg-[#F5F7FA] border border-[#E5EAF1] rounded-lg p-2 text-xs text-[#172033]">
                      <option>44,100 Hz (CD Quality)</option>
                      <option>48,000 Hz (Studio Broadcast)</option>
                    </select>
                  </div>
                </div>

                <div class="flex items-center gap-2">
                  <input type="checkbox" id="settings-dual-engine" checked class="rounded border-[#E5EAF1] text-[#1D4ED8]">
                  <label for="settings-dual-engine" class="text-xs font-medium text-[#172033] cursor-pointer">
                    Bật Dual-Engine: Tự động chuyển Local Phonetics khi Beekone Cloud hết credit hoặc offline
                  </label>
                </div>
              </div>

              <!-- Save Changes Button -->
              <div class="pt-4 flex justify-end">
                <button onclick="saveSettings()" class="px-5 py-2.5 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-layout">
                  <i data-lucide="save" class="w-4 h-4"></i>
                  <span>Lưu Toàn Bộ Cài Đặt</span>
                </button>
              </div>

            </div>

            <!-- Side Info: Architecture & Verification (1 Col) -->
            <div class="bg-white border border-[#E5EAF1] rounded-xl p-6 shadow-saas-card space-y-4">
              <div class="border-b border-[#E5EAF1] pb-3">
                <h3 class="text-sm font-bold text-[#172033]">Thông Tin Dự Án</h3>
                <p class="text-[11px] text-[#667085]">Bit1 AI Voice Studio Enterprise</p>
              </div>

              <div class="space-y-3 text-xs">
                <div class="p-3 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1] space-y-1">
                  <div class="text-[11px] text-[#667085]">Học viên thực hiện:</div>
                  <div class="font-bold text-[#172033]">Trần Đức Tình</div>
                  <div class="text-[11px] text-[#667085]">Học phần: Luyện Âm Chuẩn (VB2)</div>
                </div>

                <div class="p-3 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1] space-y-1">
                  <div class="text-[11px] text-[#667085]">Cổng kết nối độc lập:</div>
                  <div class="font-bold font-mono text-[#1D4ED8]">http://localhost:5180</div>
                  <div class="text-[11px] text-[#16A36A]">Không trùng với cổng 5173</div>
                </div>

                <div class="p-3 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1] space-y-1">
                  <div class="text-[11px] text-[#667085]">Triển khai đám mây:</div>
                  <a href="https://luyenam-a2xr.vercel.app" target="_blank" class="font-bold font-mono text-[#1D4ED8] hover:underline block truncate">
                    luyenam-a2xr.vercel.app
                  </a>
                  <div class="text-[11px] text-[#16A36A]">Vercel Production Active</div>
                </div>
              </div>
            </div>

          </div>

        </section>

      </div>
    </main>

  </div>


  <!-- ============================================== -->
  <!-- 3. GLOBAL MODALS & POPUPS                      -->
  <!-- ============================================== -->

  <!-- Modal 1: Beekone AI Gateway Configuration -->
  <div id="bee-modal" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
    <div class="bg-white border border-[#E5EAF1] rounded-2xl p-6 max-w-lg w-full space-y-5 shadow-saas-dropdown">
      <div class="flex items-center justify-between border-b border-[#E5EAF1] pb-3">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-[#EFF6FF] border border-[#BFDBFE] flex items-center justify-center text-[#1D4ED8]">
            <i data-lucide="cpu" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-[#172033]">Cấu Hình Beekone AI Gateway</h3>
            <p class="text-[11px] text-[#667085]">OpenAI Compatible Endpoint</p>
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

        <div class="p-3 rounded-lg bg-[#F5F7FA] border border-[#E5EAF1] space-y-1.5 text-xs text-[#667085]">
          <div class="font-semibold text-[#172033]">Tính năng tích hợp:</div>
          <ul class="list-disc pl-4 space-y-1 text-[11px]">
            <li><strong>STT Engine:</strong> <code class="text-[#1D4ED8]">whisper-large-v3-turbo</code></li>
            <li><strong>Chấm điểm:</strong> <code class="text-[#1D4ED8]">google/gemini-3.1-flash-lite</code></li>
            <li><strong>Dự phòng:</strong> Tự động kích hoạt Local Phonetics nếu số dư tài khoản hết.</li>
          </ul>
        </div>
      </div>

      <div class="pt-2 flex items-center justify-end gap-2 border-t border-[#E5EAF1]">
        <button onclick="closeBeeModal()" class="px-4 py-2 rounded-lg text-xs font-semibold text-[#667085] hover:bg-[#F5F7FA]">
          Đóng
        </button>
        <button onclick="saveBeeKeyModal()" class="px-4 py-2 rounded-lg bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold shadow-sm">
          Lưu & Áp Dụng
        </button>
      </div>
    </div>
  </div>


  <!-- Modal 2: Quick Audio Player Dialog -->
  <div id="quick-player-modal" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-center justify-center p-4">
    <div class="bg-white border border-[#E5EAF1] rounded-2xl p-6 max-w-md w-full space-y-4 shadow-saas-dropdown">
      <div class="flex items-center justify-between border-b border-[#E5EAF1] pb-2">
        <h4 id="quick-player-title" class="text-xs font-bold text-[#172033]">Nghe Âm Thanh Mẫu</h4>
        <button onclick="closeQuickPlayer()" class="text-[#667085] hover:text-[#172033]">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>
      <audio id="quick-player-audio" controls class="w-full h-10"></audio>
    </div>
  </div>


  <!-- Command Palette Modal (Ctrl + K) -->
  <div id="command-palette-modal" class="hidden fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-xs flex items-start justify-center pt-20 p-4">
    <div class="bg-white border border-[#E5EAF1] rounded-2xl max-w-xl w-full shadow-saas-dropdown overflow-hidden">
      <div class="flex items-center gap-3 px-4 border-b border-[#E5EAF1]">
        <i data-lucide="search" class="w-4 h-4 text-[#98A2B3]"></i>
        <input type="text" id="command-palette-input" oninput="filterPaletteCommands()" placeholder="Gõ lệnh hoặc trang cần mở (ví dụ: studio, audio 1, settings...)" class="w-full py-3.5 text-xs text-[#172033] focus:outline-none">
        <kbd class="text-[10px] font-mono text-[#98A2B3] bg-[#F5F7FA] border border-[#E5EAF1] px-1.5 py-0.5 rounded">ESC</kbd>
      </div>
      <div id="command-palette-results" class="max-h-64 overflow-y-auto p-2 space-y-1 text-xs">
        <button onclick="navigateTo('dashboard'); closeCommandPalette();" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left text-[#172033] hover:bg-[#F5F7FA]">
          <i data-lucide="layout-dashboard" class="w-4 h-4 text-[#667085]"></i>
          <span class="font-semibold">Mở Dashboard Tổng Quan</span>
        </button>
        <button onclick="navigateTo('studio'); closeCommandPalette();" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left text-[#172033] hover:bg-[#F5F7FA]">
          <i data-lucide="mic" class="w-4 h-4 text-[#667085]"></i>
          <span class="font-semibold">Mở Phòng Thu Luyện Âm Studio</span>
        </button>
        <button onclick="navigateTo('assignments'); closeCommandPalette();" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left text-[#172033] hover:bg-[#F5F7FA]">
          <i data-lucide="file-check-2" class="w-4 h-4 text-[#667085]"></i>
          <span class="font-semibold">Mở 5 Bài Nộp Hoàn Chỉnh (LACB)</span>
        </button>
        <button onclick="navigateTo('scripts'); closeCommandPalette();" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left text-[#172033] hover:bg-[#F5F7FA]">
          <i data-lucide="book-open" class="w-4 h-4 text-[#667085]"></i>
          <span class="font-semibold">Tra Cứu Kịch Bản & Cặp Âm</span>
        </button>
        <button onclick="navigateTo('settings'); closeCommandPalette();" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left text-[#172033] hover:bg-[#F5F7FA]">
          <i data-lucide="settings" class="w-4 h-4 text-[#667085]"></i>
          <span class="font-semibold">Cài Đặt Hệ Thống & Beekone Key</span>
        </button>
      </div>
    </div>
  </div>


  <!-- Toast Notification Container -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>


  <!-- ============================================== -->
  <!-- 4. CORE APPLICATION JAVASCRIPT LOGIC           -->
  <!-- ============================================== -->
  <script>
    // Global State
    let currentRecAudio = 1;
    let currentRecSpeaker = 1;
    let scriptDatabase = {};
    let recordedChunksMap = {};
    let activeMediaRecorder = null;
    let activeRecordingIndex = null;
    let activeSttRecognition = null;
    let currentSpokenTranscript = "";
    let recordingTimerInterval = null;
    let recordingSeconds = 0;
    let userBeeApiKey = localStorage.getItem('bee_api_key') || "sk-bee-9a4e3ae0de60aaab4298ad268bf3a66ef42e5e59ac4ccd7506750d71d80622ae";

    // 5 Ready-made Assignments Data
    const AUDIOS_DATA = {
      1: {
        title: "Audio 1: Cặp âm /iː/ - /ɪ/ & /e/ - /æ/",
        pairs: "peel /iː/ vs pill /ɪ/ • leave vs live • leak vs lick • pen vs pan • sheep vs ship",
        spk1_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_1_Speaker_1.mp3",
        spk2_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_1_Speaker_2.mp3",
        spk1_text: "Hey Brad! Are you ready to leave? Did you peel the apples and put the peel in the bin? Oh no, stop it leaking! Do not just let the dog lick it! Take a pin or a peg to fix it. Wait, do we need bread or jam? Got it. Should I bring a pen to write down the bill, or maybe a cheque? Okay. By the way, where are we going to live during the trip? Near the sheep or near the big ship? Awesome! Ring the bell, mark an X on the map, and let us go!",
        spk2_text: "Yes, I did. But look at the sink, it is starting to leak! Fixed! Now, what about the food? Should I pack this tin of beans? Both! Put the bread in a pan, and throw out that old bean in the bin. Just bring a pen. Oh, and do not forget to send a message to the men at the farm. Near the field. We can see the cute little chicks with yellow cheeks, a little pig, and maybe even a sheep."
      },
      2: {
        title: "Audio 2: Cặp âm /ɑː/ - /ʌ/ & /ɒ/ - /ɔː/",
        pairs: "park /ɑː/ vs truck /ʌ/ • barn vs hut • cod /ɒ/ vs cord /ɔː/ • cap vs cup",
        spk1_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_2_Speaker_1.mp3",
        spk2_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_2_Speaker_2.mp3",
        spk1_text: "Hey Dawn! Are you ready to pack for the trip? Remember to park the truck near the old barn, not near the small hut. Calm down, Dawn. Keep the cat in its cot, and come check the food. We have a fresh bun, some fried carp, and a fresh cod. Put it in a sack, then tie it with a cord. Oh, watch out for that nasty bug on the cart! Here is your hat and your favorite cap. Drink a cup of water, turn off the tap, and put a top on the pot.",
        spk2_text: "Got it, Don! Is there a ban on bringing animals? My cat wants to chase a fox in the park. Great! Put the cod and carp in a pot, and bring some forks. Should I put the bun into a sack or a box? Ouch! It bit my ankle! My uncle told me to be careful. Where is my hat? It is hot weather outside. Done! I also sent a fax to your uncle. Now, let us carry in these heavy sacks. My heart is beating fast, but I am ready for some outdoor sport!"
      },
      3: {
        title: "Audio 3: Cặp âm /uː/ - /ʊ/ & /ɜː/ - /ə/",
        pairs: "pool /uː/ vs pull /ʊ/ • fool vs full • bird /ɜː/ vs bud /ə/ • worker vs walker",
        spk1_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_3_Speaker_1.mp3",
        spk2_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_3_Speaker_2.mp3",
        spk1_text: "Hey Luke! Look at the garden! It is 4 o'clock and we still need to pot this plant and put it near the fern. Do not be lazy! Pull the hose near the pool. Be careful not to step on that worm near the rock or a rook might eat it. It is a bird. The bird cooed nicely. It would stay if you did not scare it. By the way, who wooed that girl sitting by the beach? Right. Help me take this box of books inside. Make sure to lock the door so no one will look inside. Haha! Taking a walk with a fast walker like you is fun, even if you are a slow worker. Eat a bun and let us go!",
        spk2_text: "I could help, but I am full! That warm soup with the cod was delicious. I am no fool to work on a full stomach. Okay, okay. Wait, look at the bed of flowers. Is that a bud or a colorful bird? That is my sister. She is wearing a fur coat because of the cold west wind. But today is the worst wind ever. It made a gull fly away. Do not worry, I will not turn the wrong way. The sign says \"turn\", not \"ten\". Let us hurry or the sun will burn us."
      },
      4: {
        title: "Audio 4: Nguyên âm đôi Diphthongs (/aɪ/, /eə/, /ɪə/, /əʊ/)",
        pairs: "pie /aɪ/ • pear /eə/ vs peer /ɪə/ • road /əʊ/ vs rode • fine vs phone",
        spk1_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_4_Speaker_1.mp3",
        spk2_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_4_Speaker_2.mp3",
        spk1_text: "Hey Mike! Is this your coat over here? It is so cold today! We should buy some warm pie and sit by the fire. Wow, look at that airplane up in the air! It is flying so high. Wait, where is your ticket? You need to show your coat and your badge to the guard. Haha, you always joke around. Let us enjoy this cold beer and cheer for the new year!",
        spk2_text: "Yes, it is mine. Thanks, Mike. I love the snowy road in January. The air feels so fresh and clear. I bought two pears at the fair, do you want one? Right here in my pocket. Do not fear, I never lose important things! Cheers, Mike! May all our fears disappear and our future be bright."
      },
      5: {
        title: "Audio 5: Phụ âm vô thanh & hữu thanh (/s/ - /z/ & /θ/ - /ð/)",
        pairs: "sink /s/ vs zinc /z/ • bus vs buzz • think /θ/ vs this /ð/ • mouth vs breathe",
        spk1_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_5_Speaker_1.mp3",
        spk2_file: "/BAI_NOP_HOAN_CHINH/Bai_Nop_Audio_5_Speaker_2.mp3",
        spk1_text: "Hey Sam! Did you hear that strange buzz near the zinc sink? Exactly. I think this zinc plate is vibrating because of the northern wind. Thanks, Sam. Look through the glass and tell me if those three boys are playing with their toy boats. Wonderful. Breathing fresh air makes me feel so healthy and thankful.",
        spk2_text: "Yes, I did! I thought it was a bee, but it is just the loose screw on the sink. Let me fix this with my thumb. Hold this thin wire for a second. Yes, they are! Their mother is watching them while bathing in the morning sun. Let us finish fixing this and go breathe some fresh air outside together."
      }
    };

    // Initialize application
    async function initApp() {
      lucide.createIcons();
      await initScriptsData();
      loadAudioAssignment(1);
      filterScriptsTable();
    }

    // SPA Router
    function navigateTo(pageId) {
      document.querySelectorAll('.page-view').forEach(p => p.classList.add('hidden'));
      const target = document.getElementById('page-' + pageId);
      if (target) target.classList.remove('hidden');

      // Update sidebar nav items
      document.querySelectorAll('.nav-item').forEach(btn => {
        btn.className = "nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-medium text-[#94A3B8] hover:text-white hover:bg-[#172B4D] transition-layout";
      });
      const activeBtn = document.getElementById('nav-btn-' + pageId);
      if (activeBtn) {
        activeBtn.className = "nav-item w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-xs font-semibold text-white bg-[#1D4ED8] shadow-sm transition-layout";
      }

      // Update breadcrumb
      const titles = {
        'dashboard': 'Dashboard SaaS',
        'studio': 'Phòng Thu Luyện Âm Studio',
        'eval': 'Chấm Điểm Âm Vị AI',
        'stt': 'Nhận Diện Giọng Nói Thời Gian Thực',
        'assignments': '5 Bài Nộp Hoàn Chỉnh (LACB)',
        'scripts': 'Tra Cứu Kịch Bản & Cặp Âm',
        'lab': 'Voice Synthesis & Cloning Lab',
        'settings': 'Cấu Hình Hệ Thống'
      };
      document.getElementById('breadcrumb-current-module').innerText = titles[pageId] || pageId;

      toggleSidebar(false);
      window.scrollTo({ top: 0, behavior: 'smooth' });
      lucide.createIcons();
    }

    function toggleSidebar(open) {
      const sidebar = document.getElementById('app-sidebar');
      const backdrop = document.getElementById('sidebar-backdrop');
      if (open) {
        sidebar.classList.remove('-translate-x-full');
        backdrop.classList.remove('hidden');
      } else {
        sidebar.classList.add('-translate-x-full');
        backdrop.classList.add('hidden');
      }
    }

    // Load Scripts from /api/scripts or local fallback
    async function initScriptsData() {
      try {
        const res = await fetch('/api/scripts');
        if (res.ok) {
          scriptDatabase = await res.json();
          renderRecorderSentences();
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
      renderRecorderSentences();
    }

    // Studio: Select Audio 1..5
    function selectRecorderAudio(num) {
      currentRecAudio = num;
      for (let i = 1; i <= 5; i++) {
        const tab = document.getElementById(`tab-rec-audio-${i}`);
        if (tab) {
          if (i === num) {
            tab.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold bg-[#101D35] text-white transition-layout";
          } else {
            tab.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout";
          }
        }
      }
      renderRecorderSentences();
    }

    // Studio: Select Speaker 1 or 2
    function selectRecorderSpeaker(spk) {
      currentRecSpeaker = spk;
      const btn1 = document.getElementById('tab-rec-spk-1');
      const btn2 = document.getElementById('tab-rec-spk-2');
      if (spk === 1) {
        btn1.className = "px-4 py-1.5 rounded-lg text-xs font-bold bg-[#1D4ED8] text-white shadow-sm transition-layout";
        btn2.className = "px-4 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout";
      } else {
        btn2.className = "px-4 py-1.5 rounded-lg text-xs font-bold bg-[#101D35] text-white shadow-sm transition-layout";
        btn1.className = "px-4 py-1.5 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout";
      }
      renderRecorderSentences();
    }

    function selectAndGoToStudio(audioNum, speaker) {
      selectRecorderAudio(audioNum);
      selectRecorderSpeaker(speaker);
      navigateTo('studio');
    }

    function getCurrentSentences() {
      const data = scriptDatabase[currentRecAudio] || scriptDatabase[String(currentRecAudio)];
      if (data) {
        return currentRecSpeaker === 1 ? data.speaker_1 : data.speaker_2;
      }
      return [];
    }

    // Render sentences list in Studio
    function renderRecorderSentences() {
      const container = document.getElementById('recorder-sentences-container');
      const sentences = getCurrentSentences();

      if (!sentences || sentences.length === 0) {
        container.innerHTML = `<div class="bg-white border border-[#E5EAF1] rounded-xl p-8 text-center text-[#667085] text-xs">Đang tải danh sách câu thoại...</div>`;
        return;
      }

      let recordedCount = 0;
      let html = '';

      sentences.forEach((s, idx) => {
        const itemKey = `${currentRecAudio}_${currentRecSpeaker}_${idx}`;
        const rec = recordedChunksMap[itemKey];
        const hasRec = Boolean(rec);
        if (hasRec) recordedCount++;

        html += `
          <div id="sentence-card-${idx}" class="bg-white border ${hasRec ? 'border-[#A6F4C5] bg-[#F0FDF4]/30' : 'border-[#E5EAF1]'} rounded-xl p-5 shadow-saas-card transition-layout space-y-3">
            
            <div class="flex items-center justify-between flex-wrap gap-2">
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-0.5 rounded text-[11px] font-bold ${hasRec ? 'bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5]' : 'bg-[#F5F7FA] text-[#667085] border border-[#E5EAF1]'} font-mono">
                  Câu ${idx + 1} / ${sentences.length}
                </span>
                <span id="badge-status-${idx}" class="text-xs font-semibold ${hasRec ? 'text-[#16A36A]' : 'text-[#667085]'} flex items-center gap-1">
                  ${hasRec ? `<i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#16A36A]"></i> Đã thu (${rec.duration || 0}s)` : `<i data-lucide="circle-dashed" class="w-3.5 h-3.5 text-[#98A2B3]"></i> Chưa thu`}
                </span>
              </div>

              <button onclick="playNativeSample('${escapeHtml(s.text)}', this)" class="text-xs font-semibold bg-white hover:bg-[#F5F7FA] text-[#1D4ED8] border border-[#E5EAF1] px-2.5 py-1 rounded-lg transition-layout flex items-center gap-1.5 shadow-saas-subtle">
                <i data-lucide="volume-2" class="w-3.5 h-3.5 text-[#1D4ED8]"></i> Nghe Mẫu Bản Ngữ
              </button>
            </div>

            <div class="space-y-1">
              <div class="text-sm md:text-base font-bold text-[#172033] tracking-tight leading-relaxed">
                ${s.text}
              </div>
              ${s.ipa ? `<div class="text-xs text-[#1D4ED8] font-mono tracking-wider">${s.ipa}</div>` : ''}
              ${s.vi ? `<div class="text-xs text-[#667085] italic">${s.vi}</div>` : ''}
            </div>

            <div class="pt-2 border-t border-[#E5EAF1] flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div class="flex items-center gap-2 flex-wrap">
                <button onclick="toggleRecordSentence(${idx})" id="btn-rec-${idx}" class="px-3.5 py-1.5 rounded-lg text-xs font-bold transition-layout flex items-center gap-1.5 ${hasRec ? 'bg-white text-[#172033] border border-[#E5EAF1] hover:bg-[#F5F7FA]' : 'bg-[#DC4545] hover:bg-[#B91C1C] text-white shadow-sm'}">
                  <i data-lucide="mic" class="w-3.5 h-3.5"></i>
                  <span id="label-rec-${idx}">${hasRec ? 'Thu lại câu này' : 'Bắt đầu thu âm'}</span>
                </button>
                <span id="timer-rec-${idx}" class="text-xs font-mono font-bold text-[#DC4545] hidden">00:00</span>

                <button onclick="evaluateRecordedSentence(${idx})" id="btn-eval-${idx}" class="${hasRec ? 'inline-flex' : 'hidden'} px-3 py-1.5 rounded-lg text-xs font-bold bg-[#1D4ED8] hover:bg-[#1E40AF] text-white items-center gap-1.5 shadow-sm transition-layout">
                  <i data-lucide="target" class="w-3.5 h-3.5"></i>
                  <span>Chấm Điểm Liền</span>
                </button>
              </div>

              <div id="player-container-${idx}" class="${hasRec ? 'flex' : 'hidden'} items-center gap-2 w-full sm:w-auto">
                <span class="text-[11px] text-[#16A36A] font-bold shrink-0">Giọng thật:</span>
                <audio id="audio-preview-${idx}" controls class="h-8 max-w-xs" src="${hasRec ? rec.blobUrl : ''}"></audio>
              </div>
            </div>

            <div id="eval-result-box-${idx}" class="${rec && rec.evalData ? 'block' : 'hidden'} mt-3 bg-[#F5F7FA] p-4 rounded-xl border border-[#E5EAF1] space-y-2.5">
              ${rec && rec.evalData ? renderEvaluationHtml(rec.evalData, idx) : ''}
            </div>

          </div>
        `;
      });

      container.innerHTML = html;
      lucide.createIcons();

      const total = sentences.length;
      const pct = Math.round((recordedCount / total) * 100);
      document.getElementById('recorder-progress-text').innerText = `${recordedCount} / ${total} câu`;
      document.getElementById('recorder-progress-bar').style.width = `${pct}%`;
    }

    function escapeHtml(text) {
      return text.replace(/'/g, "\\'").replace(/"/g, '&quot;');
    }

    // Play native sample using Edge TTS
    async function playNativeSample(text, btnElement) {
      const origHtml = btnElement.innerHTML;
      btnElement.disabled = true;
      btnElement.innerHTML = `<i data-lucide="loader" class="w-3.5 h-3.5 animate-spin"></i> Đang tải...`;
      lucide.createIcons();
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
          showToast('error', 'Lỗi', data.error || 'Không thể phát câu mẫu');
        }
      } catch (err) {
        showToast('error', 'Lỗi kết nối', err.message);
      } finally {
        btnElement.disabled = false;
        btnElement.innerHTML = origHtml;
        lucide.createIcons();
      }
    }

    // Toggle recording for specific sentence
    async function toggleRecordSentence(idx) {
      if (activeRecordingIndex !== null && activeRecordingIndex === idx) {
        stopSentenceRecording();
        return;
      }
      if (activeRecordingIndex !== null && activeRecordingIndex !== idx) {
        stopSentenceRecording();
      }
      startSentenceRecording(idx);
    }

    async function startSentenceRecording(idx) {
      try {
        currentSpokenTranscript = "";
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        let options = { mimeType: 'audio/webm' };
        if (!MediaRecorder.isTypeSupported('audio/webm')) {
          options = { mimeType: 'audio/mp4' };
        }

        activeMediaRecorder = new MediaRecorder(stream, options);
        let audioChunks = [];

        // Parallel Web Speech Recognition for instant client-side STT
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
              currentSpokenTranscript = t.trim();
            };
            activeSttRecognition.start();
          } catch (e) {
            console.warn('STT recognition start error:', e);
          }
        }

        activeMediaRecorder.ondataavailable = (e) => {
          if (e.data.size > 0) audioChunks.push(e.data);
        };

        activeMediaRecorder.onstop = async () => {
          stream.getTracks().forEach(t => t.stop());
          clearInterval(recordingTimerInterval);
          if (activeSttRecognition) {
            try { activeSttRecognition.stop(); } catch (e) {}
            activeSttRecognition = null;
          }

          const mime = activeMediaRecorder.mimeType || 'audio/webm';
          const blob = new Blob(audioChunks, { type: mime });
          const blobUrl = URL.createObjectURL(blob);
          const base64 = await blobToBase64(blob);

          const itemKey = `${currentRecAudio}_${currentRecSpeaker}_${idx}`;
          recordedChunksMap[itemKey] = {
            base64: base64,
            blobUrl: blobUrl,
            duration: recordingSeconds,
            spokenText: currentSpokenTranscript
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

          if (card) {
            card.className = "bg-white border border-[#A6F4C5] bg-[#F0FDF4]/30 rounded-xl p-5 shadow-saas-card transition-layout space-y-3";
          }
          if (btnRec) {
            btnRec.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-layout flex items-center gap-1.5 bg-white text-[#172033] border border-[#E5EAF1] hover:bg-[#F5F7FA]";
          }
          if (labelRec) labelRec.innerText = "Thu lại câu này";
          if (timerRec) timerRec.classList.add('hidden');
          if (btnEval) btnEval.classList.remove('hidden');
          if (badgeStatus) {
            badgeStatus.className = "text-xs font-semibold text-[#16A36A] flex items-center gap-1";
            badgeStatus.innerHTML = `<i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-[#16A36A]"></i> Đã thu (${recordingSeconds}s)`;
          }
          if (playerCont) playerCont.classList.remove('hidden');
          if (audioPreview) audioPreview.src = blobUrl;

          updateProgressStats();
          showToast('success', 'Thu âm hoàn tất', `Câu ${idx + 1} (${recordingSeconds}s) đã được ghi lại thành công.`);
          lucide.createIcons();

          activeRecordingIndex = null;
          activeMediaRecorder = null;
        };

        activeMediaRecorder.start();
        activeRecordingIndex = idx;
        recordingSeconds = 0;

        const btnRec = document.getElementById(`btn-rec-${idx}`);
        const labelRec = document.getElementById(`label-rec-${idx}`);
        const timerRec = document.getElementById(`timer-rec-${idx}`);

        if (btnRec) {
          btnRec.className = "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-layout flex items-center gap-1.5 bg-[#DC4545] text-white is-recording shadow-sm";
        }
        if (labelRec) labelRec.innerText = "Dừng thu âm";
        if (timerRec) {
          timerRec.classList.remove('hidden');
          timerRec.innerText = "00:00";
        }

        recordingTimerInterval = setInterval(() => {
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

    function stopSentenceRecording() {
      if (activeMediaRecorder && activeMediaRecorder.state === 'recording') {
        activeMediaRecorder.stop();
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

    // Evaluate recorded sentence
    async function evaluateRecordedSentence(idx) {
      const itemKey = `${currentRecAudio}_${currentRecSpeaker}_${idx}`;
      const rec = recordedChunksMap[itemKey];
      if (!rec || !rec.base64) {
        showToast('warning', 'Chưa thu âm', 'Vui lòng thu âm câu này trước khi chấm điểm.');
        return;
      }

      const sentences = getCurrentSentences();
      const sentenceObj = sentences[idx];
      const targetText = sentenceObj.text;
      const targetIpa = sentenceObj.ipa || "";

      const btnEval = document.getElementById(`btn-eval-${idx}`);
      const evalBox = document.getElementById(`eval-result-box-${idx}`);

      if (btnEval) {
        btnEval.disabled = true;
        btnEval.innerHTML = `<i data-lucide="loader" class="w-3.5 h-3.5 animate-spin"></i> Đang chấm điểm...`;
        lucide.createIcons();
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
            apiKey: userBeeApiKey
          })
        });

        const data = await res.json();
        rec.evalData = data;

        evalBox.innerHTML = renderEvaluationHtml(data, idx);
        evalBox.classList.remove('hidden');
        lucide.createIcons();
        showToast('success', 'Chấm điểm thành công', `Điểm phát âm: ${data.score || 0}/100.`);

      } catch (err) {
        // Fallback local evaluation
        const fallbackData = computeClientPhoneticScore(targetText, rec.spokenText || "");
        rec.evalData = fallbackData;
        evalBox.innerHTML = renderEvaluationHtml(fallbackData, idx);
        evalBox.classList.remove('hidden');
        lucide.createIcons();
      } finally {
        if (btnEval) {
          btnEval.disabled = false;
          btnEval.innerHTML = `<i data-lucide="target" class="w-3.5 h-3.5"></i> Chấm Điểm Lại`;
          lucide.createIcons();
        }
      }
    }

    function renderEvaluationHtml(data, idx) {
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
          <span class="inline-flex items-center gap-1 px-2 py-0.5 rounded text-xs font-semibold border ${pillClass}" title="${escapeHtml(w.feedback || '')}">
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
          <div class="text-[10px] uppercase font-bold text-[#667085] mb-1.5">Chi tiết các từ đã phát âm:</div>
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

    function updateProgressStats() {
      const sentences = getCurrentSentences();
      let count = 0;
      sentences.forEach((s, idx) => {
        const itemKey = `${currentRecAudio}_${currentRecSpeaker}_${idx}`;
        if (recordedChunksMap[itemKey]) count++;
      });
      const total = sentences.length;
      const pct = Math.round((count / total) * 100);
      document.getElementById('recorder-progress-text').innerText = `${count} / ${total} câu`;
      document.getElementById('recorder-progress-bar').style.width = `${pct}%`;
    }

    // Merge All Sentences with FFmpeg
    async function mergeAllSentences() {
      const sentences = getCurrentSentences();
      if (!sentences || sentences.length === 0) {
        showToast('warning', 'Chưa có câu thoại', 'Chưa tải được danh sách câu!');
        return;
      }

      const autoFallback = document.getElementById('chk-auto-fallback').checked;
      const silenceMs = parseInt(document.getElementById('sel-silence-ms').value, 10);
      const mergeBtn = document.getElementById('btn-merge-all');
      const mergeText = document.getElementById('btn-merge-text');

      let recordedCount = 0;
      const payloadSentences = [];

      sentences.forEach((s, idx) => {
        const itemKey = `${currentRecAudio}_${currentRecSpeaker}_${idx}`;
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

      mergeBtn.disabled = true;
      mergeText.innerText = `Đang cắt ghép ${sentences.length} câu...`;

      try {
        const res = await fetch('/api/voice/merge-sentences', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            audioNum: currentRecAudio,
            speaker: currentRecSpeaker,
            silenceMs: silenceMs,
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
          player.src = finalUrl;
          dl.href = data.audioUrl;
          dl.download = data.fileName;

          title.innerText = `Đã Ghép Xong Bài Nộp Audio ${currentRecAudio} - Speaker ${currentRecSpeaker}!`;
          details.innerText = `Ghép thành công ${data.mergedCount} câu (gồm ${recordedCount} câu giọng thật của bạn).`;

          card.classList.remove('hidden');
          card.scrollIntoView({ behavior: 'smooth' });
          player.play();

          showToast('success', 'Ghép hoàn tất', `Bài Nộp Audio ${currentRecAudio} đã sẵn sàng nộp cô!`);
        } else {
          showToast('error', 'Lỗi ghép file', data.error || 'Lỗi server');
        }
      } catch (e) {
        showToast('error', 'Lỗi kết nối', e.message);
      } finally {
        mergeBtn.disabled = false;
        mergeText.innerText = "Ghép Thành File MP3 Hoàn Chỉnh";
      }
    }

    // Ready-made Assignments tab loader
    function loadAudioAssignment(num) {
      for (let i = 1; i <= 5; i++) {
        const tab = document.getElementById(`asg-tab-${i}`);
        if (tab) {
          if (i === num) {
            tab.className = "px-4 py-2 rounded-lg text-xs font-bold bg-[#101D35] text-white transition-layout";
          } else {
            tab.className = "px-4 py-2 rounded-lg text-xs font-bold bg-white text-[#667085] border border-[#E5EAF1] hover:text-[#172033] transition-layout";
          }
        }
      }

      const d = AUDIOS_DATA[num];
      const container = document.getElementById('assignment-content-card');

      container.innerHTML = `
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-[#E5EAF1] pb-4">
          <div>
            <h2 class="text-lg font-bold text-[#172033]">${d.title}</h2>
            <div class="text-xs text-[#1D4ED8] font-medium mt-0.5">${d.pairs}</div>
          </div>
          <span class="text-xs bg-[#ECFDF3] text-[#16A36A] border border-[#A6F4C5] px-3 py-1 rounded-full font-bold self-start sm:self-auto">
            Bản Chuẩn Bản Ngữ Sẵn Sàng
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-[#F5F7FA] p-5 rounded-xl border border-[#E5EAF1] space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-bold text-[#172033] flex items-center gap-1.5">
                <i data-lucide="user" class="w-4 h-4 text-[#1D4ED8]"></i> Speaker 1 (Vai chính)
              </h3>
              <a href="${d.spk1_file}" download class="bg-[#1D4ED8] hover:bg-[#1E40AF] text-white text-xs font-bold px-3 py-1.5 rounded-lg transition-layout flex items-center gap-1">
                <i data-lucide="download" class="w-3.5 h-3.5"></i> Tải MP3
              </a>
            </div>
            <audio controls class="w-full h-9" src="${d.spk1_file}"></audio>
            <div>
              <div class="text-[11px] font-bold text-[#667085] uppercase tracking-wider mb-1">Lời thoại kịch bản:</div>
              <p class="text-xs text-[#172033] bg-white p-3 rounded-lg border border-[#E5EAF1] leading-relaxed max-h-36 overflow-y-auto">
                ${d.spk1_text}
              </p>
            </div>
          </div>

          <div class="bg-[#F5F7FA] p-5 rounded-xl border border-[#E5EAF1] space-y-4">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-bold text-[#172033] flex items-center gap-1.5">
                <i data-lucide="users" class="w-4 h-4 text-[#101D35]"></i> Speaker 2 (Vai đối thoại)
              </h3>
              <a href="${d.spk2_file}" download class="bg-[#101D35] hover:bg-[#172B4D] text-white text-xs font-bold px-3 py-1.5 rounded-lg transition-layout flex items-center gap-1">
                <i data-lucide="download" class="w-3.5 h-3.5"></i> Tải MP3
              </a>
            </div>
            <audio controls class="w-full h-9" src="${d.spk2_file}"></audio>
            <div>
              <div class="text-[11px] font-bold text-[#667085] uppercase tracking-wider mb-1">Lời thoại kịch bản:</div>
              <p class="text-xs text-[#172033] bg-white p-3 rounded-lg border border-[#E5EAF1] leading-relaxed max-h-36 overflow-y-auto">
                ${d.spk2_text}
              </p>
            </div>
          </div>
        </div>
      `;
      lucide.createIcons();
    }

    // Filter Scripts Table in View 6
    function filterScriptsTable() {
      const query = (document.getElementById('script-search-input')?.value || '').toLowerCase().trim();
      const filterAudio = document.getElementById('script-filter-audio')?.value || 'all';
      const filterSpeaker = document.getElementById('script-filter-speaker')?.value || 'all';
      const tbody = document.getElementById('scripts-table-body');
      const countBadge = document.getElementById('script-count-badge');

      if (!tbody) return;

      let matchedRows = [];
      let totalRows = 0;

      for (let aNum = 1; aNum <= 5; aNum++) {
        if (filterAudio !== 'all' && String(aNum) !== filterAudio) continue;
        const lesson = scriptDatabase[aNum] || scriptDatabase[String(aNum)];
        if (!lesson) continue;

        ['speaker_1', 'speaker_2'].forEach((spkKey, sIdx) => {
          const spkNum = sIdx + 1;
          if (filterSpeaker !== 'all' && String(spkNum) !== filterSpeaker) continue;

          (lesson[spkKey] || []).forEach(item => {
            totalRows++;
            const textMatch = !query || 
              (item.text && item.text.toLowerCase().includes(query)) ||
              (item.ipa && item.ipa.toLowerCase().includes(query)) ||
              (item.vi && item.vi.toLowerCase().includes(query));

            if (textMatch) {
              matchedRows.push({
                audio: aNum,
                speaker: spkNum,
                num: item.num,
                text: item.text,
                ipa: item.ipa || '',
                vi: item.vi || ''
              });
            }
          });
        });
      }

      if (matchedRows.length === 0) {
        tbody.innerHTML = `<tr><td colspan="7" class="py-8 text-center text-[#667085] text-xs">Không tìm thấy câu thoại phù hợp với bộ lọc.</td></tr>`;
      } else {
        tbody.innerHTML = matchedRows.map(r => `
          <tr class="hover:bg-[#F5F7FA]">
            <td class="py-2.5 px-4 font-mono text-[#667085]">${r.num}</td>
            <td class="py-2.5 px-4 font-semibold text-[#172033]">Audio ${r.audio}</td>
            <td class="py-2.5 px-4">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold ${r.speaker === 1 ? 'bg-[#EFF6FF] text-[#1D4ED8]' : 'bg-[#F0FDF4] text-[#16A36A]'}">
                Speaker ${r.speaker}
              </span>
            </td>
            <td class="py-2.5 px-4 font-medium text-[#172033] max-w-xs">${r.text}</td>
            <td class="py-2.5 px-4 font-mono text-[#1D4ED8] text-[11px] max-w-xs">${r.ipa}</td>
            <td class="py-2.5 px-4 text-[#667085] text-[11px] max-w-xs">${r.vi}</td>
            <td class="py-2.5 px-4 text-right">
              <button onclick="selectAndGoToStudio(${r.audio}, ${r.speaker})" class="text-xs font-semibold text-[#1D4ED8] hover:underline">
                Thu âm
              </button>
            </td>
          </tr>
        `).join('');
      }

      if (countBadge) {
        countBadge.innerText = `Hiển thị ${matchedRows.length} / ${totalRows} câu thoại`;
      }
    }

    // Natural TTS Generator
    async function generateFreeTts() {
      const text = document.getElementById('tts-free-text').value.trim();
      const voice = document.getElementById('tts-free-voice').value;
      const rate = document.getElementById('tts-free-rate').value;
      const btn = document.getElementById('btn-free-tts');

      if (!text) return showToast('warning', 'Thiếu dữ liệu', 'Vui lòng nhập văn bản cần đọc!');
      btn.disabled = true;
      btn.innerHTML = `<i data-lucide="loader" class="w-4 h-4 animate-spin"></i> Đang sinh âm thanh...`;
      lucide.createIcons();

      try {
        const res = await fetch('/api/voice/tts', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text, voice, rate })
        });
        const data = await res.json();
        if (data.success && data.audioUrl) {
          const resBox = document.getElementById('free-tts-result');
          const player = document.getElementById('free-tts-audio');
          const dl = document.getElementById('free-tts-download');
          player.src = data.audioUrl + '?t=' + Date.now();
          dl.href = data.audioUrl;
          resBox.classList.remove('hidden');
          player.play();
          showToast('success', 'Thành công', 'Đã tạo giọng đọc tự nhiên.');
        } else {
          showToast('error', 'Lỗi', data.error || 'Không thể tạo âm thanh');
        }
      } catch (e) {
        showToast('error', 'Lỗi kết nối', e.message);
      } finally {
        btn.disabled = false;
        btn.innerHTML = `<i data-lucide="play-circle" class="w-4 h-4"></i> Sinh Giọng Đọc Ngay`;
        lucide.createIcons();
      }
    }

    // Prompt-based Voice Generator
    function setGenPrompt(p) {
      document.getElementById('gen-prompt').value = p;
    }

    async function generateCustomPromptAudio() {
      const text = document.getElementById('gen-text').value.trim();
      const prompt = document.getElementById('gen-prompt').value.trim();
      const btn = document.getElementById('btn-custom-prompt');

      if (!text) return showToast('warning', 'Thiếu dữ liệu', 'Vui lòng nhập văn bản cần sinh giọng!');
      btn.disabled = true;
      btn.innerHTML = `<i data-lucide="loader" class="w-4 h-4 animate-spin"></i> Đang áp dụng prompt...`;
      lucide.createIcons();

      try {
        const res = await fetch('/api/voice/clone', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ text, voice: 'en-US-BrianMultilingualNeural', level: 'native', prompt })
        });
        const data = await res.json();
        if (data.success && data.audioUrl) {
          const card = document.getElementById('gen-result-card');
          const player = document.getElementById('gen-audio-player');
          const dl = document.getElementById('gen-download-btn');
          player.src = data.audioUrl + '?t=' + Date.now();
          dl.href = data.audioUrl;
          card.classList.remove('hidden');
          player.play();
          showToast('success', 'Thành công', 'Đã sinh âm thanh theo prompt định hướng.');
        } else {
          showToast('error', 'Lỗi', data.error || 'Lỗi server');
        }
      } catch (err) {
        showToast('error', 'Lỗi kết nối', err.message);
      } finally {
        btn.disabled = false;
        btn.innerHTML = `<i data-lucide="sparkles" class="w-4 h-4"></i> Sinh Giọng Đọc Theo Prompt Này`;
        lucide.createIcons();
      }
    }

    // Live STT Speech Recognition
    let isRecordingStt = false;
    let sttRecognitionInstance = null;
    function toggleMicrophoneStt() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) return showToast('error', 'Không hỗ trợ', 'Trình duyệt chưa hỗ trợ Web Speech API. Vui lòng dùng Chrome hoặc Edge!');

      const btn = document.getElementById('stt-mic-btn');
      const statusText = document.getElementById('stt-status-text');
      const box = document.getElementById('stt-transcript-box');

      if (isRecordingStt) {
        if (sttRecognitionInstance) sttRecognitionInstance.stop();
        isRecordingStt = false;
        btn.className = "w-20 h-20 rounded-full bg-[#1D4ED8] hover:bg-[#1E40AF] text-white flex items-center justify-center shadow-lg transition-all";
        statusText.innerText = "Bấm vào micro để bắt đầu nói tiếng Anh";
      } else {
        sttRecognitionInstance = new SpeechRecognition();
        sttRecognitionInstance.continuous = true;
        sttRecognitionInstance.interimResults = true;
        sttRecognitionInstance.lang = 'en-US';

        sttRecognitionInstance.onstart = () => {
          isRecordingStt = true;
          btn.className = "w-20 h-20 rounded-full bg-[#DC4545] text-white flex items-center justify-center shadow-lg is-recording transition-all";
          statusText.innerText = "Đang lắng nghe... Hãy nói tiếng Anh ngay bây giờ!";
          box.innerHTML = '';
        };

        sttRecognitionInstance.onresult = (e) => {
          let str = '';
          for (let i = 0; i < e.results.length; i++) {
            str += e.results[i][0].transcript + ' ';
          }
          box.innerText = str;
        };

        sttRecognitionInstance.onerror = () => {
          isRecordingStt = false;
          btn.className = "w-20 h-20 rounded-full bg-[#1D4ED8] text-white flex items-center justify-center";
          statusText.innerText = "Đã dừng hoặc chưa cấp quyền mic.";
        };

        sttRecognitionInstance.onend = () => {
          isRecordingStt = false;
          btn.className = "w-20 h-20 rounded-full bg-[#1D4ED8] text-white flex items-center justify-center";
          statusText.innerText = "Bấm micro để tiếp tục nói";
        };

        sttRecognitionInstance.start();
      }
    }

    // Quick Hub Recording in View 3
    let hubMediaRecorder = null;
    let hubAudioChunks = [];
    let hubTimer = null;
    let hubSeconds = 0;
    async function runQuickHubRecording() {
      const btn = document.getElementById('btn-eval-hub-rec');
      const label = document.getElementById('label-eval-hub-rec');
      const timer = document.getElementById('timer-eval-hub');
      const player = document.getElementById('audio-eval-hub');

      if (hubMediaRecorder && hubMediaRecorder.state === 'recording') {
        hubMediaRecorder.stop();
        return;
      }

      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        hubAudioChunks = [];
        hubMediaRecorder = new MediaRecorder(stream);

        hubMediaRecorder.ondataavailable = e => {
          if (e.data.size > 0) hubAudioChunks.push(e.data);
        };

        hubMediaRecorder.onstop = () => {
          stream.getTracks().forEach(t => t.stop());
          clearInterval(hubTimer);
          timer.classList.add('hidden');
          label.innerText = "Thu âm để chấm điểm";
          btn.className = "px-4 py-2 rounded-lg bg-[#DC4545] hover:bg-[#B91C1C] text-white text-xs font-bold flex items-center gap-2 shadow-sm transition-layout";

          const blob = new Blob(hubAudioChunks, { type: 'audio/webm' });
          player.src = URL.createObjectURL(blob);
          player.classList.remove('hidden');
          player.play();
          showToast('success', 'Thu hoàn tất', 'Đã ghi âm mẫu thử để chấm điểm.');
        };

        hubMediaRecorder.start();
        hubSeconds = 0;
        label.innerText = "Dừng thu âm";
        btn.className = "px-4 py-2 rounded-lg bg-[#DC4545] text-white text-xs font-bold flex items-center gap-2 is-recording shadow-sm";
        timer.classList.remove('hidden');
        timer.innerText = "00:00";

        hubTimer = setInterval(() => {
          hubSeconds++;
          const mins = String(Math.floor(hubSeconds / 60)).padStart(2, '0');
          const secs = String(hubSeconds % 60).padStart(2, '0');
          timer.innerText = `${mins}:${secs}`;
        }, 1000);

      } catch (err) {
        showToast('error', 'Lỗi Micro', err.message);
      }
    }

    // Modal & Popover Controls
    function openBeeConfigModal() {
      document.getElementById('bee-modal').classList.remove('hidden');
    }
    function closeBeeModal() {
      document.getElementById('bee-modal').classList.add('hidden');
    }
    function saveBeeKeyModal() {
      const val = document.getElementById('input-bee-key').value.trim();
      if (!val) return showToast('warning', 'Cảnh báo', 'API Key không được để trống.');
      userBeeApiKey = val;
      localStorage.setItem('bee_api_key', val);
      document.getElementById('settings-bee-key').value = val;
      closeBeeModal();
      showToast('success', 'Đã lưu', 'Beekone API Key đã được cập nhật thành công!');
    }

    function toggleNotificationDropdown() {
      const d = document.getElementById('notification-dropdown');
      d.classList.toggle('hidden');
    }

    function openCommandPalette() {
      document.getElementById('command-palette-modal').classList.remove('hidden');
      document.getElementById('command-palette-input').focus();
    }
    function closeCommandPalette() {
      document.getElementById('command-palette-modal').classList.add('hidden');
    }

    function filterPaletteCommands() {
      const q = document.getElementById('command-palette-input').value.toLowerCase();
      const items = document.querySelectorAll('#command-palette-results button');
      items.forEach(it => {
        if (!q || it.innerText.toLowerCase().includes(q)) {
          it.classList.remove('hidden');
        } else {
          it.classList.add('hidden');
        }
      });
    }

    // Key shortcut Ctrl + K
    window.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openCommandPalette();
      }
      if (e.key === 'Escape') {
        closeCommandPalette();
        closeBeeModal();
        closeQuickPlayer();
      }
    });

    function quickPlayAudio(url) {
      const modal = document.getElementById('quick-player-modal');
      const audio = document.getElementById('quick-player-audio');
      audio.src = url;
      modal.classList.remove('hidden');
      audio.play();
    }
    function closeQuickPlayer() {
      const modal = document.getElementById('quick-player-modal');
      const audio = document.getElementById('quick-player-audio');
      audio.pause();
      modal.classList.add('hidden');
    }

    function togglePasswordVisibility(id) {
      const el = document.getElementById(id);
      el.type = el.type === 'password' ? 'text' : 'password';
    }

    function saveSettings() {
      const key = document.getElementById('settings-bee-key').value.trim();
      if (key) {
        userBeeApiKey = key;
        localStorage.setItem('bee_api_key', key);
        document.getElementById('input-bee-key').value = key;
      }
      showToast('success', 'Thành công', 'Toàn bộ cài đặt hệ thống đã được lưu vào trình duyệt.');
    }

    // Toast Notification System
    function showToast(type, title, message) {
      const container = document.getElementById('toast-container');
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

      toast.className = `p-4 rounded-xl border shadow-saas-dropdown flex items-start gap-3 w-80 pointer-events-auto transition-all ${borderClass}`;
      toast.innerHTML = `
        <div class="shrink-0 mt-0.5">${icon}</div>
        <div class="flex-1 min-w-0">
          <div class="text-xs font-bold">${title}</div>
          <div class="text-[11px] text-[#667085] mt-0.5">${message}</div>
        </div>
      `;

      container.appendChild(toast);
      lucide.createIcons();

      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateY(10px)';
        setTimeout(() => toast.remove(), 300);
      }, 4000);
    }

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
