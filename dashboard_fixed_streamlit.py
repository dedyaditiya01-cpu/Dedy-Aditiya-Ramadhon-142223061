
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Dashboard Premium Etos Kerja", layout="wide")

st.title("📊 Dashboard Premium Analisis Perilaku & Etos Kerja")

# Cari file excel otomatis
excel_files = list(Path(".").glob("*.xlsx"))

df = None

if excel_files:
    try:
        df = pd.read_excel(excel_files[0])
        st.success(f"Data otomatis dimuat: {excel_files[0].name}")
    except Exception:
        pass

if df is None:
    uploaded = st.file_uploader("Upload file Excel", type=["xlsx"])
    if uploaded:
        df = pd.read_excel(uploaded)
    else:
        st.warning("Upload file Excel atau letakkan file .xlsx di repository GitHub.")
        st.stop()

# Bersihkan data
first_col = df.columns[0]
df = df[df[first_col].notna()]

col1,col2,col3 = st.columns(3)
col1.metric("Total Responden", len(df))
col2.metric("Jumlah Kolom", len(df.columns))
col3.metric("Jumlah Data", len(df))

st.divider()

# Ringkasan kolom
obj_cols = df.select_dtypes(include="object").columns

if len(obj_cols) > 0:
    selected = st.selectbox("Pilih Variabel Analisis", obj_cols)

    vc = df[selected].value_counts().reset_index()
    vc.columns = ["Kategori","Jumlah"]

    tab1,tab2,tab3 = st.tabs(["Bar Chart","Pie Chart","Data"])

    with tab1:
        fig = px.bar(vc,x="Kategori",y="Jumlah",text="Jumlah",
                     title=f"Distribusi {selected}")
        st.plotly_chart(fig,use_container_width=True)

    with tab2:
        fig = px.pie(vc,names="Kategori",values="Jumlah",
                     hole=0.5,
                     title=f"Komposisi {selected}")
        st.plotly_chart(fig,use_container_width=True)

    with tab3:
        st.dataframe(df,use_container_width=True)

    # Gauge sederhana
    skor = round((vc["Jumlah"].max()/len(df))*100,1)

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=skor,
        title={"text":"Dominasi Jawaban (%)"},
        gauge={"axis":{"range":[0,100]}}
    ))

    st.plotly_chart(gauge,use_container_width=True)
