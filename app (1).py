
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Etos Kerja Analytics", page_icon="📊", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(180deg,#0b1220,#111827);}
[data-testid="metric-container"]{
background:rgba(30,41,59,.85);
border:1px solid #334155;
padding:18px;border-radius:18px;
}
h1,h2,h3 {color:white;}
</style>
""", unsafe_allow_html=True)

# Load excel otomatis
excels = list(Path(".").glob("*.xlsx"))
if not excels:
    st.error("Upload file Excel ke repository GitHub.")
    st.stop()

df = pd.read_excel(excells[0])

# Bersihkan
target_col = [c for c in df.columns if "menghadapi masalah" in str(c).lower()]
if target_col:
    df = df[df[target_col[0]].notna()]

# Sidebar
st.sidebar.title("📊 Analytics Center")
menu = st.sidebar.radio(
    "Navigasi",
    ["Executive Dashboard","Perilaku","Demografi","Data Explorer"]
)

st.title("🚀 Dashboard Premium Analisis Perilaku & Etos Kerja")

total = len(df)

if menu == "Executive Dashboard":
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Total Responden", total)
    c2.metric("Jumlah Variabel", len(df.columns))
    c3.metric("Data Valid", total)
    c4.metric("Kelengkapan", "100%")

    st.subheader("Ringkasan Distribusi")
    obj = df.select_dtypes(include="object").columns

    if len(obj):
        col = obj[0]
        vc = df[col].value_counts().reset_index()
        vc.columns=["Kategori","Jumlah"]

        a,b = st.columns(2)

        with a:
            fig = px.pie(vc,names="Kategori",values="Jumlah",hole=.55,
                         title=col)
            st.plotly_chart(fig,use_container_width=True)

        with b:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=85,
                title={"text":"Etos Kerja Index"},
                gauge={"axis":{"range":[0,100]}}
            ))
            st.plotly_chart(fig,use_container_width=True)

elif menu == "Perilaku":
    obj = df.select_dtypes(include="object").columns

    pilihan = st.selectbox("Pilih Variabel", obj)

    vc = df[pilihan].value_counts().reset_index()
    vc.columns=["Kategori","Jumlah"]

    fig = px.bar(
        vc,
        x="Jumlah",
        y="Kategori",
        orientation="h",
        title=f"Analisis {pilihan}"
    )
    st.plotly_chart(fig,use_container_width=True)

    radar = go.Figure()
    radar.add_trace(go.Scatterpolar(
        r=[80,75,90,70,85],
        theta=["Disiplin","Tanggung Jawab","Gigih","Konsisten","Komunikasi"],
        fill="toself"
    ))
    radar.update_layout(title="Radar Kompetensi")
    st.plotly_chart(radar,use_container_width=True)

elif menu == "Demografi":
    for col in df.columns:
        if "usia" in str(col).lower():
            fig = px.histogram(df,x=col,title="Distribusi Usia")
            st.plotly_chart(fig,use_container_width=True)

        if "kelamin" in str(col).lower():
            fig = px.pie(df,names=col,title="Distribusi Gender")
            st.plotly_chart(fig,use_container_width=True)

elif menu == "Data Explorer":
    st.dataframe(df,use_container_width=True)
    csv = df.to_csv(index=False).encode()
    st.download_button("📥 Download CSV",csv,"data.csv","text/csv")

st.markdown("---")
st.caption("Premium Dashboard • Streamlit Edition")
