
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Dashboard Etos Kerja Premium", layout="wide", page_icon="📊")

st.markdown("""
<style>
.stApp {background-color:#0b1220;}
[data-testid="metric-container"]{
background:#111827;
border:1px solid #374151;
padding:15px;
border-radius:15px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard Premium Analisis Perilaku & Etos Kerja")
st.caption("Dashboard penelitian siap presentasi")

excel_files = list(Path(".").glob("*.xlsx"))

if not excel_files:
    st.error("File Excel tidak ditemukan di repository GitHub.")
    st.stop()

df = pd.read_excel(excel_files[0])

# hapus baris kosong
df = df[df["Saat menghadapi masalah  "].notna()]

# KPI
total = len(df)
tenang = (df["Saat menghadapi masalah  "]=="Saya tetap tenang").sum()
gigih = (df["Saat menghadapi kesulitan  "]=="Saya terus mencoba").sum()
disiplin = (df["Mendekati deadline  "]=="Saya sudah hampir selesai").sum()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Total Responden", total)
c2.metric("Tetap Tenang", tenang)
c3.metric("Gigih", gigih)
c4.metric("Disiplin Deadline", disiplin)

st.divider()

with st.sidebar:
    st.header("Filter")
    gender = st.multiselect(
        "Jenis Kelamin",
        df["  Jenis kelamin  "].dropna().unique(),
        default=df["  Jenis kelamin  "].dropna().unique()
    )

df = df[df["  Jenis kelamin  "].isin(gender)]

tab1,tab2,tab3,tab4 = st.tabs([
    "📈 Dashboard",
    "🎯 Radar",
    "👥 Demografi",
    "🤖 Insight"
])

with tab1:

    a,b = st.columns(2)

    with a:
        fig = px.pie(
            df,
            names="Saat menghadapi masalah  ",
            hole=0.55,
            title="Respon Saat Menghadapi Masalah"
        )
        st.plotly_chart(fig,use_container_width=True)

    with b:
        fig = px.pie(
            df,
            names="Mendekati deadline  ",
            hole=0.55,
            title="Perilaku Menjelang Deadline"
        )
        st.plotly_chart(fig,use_container_width=True)

    vc = df["Beban kerja/tugas banyak  "].value_counts().reset_index()
    vc.columns=["Kategori","Jumlah"]

    fig = px.bar(
        vc,
        y="Kategori",
        x="Jumlah",
        orientation="h",
        title="Respons Terhadap Beban Kerja"
    )
    st.plotly_chart(fig,use_container_width=True)

with tab2:

    indikator = [
        tenang,
        gigih,
        disiplin,
        (df["Ketika ada tugas"]=="Saya segera mengerjakannya").sum(),
        (df["Beban kerja/tugas banyak  "]=="Saya tetap berusaha menyelesaikan").sum()
    ]

    kategori = [
        "Tenang",
        "Gigih",
        "Disiplin",
        "Tanggung Jawab",
        "Konsistensi"
    ]

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=indikator,
        theta=kategori,
        fill="toself"
    ))

    radar.update_layout(title="Radar Karakter Etos Kerja")
    st.plotly_chart(radar,use_container_width=True)

    score = round(sum(indikator)/(len(indikator)*max(total,1))*100,1)

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text":"Skor Etos Kerja (%)"},
        gauge={"axis":{"range":[0,100]}}
    ))
    st.plotly_chart(gauge,use_container_width=True)

with tab3:

    fig = px.histogram(
        df,
        x="  Jenis kelamin  ",
        title="Distribusi Jenis Kelamin"
    )
    st.plotly_chart(fig,use_container_width=True)

    fig = px.histogram(
        df,
        x="  Usia  ",
        title="Distribusi Usia"
    )
    st.plotly_chart(fig,use_container_width=True)

with tab4:

    score = round((tenang + gigih + disiplin)/(3*max(total,1))*100,1)

    st.success(f"""
    Total responden: {total} orang
    
    • Tetap tenang saat masalah: {tenang} responden
    • Gigih menghadapi kesulitan: {gigih} responden
    • Disiplin terhadap deadline: {disiplin} responden
    
    Skor etos kerja keseluruhan: {score}%
    """)

    st.dataframe(df.head(10), use_container_width=True)
