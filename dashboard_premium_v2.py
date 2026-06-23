
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Etos Kerja", layout="wide", page_icon="📊")

st.markdown("""
<style>
.main {padding-top:1rem;}
.metric-card{
background: linear-gradient(135deg,#0f172a,#1e293b);
padding:15px;border-radius:15px;color:white;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard Premium Analisis Perilaku & Etos Kerja")
st.caption("Visualisasi hasil survei responden")

uploaded = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded:
    df = pd.read_excel(uploaded)
else:
    st.info("Upload file Excel survei untuk memulai.")
    st.stop()

df = df[df["Saat menghadapi masalah  "].notna()]

st.sidebar.header("Filter")
if "  Jenis kelamin  " in df.columns:
    gender = st.sidebar.multiselect(
        "Jenis Kelamin",
        df["  Jenis kelamin  "].dropna().unique(),
        default=df["  Jenis kelamin  "].dropna().unique()
    )
    df = df[df["  Jenis kelamin  "].isin(gender)]

total = len(df)

tenang = (df["Saat menghadapi masalah  "]=="Saya tetap tenang").sum()
gigih = (df["Saat menghadapi kesulitan  "]=="Saya terus mencoba").sum()

c1,c2,c3 = st.columns(3)
c1.metric("Total Responden", total)
c2.metric("Tetap Tenang", tenang)
c3.metric("Gigih Menghadapi Kesulitan", gigih)

st.divider()

tab1,tab2,tab3 = st.tabs(["📈 Perilaku","💼 Etos Kerja","📋 Data"])

with tab1:
    a,b = st.columns(2)

    with a:
        fig = px.pie(df,names="Saat menghadapi masalah  ",
                     title="Respon Saat Menghadapi Masalah")
        st.plotly_chart(fig,use_container_width=True)

    with b:
        fig = px.pie(df,names="Jika ada orang melakukan kesalahan  ",
                     title="Sikap terhadap Kesalahan Orang Lain")
        st.plotly_chart(fig,use_container_width=True)

    vc = df["Ketika rencana gagal  "].value_counts().reset_index()
    vc.columns=["Kategori","Jumlah"]
    fig = px.bar(vc,x="Kategori",y="Jumlah",text="Jumlah",
                 title="Respons Saat Rencana Gagal")
    st.plotly_chart(fig,use_container_width=True)

with tab2:
    vc = df["Beban kerja/tugas banyak  "].value_counts().reset_index()
    vc.columns=["Kategori","Jumlah"]
    fig = px.bar(vc,y="Kategori",x="Jumlah",orientation="h",
                 title="Respons terhadap Beban Kerja")
    st.plotly_chart(fig,use_container_width=True)

    fig = px.pie(df,names="Mendekati deadline  ",
                 title="Perilaku Menjelang Deadline")
    st.plotly_chart(fig,use_container_width=True)

with tab3:
    st.dataframe(df,use_container_width=True)
