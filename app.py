import streamlit as st
from streamlit_option_menu import option_menu
import requests
import sqlite3
import pandas as pd
from ddgs import DDGS
import database  # Memanggil database.py yang ada di folder yang sama

# --- KONFIGURASI ---
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen2.5:1.5b"
st.set_page_config(page_title="Cakrawala AI | Enterprise Helpdesk", layout="wide", page_icon="🎓")

# Inisialisasi Database
database.init_db()

# --- FUNGSI SEARCH ---
def web_search(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=2))
            return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except:
        return "Pencarian web tidak tersedia."

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎓 Cakrawala University")
    menu = option_menu("Navigation", ["Smart Chat", "Tiket Admin", "Settings"], 
                       icons=['robot', 'database', 'gear'], default_index=0)

# --- HALAMAN SMART CHAT ---
if menu == "Smart Chat":
    st.title("🤖 Asisten IT Cakrawala")
    if "chat" not in st.session_state: st.session_state.chat = []
    
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
        
    if prompt := st.chat_input("Tanyakan solusi IT kampus..."):
        st.session_state.chat.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.spinner("Mencari solusi..."):
            search_res = web_search(prompt)
            enhanced_prompt = f"Info Internet: {search_res}\n\nUser: {prompt}"
            
            try:
                res = requests.post(OLLAMA_URL, json={
                    "model": MODEL, 
                    "messages": [{"role": "system", "content": "Anda asisten IT Cakrawala University."}] + 
                                [{"role": "user", "content": enhanced_prompt}],
                    "stream": False 
                }, timeout=120)
                
                if res.status_code == 200:
                    content = res.json()["message"]["content"]
                    st.session_state.chat.append({"role": "assistant", "content": content})
                    with st.chat_message("assistant"): st.markdown(content)
                    
                    # Auto Save ke database
                    database.save_ticket("Mahasiswa", prompt, "High")
                else:
                    st.error(f"Ollama Error: {res.status_code}")
            except Exception as e:
                st.error(f"Gagal koneksi ke AI: {e}")

# --- HALAMAN ADMIN ---
elif menu == "Tiket Admin":
    st.title("📊 Admin Control Panel")
    conn = sqlite3.connect('cakrawala_helpdesk.db')
    df = pd.read_sql_query("SELECT * FROM tickets", conn)
    
    if not df.empty:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total", len(df))
        c2.metric("Pending", len(df[df['status'] == 'Pending']))
        c3.metric("Resolved", len(df[df['status'] == 'Resolved']))
        
        st.dataframe(df, use_container_width=True)
        
        t_id = st.number_input("ID Tiket untuk di-resolve:", min_value=1, step=1)
        if st.button("Tandai Selesai"):
            c = conn.cursor()
            c.execute("UPDATE tickets SET status = 'Resolved' WHERE id = ?", (t_id,))
            conn.commit()
            st.rerun()
    else:
        st.info("Database kosong.")
    conn.close()

# --- HALAMAN SETTINGS ---
elif menu == "Settings":
    st.title("⚙️ Pengaturan Sistem")
    st.write("Cakrawala AI Pro - Local Infrastructure")
    st.toggle("Gunakan Hybrid Web Search", value=True)