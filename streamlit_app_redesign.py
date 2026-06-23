import streamlit as st
import pandas as pd

# TEMPEL DATA = [...] MILIKMU DI SINI
# Jangan ubah bagian data

st.set_page_config(
    page_title="Analisis Perilaku dan Etos Kerja",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color:#0f172a;
}
.hero {
    text-align:center;
    padding:40px;
}
.hero h1 {
    color:white;
}
.hero p {
    color:#cbd5e1;
}
</style>
""", unsafe_allow_html=True)

df = pd.DataFrame(data)

# Bersihkan baris ringkasan yang ikut masuk data
if "Timestamp" in df.columns:
    df = df[
        ~df["Timestamp"].astype(str).isin(
            ["Jenis kelamin","Usia","Status Anda saat ini","TOTAL"]
        )
    ]

menu = st.sidebar.radio(
    "📌 Menu",
    [
        "Dashboard",
        "Analisis Perilaku",
        "Analisis Etos Kerja",
        "Data Responden"
    ]
)

if menu == "Dashboard":

    st.markdown("""
    <div class='hero'>
        <h1>📊 Analisis Perilaku dan Etos Kerja</h1>
        <p>Dashboard Interaktif Hasil Survei Responden</p>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    total = len(df)

    mahasiswa = len(df[df["Status Anda saat ini"]=="Mahasiswa"])
    pekerja = len(df[df["Status Anda saat ini"]=="Pekerja"])
    keduanya = len(df[df["Status Anda saat ini"]=="Keduanya"])

    c1.metric("Total", total)
    c2.metric("Mahasiswa", mahasiswa)
    c3.metric("Pekerja", pekerja)
    c4.metric("Keduanya", keduanya)

    st.divider()

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Distribusi Jenis Kelamin")
        gender = df["  Jenis kelamin  "].value_counts()
        st.bar_chart(gender)

    with col2:
        st.subheader("Status Responden")
        status = df["Status Anda saat ini"].value_counts()
        st.bar_chart(status)

    st.success("""
    Mayoritas responden cenderung tetap tenang ketika menghadapi masalah
    dan lebih memilih mencari solusi saat rencana gagal.
    """)

elif menu == "Analisis Perilaku":

    st.title("🧠 Analisis Perilaku")

    pilihan = st.selectbox(
        "Pilih Variabel",
        [
            "Saat menghadapi masalah  ",
            "Jika ada orang melakukan kesalahan  ",
            "Ketika rencana gagal  "
        ]
    )

    hasil = df[pilihan].value_counts()

    chart_data = hasil.reset_index()
    chart_data.columns = ["Kategori","Jumlah"]

    st.bar_chart(
        chart_data.set_index("Kategori")
    )

elif menu == "Analisis Etos Kerja":

    st.title("💼 Analisis Etos Kerja")

    pilihan = st.selectbox(
        "Pilih Variabel",
        [
            "Ketika ada tugas",
            "Waktu luang  ",
            "Mendekati deadline  ",
            "Saat menghadapi kesulitan  ",
            "Beban kerja/tugas banyak  "
        ]
    )

    hasil = df[pilihan].value_counts()

    chart_data = hasil.reset_index()
    chart_data.columns = ["Kategori","Jumlah"]

    st.bar_chart(
        chart_data.set_index("Kategori")
    )

else:

    st.title("📋 Data Responden")

    cari = st.text_input("Cari Data")

    if cari:

        mask = df.astype(str).apply(
            lambda x: x.str.contains(
                cari,
                case=False,
                na=False
            )
        ).any(axis=1)

        st.dataframe(
            df[mask],
            use_container_width=True
        )

    else:
        st.dataframe(
            df,
            use_container_width=True
        )

data = [
  {
    "Timestamp": "2026-04-14 13:14:19.805000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 14:56:40.886000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 14:58:19.970000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 14:58:28.738000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 14:58:48.829000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-14 16:00:33.441000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 16:01:40.927000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 16:02:00.122000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 16:08:14.484000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-14 17:27:54.394000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-14 17:34:15.838000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-15 21:04:06.833000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-19 09:18:07.730000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-19 09:18:35.456000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-19 19:51:50.855000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 21:56:17.788000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:02:39.908000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:03:08.341000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:03:36.266000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-20 22:03:59.408000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-20 22:04:23.910000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:04:26.076000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:04:47.635000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:05:11.501000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:05:12.173000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:05:40.440000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-20 22:05:42.420000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:06:49.881000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 22:07:00.776000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-20 22:07:33.368000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya cenderung menyerah",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "2026-04-20 22:13:42.541000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 23:25:57.453000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-20 23:50:29.888000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "30 tahun >",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 18:38:47.709000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 18:39:11.271000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 18:39:36.174000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "< 20 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya sering menunda",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 18:40:07.653000",
    "Status Anda saat ini": "Pekerja",
    "  Usia  ": "26–30 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya mudah emosi",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Lebih banyak digunakan untuk santai",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 19:38:45.118000",
    "Status Anda saat ini": "Keduanya",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-21 19:39:15.758000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Laki-laki",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya langsung kesal/marah",
    "Ketika rencana gagal  ": "Saya cepat frustrasi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Sudah selesai sebelumnya",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya tetap berusaha menyelesaikan"
  },
  {
    "Timestamp": "2026-04-28 16:12:15.068000",
    "Status Anda saat ini": "Mahasiswa",
    "  Usia  ": "20–25 tahun",
    "  Jenis kelamin  ": "Perempuan",
    "Saat menghadapi masalah  ": "Saya tetap tenang",
    "Jika ada orang melakukan kesalahan  ": "Saya mencoba memahami dulu",
    "Ketika rencana gagal  ": "Saya mencari solusi",
    "Ketika ada tugas": "Saya langsung mengerjakan",
    "Waktu luang  ": "Digunakan untuk hal produktif",
    "Mendekati deadline  ": "Baru mulai mengerjakan",
    "Saat menghadapi kesulitan  ": "Saya terus mencoba",
    "Beban kerja/tugas banyak  ": "Saya merasa kewalahan dan berhenti"
  },
  {
    "Timestamp": "Jenis kelamin",
    "Status Anda saat ini": "Frequency",
    "  Usia  ": "Precent",
    "  Jenis kelamin  ": "Komulatif",
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Laki-laki",
    "Status Anda saat ini": 25.0,
    "  Usia  ": 0.625,
    "  Jenis kelamin  ": 0.625,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Perempuan",
    "Status Anda saat ini": 15.0,
    "  Usia  ": 0.375,
    "  Jenis kelamin  ": 1,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "TOTAL",
    "Status Anda saat ini": 40,
    "  Usia  ": 1,
    "  Jenis kelamin  ": None,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Usia",
    "Status Anda saat ini": "Frequency",
    "  Usia  ": "Precent",
    "  Jenis kelamin  ": "Komulatif",
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "< 20 tahun",
    "Status Anda saat ini": 9.0,
    "  Usia  ": 0.225,
    "  Jenis kelamin  ": 0.225,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "20–25 tahun",
    "Status Anda saat ini": 20.0,
    "  Usia  ": 0.5,
    "  Jenis kelamin  ": 0.725,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "26–30 tahun",
    "Status Anda saat ini": 10.0,
    "  Usia  ": 0.25,
    "  Jenis kelamin  ": 0.975,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "30 tahun >",
    "Status Anda saat ini": 1.0,
    "  Usia  ": 0.025,
    "  Jenis kelamin  ": 1,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "TOTAL",
    "Status Anda saat ini": 40.0,
    "  Usia  ": None,
    "  Jenis kelamin  ": None,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Status Anda saat ini",
    "Status Anda saat ini": "Frequency",
    "  Usia  ": "Precent",
    "  Jenis kelamin  ": "Komulatif",
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Mahasiswa",
    "Status Anda saat ini": 21.0,
    "  Usia  ": 0.525,
    "  Jenis kelamin  ": 0.525,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Pekerja",
    "Status Anda saat ini": 9.0,
    "  Usia  ": 0.225,
    "  Jenis kelamin  ": 0.75,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "Keduanya",
    "Status Anda saat ini": 10.0,
    "  Usia  ": 0.25,
    "  Jenis kelamin  ": 1,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  },
  {
    "Timestamp": "TOTAL",
    "Status Anda saat ini": 40.0,
    "  Usia  ": None,
    "  Jenis kelamin  ": None,
    "Saat menghadapi masalah  ": None,
    "Jika ada orang melakukan kesalahan  ": None,
    "Ketika rencana gagal  ": None,
    "Ketika ada tugas": None,
    "Waktu luang  ": None,
    "Mendekati deadline  ": None,
    "Saat menghadapi kesulitan  ": None,
    "Beban kerja/tugas banyak  ": None
  }
]

st.set_page_config(page_title="Analisis Perilaku dan Etos Kerja", page_icon="📊", layout="wide")

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}
.hero {
    text-align:center;
    padding:40px 10px;
}
.hero h1 {color:white;font-size:3rem;}
.hero p {color:#cbd5e1;font-size:1.1rem;}
</style>
""", unsafe_allow_html=True)

df = pd.DataFrame(data)

if "Timestamp" in df.columns:
    df = df[~df["Timestamp"].astype(str).isin(["Jenis kelamin","Usia","Status Anda saat ini","TOTAL"])]

menu = st.sidebar.radio(
    "📌 Menu",
    ["Dashboard","Analisis Perilaku","Analisis Etos Kerja","Data Responden"]
)

if menu == "Dashboard":
    st.markdown("""
    <div class="hero">
        <h1>📊 Analisis Perilaku dan Etos Kerja</h1>
        <p>Dashboard Interaktif Hasil Survei Responden</p>
    </div>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    total = len(df)
    mahasiswa = len(df[df["Status Anda saat ini"]=="Mahasiswa"])
    pekerja = len(df[df["Status Anda saat ini"]=="Pekerja"])
    keduanya = len(df[df["Status Anda saat ini"]=="Keduanya"])

    c1.metric("Total", total)
    c2.metric("Mahasiswa", mahasiswa)
    c3.metric("Pekerja", pekerja)
    c4.metric("Keduanya", keduanya)

    col1,col2 = st.columns(2)

    gender = df["  Jenis kelamin  "].value_counts()
    fig1 = px.pie(values=gender.values,names=gender.index,hole=.5,title="Distribusi Jenis Kelamin")

    status = df["Status Anda saat ini"].value_counts()
    fig2 = px.bar(x=status.index,y=status.values,title="Status Responden")

    col1.plotly_chart(fig1,use_container_width=True)
    col2.plotly_chart(fig2,use_container_width=True)

    st.info("Mayoritas responden cenderung tetap tenang saat menghadapi masalah dan lebih memilih mencari solusi ketika rencana gagal.")

elif menu == "Analisis Perilaku":
    pilihan = st.selectbox(
        "Pilih Variabel",
        [
            "Saat menghadapi masalah  ",
            "Jika ada orang melakukan kesalahan  ",
            "Ketika rencana gagal  "
        ]
    )

    hasil = df[pilihan].value_counts()
    fig = px.bar(x=hasil.index,y=hasil.values,title=pilihan)
    st.plotly_chart(fig,use_container_width=True)

elif menu == "Analisis Etos Kerja":
    pilihan = st.selectbox(
        "Pilih Variabel",
        [
            "Ketika ada tugas",
            "Waktu luang  ",
            "Mendekati deadline  ",
            "Saat menghadapi kesulitan  ",
            "Beban kerja/tugas banyak  "
        ]
    )

    hasil = df[pilihan].value_counts()
    fig = px.bar(x=hasil.index,y=hasil.values,title=pilihan)
    st.plotly_chart(fig,use_container_width=True)

else:
    cari = st.text_input("🔍 Cari Data")

    if cari:
        mask = df.astype(str).apply(lambda x: x.str.contains(cari,case=False,na=False)).any(axis=1)
        st.dataframe(df[mask], use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)
