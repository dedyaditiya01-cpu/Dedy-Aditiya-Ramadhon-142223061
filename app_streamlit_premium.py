
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Analisis Perilaku & Etos Kerja", page_icon="📊", layout="wide")

st.markdown("""
<h1 style='text-align:center;'>📊 Dashboard Analisis Perilaku & Etos Kerja</h1>
<p style='text-align:center;'>Visualisasi Premium Hasil Survei</p>
""", unsafe_allow_html=True)

uploaded = st.file_uploader("Upload file Excel survei", type=["xlsx"])

if uploaded:
    df = pd.read_excel(uploaded)

    # Bersihkan baris ringkasan yang bukan responden
    df = df[df["Saat menghadapi masalah  "].notna()].copy()

    st.sidebar.header("Filter")

    total_responden = len(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Responden", total_responden)
    col2.metric("Tenang saat masalah", (df["Saat menghadapi masalah  "]=="Saya tetap tenang").sum())
    col3.metric("Tetap mencoba saat kesulitan", (df["Saat menghadapi kesulitan  "]=="Saya terus mencoba").sum())

    st.divider()

    def count_chart(column, title):
        vc = df[column].value_counts().reset_index()
        vc.columns = ["Kategori", "Jumlah"]
        fig = px.bar(
            vc,
            x="Kategori",
            y="Jumlah",
            text="Jumlah",
            title=title
        )
        fig.update_layout(height=450)
        return fig

    tab1, tab2, tab3 = st.tabs(["📈 Perilaku", "💼 Etos Kerja", "📋 Data Mentah"])

    with tab1:
        c1, c2 = st.columns(2)

        with c1:
            st.plotly_chart(
                px.pie(
                    df,
                    names="Saat menghadapi masalah  ",
                    title="Respon Saat Menghadapi Masalah"
                ),
                use_container_width=True
            )

        with c2:
            st.plotly_chart(
                px.pie(
                    df,
                    names="Jika ada orang melakukan kesalahan  ",
                    title="Sikap Terhadap Kesalahan Orang Lain"
                ),
                use_container_width=True
            )

        st.plotly_chart(
            count_chart(
                "Ketika rencana gagal  ",
                "Respons Saat Rencana Gagal"
            ),
            use_container_width=True
        )

    with tab2:
        colA, colB = st.columns(2)

        with colA:
            st.plotly_chart(
                px.pie(
                    df,
                    names="Ketika ada tugas",
                    title="Kebiasaan Saat Mendapat Tugas"
                ),
                use_container_width=True
            )

        with colB:
            st.plotly_chart(
                px.pie(
                    df,
                    names="Mendekati deadline  ",
                    title="Perilaku Menjelang Deadline"
                ),
                use_container_width=True
            )

        st.plotly_chart(
            count_chart(
                "Beban kerja/tugas banyak  ",
                "Respons Saat Beban Kerja Tinggi"
            ),
            use_container_width=True
        )

        st.plotly_chart(
            count_chart(
                "Saat menghadapi kesulitan  ",
                "Ketahanan Menghadapi Kesulitan"
            ),
            use_container_width=True
        )

    with tab3:
        st.dataframe(df, use_container_width=True)

else:
    st.info("Upload file Excel survei untuk menampilkan dashboard.")
