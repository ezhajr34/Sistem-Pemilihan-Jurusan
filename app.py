import streamlit as st

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Sistem Pakar Jurusan",
    page_icon="🎓",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2c3e50;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown('<p class="title">🎓 Sistem Pemilihan Jurusan</p>', unsafe_allow_html=True)
st.write("### Rekomendasi jurusan berdasarkan minat dan kemampuan")

# =========================
# SIDEBAR
# =========================
st.sidebar.title("ℹ️ Tentang")
st.sidebar.info("Aplikasi ini membantu menentukan jurusan yang sesuai dengan minat mahasiswa")

# =========================
# LAYOUT 2 KOLOM
# =========================
col1, col2 = st.columns(2)

# =========================
# KOLOM 1 - DATA
# =========================
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📝 Data Mahasiswa")

    nama = st.text_input("Nama")
    nim = st.text_input("NIM (10 digit)")
    kelas = st.text_input("Kelas")

    if nim and (not nim.isdigit() or len(nim) != 10):
        st.error("NIM harus 10 digit angka!")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# KOLOM 2 - MINAT
# =========================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Pilih Minat")

    ngoding = st.checkbox("💻 Suka Ngoding")
    desain = st.checkbox("🎨 Suka Desain Grafis")
    matematika = st.checkbox("📊 Suka Matematika")
    analisis = st.checkbox("📈 Suka Analisis Data")
    jaringan = st.checkbox("🌐 Suka Jaringan Komputer")
    multimedia = st.checkbox("🎬 Suka Multimedia")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# BUTTON
# =========================
st.markdown("##")
if st.button("🔍 Rekomendasi Jurusan"):

    if nama == "" or nim == "" or kelas == "":
        st.warning("Semua data harus diisi!")
    
    elif not nim.isdigit() or len(nim) != 10:
        st.warning("NIM harus 10 digit angka!")

    else:
        st.markdown("## 📊 Hasil Rekomendasi")
        st.success(f"""
        Nama   : {nama}  
        NIM    : {nim}  
        Kelas  : {kelas}
        """)

        if ngoding and matematika:
            st.info("🎯 Teknik Informatika\n\nCocok untuk pemrograman dan software.")

        elif analisis and matematika:
            st.info("📊 Sistem Informasi\n\nCocok untuk analisis data dan bisnis.")

        elif desain and multimedia:
            st.info("🎨 DKV\n\nCocok untuk desain dan kreatif.")

        elif jaringan:
            st.info("🌐 Teknik Komputer\n\nCocok untuk jaringan dan hardware.")

        elif multimedia and not ngoding:
            st.info("🎬 Multimedia\n\nCocok untuk video dan animasi.")

        else:
            st.error("Belum bisa menentukan jurusan")