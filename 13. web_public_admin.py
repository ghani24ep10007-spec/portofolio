import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. KONFIGURASI HALAMAN (RESPONSIF) ---
st.set_page_config(
    page_title="SIAKAD Al-Ghazali",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS CUSTOM (AGAR LEBIH CANTIK) ---
st.markdown("""
<style>
    .big-font { font-size:30px !important; font-weight: bold; color: #1E90FF; }
    .card { background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 3. STATE SESSION (SIMPAN STATUS LOGIN) ---
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# --- 4. SIDEBAR LOGIN (KUNCI RAHASIA) ---
with st.sidebar:
    st.title("🔐 Area Terbatas")
    
    if st.session_state['login_status'] == False:
        st.write("Silakan login untuk masuk ke Dashboard Admin.")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login Masuk"):
            if username == "admin" and password == "12345":
                st.session_state['login_status'] = True
                st.success("Login Berhasil!")
                st.rerun() # Refresh halaman otomatis
            else:
                st.error("Username/Password salah!")
    else:
        st.write(f"Halo, Admin Rizqi! 👋")
        if st.button("Logout Keluar"):
            st.session_state['login_status'] = False
            st.rerun()

# ========================================================
# LOGIKA PEMISAH TAMPILAN (FRONTEND VS BACKEND)
# ========================================================

if st.session_state['login_status'] == False:
    # --- TAMPILAN 1: HALAMAN DEPAN (PUBLIC / UMUM) ---
    
    # Hero Section
    st.title("🎓 Universitas Al-Ghazali")
    st.markdown("### *Mencetak Generasi Unggul di Era Digital*")
    st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", use_container_width=True)
    
    st.divider()

    # Kolom Fitur (Responsif)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h3>📚 Kurikulum Modern</h3><p>Belajar Python, AI, dan Data Science sejak semester awal.</p></div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="card"><h3>💻 Lab Komputer</h3><p>Fasilitas laboratorium canggih dengan spesifikasi tinggi.</p></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><h3>🏆 Prestasi</h3><p>Juara 1 Lomba Coding Nasional tahun 2025.</p></div>', unsafe_allow_html=True)

    # Berita Terkini
    st.subheader("📰 Berita Kampus Terkini")
    berita = {
        "Penerimaan Mahasiswa Baru 2026 Dibuka": "Segera daftarkan diri Anda sebelum kuota penuh.",
        "Seminar Nasional AI & Machine Learning": "Menghadirkan pembicara dari Google dan Tesla.",
        "Mahasiswa SI Buat Aplikasi Canggih": "Rizqi Ghani menciptakan dashboard monitoring otomatis."
    }
    
    for judul, isi in berita.items():
        with st.expander(judul):
            st.write(isi)

    # Footer
    st.markdown("---")
    st.caption("© 2026 Universitas Al-Ghazali | Web Official | Developed by Rizqi")

else:
    # --- TAMPILAN 2: HALAMAN BELAKANG (ADMIN DASHBOARD) ---
    
    st.title("⚙️ Dashboard Administrator")
    st.info("Anda berada dalam Mode Admin. Gunakan data ini dengan bijak.")
    
    # Tab Navigasi Admin
    tab1, tab2, tab3 = st.tabs(["📊 Statistik", "📂 Data Mahasiswa", "🤖 Prediksi AI"])
    
    with tab1:
        # Metrik Admin
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Pendaftar", "1,500", "+50")
        c2.metric("Mahasiswa Aktif", "1,200", "+10")
        c3.metric("Dosen", "85", "Tetap")
        c4.metric("Server Load", "34%", "-2%")
        
        # Grafik Kunjungan
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Visitor', 'Alumni'])
        st.line_chart(chart_data)

    with tab2:
        st.subheader("Database Mahasiswa SI")
        # Data Dummy
        df = pd.DataFrame({
            'NIM': [101, 102, 103, 104, 105],
            'Nama': ['Rizqi', 'Faqih', 'Andreanis', 'Toik', 'Nawalia'],
            'IPK': [3.9, 3.7, 3.8, 3.5, 3.85],
            'Status SPP': ['Lunas', 'Lunas', 'Menunggak', 'Lunas', 'Lunas']
        })
        st.dataframe(df, use_container_width=True)
        
        if st.button("Download Laporan CSV"):
            st.toast('Laporan sedang diunduh...', icon='📥')

    with tab3:
        st.subheader("Simulasi Prediksi Kelulusan")
        ipk_input = st.slider("Masukkan IPK:", 0.0, 4.0, 3.0)
        if ipk_input > 3.5:
            st.success("Prediksi: LULUS DENGAN PUJIAN (CUMLAUDE)")
        elif ipk_input > 2.75:
            st.warning("Prediksi: LULUS SANGAT MEMUASKAN")
        else:
            st.error("Prediksi: PERLU PERBAIKAN NILAI")