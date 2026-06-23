
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard Premium Etos Kerja", layout="wide", page_icon="📊")

st.markdown("""
<style>
.stApp {background:#0f172a;}
h1,h2,h3,p,label {color:white !important;}
[data-testid="metric-container"]{
background:#1e293b;
border:1px solid #334155;
padding:15px;
border-radius:16px;
}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_excel("Analisis Perilaku dan Etos Kerja (1)(1).xlsx")

df = load_data()
df = df[df["Saat menghadapi masalah  "].notna()]

st.title("📊 Dashboard Premium Analisis Perilaku & Etos Kerja")
st.caption("Visualisasi Interaktif Hasil Penelitian")

# KPI
total = len(df)
tenang = (df["Saat menghadapi masalah  "]=="Saya tetap tenang").sum()
gigih = (df["Saat menghadapi kesulitan  "]=="Saya terus mencoba").sum()

c1,c2,c3 = st.columns(3)
c1.metric("Total Responden", total)
c2.metric("Tetap Tenang", tenang)
c3.metric("Gigih", gigih)

st.divider()

tab1,tab2,tab3,tab4 = st.tabs([
"📈 Dashboard Utama",
"🎯 Radar Analisis",
"👥 Demografi",
"🤖 Insight"
])

with tab1:

    col1,col2 = st.columns(2)

    with col1:
        fig = px.pie(
            df,
            names="Saat menghadapi masalah  ",
            title="Respon Saat Menghadapi Masalah",
            hole=.5
        )
        st.plotly_chart(fig,use_container_width=True)

    with col2:
        fig = px.pie(
            df,
            names="Mendekati deadline  ",
            title="Perilaku Menjelang Deadline",
            hole=.5
        )
        st.plotly_chart(fig,use_container_width=True)

    vc = df["Beban kerja/tugas banyak  "].value_counts().reset_index()
    vc.columns=["Kategori","Jumlah"]
    fig = px.bar(
        vc,
        x="Jumlah",
        y="Kategori",
        orientation="h",
        title="Respons Terhadap Beban Kerja"
    )
    st.plotly_chart(fig,use_container_width=True)

with tab2:

    radar_data = {
        "Ketahanan":[gigih],
        "Ketenangan":[tenang],
        "Tanggung Jawab":[(df["Ketika ada tugas"]=="Saya segera mengerjakannya").sum()],
        "Disiplin":[(df["Mendekati deadline  "]=="Saya sudah hampir selesai").sum()],
        "Konsistensi":[(df["Beban kerja/tugas banyak  "]=="Saya tetap berusaha menyelesaikan").sum()]
    }

    categories=list(radar_data.keys())
    values=[v[0] for v in radar_data.values()]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Skor'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True)),
        title="Radar Karakter Etos Kerja"
    )
    st.plotly_chart(fig,use_container_width=True)

    score = round(sum(values)/(total*len(values))*100,1)

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text':"Skor Etos Kerja"},
        gauge={'axis':{'range':[0,100]}}
    ))
    st.plotly_chart(gauge,use_container_width=True)

with tab3:

    if "  Jenis kelamin  " in df.columns:
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

    st.subheader("Insight Otomatis")

    st.success(f"""
    Total responden sebanyak {total} orang.

    • {tenang} responden cenderung tetap tenang saat menghadapi masalah.
    • {gigih} responden menunjukkan kegigihan saat menghadapi kesulitan.
    • Skor etos kerja keseluruhan mencapai {score}%.
    • Mayoritas responden menunjukkan tanggung jawab dan daya tahan kerja yang baik.
    """)

    st.info("""
    Kesimpulan:
    Secara umum responden memiliki karakter etos kerja yang positif,
    ditunjukkan oleh kemampuan menghadapi tekanan, menyelesaikan tugas,
    dan mempertahankan usaha saat mengalami kesulitan.
    """)
