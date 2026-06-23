import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import datetime

st.set_page_config(
    page_title="Analisis Perilaku & Etos Kerja",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif !important; }
.stApp { background: #08071a !important; }
.block-container { padding: 2rem 2.5rem !important; max-width: 1280px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0e0c24 0%, #0a0918 100%) !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}
[data-testid="stSidebar"] .stRadio > label { display: none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap: 4px !important; }
[data-testid="stSidebar"] .stRadio label {
    display: flex !important;
    align-items: center;
    padding: 10px 14px !important;
    border-radius: 10px !important;
    font-size: 0.875rem !important;
    color: #8b87a8 !important;
    transition: all .2s !important;
    cursor: pointer !important;
}
[data-testid="stSidebar"] .stRadio label:hover { background: rgba(255,255,255,.05) !important; color: #e0ddf5 !important; }
[data-testid="stSidebar"] .stRadio label[data-baseweb="radio"]:has(input:checked),
[data-testid="stSidebar"] input[type="radio"]:checked + div { color: #c4b5fd !important; }

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 16px !important;
    padding: 1.25rem 1.4rem !important;
    backdrop-filter: blur(8px);
}
[data-testid="stMetricLabel"] p { color: #7c79a0 !important; font-size: 0.72rem !important; text-transform: uppercase; letter-spacing: .08em; font-weight: 600 !important; }
[data-testid="stMetricValue"] { color: #fff !important; font-size: 2rem !important; font-weight: 800 !important; }
[data-testid="stMetricDelta"] { display: none !important; }

/* ── Dataframe ── */
[data-testid="stDataFrame"] { border-radius: 14px !important; overflow: hidden; border: 1px solid rgba(255,255,255,.07) !important; }
.dvn-scroller { background: #0e0c24 !important; }

/* ── Multiselect ── */
[data-testid="stMultiSelect"] > div { background: rgba(255,255,255,.04) !important; border-color: rgba(255,255,255,.1) !important; border-radius: 10px !important; }
.stMultiSelect span[data-baseweb="tag"] { background: rgba(139,92,246,.25) !important; color: #c4b5fd !important; border-radius: 6px !important; }

/* ── Divider ── */
hr { border-color: rgba(255,255,255,0.07) !important; margin: 2rem 0 !important; }

/* ── Hide default elements ── */
#MainMenu, footer, header { visibility: hidden !important; }
.stDeployButton { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Data ─────────────────────────────────────────────────────────────────────
@st.cache_data
def load():
    raw = pd.read_excel("data.xlsx")
    df = raw[raw["Timestamp"].apply(lambda x: isinstance(x, datetime.datetime))].copy()
    df.columns = [c.strip() for c in df.columns]
    return df

df = load()
T = len(df)

# ── Colors ────────────────────────────────────────────────────────────────────
P = "#7c3aed"   # violet
B = "#3b82f6"   # blue
G = "#10b981"   # emerald
A = "#f59e0b"   # amber
R = "#ef4444"   # rose
S = "#06b6d4"   # cyan
BORDER = "rgba(255,255,255,0.08)"
FONT   = "Inter"

def chart_base():
    return dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font=dict(family=FONT, color="#c4c0e0"), margin=dict(l=0,r=0,t=32,b=0))

def grid():
    return dict(gridcolor="rgba(255,255,255,0.05)", zerolinecolor="rgba(255,255,255,0.05)")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='padding:1.5rem 0 1rem'>
      <div style='font-size:1.1rem;font-weight:800;color:#e0ddf5;letter-spacing:-.01em'>Analisis Perilaku</div>
      <div style='font-size:.75rem;color:#5c5880;margin-top:2px'>&amp; Etos Kerja · 2026</div>
    </div>""", unsafe_allow_html=True)

    page = st.radio("nav", [
        "🏠  Beranda",
        "📊  Data & Grafik",
        "👥  Responden",
        "✅  Kesimpulan",
        "ℹ️  Tentang",
    ], label_visibility="collapsed")

    st.markdown(f"""
    <div style='margin-top:2rem;padding:1rem;background:rgba(124,58,237,.1);
                border:1px solid rgba(124,58,237,.25);border-radius:12px'>
      <div style='font-size:1.4rem;font-weight:800;color:#c4b5fd'>{T}</div>
      <div style='font-size:.72rem;color:#7c79a0;text-transform:uppercase;letter-spacing:.07em;margin-top:2px'>Total Responden</div>
    </div>
    <div style='margin-top:.75rem;padding:.8rem 1rem;background:rgba(255,255,255,.03);
                border:1px solid rgba(255,255,255,.07);border-radius:12px;font-size:.8rem;color:#5c5880;line-height:1.9'>
      Metode: Survei Online<br>Periode: April 2026<br>Pertanyaan: 8 item
    </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# BERANDA
# ════════════════════════════════════════════════════════════════════════════
if page == "🏠  Beranda":
    st.markdown("""
    <div style='margin-bottom:2.5rem'>
      <div style='display:inline-block;background:rgba(124,58,237,.15);color:#c4b5fd;
                  border:1px solid rgba(124,58,237,.3);padding:.3rem 1rem;border-radius:999px;
                  font-size:.7rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;
                  margin-bottom:1rem'>Penelitian Akademik 2026</div>
      <h1 style='font-size:2.6rem;font-weight:800;color:#fff;line-height:1.15;
                 letter-spacing:-.03em;margin:0 0 .75rem'>
        Analisis Perilaku<br>
        <span style='background:linear-gradient(135deg,#7c3aed,#3b82f6);
                     -webkit-background-clip:text;-webkit-text-fill-color:transparent'>& Etos Kerja</span>
      </h1>
      <p style='color:#7c79a0;font-size:1rem;max-width:560px;line-height:1.75;margin:0'>
        Memahami pola perilaku, respons emosional, dan etos kerja mahasiswa serta pekerja
        melalui data survei yang komprehensif dan terstruktur.
      </p>
    </div>""", unsafe_allow_html=True)

    vc_s = df["Status Anda saat ini"].value_counts()
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric("Total Responden", T)
    c2.metric("Mahasiswa", int(vc_s.get("Mahasiswa",0)))
    c3.metric("Pekerja", int(vc_s.get("Pekerja",0)))
    c4.metric("Keduanya", int(vc_s.get("Keduanya",0)))
    c5.metric("Pertanyaan", 8)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    # ── Highlights ──
    st.markdown("<div style='font-size:1.1rem;font-weight:700;color:#e0ddf5;margin-bottom:.3rem'>Temuan Utama</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.85rem;color:#5c5880;margin-bottom:1.2rem'>Ringkasan dari survei perilaku dan etos kerja.</div>", unsafe_allow_html=True)

    hl = [
        (round(df["Saat menghadapi masalah"].value_counts().get("Saya tetap tenang",0)/T*100), "Tetap Tenang\nSaat Menghadapi Masalah", G, "rgba(16,185,129,.12)", "rgba(16,185,129,.3)"),
        (round(df["Ketika rencana gagal"].value_counts().get("Saya mencari solusi",0)/T*100), "Mencari Solusi\nKetika Rencana Gagal", S, "rgba(6,182,212,.12)", "rgba(6,182,212,.3)"),
        (round(df["Saat menghadapi kesulitan"].value_counts().get("Saya terus mencoba",0)/T*100), "Terus Mencoba\nSaat Kesulitan", P, "rgba(124,58,237,.12)", "rgba(124,58,237,.3)"),
        (round(df["Beban kerja/tugas banyak"].value_counts().get("Saya tetap berusaha menyelesaikan",0)/T*100), "Gigih\nMeski Beban Berat", A, "rgba(245,158,11,.12)", "rgba(245,158,11,.3)"),
    ]
    cols = st.columns(4)
    for col,(pct,lbl,color,bg,border) in zip(cols,hl):
        col.markdown(f"""
        <div style='background:{bg};border:1px solid {border};border-radius:16px;
                    padding:1.4rem 1.2rem;text-align:center'>
          <div style='font-size:2.4rem;font-weight:800;color:{color};line-height:1'>{pct}%</div>
          <div style='font-size:.75rem;color:#7c79a0;margin-top:.5rem;line-height:1.5;white-space:pre-line'>{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)

    # ── Mini charts row ──
    st.markdown("<div style='font-size:1.1rem;font-weight:700;color:#e0ddf5;margin-bottom:.3rem'>Distribusi Responden</div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.85rem;color:#5c5880;margin-bottom:1.2rem'>Profil dasar 40 responden survei.</div>", unsafe_allow_html=True)

    ca, cb, cc = st.columns(3)
    with ca:
        vc = df["Status Anda saat ini"].value_counts()
        fig = go.Figure(go.Pie(labels=vc.index, values=vc.values, hole=.65,
            marker=dict(colors=[P,G,A], line=dict(color="#08071a",width=3)),
            textfont=dict(color="#fff",size=12)))
        fig.update_layout(**chart_base(), title=dict(text="Status",font=dict(size=13,color="#8b87a8"),x=0),
                          legend=dict(font=dict(color="#8b87a8",size=11),bgcolor="rgba(0,0,0,0)"))
        st.plotly_chart(fig, use_container_width=True)
    with cb:
        vc = df["Usia"].value_counts()
        fig = go.Figure(go.Bar(x=vc.index, y=vc.values,
            marker=dict(color=[S,P,B,R], line=dict(width=0)), text=vc.values,
            textposition="outside", textfont=dict(color="#8b87a8",size=11)))
        fig.update_layout(**chart_base(), title=dict(text="Kelompok Usia",font=dict(size=13,color="#8b87a8"),x=0),
                          xaxis=dict(**grid(),tickfont=dict(color="#5c5880")),
                          yaxis=dict(**grid(),tickfont=dict(color="#5c5880")))
        st.plotly_chart(fig, use_container_width=True)
    with cc:
        vc = df["Jenis kelamin"].value_counts()
        fig = go.Figure(go.Pie(labels=vc.index, values=vc.values, hole=.65,
            marker=dict(colors=[B,R], line=dict(color="#08071a",width=3)),
            textfont=dict(color="#fff",size=12)))
        fig.update_layout(**chart_base(), title=dict(text="Jenis Kelamin",font=dict(size=13,color="#8b87a8"),x=0),
                          legend=dict(font=dict(color="#8b87a8",size=11),bgcolor="rgba(0,0,0,0)"))
        st.plotly_chart(fig, use_container_width=True)

    # ── Progress summary ──
    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1.1rem;font-weight:700;color:#e0ddf5;margin-bottom:1rem'>Profil Perilaku Positif</div>", unsafe_allow_html=True)

    cmap = {
        "Saat menghadapi masalah": ("Saya tetap tenang", G),
        "Jika ada orang melakukan kesalahan": ("Saya mencoba memahami dulu", S),
        "Ketika rencana gagal": ("Saya mencari solusi", P),
        "Mendekati deadline": ("Sudah selesai sebelumnya", A),
        "Saat menghadapi kesulitan": ("Saya terus mencoba", B),
        "Beban kerja/tugas banyak": ("Saya tetap berusaha menyelesaikan", G),
    }
    labels_short = ["Tenang hadapi masalah","Empati pada kesalahan","Solusi rencana gagal","Disiplin deadline","Tahan kesulitan","Gigih beban kerja"]

    for (col_name,(ans,color)),short in zip(cmap.items(),labels_short):
        val = df[col_name].value_counts().get(ans,0)
        pct = round(val/T*100)
        st.markdown(f"""
        <div style='margin-bottom:.85rem'>
          <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:.35rem'>
            <span style='font-size:.82rem;color:#c4c0e0'>{short}</span>
            <span style='font-size:.78rem;color:#5c5880;font-weight:600'>{val}/{T} &nbsp;·&nbsp; <span style='color:{color}'>{pct}%</span></span>
          </div>
          <div style='background:rgba(255,255,255,.06);border-radius:999px;height:6px;overflow:hidden'>
            <div style='width:{pct}%;background:{color};height:6px;border-radius:999px;
                        box-shadow:0 0 10px {color}60'></div>
          </div>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# DATA & GRAFIK
# ════════════════════════════════════════════════════════════════════════════
elif page == "📊  Data & Grafik":
    st.markdown("<h2 style='color:#fff;font-weight:800;letter-spacing:-.02em;margin-bottom:.3rem'>Data & Grafik Lengkap</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.88rem;color:#5c5880;margin-bottom:2rem'>Eksplorasi hasil survei 40 responden melalui grafik interaktif.</div>", unsafe_allow_html=True)

    def hbar(series, title, colors):
        vc = series.value_counts()
        pcts = [round(v/T*100) for v in vc.values]
        texts = [f"{v} ({p}%)" for v,p in zip(vc.values,pcts)]
        fig = go.Figure(go.Bar(
            y=vc.index, x=vc.values, orientation="h",
            marker=dict(color=colors[:len(vc)], line=dict(width=0)),
            text=texts, textposition="outside",
            textfont=dict(color="#7c79a0",size=11)
        ))
        fig.update_layout(**chart_base(),
            title=dict(text=title,font=dict(size=13,color="#8b87a8"),x=0),
            xaxis=dict(**grid(),tickfont=dict(color="#5c5880")),
            yaxis=dict(**grid(),tickfont=dict(color="#c4c0e0"),autorange="reversed"),
            height=160)
        return fig

    def donut(series, title, colors):
        vc = series.value_counts()
        fig = go.Figure(go.Pie(labels=vc.index, values=vc.values, hole=.62,
            marker=dict(colors=colors[:len(vc)], line=dict(color="#08071a",width=3)),
            textfont=dict(color="#fff",size=11)))
        fig.update_layout(**chart_base(),
            title=dict(text=title,font=dict(size=13,color="#8b87a8"),x=0),
            legend=dict(font=dict(color="#8b87a8",size=11),bgcolor="rgba(0,0,0,0)"),
            height=220)
        return fig

    # Section: Emosional
    st.markdown("<div style='font-size:.7rem;font-weight:700;color:#5c5880;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1rem'>Perilaku Emosional</div>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1: st.plotly_chart(hbar(df["Saat menghadapi masalah"],"Saat menghadapi masalah",[G,R]), use_container_width=True)
    with c2: st.plotly_chart(hbar(df["Jika ada orang melakukan kesalahan"],"Jika ada orang melakukan kesalahan",[S,A]), use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Section: Etos Kerja
    st.markdown("<div style='font-size:.7rem;font-weight:700;color:#5c5880;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1rem'>Etos Kerja & Produktivitas</div>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.plotly_chart(donut(df["Ketika rencana gagal"],"Rencana Gagal",[P,R]), use_container_width=True)
    with c2: st.plotly_chart(donut(df["Ketika ada tugas"],"Ketika Ada Tugas",[G,A]), use_container_width=True)
    with c3: st.plotly_chart(donut(df["Waktu luang"],"Waktu Luang",[A,P]), use_container_width=True)
    with c4: st.plotly_chart(donut(df["Mendekati deadline"],"Deadline",[G,R]), use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Section: Resiliensi
    st.markdown("<div style='font-size:.7rem;font-weight:700;color:#5c5880;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1rem'>Resiliensi & Ketahanan</div>", unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1: st.plotly_chart(hbar(df["Saat menghadapi kesulitan"],"Saat menghadapi kesulitan",[P,R]), use_container_width=True)
    with c2: st.plotly_chart(hbar(df["Beban kerja/tugas banyak"],"Beban kerja/tugas banyak",[G,R]), use_container_width=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Radar
    st.markdown("<div style='font-size:.7rem;font-weight:700;color:#5c5880;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1rem'>Radar Profil Perilaku Positif</div>", unsafe_allow_html=True)

    radar_data = [
        ("Tenang\nHadapi Masalah", df["Saat menghadapi masalah"].value_counts().get("Saya tetap tenang",0)),
        ("Empati\nPada Kesalahan", df["Jika ada orang melakukan kesalahan"].value_counts().get("Saya mencoba memahami dulu",0)),
        ("Solusi\nRencana Gagal", df["Ketika rencana gagal"].value_counts().get("Saya mencari solusi",0)),
        ("Proaktif\nTugas", df["Ketika ada tugas"].value_counts().get("Saya langsung mengerjakan",0)),
        ("Produktif\nWaktu Luang", df["Waktu luang"].value_counts().get("Digunakan untuk hal produktif",0)),
        ("Disiplin\nDeadline", df["Mendekati deadline"].value_counts().get("Sudah selesai sebelumnya",0)),
        ("Tahan\nKesulitan", df["Saat menghadapi kesulitan"].value_counts().get("Saya terus mencoba",0)),
        ("Gigih\nBeban Kerja", df["Beban kerja/tugas banyak"].value_counts().get("Saya tetap berusaha menyelesaikan",0)),
    ]
    cats = [r[0] for r in radar_data]
    vals = [round(r[1]/T*100) for r in radar_data]
    vals_closed = vals + [vals[0]]
    cats_closed = cats + [cats[0]]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=vals_closed, theta=cats_closed, fill="toself",
        fillcolor="rgba(124,58,237,0.15)", line=dict(color=P,width=2.5),
        marker=dict(color=P,size=7,symbol="circle")))
    fig.update_layout(**chart_base(), height=420,
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True,range=[0,100],color="#3a3660",
                           gridcolor="rgba(255,255,255,0.07)",ticksuffix="%",
                           tickfont=dict(color="#5c5880",size=10)),
            angularaxis=dict(color="#7c79a0",gridcolor="rgba(255,255,255,0.07)",
                            tickfont=dict(color="#8b87a8",size=11))
        ), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# RESPONDEN
# ════════════════════════════════════════════════════════════════════════════
elif page == "👥  Responden":
    st.markdown(f"<h2 style='color:#fff;font-weight:800;letter-spacing:-.02em;margin-bottom:.3rem'>Daftar Responden</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:.88rem;color:#5c5880;margin-bottom:1.5rem'><span style='color:#c4b5fd;font-weight:700'>{T}</span> responden berpartisipasi dalam survei ini.</div>", unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        f_status = st.multiselect("Filter Status", df["Status Anda saat ini"].unique().tolist(), default=df["Status Anda saat ini"].unique().tolist())
    with c2:
        f_gender = st.multiselect("Filter Jenis Kelamin", df["Jenis kelamin"].unique().tolist(), default=df["Jenis kelamin"].unique().tolist())

    dv = df[df["Status Anda saat ini"].isin(f_status) & df["Jenis kelamin"].isin(f_gender)].copy()
    dv.insert(0,"No", range(1,len(dv)+1))
    dv["Timestamp"] = dv["Timestamp"].apply(lambda x: x.strftime("%d %b %Y  %H:%M"))
    st.dataframe(
        dv[["No","Timestamp","Status Anda saat ini","Usia","Jenis kelamin"]].reset_index(drop=True),
        use_container_width=True, hide_index=True,
        column_config={
            "No": st.column_config.NumberColumn("No", width=60),
            "Timestamp": st.column_config.TextColumn("Waktu Respons", width=180),
            "Status Anda saat ini": st.column_config.TextColumn("Status"),
            "Usia": st.column_config.TextColumn("Usia"),
            "Jenis kelamin": st.column_config.TextColumn("Jenis Kelamin"),
        }
    )
    st.markdown(f"<div style='font-size:.78rem;color:#5c5880;margin-top:.5rem'>Menampilkan {len(dv)} dari {T} responden</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# KESIMPULAN
# ════════════════════════════════════════════════════════════════════════════
elif page == "✅  Kesimpulan":
    st.markdown("<h2 style='color:#fff;font-weight:800;letter-spacing:-.02em;margin-bottom:.3rem'>Temuan & Kesimpulan</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.88rem;color:#5c5880;margin-bottom:2rem'>Analisis mendalam dari data survei 40 responden.</div>", unsafe_allow_html=True)

    findings = [
        (G, "rgba(16,185,129,.1)", "rgba(16,185,129,.25)", "Kecerdasan Emosional Cukup Baik",
         "80% responden tetap tenang saat menghadapi masalah, dan 70% mencoba memahami situasi sebelum bereaksi terhadap kesalahan orang lain — indikator kecerdasan emosional yang relatif baik."),
        (B, "rgba(59,130,246,.1)", "rgba(59,130,246,.25)", "Orientasi Solusi yang Kuat",
         "75% responden memilih mencari solusi ketika rencana tidak berjalan sesuai harapan. Ini adalah indikator growth mindset yang penting dalam lingkungan akademik maupun profesional."),
        (A, "rgba(245,158,11,.1)", "rgba(245,158,11,.25)", "Prokrastinasi Masih Umum",
         "50% responden mengaku sering menunda tugas, dan 45% baru mulai mengerjakan saat mendekati deadline. Manajemen waktu perlu mendapat perhatian lebih serius."),
        (P, "rgba(124,58,237,.1)", "rgba(124,58,237,.25)", "Resiliensi Tinggi",
         "75% tetap mencoba saat menghadapi kesulitan, dan 72.5% tetap berusaha meski beban kerja berat. Tingkat resiliensi yang tinggi adalah modal utama menghadapi dunia yang dinamis."),
    ]
    for color,bg,border,title,body in findings:
        st.markdown(f"""
        <div style='background:{bg};border:1px solid {border};border-left:3px solid {color};
                    border-radius:14px;padding:1.25rem 1.4rem;margin-bottom:.9rem'>
          <div style='font-size:.95rem;font-weight:700;color:{color};margin-bottom:.4rem'>{title}</div>
          <div style='font-size:.87rem;color:#8b87a8;line-height:1.7'>{body}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1rem;font-weight:700;color:#e0ddf5;margin-bottom:1rem'>Profil Ringkas Responden</div>", unsafe_allow_html=True)
    profile = [("52.5%","Mahasiswa",P),("22.5%","Pekerja",G),("25%","Keduanya",A),
               ("62.5%","Laki-laki",S),("37.5%","Perempuan",R),("50%","Usia 20–25 thn",B)]
    cols = st.columns(6)
    for col,(pct,lbl,c) in zip(cols,profile):
        col.markdown(f"""
        <div style='background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
                    border-radius:14px;padding:1rem;text-align:center'>
          <div style='font-size:1.5rem;font-weight:800;color:{c}'>{pct}</div>
          <div style='font-size:.72rem;color:#5c5880;margin-top:.3rem;line-height:1.4'>{lbl}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1rem;font-weight:700;color:#e0ddf5;margin-bottom:1rem'>Rekomendasi</div>", unsafe_allow_html=True)
    recs = [
        (P,"rgba(124,58,237,.15)","#c4b5fd","01","Pelatihan Manajemen Waktu",
         "Tingginya angka prokrastinasi menunjukkan kebutuhan nyata akan program time management seperti teknik Pomodoro, time blocking, atau priority matrix."),
        (G,"rgba(16,185,129,.15)","#6ee7b7","02","Pengembangan Kecerdasan Emosional",
         "20–30% responden masih perlu pengembangan lebih lanjut melalui mentoring, konseling, atau workshop manajemen emosi dan komunikasi efektif."),
        (A,"rgba(245,158,11,.15)","#fde68a","03","Optimalisasi Waktu Luang",
         "60% responden menggunakan waktu luang untuk bersantai. Program pengembangan diri, komunitas belajar, atau proyek kolaboratif dapat membantu mengoptimalkan potensi ini."),
    ]
    for color,bg,text_c,no,title,body in recs:
        st.markdown(f"""
        <div style='background:{bg};border:1px solid rgba(255,255,255,.07);border-radius:14px;
                    padding:1.2rem 1.4rem;margin-bottom:.75rem;display:flex;gap:1.1rem;align-items:flex-start'>
          <div style='background:rgba(0,0,0,.2);color:{text_c};border-radius:10px;
                      padding:.4rem .85rem;font-weight:800;font-size:.9rem;white-space:nowrap;
                      min-width:42px;text-align:center'>{no}</div>
          <div>
            <div style='font-size:.9rem;font-weight:700;color:{color};margin-bottom:.3rem'>{title}</div>
            <div style='font-size:.84rem;color:#8b87a8;line-height:1.65'>{body}</div>
          </div>
        </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# TENTANG
# ════════════════════════════════════════════════════════════════════════════
elif page == "ℹ️  Tentang":
    st.markdown("<h2 style='color:#fff;font-weight:800;letter-spacing:-.02em;margin-bottom:.3rem'>Tentang Penelitian</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:.88rem;color:#5c5880;margin-bottom:2rem'>Metodologi, tujuan, dan detail kuesioner penelitian ini.</div>", unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style='background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
                    border-radius:16px;padding:1.4rem'>
          <div style='font-size:.95rem;font-weight:700;color:#c4b5fd;margin-bottom:.9rem'>Tujuan Penelitian</div>
          <ul style='color:#8b87a8;font-size:.87rem;line-height:2.1;padding-left:1.2rem;margin:0'>
            <li>Respons emosional terhadap masalah & konflik</li>
            <li>Kebiasaan dan pola kerja sehari-hari</li>
            <li>Tingkat resiliensi dan ketahanan mental</li>
            <li>Penggunaan waktu luang & produktivitas</li>
            <li>Kemampuan menghadapi tekanan & beban kerja</li>
          </ul>
        </div>""", unsafe_allow_html=True)
    with c2:
        meta = [("Metode","Survei Kuesioner Online (Google Forms)"),
                ("Responden","40 orang valid"),("Periode","14 April – 28 April 2026"),
                ("Pertanyaan","8 item pilihan ganda"),("Analisis","Statistik deskriptif & visualisasi")]
        rows = "".join([f"<tr><td style='color:#5c5880;padding:.55rem 0;font-size:.83rem;width:110px'>{k}</td><td style='color:#c4c0e0;font-size:.87rem;font-weight:500'>{v}</td></tr>" for k,v in meta])
        st.markdown(f"""
        <div style='background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.08);
                    border-radius:16px;padding:1.4rem'>
          <div style='font-size:.95rem;font-weight:700;color:#c4b5fd;margin-bottom:.9rem'>Metodologi</div>
          <table style='width:100%;border-collapse:collapse'>{rows}</table>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size:1rem;font-weight:700;color:#e0ddf5;margin-bottom:1rem'>Pertanyaan Kuesioner</div>", unsafe_allow_html=True)

    questions = [
        ("Q1","Saat menghadapi masalah, saya…",["Saya tetap tenang","Saya mudah emosi"],G),
        ("Q2","Jika ada orang melakukan kesalahan, saya…",["Saya mencoba memahami dulu","Saya langsung kesal/marah"],S),
        ("Q3","Ketika rencana gagal, saya…",["Saya mencari solusi","Saya cepat frustrasi"],P),
        ("Q4","Ketika ada tugas, saya…",["Saya langsung mengerjakan","Saya sering menunda"],B),
        ("Q5","Waktu luang saya…",["Digunakan untuk hal produktif","Lebih banyak untuk santai"],A),
        ("Q6","Mendekati deadline, saya…",["Sudah selesai sebelumnya","Baru mulai mengerjakan"],G),
        ("Q7","Saat menghadapi kesulitan, saya…",["Saya terus mencoba","Saya cenderung menyerah"],P),
        ("Q8","Beban kerja/tugas banyak, saya…",["Saya tetap berusaha menyelesaikan","Saya merasa kewalahan dan berhenti"],G),
    ]
    for no,q,opts,color in questions:
        badges = "".join([f'<span style="background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);padding:.25rem .75rem;border-radius:999px;font-size:.75rem;color:#7c79a0;margin-right:.4rem">{o}</span>' for o in opts])
        st.markdown(f"""
        <div style='background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.07);
                    border-radius:13px;padding:1rem 1.2rem;margin-bottom:.55rem;
                    display:flex;gap:.9rem;align-items:flex-start'>
          <span style='background:rgba(124,58,237,.2);color:{color};border-radius:8px;
                       padding:.25rem .65rem;font-size:.75rem;font-weight:700;white-space:nowrap'>{no}</span>
          <div>
            <div style='font-size:.88rem;font-weight:600;color:#e0ddf5;margin-bottom:.45rem'>{q}</div>
            <div>{badges}</div>
          </div>
        </div>""", unsafe_allow_html=True)
