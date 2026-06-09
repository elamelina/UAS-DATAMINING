# 🩺 Aplikasi Prediksi Diabetes Menggunakan Support Vector Machine (SVM)

Proyek ini merupakan implementasi **Data Mining** untuk mendeteksi dini indikasi penyakit Diabetes Melitus pada pasien. Aplikasi ini dibangun berbasis web menggunakan framework **Streamlit** dan menggunakan model klasifikasi **Support Vector Machine (SVM)** yang dilatih dengan *Pima Indians Diabetes Dataset*.

Proyek ini diajukan untuk memenuhi tugas akhir kelompok pada mata kuliah **UAS Data Mining**.

---

## 👥 Anggota Kelompok 5 (Teknik Informatika 6C)
Aplikasi ini dikembangkan oleh Kelompok 5 kelas TI 6C dari **Universitas Islam Negeri Sultan Syarif Kasim Riau**:

| Nama Anggota | NIM | Peran / Kontribusi |
| :--- | :---: | :--- |
| **Ela Melina** | `12350121201` | Data Preprocessing & Modeling SVM |
| **Hairunisha** | `12350121408` | Desain UI/UX & Implementasi Streamlit |
| **Naya Nabila** | `12350121319` | Penyusunan Literatur & Analisis Dataset |

---

## 📊 Spesifikasi & Atribut Dataset
Dataset yang digunakan adalah **Pima Indians Diabetes Dataset** (sumber: UCI Machine Learning / Kaggle) dengan total **768 records data medis** pasien perempuan keturunan suku Pima. 

Model memproses 8 parameter klinis (fitur) berikut untuk melakukan prediksi:
1. `Pregnancies`: Jumlah kehamilan pasien.
2. `Glucose`: Kadar glukosa plasma dalam tes toleransi glukosa oral 2 jam.
3. `Blood Pressure`: Tekanan darah diastolik (mm Hg).
4. `Skin Thickness`: Ketebalan lipatan kulit trisep (mm).
5. `Insulin`: Kadar insulin serum 2 jam (mu U/ml).
6. `BMI`: Body Mass Index (Berat badan dalam kg / (Tinggi badan dalam m)²).
7. `Diabetes Pedigree Function`: Skor riwayat genetik diabetes dalam keluarga.
8. `Age`: Usia pasien (tahun).

* **Target Variabel (Outcome):** Kelas biner (`0`: Tidak Terindikasi, `1`: Terindikasi Diabetes).
* **Akurasi Model:** **77.27%** menggunakan algoritma Support Vector Machine (SVM).

---

## 🚀 Fitur Utama Aplikasi
* **Dashboard Panel Modern:** Tampilan UI interaktif dengan kartu metrik performa algoritma.
* **Informasi Edukasi Interaktif:** Menggunakan kustomisasi CSS tingkat lanjut untuk menampilkan tipe, gejala, pencegahan, dan komplikasi diabetes secara visual di dalam tab expander.
* **Form Input Valid:** Pengisian data klinis pasien dengan batas minimum angka dinamis.
* **Hasil Diagnosa & Bar Risiko:** Sistem tidak hanya memberikan hasil status klasifikasi, tetapi juga menampilkan visualisasi persentase tingkat risiko diabetes menggunakan komponen `st.progress`.

---

## 🛠️ Panduan Instalasi dan Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer lokal Anda:

### 1. Clone Repositori
```bash
git clone (https://github.com/elamelina/UAS-DATAMINING.git)
cd nama-repo-anda
