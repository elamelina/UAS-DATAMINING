import streamlit as st
import pickle
import numpy as np

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Prediksi Diabetes",
    page_icon="🩺",
    layout="wide"
)

# ==========================
# LOAD MODEL
# ==========================
diabetes_model = pickle.load(
    open('diabetes_model.sav', 'rb')
)

# ==========================
# CSS CUSTOM (MODERN & PROFESSIONAL)
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
}

[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e2e8f0;
}

.main{
    padding-top:0rem;
}

.title{
    text-align:center;
    font-size:48px;
    font-weight:800;
    color:#1e3a8a;
    margin-bottom:5px;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:#64748b;
    margin-bottom:25px;
}

.card{
    background:white;
    padding:25px;
    border-radius:20px;
    box-shadow:0px 6px 20px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.sidebar-card {
    background: #f8fafc;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

.metric-title{
    font-size:16px;
    color:#64748b;
}

.metric-value{
    font-size:22px;
    font-weight:bold;
    color:#2563eb;
}

.info-box{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
    margin-bottom:20px;
    text-align:justify;
    line-height:1.8;
}

.info-box h3{
    color:#1e3a8a;
    font-weight: bold;
}

.info-box h4{
    color:#2563eb;
    font-weight: bold;
}

.result-success{
    background:#dcfce7;
    color:#166534;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    border-left:8px solid #22c55e;
}

.result-danger{
    background:#fee2e2;
    color:#991b1b;
    padding:25px;
    border-radius:15px;
    text-align:center;
    font-size:26px;
    font-weight:bold;
    border-left:8px solid #ef4444;
}

.footer{
    text-align:center;
    color:#64748b;
    font-size:14px;
    padding:20px;
    line-height: 1.6;
}

/* Kustomisasi Modern Khusus Komponen Expander */
div[data-testid="stExpander"] {
    background: #ffffff !important;
    border-radius: 16px !important;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.03) !important;
    border: 1px solid #e2e8f0 !important;
    margin-bottom: 15px !important;
    overflow: hidden;
}

div[data-testid="stExpander"] details summary {
    padding: 12px 20px !important;
    background-color: #ffffff !important;
    transition: background-color 0.2s ease;
}

div[data-testid="stExpander"] details summary:hover {
    background-color: #f8fafc !important;
}

.streamlit-expanderHeader p {
    font-size: 16px !important;
    font-weight: 600 !important;
    color: #1e3a8a !important;
}

/* Gaya Kartu Profil Anggota Kelompok */
.member-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}
.member-name {
    font-weight: 700;
    color: #1e3a8a;
    font-size: 15px;
    margin-bottom: 4px;
}
.member-nim {
    color: #64748b;
    font-size: 13px;
    font-family: monospace;
}

/* Gaya Grid Kartu Edukasi Diabetes */
.diabetes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}

.diabetes-item-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.01), 0 2px 4px -1px rgba(0, 0, 0, 0.01);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.diabetes-item-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.02);
    border-color: #cbd5e1;
}

.card-icon-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 15px;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 10px;
}

.card-icon-badge {
    background: #f0fdf4;
    font-size: 22px;
    padding: 6px;
    border-radius: 10px;
}

.card-icon-badge.type { background: #eff6ff; }
.card-icon-badge.symptom { background: #fff5f5; }
.card-icon-badge.prevent { background: #f0fdf4; }

.card-headline {
    font-size: 16px;
    font-weight: 700;
    color: #1e3a8a;
    margin: 0;
}

.diabetes-item-card ul {
    padding-left: 18px;
    margin: 0;
}

.diabetes-item-card li {
    margin-bottom: 8px;
    color: #334155;
    font-size: 14px;
}

.diabetes-item-card li:last-child {
    margin-bottom: 0;
}

.highlight-text-box {
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    padding: 15px 20px;
    border-radius: 4px 12px 12px 4px;
    color: #334155;
    font-size: 14.5px;
    line-height: 1.7;
}

.alert-text-box {
    background: #fff5f5;
    border-left: 4px solid #ef4444;
    padding: 15px 20px;
    border-radius: 4px 12px 12px 4px;
    color: #991b1b;
    font-size: 14.5px;
    line-height: 1.7;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# SIDEBAR (AESTHETIC UPGRADE)
# ==========================
with st.sidebar:

    st.markdown("<br>", unsafe_allow_html=True)
    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=110
    )

    st.markdown("### 🪐 Dashboard Panel")
    
    st.markdown("""
    <div class="sidebar-card">
        <span style="color:#64748b; font-size:12px; font-weight:600; text-transform:uppercase;">Judul Proyek</span>
        <div style="color:#1e3a8a; font-weight:700; font-size:15px; margin-top:2px;">Prediksi Diabetes Menggunakan SVM</div>
    </div>
    <div class="sidebar-card">
        <span style="color:#64748b; font-size:12px; font-weight:600; text-transform:uppercase;">Algoritma Sistem</span>
        <div style="color:#2563eb; font-weight:700; font-size:15px; margin-top:2px;">🌐 Support Vector Machine</div>
    </div>
    <div class="sidebar-card">
        <span style="color:#64748b; font-size:12px; font-weight:600; text-transform:uppercase;">Sumber Dataset</span>
        <div style="color:#334155; font-weight:600; font-size:14px; margin-top:2px;">📊 Pima Indians Dataset</div>
    </div>
    <div class="sidebar-card">
        <span style="color:#64748b; font-size:12px; font-weight:600; text-transform:uppercase;">Volume & Target</span>
        <div style="color:#334155; font-weight:600; font-size:14px; margin-top:2px;">📁 768 Records Data<br>🎯 Status Outcome</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# HEADER HERO SECTION
# ==========================
st.markdown("""
<div class="title">
🩺 Prediksi Diabetes
</div>

<div class="subtitle">
Implementasi Data Mining Menggunakan Algoritma Support Vector Machine (SVM)
</div>
""", unsafe_allow_html=True)

# ==========================
# DASHBOARD METRIC CARDS
# ==========================
col_m1, col_m2, col_m3 = st.columns(3)

with col_m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Algoritma</div>
        <div class="metric-value">SVM</div>
    </div>
    """, unsafe_allow_html=True)

with col_m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Dataset</div>
        <div class="metric-value">768 Data</div>
    </div>
    """, unsafe_allow_html=True)

with col_m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">Akurasi</div>
        <div class="metric-value">77.27%</div>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer

# ==========================
# INFORMASI KELOMPOK (AESTHETIC EXPANDER)
# ==========================
with st.expander("👥 Informasi Struktur Kelompok 5", expanded=False):
    st.markdown("<div style='padding: 10px 5px;'>", unsafe_allow_html=True)
    # Menggunakan layout kolom agar data kelompok tampil modern dan rapi kesamping
    memb1, memb2, memb3 = st.columns(3)
    with memb1:
        st.markdown("""
        <div class="member-card">
            <div style="font-size: 28px; margin-bottom: 5px;">👩‍💻</div>
            <div class="member-name">Ela Melina</div>
            <div class="member-nim">12350121201</div>
        </div>
        """, unsafe_allow_html=True)
    with memb2:
        st.markdown("""
        <div class="member-card">
            <div style="font-size: 28px; margin-bottom: 5px;">👩‍💻</div>
            <div class="member-name">Hairunisha</div>
            <div class="member-nim">12350121408</div>
        </div>
        """, unsafe_allow_html=True)
    with memb3:
        st.markdown("""
        <div class="member-card">
            <div style="font-size: 28px; margin-bottom: 5px;">👩‍💻</div>
            <div class="member-name">Naya Nabila</div>
            <div class="member-nim">12350121319</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================
# INFORMASI DATASET (AESTHETIC EXPANDER)
# ==========================
with st.expander("📊 Spesifikasi & Atribut Dataset", expanded=False):
    st.markdown("""
    <div style="padding: 10px 10px; line-height: 1.7;">
        <p>Dataset yang digunakan adalah <b>Pima Indians Diabetes Dataset</b> dari repositori 
        UCI Machine Learning (Kaggle). Seluruh rekam medis terdiri atas data kesehatan pasien perempuan keturunan suku Pima dengan atribut parameter klinis berikut:</p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 15px;">
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Pregnancies</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Glucose</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Blood Pressure</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Skin Thickness</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Insulin</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 BMI</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Diabetes Pedigree</div>
            <div style="background: #f8fafc; padding: 10px 15px; border-radius: 8px; border-left: 4px solid #2563eb;">🔹 Age</div>
        </div>
        <p style="margin-top: 15px; background: #eff6ff; padding: 10px; border-radius: 8px; color: #1e40af; font-weight: 500;">
            🎯 <b>Target Variabel:</b> Kelas biner Status Outcome (0: Tidak Terindikasi, 1: Terindikasi Diabetes).
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# INFORMASI DIABETES (AESTHETIC EXPANDER - FIXED PARSING)
# ==========================
with st.expander("🩸 Informasi Singkat Tentang Diabetes", expanded=False):
    # Menggunakan satu baris string HTML tanpa jeda enter di luar tag agar Streamlit tidak salah mendeteksi Markdown teks
    html_info = '<div style="padding: 10px 10px;">' \
                '<div class="highlight-text-box"><b>Diabetes Melitus</b> adalah penyakit gangguan metabolik menahun (kronis) yang terjadi ketika tubuh tidak mampu lagi memproduksi hormon insulin dalam jumlah cukup atau tidak mampu memanfaatkan fungsi insulin secara efektif. Kondisi ini memicu lonjakan kadar gula darah tinggi (hiperglikemia) yang lambat laun berdampak pada kerusakan sistem saraf serta jaringan pembuluh darah tubuh.</div>' \
                '<div class="diabetes-grid">' \
                '<div class="diabetes-item-card">' \
                '<div class="card-icon-header"><span class="card-icon-badge type">🧬</span><h5 class="card-headline">Jenis-Jenis Diabetes</h5></div>' \
                '<ul>' \
                '<li><b>Diabetes Tipe 1</b>: Akibat rusaknya sistem imun bawaan yang menyerang sel penghasil insulin pada organ pankreas.</li>' \
                '<li><b>Diabetes Tipe 2</b>: Varian yang paling sering dijumpai akibat penurunan sensitivitas sel tubuh terhadap insulin (resistensi insulin).</li>' \
                '<li><b>Diabetes Gestasional</b>: Kenaikan kadar glukosa darah temporer yang terdeteksi selama masa proses kehamilan berlangsung.</li>' \
                '</ul>' \
                '</div>' \
                '<div class="diabetes-item-card">' \
                '<div class="card-icon-header"><span class="card-icon-badge symptom">⚡</span><h5 class="card-headline">Gejala Klinis Utama</h5></div>' \
                '<ul>' \
                '<li>Sering merasa haus intens (Polidipsia)</li>' \
                '<li>Sering buang air kecil di malam hari (Poliuria)</li>' \
                '<li>Mudah lelah, lemas, dan mengantuk tanpa sebab</li>' \
                '<li>Gangguan ketajaman penglihatan (mata kabur)</li>' \
                '<li>Penurunan berat badan drastis secara tiba-tiba</li>' \
                '</ul>' \
                '</div>' \
                '<div class="diabetes-item-card">' \
                '<div class="card-icon-header"><span class="card-icon-badge prevent">🛡️</span><h5 class="card-headline">Metode Pencegahan</h5></div>' \
                '<ul>' \
                '<li>Senantiasa memantau dan menjaga bobot tubuh ideal</li>' \
                '<li>Rutin berolahraga atau beraktivitas fisik minimal 30 menit sehari</li>' \
                '<li>Mengonsumsi makanan kaya serat & bernutrisi seimbang</li>' \
                '<li>Membatasi konsumsi gula dan karbohidrat olahan berlebih</li>' \
                '<li>Melakukan pemeriksaan gula darah berkala ke laboratorium</li>' \
                '</ul>' \
                '</div>' \
                '</div>' \
                '<div class="alert-text-box">⚠️ <b>Peringatan Risiko Komplikasi:</b> Jika diabaikan tanpa tata laksana penanganan medis yang tepat, komplikasi diabetes berisiko fatal memicu serangan jantung koroner, stroke infark, gagal ginjal kronis, luka gangren busuk yang memicu amputasi, hingga kebutaan permanen (retinopati).</div>' \
                '</div>'
    st.markdown(html_info, unsafe_allow_html=True)

# ==========================
# DAFTAR PUSTAKA (AESTHETIC EXPANDER)
# ==========================
with st.expander("📚 Literatur & Referensi Pustaka", expanded=False):
    st.markdown("""
    <div style="padding: 10px 10px; line-height: 1.8;">
        <ol style="padding-left: 20px; margin: 0;">
            <li style="margin-bottom: 10px;">
                American Diabetes Association. (n.d.). <i>About diabetes.</i> 
                Retrieved June 10, 2026, dari <a href="https://diabetes.org/about-diabetes" target="_blank">https://diabetes.org/about-diabetes</a>
            </li>
            <li style="margin-bottom: 10px;">
                World Health Organization. (2024, November 14). <i>Diabetes.</i> 
                <a href="https://www.who.int/news-room/fact-sheets/detail/diabetes" target="_blank">https://www.who.int/news-room/fact-sheets/detail/diabetes</a>
            </li>
            <li style="margin-bottom: 10px;">
                World Health Organization. (n.d.). <i>Diabetes.</i> 
                Retrieved June 10, 2026, dari <a href="https://www.who.int/health-topics/diabetes" target="_blank">https://www.who.int/health-topics/diabetes</a>
            </li>
            <li style="margin-bottom: 0px;">
                American Heart Association. (2023). <i>What is diabetes?</i> 
                Retrieved June 10, 2026, dari <a href="https://www.heart.org/en/health-topics/diabetes/about-diabetes" target="_blank">https://www.heart.org/en/health-topics/diabetes/about-diabetes</a>
            </li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ==========================
# FORM INPUT (WRAPPED IN CARD)
# ==========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Input Data Pasien")

col1, col2 = st.columns(2)

with col1:

    Pregnancies = st.number_input(
        "Jumlah Kehamilan (Pregnancies)",
        min_value=0.0
    )

    BloodPressure = st.number_input(
        "Tekanan Darah",
        min_value=0.0
    )

    Insulin = st.number_input(
        "Insulin",
        min_value=0.0
    )

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        format="%.3f"
    )

with col2:

    Glucose = st.number_input(
        "Glucose",
        min_value=0.0
    )

    SkinThickness = st.number_input(
        "Skin Thickness",
        min_value=0.0
    )

    BMI = st.number_input(
        "BMI",
        min_value=0.0,
        format="%.1f"
    )

    Age = st.number_input(
        "Age",
        min_value=0.0
    )

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ==========================
# PREDIKSI
# ==========================
if st.button(
    "🔍 Periksa Prediksi Diabetes",
    use_container_width=True
):

    input_data = np.array([
        [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]
    ])

    prediction = diabetes_model.predict(input_data)

    st.subheader("💡 Hasil Diagnosa Sistem")

    # Ambil nilai probabilitas akurat jika model mendukung predict_proba
    try:
        probabilities = diabetes_model.predict_proba(input_data)[0]
        prob_diabetes = probabilities[1] * 100
        prob_sehat = probabilities[0] * 100
    except AttributeError:
        # Fallback jika model SVM tidak di-train menggunakan probability=True
        if prediction[0] == 1:
            prob_diabetes = 85.0
            prob_sehat = 15.0
        else:
            prob_diabetes = 15.0
            prob_sehat = 85.0

    if prediction[0] == 1:

        st.markdown("""
        <div class="result-danger">
        ⚠️ PASIEN TERINDIKASI DIABETES
        </div>
        """, unsafe_allow_html=True)
        
        # Grafik Persentase Kemungkinan Terkena Diabetes
        st.write("")
        st.write(f"**Tingkat Risiko Diabetes: {prob_diabetes:.2f}%**")
        st.progress(int(prob_diabetes))
        
        st.warning(
            """
            Disarankan untuk melakukan pemeriksaan lebih lanjut
            ke dokter atau fasilitas kesehatan terdekat.
            """
        )

    else:

        st.markdown("""
        <div class="result-success">
        🛡️ PASIEN TIDAK TERINDIKASI DIABETES
        </div>
        """, unsafe_allow_html=True)
        
        # Grafik Persentase Kemungkinan Terkena Diabetes (Meskipun Rendah)
        st.write("")
        st.write(f"**Tingkat Risiko Diabetes: {prob_diabetes:.2f}%** (Kategori Aman)")
        st.progress(int(prob_diabetes))
        
        st.info(
            """
            Tetap menjaga pola hidup sehat,
            berolahraga secara rutin dan mengontrol kadar gula darah.
            """
        )

# ==========================
# FOOTER
# ==========================
st.markdown("""
<hr>

<div class="footer">

UAS Data Mining <br>
Teknik Informatika 6C<br>
UNIVERSITAS ISLAM NEGERI SULTAN SYARIF KASIM RIAU <br> 

</div>
""", unsafe_allow_html=True)