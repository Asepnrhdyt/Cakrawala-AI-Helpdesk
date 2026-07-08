# 🎓 Cakrawala AI Helpdesk System

Sistem Informasi Manajemen Tiket (SIM-Tiket) berbasis **Hybrid Retrieval-Augmented Generation (RAG)** yang dirancang untuk mendukung operasional IT Helpdesk Universitas Cakrawala.

## 🚀 Fitur Utama
- **Local-First AI:** Menggunakan `Ollama` dengan model `Qwen2.5` untuk memproses keluhan secara privat di jaringan lokal.
- **Hybrid Search:** Integrasi `DuckDuckGo Search API` untuk memberikan jawaban yang akurat, faktual, dan *up-to-date*.
- **Data Persistence:** Manajemen siklus hidup tiket menggunakan `SQLite` untuk pelacakan dan audit operasional.
- **Admin Control Panel:** Dashboard interaktif untuk mutasi data dan manajemen status tiket oleh staf IT.
- **Enterprise UI:** Antarmuka responsif dengan desain kustom yang merepresentasikan identitas Universitas Cakrawala.

## 🛠️ Stack Teknologi
- **Frontend:** Streamlit, Streamlit Option Menu.
- **Backend:** Python, SQLite, Pandas.
- **AI Engine:** Ollama (Qwen2.5-1.5B).
- **Integrasi:** DuckDuckGo Search API.

## 📦 Cara Menjalankan

1. **Clone repository:**
   ```bash
   git clone [https://github.com/Asepnrhdyt/Cakrawala-AI-Helpdesk.git](https://github.com/Asepnrhdyt/Cakrawala-AI-Helpdesk.git)
   cd Cakrawala-AI-Helpdesk

2. **Install Depedensi:**
   ```bash
   pip install -r requirements.txt
   
3. **Jalankan Ollama:**
   ```bash
   Pastikan Ollama terinstall dan model Qwen2.5 sudah terunduh:
   ollama pull qwen2.5:1.5b
   ollama serve

4. **Jalankan Aplikasi:**
   ```bash
   streamlit run app.py
