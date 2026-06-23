import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Analisis Perilaku & Etos Kerja",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Metric cards */
[data-testid="metric-container"] {
    background: #1e1b2e;
    border: 1px solid #2e2b45;
    border-radius: 12px;
    padding: 1rem 1.2rem;
}
[data-testid="metric-container"] label { color: #9b98b0 !important; font-size: .78rem !important; text-transform: uppercase; letter-spacing: .05em; }
[data-testid="metric-container"] [data-testid="stMetricValue"] { color: #a5b4fc !important; font-size: 2rem !important; font-weight: 800 !important; }

/* Sidebar */
[data-testid="stSidebar"] { background: #13111e !important; border-right: 1px solid #2e2b45; }
[data-testid="stSidebar"] .stRadio label { font-size: .88rem; color: #c4c2d4; }

/* Divider */
hr { border-color: #2e2b45 !important; }

/* Section header */
.section-title { font-size: 1.4rem; font-weight: 800; color: #e8e6f0; margin-bottom: .2rem; }
.section-sub   { font-size: .88rem; color: #9b98b0; margin-bottom: 1.2rem; }

/* Highlight badge */
.badge-box {
    background: #1e1b2e;
    border: 1px solid #2e2b45;
    border-radius: 12px;
    padding: 1.1rem 1.3rem;
    text-align: center;
}
.badge-pct { font-size: 2rem; font-weight: 800; }
.badge-lbl { font-size: .78rem; color: #9b98b0; margin-top: .25rem; line-height: 1.5; }

/* Info cards */
.info-card {
    background: #1e1b2e;
    border: 1px solid #2e2b45;
    border-radius: 12px;
    padding: 1.2rem 1.3rem;
    margin-bottom: .75rem;
}
.info-card h4 { margin: 0 0 .5rem; font-size: .95rem; font-weight: 700; }
.info-card p  { margin: 0; font-size: .85rem; color: #9b98b0; line-height: 1.65; }
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df_raw = pd.read_excel("data.xlsx")
    df = df_raw[df_raw["Timestamp"].apply(lambda x: isinstance(x, datetime.datetime))].copy()
    df.columns = [c.strip() for c in df.columns]
    return df

df = load_data()
T = len(df)

# ── Colour palette ─────────────────────────────────────────────────────────────
CLR = {
    "primary": "#4f46e5", "accent": "#7c3aed",
    "green": "#10b981",   "amber": "#f59e0b",
    "rose":  "#f43f5e",   "sky":   "#38bdf8",
    "purple":"#a855f7",   "bg":    "#0f0e17",
    "card":  "#1e1b2e",   "border":"#2e2b45",
    "muted": "#9b98b0",   "text":  "#e8e6f0",
}

def plotly_defaults():
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color=CLR["text"],
        font_family="Inter",
        margin=dict(l=10, r=10, t=30, b=10),
    )

# ── Sidebar nav ───────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⬡ Analisis Perilaku")
    st.markdown("<small style='color:#9b98b0'>& Etos Kerja — 2026</small>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Navigasi", [
        "🏠 Beranda",
        "📊 Data & Grafik",
        "👥 Responden",
        "✅ Kesimpulan",
        "ℹ️ Tentang",
    ])
    st.markdown("---")
    st.markdown(f"<small style='color:#9b98b0'>Total Responden: <b style='color:#a5b4fc'>{T}</b></small>", unsafe_allow_html=True)
    st.markdown("<small style='color:#9b98b0'>Periode: April 2026</small>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: BERANDA
# ════════════════════════════════════════════════════════════════════════════════
if page == "🏠 Beranda":
    st.markdown("""
    <div style='margin-bottom:2rem'>
      <span style='background:rgba(79,70,229,.15);color:#a5b4fc;border:1px solid rgba(79,70,229,.3);
            padding:.3rem 1rem;border-radius:999px;font-size:.75rem;font-weight:600;
            letter-spacing:.06em;text-transform:uppercase'>Penelitian Akademik 2026</span>
      <h1 style='font-size:2.2rem;font-weight:800;margin:.75rem 0 .5rem;line-height:1.2;color:#e8e6f0'>
        Analisis <span style='background:linear-gradient(135deg,#4f46e5,#7c3aed);
        -webkit-background-clip:text;-webkit-text-fill-color:transparent'>Perilaku & Etos Kerja</span>
      </h1>
      <p style='color:#9b98b0;font-size:1rem;max-width:620px;line-height:1.7'>
        Memahami pola perilaku, respons emosional, dan etos kerja mahasiswa serta pekerja
        melalui data survei yang komprehensif dan terstruktur.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Stat cards
    vc_status = df["Status Anda saat ini"].value_counts()
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Responden", T)
    c2.metric("Mahasiswa", vc_status.get("Mahasiswa", 0))
    c3.metric("Pekerja", vc_status.get("Pekerja", 0))
    c4.metric("Keduanya", vc_status.get("Keduanya", 0))
    c5.metric("Pertanyaan", 8)

    st.markdown("---")
    st.markdown('<div class="section-title">Temuan Utama</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Ringkasan temuan paling signifikan dari survei.</div>', unsafe_allow_html=True)

    highlights = [
        (f"{round(df['Saat menghadapi masalah'].value_counts().get('Saya tetap tenang',0)/T*100)}%", "Tetap Tenang Saat Menghadapi Masalah", CLR["green"]),
        (f"{round(df['Ketika rencana gagal'].value_counts().get('Saya mencari solusi',0)/T*100)}%", "Mencari Solusi Ketika Rencana Gagal", CLR["sky"]),
        (f"{round(df['Saat menghadapi kesulitan'].value_counts().get('Saya terus mencoba',0)/T*100)}%", "Terus Mencoba Saat Menghadapi Kesulitan", CLR["accent"]),
        (f"{round(df['Beban kerja/tugas banyak'].value_counts().get('Saya tetap berusaha menyelesaikan',0)/T*100)}%", "Tetap Berusaha Menyelesaikan Beban Kerja", CLR["amber"]),
    ]
    cols = st.columns(4)
    for col, (pct, lbl, color) in zip(cols, highlights):
        col.markdown(f"""
        <div class="badge-box">
          <div class="badge-pct" style="color:{color}">{pct}</div>
          <div class="badge-lbl">{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">Sekilas Data</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Distribusi utama responden.</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        vc = df["Status Anda saat ini"].value_counts()
        fig = go.Figure(go.Pie(
            labels=vc.index.tolist(), values=vc.values.tolist(),
            hole=.6, marker_colors=[CLR["primary"], CLR["green"], CLR["amber"]],
            textfont_color=CLR["text"]
        ))
        fig.update_layout(title="Status Responden", **plotly_defaults(),
                          legend=dict(font_color=CLR["muted"]))
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        vc = df["Usia"].value_counts()
        fig = go.Figure(go.Bar(
            x=vc.index.tolist(), y=vc.values.tolist(),
            marker_color=[CLR["sky"], CLR["primary"], CLR["accent"], CLR["rose"]],
            marker_line_width=0
        ))
        fig.update_layout(title="Kelompok Usia", **plotly_defaults(),
                          xaxis=dict(color=CLR["muted"], gridcolor=CLR["border"]),
                          yaxis=dict(color=CLR["muted"], gridcolor=CLR["border"]))
        st.plotly_chart(fig, use_container_width=True)

    # Summary progress bars
    st.markdown('<div class="section-title" style="margin-top:1rem">Profil Perilaku Positif</div>', unsafe_allow_html=True)
    items = [
        ("Saat menghadapi masalah", "Saya tetap tenang", CLR["green"]),
        ("Jika orang lain salah", "Saya mencoba memahami dulu", CLR["sky"]),
        ("Ketika rencana gagal", "Saya mencari solusi", CLR["primary"]),
        ("Mendekati deadline", "Sudah selesai sebelumnya", CLR["amber"]),
        ("Saat menghadapi kesulitan", "Saya terus mencoba", CLR["accent"]),
        ("Beban kerja banyak", "Saya tetap berusaha menyelesaikan", CLR["green"]),
    ]
    col_q_map = {
        "Saat menghadapi masalah": "Saat menghadapi masalah",
        "Jika orang lain salah": "Jika ada orang melakukan kesalahan",
        "Ketika rencana gagal": "Ketika rencana gagal",
        "Mendekati deadline": "Mendekati deadline",
        "Saat menghadapi kesulitan": "Saat menghadapi kesulitan",
        "Beban kerja banyak": "Beban kerja/tugas banyak",
    }
    for label, ans, color in items:
        col = col_q_map[label]
        val = df[col].value_counts().get(ans, 0)
        pct = round(val / T * 100)
        st.markdown(f"""
        <div style='margin-bottom:.7rem'>
          <div style='display:flex;justify-content:space-between;font-size:.84rem;margin-bottom:.3rem'>
            <span style='color:#e8e6f0'><b>{label}:</b> {ans}</span>
            <span style='color:#9b98b0;white-space:nowrap'>{val}/{T} ({pct}%)</span>
          </div>
          <div style='background:#2e2b45;border-radius:999px;height:7px'>
            <div style='width:{pct}%;background:{color};border-radius:999px;height:7px'></div>
          </div>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: DATA & GRAFIK
# ════════════════════════════════════════════════════════════════════════════════
elif page == "📊 Data & Grafik":
    st.markdown('<div class="section-title">Data & Grafik Lengkap</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Eksplorasi hasil survei dari 40 responden melalui grafik interaktif.</div>', unsafe_allow_html=True)

    # ─ DEMOGRAFI ─
    st.markdown("#### Demografi Responden")
    c1, c2, c3 = st.columns(3)

    with c1:
        vc = df["Status Anda saat ini"].value_counts()
        fig = go.Figure(go.Pie(labels=vc.index.tolist(), values=vc.values.tolist(),
            hole=.55, marker_colors=[CLR["primary"], CLR["green"], CLR["amber"]]))
        fig.update_layout(title="Status", **plotly_defaults(), legend=dict(font_color=CLR["muted"]))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        vc = df["Usia"].value_counts()
        fig = go.Figure(go.Bar(x=vc.index, y=vc.values,
            marker_color=[CLR["sky"], CLR["primary"], CLR["accent"], CLR["rose"]], marker_line_width=0))
        fig.update_layout(title="Kelompok Usia", **plotly_defaults(),
            xaxis=dict(color=CLR["muted"], gridcolor=CLR["border"]),
            yaxis=dict(color=CLR["muted"], gridcolor=CLR["border"]))
        st.plotly_chart(fig, use_container_width=True)

    with c3:
        vc = df["Jenis kelamin"].value_counts()
        fig = go.Figure(go.Pie(labels=vc.index.tolist(), values=vc.values.tolist(),
            hole=.55, marker_colors=[CLR["sky"], CLR["rose"]]))
        fig.update_layout(title="Jenis Kelamin", **plotly_defaults(), legend=dict(font_color=CLR["muted"]))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ─ PERILAKU EMOSIONAL ─
    st.markdown("#### Perilaku Emosional")
    c1, c2 = st.columns(2)

    def hbar(col_data, title, colors):
        vc = col_data.value_counts()
        fig = go.Figure(go.Bar(
            y=vc.index.tolist(), x=vc.values.tolist(), orientation="h",
            marker_color=colors, marker_line_width=0,
            text=[f"{v} ({round(v/T*100)}%)" for v in vc.values],
            textposition="outside", textfont_color=CLR["muted"]
        ))
        fig.update_layout(title=title, **plotly_defaults(),
            xaxis=dict(color=CLR["muted"], gridcolor=CLR["border"]),
            yaxis=dict(color=CLR["muted"], autorange="reversed"))
        return fig

    with c1:
        st.plotly_chart(hbar(df["Saat menghadapi masalah"],
            "Saat Menghadapi Masalah", [CLR["green"], CLR["rose"]]), use_container_width=True)
    with c2:
        st.plotly_chart(hbar(df["Jika ada orang melakukan kesalahan"],
            "Jika Ada Orang Melakukan Kesalahan", [CLR["sky"], CLR["amber"]]), use_container_width=True)

    st.markdown("---")

    # ─ ETOS KERJA ─
    st.markdown("#### Etos Kerja & Produktivitas")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(hbar(df["Ketika rencana gagal"],
            "Ketika Rencana Gagal", [CLR["primary"], CLR["rose"]]), use_container_width=True)
        st.plotly_chart(hbar(df["Waktu luang"],
            "Penggunaan Waktu Luang", [CLR["amber"], CLR["primary"]]), use_container_width=True)
    with c2:
        st.plotly_chart(hbar(df["Ketika ada tugas"],
            "Ketika Ada Tugas", [CLR["green"], CLR["amber"]]), use_container_width=True)
        st.plotly_chart(hbar(df["Mendekati deadline"],
            "Mendekati Deadline", [CLR["green"], CLR["rose"]]), use_container_width=True)

    st.markdown("---")

    # ─ RESILIENSI ─
    st.markdown("#### Resiliensi & Ketahanan")
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(hbar(df["Saat menghadapi kesulitan"],
            "Saat Menghadapi Kesulitan", [CLR["purple"], CLR["rose"]]), use_container_width=True)
    with c2:
        st.plotly_chart(hbar(df["Beban kerja/tugas banyak"],
            "Saat Beban Kerja Banyak", [CLR["green"], CLR["rose"]]), use_container_width=True)

    st.markdown("---")

    # ─ RADAR ─
    st.markdown("#### Radar Profil Perilaku Positif")
    categories = [
        "Tenang\nHadapi Masalah", "Empati\nPada Kesalahan",
        "Solusi\nRencana Gagal", "Proaktif\nTugas",
        "Produktif\nWaktu Luang", "Disiplin\nDeadline",
        "Tahan\nKesulitan", "Gigih\nBeban Kerja",
    ]
    positif = [
        df["Saat menghadapi masalah"].value_counts().get("Saya tetap tenang", 0),
        df["Jika ada orang melakukan kesalahan"].value_counts().get("Saya mencoba memahami dulu", 0),
        df["Ketika rencana gagal"].value_counts().get("Saya mencari solusi", 0),
        df["Ketika ada tugas"].value_counts().get("Saya langsung mengerjakan", 0),
        df["Waktu luang"].value_counts().get("Digunakan untuk hal produktif", 0),
        df["Mendekati deadline"].value_counts().get("Sudah selesai sebelumnya", 0),
        df["Saat menghadapi kesulitan"].value_counts().get("Saya terus mencoba", 0),
        df["Beban kerja/tugas banyak"].value_counts().get("Saya tetap berusaha menyelesaikan", 0),
    ]
    vals = [round(v / T * 100) for v in positif] + [round(positif[0] / T * 100)]
    cats = categories + [categories[0]]

    fig = go.Figure(go.Scatterpolar(
        r=vals, theta=cats, fill="toself",
        line_color=CLR["primary"],
        fillcolor="rgba(79,70,229,0.2)",
        marker=dict(color=CLR["accent"], size=7)
    ))
    fig.update_layout(
        **plotly_defaults(),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 100], color=CLR["muted"],
                            gridcolor=CLR["border"], ticksuffix="%"),
            angularaxis=dict(color=CLR["muted"], gridcolor=CLR["border"])
        ),
        showlegend=False, height=450
    )
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: RESPONDEN
# ════════════════════════════════════════════════════════════════════════════════
elif page == "👥 Responden":
    st.markdown('<div class="section-title">Daftar Responden</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-sub">Total <b style="color:#a5b4fc">{T}</b> responden berpartisipasi dalam survei ini.</div>', unsafe_allow_html=True)

    col_filter1, col_filter2 = st.columns([1, 1])
    with col_filter1:
        filter_status = st.multiselect("Filter Status", options=df["Status Anda saat ini"].unique().tolist(), default=df["Status Anda saat ini"].unique().tolist())
    with col_filter2:
        filter_gender = st.multiselect("Filter Jenis Kelamin", options=df["Jenis kelamin"].unique().tolist(), default=df["Jenis kelamin"].unique().tolist())

    df_view = df[df["Status Anda saat ini"].isin(filter_status) & df["Jenis kelamin"].isin(filter_gender)].copy()
    df_view["No"] = range(1, len(df_view) + 1)
    df_view["Timestamp"] = df_view["Timestamp"].apply(lambda x: x.strftime("%d %b %Y %H:%M"))
    df_display = df_view[["No", "Timestamp", "Status Anda saat ini", "Usia", "Jenis kelamin"]].reset_index(drop=True)

    st.dataframe(df_display, use_container_width=True, hide_index=True,
        column_config={
            "No": st.column_config.NumberColumn("No", width="small"),
            "Timestamp": st.column_config.TextColumn("Waktu Respons"),
            "Status Anda saat ini": st.column_config.TextColumn("Status"),
            "Usia": st.column_config.TextColumn("Usia"),
            "Jenis kelamin": st.column_config.TextColumn("Jenis Kelamin"),
        }
    )
    st.markdown(f"<small style='color:#9b98b0'>Menampilkan {len(df_display)} dari {T} responden</small>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: KESIMPULAN
# ════════════════════════════════════════════════════════════════════════════════
elif page == "✅ Kesimpulan":
    st.markdown('<div class="section-title">Temuan & Kesimpulan</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Analisis mendalam dari data survei 40 responden mengenai perilaku dan etos kerja.</div>', unsafe_allow_html=True)

    findings = [
        ("🟢", "#10b981", "Kecerdasan Emosional Cukup Baik",
         "Sebanyak <b>80% responden</b> tetap tenang saat menghadapi masalah, dan <b>70%</b> mencoba memahami situasi sebelum bereaksi terhadap kesalahan orang lain. Ini menunjukkan tingkat kecerdasan emosional yang relatif baik."),
        ("🔵", "#4f46e5", "Orientasi Solusi yang Kuat",
         "Mayoritas responden (<b>75%</b>) memilih mencari solusi ketika rencana tidak berjalan sesuai harapan — indikator <em>growth mindset</em> yang penting dalam lingkungan akademik maupun profesional."),
        ("🟡", "#f59e0b", "Prokrastinasi Masih Umum",
         "Tepat <b>50% responden</b> mengaku sering menunda tugas, dan <b>45%</b> baru mulai mengerjakan saat mendekati deadline. Manajemen waktu perlu ditingkatkan."),
        ("🟣", "#7c3aed", "Resiliensi Tinggi",
         "Sebesar <b>75% responden</b> tetap mencoba saat kesulitan, dan <b>72.5%</b> tetap berusaha meski beban kerja berat. Tingkat resiliensi yang tinggi adalah aset berharga."),
    ]
    for icon, color, title, body in findings:
        st.markdown(f"""
        <div class="info-card" style="border-left:3px solid {color}">
          <h4 style="color:{color}">{icon} {title}</h4>
          <p>{body}</p>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Ringkasan Profil Responden")
    cols = st.columns(6)
    profile = [
        ("52.5%", "Mahasiswa\n(21 orang)", CLR["primary"]),
        ("22.5%", "Pekerja\n(9 orang)", CLR["green"]),
        ("25%", "Keduanya\n(10 orang)", CLR["amber"]),
        ("62.5%", "Laki-laki\n(25 orang)", CLR["sky"]),
        ("37.5%", "Perempuan\n(15 orang)", CLR["rose"]),
        ("50%", "Usia 20–25\ntahun", CLR["purple"]),
    ]
    for col, (pct, lbl, color) in zip(cols, profile):
        col.markdown(f"""
        <div class="badge-box">
          <div class="badge-pct" style="color:{color};font-size:1.6rem">{pct}</div>
          <div class="badge-lbl">{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### Rekomendasi")
    recs = [
        ("01", CLR["primary"], "rgba(79,70,229,.15)", "#a5b4fc", "Pelatihan Manajemen Waktu",
         "Mengingat tingginya angka prokrastinasi, program pelatihan time management seperti teknik Pomodoro, time blocking, atau priority matrix sangat direkomendasikan."),
        ("02", CLR["green"], "rgba(16,185,129,.15)", "#6ee7b7", "Pengembangan Kecerdasan Emosional",
         "20–30% responden masih perlu pengembangan melalui mentoring, konseling, atau workshop manajemen emosi."),
        ("03", CLR["amber"], "rgba(245,158,11,.15)", "#fde68a", "Optimalisasi Waktu Luang",
         "60% responden menggunakan waktu luang untuk bersantai. Program pengembangan diri atau komunitas dapat membantu mengoptimalkan waktu tersebut."),
    ]
    for no, color, bg, text_c, title, body in recs:
        st.markdown(f"""
        <div class="info-card">
          <div style="display:flex;gap:1rem;align-items:flex-start">
            <div style="background:{bg};color:{text_c};border-radius:8px;padding:.4rem .75rem;
                        font-weight:700;white-space:nowrap;font-size:.9rem">{no}</div>
            <div>
              <h4 style="color:{color};margin:0 0 .35rem">{title}</h4>
              <p style="margin:0">{body}</p>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: TENTANG
# ════════════════════════════════════════════════════════════════════════════════
elif page == "ℹ️ Tentang":
    st.markdown('<div class="section-title">Tentang Penelitian Ini</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Informasi lengkap mengenai metodologi, tujuan, dan detail kuesioner.</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="info-card">
          <h4 style="color:#a5b4fc">Tujuan Penelitian</h4>
          <p>Memahami pola perilaku dan etos kerja di kalangan mahasiswa dan pekerja, mencakup:
          <ul style="margin-top:.5rem;padding-left:1.2rem;line-height:2">
            <li>Respons emosional terhadap masalah dan konflik</li>
            <li>Kebiasaan dan pola kerja sehari-hari</li>
            <li>Tingkat resiliensi dan ketahanan mental</li>
            <li>Penggunaan waktu luang dan produktivitas</li>
            <li>Kemampuan menghadapi tekanan dan beban kerja</li>
          </ul></p>
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="info-card">
          <h4 style="color:#a5b4fc">Metodologi</h4>
          <p>
          <b>Metode:</b> Survei Kuesioner Online (Google Forms)<br><br>
          <b>Responden:</b> 40 orang valid<br><br>
          <b>Periode:</b> 14 April – 28 April 2026<br><br>
          <b>Pertanyaan:</b> 8 pertanyaan pilihan ganda<br><br>
          <b>Analisis:</b> Statistik deskriptif & visualisasi interaktif
          </p>
        </div>""", unsafe_allow_html=True)

    st.markdown("#### Pertanyaan Kuesioner")
    questions = [
        ("Q1", "Saat menghadapi masalah, saya…", ["Saya tetap tenang", "Saya mudah emosi"]),
        ("Q2", "Jika ada orang melakukan kesalahan, saya…", ["Saya mencoba memahami dulu", "Saya langsung kesal/marah"]),
        ("Q3", "Ketika rencana gagal, saya…", ["Saya mencari solusi", "Saya cepat frustrasi"]),
        ("Q4", "Ketika ada tugas, saya…", ["Saya langsung mengerjakan", "Saya sering menunda"]),
        ("Q5", "Waktu luang saya…", ["Digunakan untuk hal produktif", "Lebih banyak untuk santai"]),
        ("Q6", "Mendekati deadline, saya…", ["Sudah selesai sebelumnya", "Baru mulai mengerjakan"]),
        ("Q7", "Saat menghadapi kesulitan, saya…", ["Saya terus mencoba", "Saya cenderung menyerah"]),
        ("Q8", "Beban kerja/tugas banyak, saya…", ["Saya tetap berusaha menyelesaikan", "Saya merasa kewalahan dan berhenti"]),
    ]
    for no, q, opts in questions:
        opts_html = " ".join([f'<span style="background:#13111e;border:1px solid #2e2b45;padding:.2rem .65rem;border-radius:6px;font-size:.78rem;color:#9b98b0;margin-right:.35rem">{o}</span>' for o in opts])
        st.markdown(f"""
        <div class="info-card" style="margin-bottom:.6rem">
          <div style="display:flex;gap:.75rem;align-items:flex-start">
            <span style="background:rgba(79,70,229,.15);color:#a5b4fc;border-radius:6px;
                         padding:.2rem .6rem;font-size:.8rem;font-weight:700;white-space:nowrap">{no}</span>
            <div>
              <div style="font-size:.9rem;font-weight:600;color:#e8e6f0;margin-bottom:.45rem">{q}</div>
              <div>{opts_html}</div>
            </div>
          </div>
        </div>""", unsafe_allow_html=True)
