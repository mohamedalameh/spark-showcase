import streamlit as st
import os
import streamlit.components.v1 as components
import base64


st.set_page_config(
    page_title="SPARK Automation Showcase",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

            

/* NEW SPARK HOME DESIGN */
.spark-hero {
    min-height: 720px;
    padding: 40px 35px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.78) 45%, rgba(2,8,23,0.25) 100%),
        radial-gradient(circle at 72% 42%, rgba(0,229,255,0.30), transparent 28%),
        radial-gradient(circle at 82% 65%, rgba(124,77,255,0.32), transparent 26%);
    border: 1px solid rgba(0,229,255,0.22);
    box-shadow: 0 0 60px rgba(0,229,255,0.14);
    position: relative;
    overflow: hidden;
}

.spark-hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,229,255,0.07) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,229,255,0.07) 1px, transparent 1px);
    background-size: 55px 55px;
    opacity: 0.45;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 680px;
}

.badge {
    display: inline-block;
    padding: 9px 18px;
    border-radius: 999px;
    background: rgba(0,120,255,0.25);
    border: 1px solid rgba(0,229,255,0.35);
    color: #dffbff;
    font-weight: 800;
    margin-bottom: 25px;
}

.spark-big {
    font-size: 105px;
    font-weight: 900;
    line-height: 0.9;
    background: linear-gradient(90deg, #65f7ff, #1688ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 40px rgba(0,229,255,0.45);
}

.spark-sub {
    font-size: 44px;
    font-weight: 900;
    color: white;
    margin-top: 12px;
}

.hero-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}

.hero-buttons {
    margin-top: 35px;
    display: flex;
    gap: 22px;
}

.primary-btn, .secondary-btn {
    padding: 16px 30px;
    border-radius: 16px;
    font-weight: 800;
    text-decoration: none;
    color: white !important;
}

.primary-btn {
    background: linear-gradient(90deg, #007bff, #00e5ff);
    box-shadow: 0 0 35px rgba(0,229,255,0.45);
}

.secondary-btn {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.25);
}

.home-kpis {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-top: 45px;
    position: relative;
    z-index: 2;
}

.home-kpi {
    background: rgba(8,20,38,0.78);
    border: 1px solid rgba(0,229,255,0.20);
    border-radius: 18px;
    padding: 22px;
}

.home-kpi h3 {
    color: #00e5ff;
    font-size: 30px;
    margin: 0;
}

.module-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 18px;
    margin-top: 28px;
}

.module-card {
    background: rgba(8,20,38,0.86);
    border: 1px solid rgba(0,229,255,0.18);
    border-radius: 20px;
    padding: 24px;
    text-align: center;
    min-height: 180px;
    transition: 0.3s ease;
}

.module-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 35px rgba(0,229,255,0.28);
    border-color: rgba(0,229,255,0.55);
}

.module-icon {
    font-size: 42px;
    margin-bottom: 12px;
}








            



.card p {
    color: #d7e7ff !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
}

.flow-box p {
    color: #d7e7ff !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

.flow-box b {
    color: white !important;
}

.card {
    transition: 0.3s ease !important;
}

.card:hover {
    transform: translateY(-6px);
    border-color: rgba(0,229,255,0.45);
    box-shadow: 0 0 30px rgba(0,229,255,0.22);
}

.flow-box {
    transition: 0.3s ease !important;
}

.flow-box:hover {
    transform: translateY(-7px);
    border-color: rgba(0,229,255,0.55);
    box-shadow: 0 0 25px rgba(0,229,255,0.22);
}




































html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top right, #082b5c 0%, #020814 35%, #01040a 100%);
    color: white;
}

section[data-testid="stSidebar"] {
    background: #07111f;
    border-right: 1px solid rgba(0, 221, 255, 0.15);
}

section[data-testid="stSidebar"] .stRadio label {
    color: #ffffff !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
    background: rgba(0, 229, 255, 0.06);
    border: 1px solid rgba(0, 229, 255, 0.15);
    padding: 10px 14px;
    border-radius: 12px;
    margin-bottom: 8px;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
    background: rgba(0, 229, 255, 0.14);
    border: 1px solid rgba(0, 229, 255, 0.35);
    transform: translateX(2px);
}

section[data-testid="stSidebar"] .stMarkdown h2 {
    color: white !important;
    font-weight: 800 !important;
}

section[data-testid="stSidebar"] p {
    color: #d7e7ff !important;
    font-size: 15px !important;
}

            





.hero-network {
    position: absolute;
    top: 0;
    right: 0;
    width: 58%;
    height: 100%;
    background:
        radial-gradient(circle at 30% 40%, rgba(0,229,255,0.35), transparent 14%),
        radial-gradient(circle at 60% 55%, rgba(124,77,255,0.38), transparent 14%),
        radial-gradient(circle at 78% 28%, rgba(0,229,255,0.30), transparent 12%),
        radial-gradient(circle at 80% 75%, rgba(124,77,255,0.30), transparent 12%);
}

.hero-network::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,229,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,229,255,0.05) 1px, transparent 1px);
    background-size: 40px 40px;
}

.hero-network::after {
    content: "";
    position: absolute;
    width: 500px;
    height: 500px;
    right: 8%;
    top: 15%;
    background: radial-gradient(circle, rgba(0,229,255,0.22), transparent 70%);
    filter: blur(40px);
}

            






            



/* SIDEBAR BUTTONS */
section[data-testid="stSidebar"] .stButton > button {

    background: rgba(0, 229, 255, 0.045) !important;

    color: #ffffff !important;

    border: 1px solid rgba(0, 229, 255, 0.18) !important;

    border-radius: 11px !important;

    padding: 0.18rem 0.65rem !important;

    min-height: 34px !important;

    font-weight: 700 !important;

    font-size: 13px !important;

    width: 100% !important;

    text-align: left !important;

    transition: all 0.22s ease-in-out !important;

    backdrop-filter: blur(10px);

    position: relative;

    overflow: hidden;

    box-shadow: none !important;
}

/* HOVER */
section[data-testid="stSidebar"] .stButton > button:hover {

    background:
        linear-gradient(
            90deg,
            rgba(0,123,255,0.22),
            rgba(0,229,255,0.15)
        ) !important;

    border-color: #00e5ff !important;

    transform: translateX(4px);

    box-shadow:
        0 0 12px rgba(0,229,255,0.18);

    color: white !important;
}

/* CLICK */
section[data-testid="stSidebar"] .stButton > button:active {

    transform: scale(0.96);
}

/* SHINE EFFECT */
section[data-testid="stSidebar"] .stButton > button::before {

    content: "";

    position: absolute;

    top: 0;
    left: -130%;

    width: 70%;
    height: 100%;

    background:
        linear-gradient(
            120deg,
            transparent,
            rgba(255,255,255,0.16),
            transparent
        );

    transition: 0.55s;
}

section[data-testid="stSidebar"] .stButton > button:hover::before {

    left: 130%;
}

/* ACTIVE / SELECTED BUTTON */
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {

    background:
        linear-gradient(
            90deg,
            rgba(0,123,255,0.45),
            rgba(0,229,255,0.28)
        ) !important;

    border: 1px solid #00e5ff !important;

    color: white !important;

    box-shadow:
        0 0 14px rgba(0,229,255,0.30),
        inset 0 0 12px rgba(0,229,255,0.10);

    transform: translateX(3px);
}
























section[data-testid="stSidebar"] h3 {
    color: #00e5ff !important;
    font-size: 20px !important;
    font-weight: 900 !important;
    letter-spacing: 0.5px;
    margin-top: 10px !important;
    margin-bottom: 14px !important;

    text-shadow:
        0 0 8px rgba(0,229,255,0.65),
        0 0 18px rgba(0,229,255,0.35);

    animation: glowTitle 2.2s ease-in-out infinite alternate;
}

@keyframes glowTitle {
    from {
        opacity: 0.75;
        transform: translateX(0px);
    }

    to {
        opacity: 1;
        transform: translateX(4px);
    }
}












</style>
""", unsafe_allow_html=True)


###################################################################




st.sidebar.markdown("## ⚡ SPARK")
st.sidebar.markdown("Automation Engine")
st.sidebar.markdown("---")

# DEFAULT PAGE
page = "Home"

# =========================
# HOME
# =========================


if st.sidebar.button("🏠 Home"):
    page = "Home"



st.sidebar.markdown("---")



if st.sidebar.button("Automation Portfolio"):
    page = "Automation Portfolio"



st.sidebar.markdown("---")



# =========================
# Optimization
# =========================
st.sidebar.markdown("### Optimization Tools")



if st.sidebar.button("SPARK"):
    page = "SPARK"

if st.sidebar.button("SSV Builder"):
    page = "SSV Builder"

if st.sidebar.button("SSV Plot Processing"):
    page = "SSV Plot Processing"

if st.sidebar.button("TMR Report Builder"):
    page = "TMR Report Builder"

if st.sidebar.button("4G / 5G Dashboard"):
    page = "4G / 5G Dashboard"

if st.sidebar.button("Worst Cells Dashboard"):
    page = "Worst Cells Dashboard"

st.sidebar.markdown("---")

# =========================
# Radio Planning
# =========================
st.sidebar.markdown("### Radio Planning")

if st.sidebar.button("KML Plotter"):
    page = "KML Plotter"

if st.sidebar.button("Radio LLD Automation"):
    page = "Radio LLD Automation"

if st.sidebar.button("Site Database"):
    page = "Site Database"

if st.sidebar.button("Ookla Weekly & API Script"):
    page = "Ookla Weekly & API Script"


st.sidebar.markdown("---")



# =========================
# X-haul Transmission
# =========================
st.sidebar.markdown("### X-haul Transmission")

if st.sidebar.button("GLI_TX_Report"):
    page = "GLI_TX_Report"

if st.sidebar.button("LINK Perf Chart creation "):
    page = "LINK Perf Chart creation "


st.sidebar.markdown("---")




# =========================
# Management
# =========================
st.sidebar.markdown("### Management Tools")

if st.sidebar.button("Acceptance Tracker"):
    page = "Acceptance Tracker"


###############################################################






def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()



def show_video(video_path, video_id, missing_message):

    if os.path.exists(video_path):

        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()

        video_base64 = base64.b64encode(video_bytes).decode()

        components.html(f"""
        <div style="display:flex; justify-content:center;">
            <video width="60%" autoplay muted controls style="border-radius:18px;" id="{video_id}">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>

        <script>
        const video = document.getElementById("{video_id}");

        video.playbackRate = 1.3;

        video.onloadedmetadata = function() {{
            video.play();
        }};
        </script>
        """, height=1200)

    else:
        st.warning(missing_message)

################################################# KSPARKML #####################################################

def show_spark_page():

    # =====================================================
    # HERO SECTION
    # =====================================================

    components.html("""
<style>

.spark-hero {
    min-height: 700px;
    padding: 55px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.78) 45%, rgba(2,8,23,0.25) 100%),
        radial-gradient(circle at 72% 42%, rgba(0,229,255,0.30), transparent 28%),
        radial-gradient(circle at 82% 65%, rgba(124,77,255,0.32), transparent 26%);
    border: 1px solid rgba(0,229,255,0.22);
    box-shadow: 0 0 60px rgba(0,229,255,0.14);
    position: relative;
    overflow: hidden;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.spark-hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,229,255,0.07) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,229,255,0.07) 1px, transparent 1px);
    background-size: 55px 55px;
    opacity: 0.45;
}

.hero-network {
    position: absolute;
    top: 0;
    right: 0;
    width: 58%;
    height: 100%;
    background:
        radial-gradient(circle at 30% 40%, rgba(0,229,255,0.35), transparent 14%),
        radial-gradient(circle at 60% 55%, rgba(124,77,255,0.38), transparent 14%),
        radial-gradient(circle at 78% 28%, rgba(0,229,255,0.30), transparent 12%),
        radial-gradient(circle at 80% 75%, rgba(124,77,255,0.30), transparent 12%);
}

.hero-content {
    position: relative;
    z-index: 5;
    max-width: 760px;
}

.badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(0,120,255,0.25);
    border: 1px solid rgba(0,229,255,0.35);
    color: #dffbff;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 25px;
}

.spark-big {
    font-size: 105px;
    font-weight: 900;
    line-height: 0.9;
    background: linear-gradient(90deg, #65f7ff, #1688ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.spark-sub {
    font-size: 44px;
    font-weight: 900;
    color: white;
    margin-top: 14px;
}

.hero-desc {
    color: #d7e7ff;
    font-size: 21px;
    line-height: 1.6;
    margin-top: 24px;
}

.hero-buttons {
    margin-top: 35px;
    display: flex;
    gap: 22px;
}

.secondary-btn {
    padding: 16px 30px;
    border-radius: 16px;
    font-weight: 800;
    text-decoration: none;
    color: white !important;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.25);
}

.secondary-btn:hover {
    background: rgba(255,255,255,0.12);
}

.home-kpis {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-top: 55px;
    position: relative;
    z-index: 5;
}

.home-kpi {
    background: rgba(8,20,38,0.78);
    border: 1px solid rgba(0,229,255,0.20);
    border-radius: 18px;
    padding: 22px;
}

.home-kpi h3 {
    color: #00e5ff;
    font-size: 30px;
    margin: 0;
}

.home-kpi p {
    color: #d7e7ff;
    margin: 6px 0 0 0;
}

</style>

<div class="spark-hero">

    <div class="hero-network"></div>

    <div class="hero-content">

        <div class="badge">
            ● AI-POWERED &nbsp;&nbsp; LTE / 5G AUTOMATION
        </div>

        <div class="spark-big">SPARK ⚡</div>

        <div class="spark-sub">
            AUTOMATION ENGINE
        </div>

        <p class="hero-desc">
            Smart Parsing, Analysis & RAN Kit for LTE/5G network optimization.
            Built to automate audits, XML parsing, KPI analysis, reporting,
            and large-scale telecom workflows with enterprise-grade efficiency.
        </p>

        <div class="hero-buttons">
            <a class="secondary-btn" href="javascript:void(0);" onclick="
            window.parent.document.querySelector('#spark-demo').scrollIntoView({
                behavior: 'smooth'
            });
            ">
                ▶ Watch Demo
            </a>
        </div>

    </div>

    <div class="home-kpis">

        <div class="home-kpi">
            <h3>&lt; 2 Min</h3>
            <p>Large XML Parsing</p>
        </div>

        <div class="home-kpi">
            <h3>95%+</h3>
            <p>Audit Time Reduction</p>
        </div>

        <div class="home-kpi">
            <h3>4G / 5G</h3>
            <p>Multi-Tech Support</p>
        </div>

        <div class="home-kpi">
            <h3>Auto</h3>
            <p>Reports & XML Output</p>
        </div>

    </div>

</div>
""", height=760)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # 4 INFO CARDS
    # =====================================================

    components.html("""
    <style>

    .spark-four-wrap {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 22px;
        align-items: stretch;
        font-family: Inter, Arial, sans-serif;
    }

    .spark-info-card {
        background: rgba(8,20,38,0.92);
        border: 1px solid rgba(0,229,255,0.22);
        border-radius: 22px;
        padding: 24px;
        min-height: 340px;
        color: white;
        transition: all 0.35s ease;
        cursor: pointer;
        box-shadow: 0 0 25px rgba(0,229,255,0.08);
    }

    .spark-info-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: rgba(0,229,255,0.75);
        box-shadow:
            0 0 28px rgba(0,229,255,0.32),
            0 0 60px rgba(0,229,255,0.14);
    }

    .spark-card-title {
        color: #ffffff;
        font-size: 26px;
        font-weight: 900;
        line-height: 1.15;
        margin-bottom: 20px;
    }

    .spark-line {
        color: #d7e7ff;
        font-size: 14px;
        line-height: 1.9;
        margin-bottom: 8px;
        font-weight: 600;
    }

    </style>

    <div class="spark-four-wrap">

        <div class="spark-info-card">

            <div class="spark-card-title">
                Problem Solved
            </div>

            <div class="spark-line">❌ Manual XML/RAML parsing</div>
            <div class="spark-line">❌ Repetitive parameter audits</div>
            <div class="spark-line">❌ Time-consuming neighbor checks</div>
            <div class="spark-line">❌ High risk of human error</div>
            <div class="spark-line">❌ Slow reporting and validation cycles</div>

        </div>

        <div class="spark-info-card">

            <div class="spark-card-title">
                Automation Result
            </div>

            <div class="spark-line">✅ Fast parsing of large network files</div>
            <div class="spark-line">✅ Automated LTE/5G audit engine</div>
            <div class="spark-line">✅ Parameter inconsistency detection</div>
            <div class="spark-line">✅ Clean Excel/XML output generation</div>
            <div class="spark-line">✅ Scalable workflow for thousands of sites</div>

        </div>

        <div class="spark-info-card">

            <div class="spark-card-title">
                Current Capabilities
            </div>

            <div class="spark-line">✅ Automated XML generation from CSV/Excel inputs</div>
            <div class="spark-line">✅ LNREL / LNADJG / LNADJGNB audit handling</div>
            <div class="spark-line">✅ AMLE automation</div>
            <div class="spark-line">✅ 5G Carrier Aggregation</div>
            <div class="spark-line">✅ Handover analysis integration</div>

        </div>

        <div class="spark-info-card">

            <div class="spark-card-title">
                Future Modules
            </div>

            <div class="spark-line">🚀 LTE Carrier Aggregation auditing</div>
            <div class="spark-line">🚀 LNHOIF / AMLEPR / IRFIM</div>
            <div class="spark-line">🚀 MODPR / ANR / SIB audits</div>
            <div class="spark-line">🚀 PMAX / Power audits</div>
            <div class="spark-line">🚀 RET optimization</div>
            <div class="spark-line">🚀 Load Balancing & Layering</div>
            <div class="spark-line">🚀 KPI-driven automation features</div>

        </div>

    </div>

    """, height=430)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SPARK CORE MODULES
    # =====================================================

    components.html("""
    <style>

    .module-flow{
        display:grid;
        grid-template-columns:1fr 55px 1fr 55px 1fr 55px 1fr;
        gap:10px;
        align-items:center;
        margin-top:28px;
    }

    .module-card{
        background:rgba(8,20,38,0.86);
        border:1px solid rgba(0,229,255,0.18);
        border-radius:20px;
        padding:24px;
        text-align:center;
        min-height:180px;
        transition:0.3s ease;
        color:white;
        font-family:Inter,Arial,sans-serif;
    }

    .module-card:hover{
        transform:translateY(-8px);
        box-shadow:0 0 35px rgba(0,229,255,0.28);
        border-color:rgba(0,229,255,0.55);
    }

    .module-icon{
        font-size:42px;
        margin-bottom:12px;
    }

    .module-card h3{
        font-size:20px;
        margin:10px 0;
    }

    .module-card p{
        color:#b8c7dd;
        font-size:14px;
        line-height:1.5;
    }

    .flow-arrow{
        font-size:62px;
        font-weight:900;
        color:#00e5ff;
        text-align:center;
        animation: arrowPulse 1.3s infinite ease-in-out;
        text-shadow:
            0 0 10px rgba(0,229,255,0.9),
            0 0 25px rgba(0,229,255,0.9),
            0 0 45px rgba(0,229,255,0.7);

        display:flex;
        align-items:center;
        justify-content:center;
    }

    @keyframes arrowPulse{
        0%{
            transform:translateX(0);
            opacity:0.45;
        }
        50%{
            transform:translateX(8px);
            opacity:1;
        }
        100%{
            transform:translateX(0);
            opacity:0.45;
        }
    }

    .section-title{
        color:white;
        font-size:26px;
        font-weight:800;
        margin-bottom:14px;
        font-family:Inter,Arial,sans-serif;
    }

    </style>

    <div class="section-title">SPARK Core Modules</div>

    <div class="module-flow">

        <div class="module-card">
            <div class="module-icon">📄</div>
            <h3>XML / RAML Parser</h3>
            <p>Fast parsing of large NetAct XML and RAML files.</p>
        </div>

        <div class="flow-arrow">➜</div>

        <div class="module-card">
            <div class="module-icon">⚙️</div>
            <h3>Parameter Audit</h3>
            <p>Automated LTE/5G parameter validation and inconsistency checks.</p>
        </div>

        <div class="flow-arrow">➜</div>

        <div class="module-card">
            <div class="module-icon">📊</div>
            <h3>Excel Reports</h3>
            <p>Clean automated reporting outputs for engineering review.</p>
        </div>

        <div class="flow-arrow">➜</div>

        <div class="module-card">
            <div class="module-icon">🧾</div>
            <h3>XML Generator</h3>
            <p>Automated XML creation for corrections and deployment actions.</p>
        </div>

    </div>

    """, height=360)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # DEMO VIDEO
    # =====================================================

    st.markdown("""
    <div id="spark-demo" class="card" style="scroll-margin-top:80px;">
        <div class="section-title">Demo Video</div>
        <p style="color:#b8c7dd;">
            End-to-end demonstration of SPARK parsing,
            audit automation, and report generation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    show_video(
        "assets/spark_demo.mp4",
        "sparkDemoVideo",
        "Add your video here: assets/spark_demo.mp4"
    )




############################## kml ####################


def show_kml_page():

    st.markdown("""
<style>

.kml-card {
    background: rgba(8,20,38,0.82);
    border: 1px solid rgba(0,229,255,0.22);
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 0 25px rgba(0,229,255,0.08);
    transition: 0.3s ease;
    min-height: 135px;
}

.kml-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0,229,255,0.55);
    box-shadow: 0 0 30px rgba(0,229,255,0.25);
}

.kml-flow-box {
    background: rgba(8,20,38,0.86);
    border: 1px solid rgba(0,229,255,0.22);
    border-radius: 18px;
    padding: 22px;
    text-align: center;
    min-height: 125px;
    transition: 0.3s ease;
}

.kml-flow-box:hover {
    transform: translateY(-7px);
    border-color: rgba(0,229,255,0.55);
    box-shadow: 0 0 28px rgba(0,229,255,0.25);
}

.kml-card p,
.kml-flow-box p {
    color: #d7e7ff !important;
}

.kml-section-title {
    color: white;
    font-size: 24px;
    font-weight: 900;
    margin-bottom: 14px;
}

</style>
""", unsafe_allow_html=True)

    # =========================
    # PREMIUM HERO
    # =========================

    components.html("""
<style>

.kml-hero {

    min-height: 420px;

    padding: 50px;

    border-radius: 30px;

    background:
        linear-gradient(
            90deg,
            rgba(2,8,23,0.98) 0%,
            rgba(2,8,23,0.82) 45%,
            rgba(2,8,23,0.35) 100%
        ),

        radial-gradient(
            circle at 75% 40%,
            rgba(255,209,102,0.22),
            transparent 28%
        ),

        radial-gradient(
            circle at 85% 70%,
            rgba(255,159,28,0.16),
            transparent 26%
        );

    border:
        1px solid rgba(255,209,102,0.28);

    box-shadow:
        0 0 55px rgba(255,209,102,0.12);

    color:
        white;

    font-family:
        Inter, Arial, sans-serif;
}

.kml-badge {

    display: inline-block;

    padding: 10px 20px;

    border-radius: 999px;

    background:
        linear-gradient(
            90deg,
            #ffd166,
            #ff9f1c
        );

    color:
        #111827;

    font-weight:
        900;

    font-size:
        14px;

    margin-bottom:
        24px;

    box-shadow:
        0 0 20px rgba(255,209,102,0.28);
}

.kml-big {

    font-size:
        74px;

    font-weight:
        900;

    line-height:
        0.95;

    background:
        linear-gradient(
            90deg,
            #ffd166,
            #ff9f1c
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    text-shadow:
        0 0 30px rgba(255,209,102,0.18);
}

.kml-sub {

    font-size:
        34px;

    font-weight:
        900;

    margin-top:
        14px;

    color:
        #ffffff;
}

.kml-desc {

    color:
        #f8fafc;

    font-size:
        20px;

    line-height:
        1.7;

    margin-top:
        22px;

    max-width:
        1050px;
}

</style>

<div class="kml-hero">

    <div class="kml-badge">
        🗺️ KML VISUALIZATION ENGINE
    </div>

    <div class="kml-big">
        KML Network Plotter
    </div>

    <div class="kml-sub">
        Automated LTE/5G/2G Google Earth Visualization
    </div>

    <p class="kml-desc">
        Converts network site data into clean, optimized KML/KMZ layers
        with sector visualization, technology separation, category-based sizing,
        and professional map-ready outputs for optimization and management teams.
    </p>

</div>
""", height=470)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # KPI BOXES
    # =========================

    k1, k2, k3, k4 = st.columns(4)

    data = [
        ("45MB → 7MB", "KMZ Size Optimization"),
        ("4G / 5G / 2G", "Multi-Tech Layers"),
        ("Auto", "Sector Generation"),
        ("Google Earth", "Ready Output"),
    ]

    for col, (num, label) in zip([k1, k2, k3, k4], data):
        with col:
            st.markdown(f"""
<div class="kml-card">
    <div class="kpi-number" style="font-size:30px;">{num}</div>
    <div class="kpi-label">{label}</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # PROBLEM / RESULT
    # =========================

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Problem Solved</div>
    <p>❌ Manual Google Earth plotting</p>
    <p>❌ Large KML/KMZ file sizes</p>
    <p>❌ Difficult technology separation</p>
    <p>❌ Time-consuming sector visualization</p>
    <p>❌ No standard visual output</p>
</div>
""", unsafe_allow_html=True)

    with right:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Automation Result</div>
    <p>✅ One-click KMZ generation</p>
    <p>✅ LTE/5G/2G layers organized automatically</p>
    <p>✅ Sector azimuth and beam visualization</p>
    <p>✅ Smaller optimized output</p>
    <p>✅ Professional map-ready delivery</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # FLOW
    # =========================

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">KML Processing Flow</div>
</div>
""", unsafe_allow_html=True)

    f1, f2, f3, f4, f5 = st.columns(5)

    flow = [
        ("📥", "Input<br>Excel / CSV"),
        ("🧹", "Clean<br>Coordinates"),
        ("📡", "Build<br>Sectors"),
        ("🗂️", "Create<br>Layers"),
        ("🌍", "Export<br>KMZ"),
    ]

    for col, (icon, text) in zip([f1, f2, f3, f4, f5], flow):
        with col:
            st.markdown(f"""
<div class="kml-flow-box">
    <div style="font-size:38px;">{icon}</div>
    <p>{text}</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # VIDEO
    # =========================

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <p>End-to-end demonstration of automated network visualization processing.</p>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/kml_demo.mp4",
        "kmlDemoVideo",
        "Add your video here: assets/kml_demo.mp4"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # GALLERY
    # =========================

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Visual Gallery</div>
    <p>KML visualization outputs and Google Earth rendering examples.</p>
</div>
""", unsafe_allow_html=True)

    images = [
        ("assets/kml_tool_interface.png", "Tool Interface"),
        ("assets/kml_google_earth_output.png", "Google Earth Output"),
        ("assets/kml_haram_outer_view.png", "Haram and Outer"),
        ("assets/kml_haram_zoom.png", "Haram Zoom"),
        ("assets/kml_sector_size_sets.png", "Different Sector Sizes"),
        ("assets/kml_site_sector_info.png", "Site/Sector Info"),
    ]

    for i in range(0, len(images), 3):

        cols = st.columns(3)

        for col, (path, caption) in zip(cols, images[i:i+3]):

            with col:

                if os.path.exists(path):

                    st.image(
                        path,
                        caption=caption,
                        use_container_width=True
                    )

                else:

                    st.markdown(f"""
<div class="kml-flow-box">
    <div style="font-size:48px;">🖼️</div>
    <b>{caption}</b>
    <p style="color:#8ea6c5;">Add: {path}</p>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =========================
    # BUSINESS IMPACT
    # =========================

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Business Impact</div>
    <p>⚡ Faster site visualization for planning and optimization teams</p>
    <p>🌍 Cleaner Google Earth delivery for field and management review</p>
    <p>📉 Reduced file size and easier sharing</p>
    <p>🎯 Better visibility of coverage, sectors, and technology layers</p>
</div>
""", unsafe_allow_html=True)



###################################################### Ookla #####################################

def show_ookla_page():

    components.html("""
<style>
.ookla-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(0,229,255,0.28), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(124,77,255,0.25), transparent 26%);
    border: 1px solid rgba(0,229,255,0.22);
    box-shadow: 0 0 55px rgba(0,229,255,0.14);
    position: relative;
    overflow: hidden;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.ookla-hero::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(0,229,255,0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,229,255,0.06) 1px, transparent 1px);
    background-size: 55px 55px;
    opacity: 0.4;
}

.ookla-content {
    position: relative;
    z-index: 5;
    max-width: 760px;
}

.ookla-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(0,120,255,0.25);
    border: 1px solid rgba(0,229,255,0.35);
    color: #dffbff;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}

.ookla-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #65f7ff, #1688ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.ookla-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.ookla-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="ookla-hero">
    <div class="ookla-content">
        <div class="ookla-badge">📊 OOKLA &nbsp;&nbsp; POWER BI / API AUTOMATION</div>
        <div class="ookla-big">Ookla Weekly Report</div>
        <div class="ookla-sub">Automated Market Performance Dashboard</div>
        <p class="ookla-desc">
            Automated Ookla data extraction, processing, and visualization for weekly
            LTE/5G performance tracking, province ranking, carrier comparison,
            and market-level speed analysis.
        </p>
    </div>
</div>
""", height=490)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.ookla-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.ookla-info-card {
    background: rgba(8,20,38,0.86);
    border: 1px solid rgba(0,229,255,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,229,255,0.08);
}

.ookla-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,229,255,0.75);
    box-shadow:
        0 0 28px rgba(0,229,255,0.32),
        0 0 60px rgba(0,229,255,0.14);
}

.ookla-card-title {
    color: #ffffff;
    font-size: 28px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.ookla-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.85;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="ookla-three-wrap">

    <div class="ookla-info-card">
        <div class="ookla-card-title">API Automation Workflow</div>
        <div class="ookla-line">✅ Checks existing data before downloading</div>
        <div class="ookla-line">✅ Downloads only new Ookla records</div>
        <div class="ookla-line">✅ Manual or scheduled execution</div>
        <div class="ookla-line">✅ Windows Task Scheduler support</div>
        <div class="ookla-line">✅ SharePoint centralized storage</div>
        <div class="ookla-line">✅ Historical data accumulation</div>
    </div>

    <div class="ookla-info-card">
        <div class="ookla-card-title">Power BI Dashboard Value</div>
        <div class="ookla-line">✅ SharePoint-linked Power BI refresh</div>
        <div class="ookla-line">✅ Avoids Power BI Pro license requests</div>
        <div class="ookla-line">✅ Accessible from team laptops</div>
        <div class="ookla-line">✅ Province / City / Raw-data views</div>
        <div class="ookla-line">✅ Zain / STC / Mobily comparison</div>
        <div class="ookla-line">✅ 4G / 5G / Overall monitoring</div>
    </div>

    <div class="ookla-info-card">
        <div class="ookla-card-title">Ranking & Monitoring Insight</div>
        <div class="ookla-line">🏆 Province operator ranking</div>
        <div class="ookla-line">📅 Weekly / Monthly Report</div>
        <div class="ookla-line">📍 Last-day monitoring view and Ranking</div>
        <div class="ookla-line">📊 Action effectiveness validation</div>
        <div class="ookla-line">⚡ Faster optimization decisions</div>
        <div class="ookla-line">📈 Continuous performance tracking</div>
    </div>

</div>
""", height=390)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Dashboard Preview</div>
    <div>Power BI view for Ookla weekly market analysis.</div>
</div>
""", unsafe_allow_html=True)

    if os.path.exists("assets/Ookla_PI.png"):
        st.image("assets/Ookla_PI.png", use_container_width=True)
    else:
        st.warning("Add your image here: assets/Ookla_PI.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <div>API script execution and dashboard workflow demonstration.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/Ookla_video.mp4",
        "ooklaDemoVideo",
        "Add your video here: assets/Ookla_video.mp4"
    )



############################## worst cell ####################


def show_worst_cells_page():

    components.html("""
<style>
.worst-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(255,80,80,0.25), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(0,229,255,0.22), transparent 26%);
    border: 1px solid rgba(0,229,255,0.22);
    box-shadow: 0 0 55px rgba(0,229,255,0.14);
    position: relative;
    overflow: hidden;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.worst-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(255,80,80,0.18);
    border: 1px solid rgba(255,120,120,0.35);
    color: #ffe5e5;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}

.worst-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #ff6b6b, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.worst-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.worst-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}



</style>

<div class="worst-hero">
    <div>
        <div class="worst-badge">🚨 WORST CELLS &nbsp;&nbsp; POWER BI / DAILY AUTOMATION</div>
        <div class="worst-big">Worst Cells Dashboard</div>
        <div class="worst-sub">Daily KPI Degradation Monitoring</div>
        <p class="worst-desc">
            Automated daily dashboard for detecting worst cells, zero traffic,
            repeated degradation, SR issues, and failure-count problems across RC02,
            RC03, and RC05 with clear visual ranking and color-based prioritization.
        </p>
    </div>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""

                    
<style>
.worst-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.worst-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,229,255,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,229,255,0.08);
}

.worst-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,229,255,0.75);
    box-shadow:
        0 0 28px rgba(0,229,255,0.32),
        0 0 60px rgba(0,229,255,0.14);
}

.worst-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.worst-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>


<div class="worst-three-wrap">
    <div class="worst-info-card">
        <div class="worst-card-title">Daily Automation Workflow</div>
        <div class="worst-line">✅ Scheduled daily Report 001 from NetAct</div>
        <div class="worst-line">✅ Uses NetAct scheduling for automatic export</div>
        <div class="worst-line">✅ Outlook macro saves RC02/RC03/RC05 attachments</div>
        <div class="worst-line">✅ Files stored automatically into local folders</div>
        <div class="worst-line">✅ Power BI connected directly to these folders</div>
        <div class="worst-line">✅ Dashboard refreshes from daily inputs</div>
    </div>

    <div class="worst-info-card">
        <div class="worst-card-title">Worst Cell Detection</div>
        <div class="worst-line">🚨 Dedicated view for worst cells by SR</div>
        <div class="worst-line">📉 Failure-count based prioritization</div>
        <div class="worst-line">🟥 Red highlights for critical degradation</div>
        <div class="worst-line">🟨 Yellow highlights for warning cases</div>
        <div class="worst-line">🟩 Green highlights for healthy cells</div>
        <div class="worst-line">⚡ Faster troubleshooting focus</div>
    </div>

    <div class="worst-info-card">
        <div class="worst-card-title">Filtering & Zero Traffic</div>
        <div class="worst-line">✅ Filter by RC02 / RC03 / RC05</div>
        <div class="worst-line">✅ Filter by date and specific site</div>
        <div class="worst-line">✅ Detect zero-traffic cells</div>
        <div class="worst-line">✅ Count repeated zero-traffic days</div>
        <div class="worst-line">✅ Detect traffic reduction trends</div>
        <div class="worst-line">✅ Faster daily monitoring actions</div>
    </div>
</div>
""", height=600)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Dashboard Preview</div>
    <div>Power BI views for worst-cell ranking, zero traffic, traffic reduction, and KPI trend monitoring.</div>
</div>
""", unsafe_allow_html=True)

    if os.path.exists("assets/Panormic_1.png"):
        st.image("assets/Panormic_1.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/Panormic_1.png")

    st.markdown("<br>", unsafe_allow_html=True)

    if os.path.exists("assets/Panormic_2.png"):
        st.image("assets/Panormic_2.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/Panormic_2.png")




#########################################   4G 5G dasboard ################################################



def show_4g5g_dashboard_page():

    components.html("""
<style>
.dashboard-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(0,255,120,0.22), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(0,229,255,0.20), transparent 26%);
    border: 1px solid rgba(0,255,120,0.22);
    box-shadow: 0 0 55px rgba(0,255,120,0.12);
    position: relative;
    overflow: hidden;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.dashboard-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(0,255,120,0.16);
    border: 1px solid rgba(0,255,120,0.35);
    color: #dfffea;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}

.dashboard-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #00ff88, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.dashboard-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
    color: white;
}

.dashboard-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}

.dashboard-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.dashboard-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,255,120,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,255,120,0.08);
}

.dashboard-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,255,120,0.75);
    box-shadow:
        0 0 28px rgba(0,255,120,0.28),
        0 0 60px rgba(0,255,120,0.12);
}

.dashboard-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.dashboard-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="dashboard-hero">

    <div>
        <div class="dashboard-badge">
            📊 4G / 5G &nbsp;&nbsp; KPI ANALYTICS / ROOT CAUSE
        </div>

        <div class="dashboard-big">
            4G / 5G Dashboard
        </div>

        <div class="dashboard-sub">
            Automated KPI & Root Cause Monitoring
        </div>

        <p class="dashboard-desc">
            Advanced Power BI dashboard integrating accessibility, retainability,
            mobility, traffic, utilization, and root-cause KPIs into a single
            automated monitoring platform for faster analysis and troubleshooting.
        </p>
    </div>

</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.dashboard-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.dashboard-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,255,120,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,255,120,0.08);
}

.dashboard-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,255,120,0.75);
    box-shadow:
        0 0 28px rgba(0,255,120,0.28),
        0 0 60px rgba(0,255,120,0.12);
}

.dashboard-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.dashboard-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="dashboard-three-wrap">

    <div class="dashboard-info-card">
        <div class="dashboard-card-title">Combined NetAct Reporting</div>
        <div class="dashboard-line">✅ Customized combined NetAct reports</div>
        <div class="dashboard-line">✅ Multiple reports merged into one</div>
        <div class="dashboard-line">✅ Includes main KPIs and counters</div>
        <div class="dashboard-line">✅ Includes root-cause KPIs</div>
        <div class="dashboard-line">✅ Cleaner and centralized analysis</div>
        <div class="dashboard-line">✅ Faster engineering workflow</div>
    </div>

    <div class="dashboard-info-card">
        <div class="dashboard-card-title">Flexible Dashboard Execution</div>
        <div class="dashboard-line">✅ RAW / Hourly / Daily modes</div>
        <div class="dashboard-line">✅ Can run for one site or cluster</div>
        <div class="dashboard-line">✅ RC-level monitoring support</div>
        <div class="dashboard-line">✅ Easy filtering and navigation</div>
        <div class="dashboard-line">✅ Quick troubleshooting visibility</div>
        <div class="dashboard-line">✅ Faster issue localization</div>
    </div>

    <div class="dashboard-info-card">
        <div class="dashboard-card-title">Visualization & Time Saving</div>
        <div class="dashboard-line">📊 Easy-to-read charts and matrix views</div>
        <div class="dashboard-line">📈 KPI trend monitoring</div>
        <div class="dashboard-line">⚡ Quick root-cause analysis</div>
        <div class="dashboard-line">🚨 Faster worst-cell identification</div>
        <div class="dashboard-line">🟢 Clear performance visibility</div>
        <div class="dashboard-line">⏳ Saves significant engineering time</div>
    </div>

</div>
""", height=390)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">4G Dashboard Preview</div>
    <div>Power BI visualization for LTE KPI analysis and troubleshooting.</div>
</div>
""", unsafe_allow_html=True)

    if os.path.exists("assets/4G_pic.png"):
        st.image("assets/4G_pic.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/4G_pic.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">5G Dashboard Preview</div>
    <div>Power BI visualization for NR KPI analysis and mobility monitoring.</div>
</div>
""", unsafe_allow_html=True)

    if os.path.exists("assets/5G_pic.png"):
        st.image("assets/5G_pic.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/5G_pic.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Dashboard Demo Video</div>
    <div>4G / 5G dashboard navigation and KPI analysis workflow.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/dashboard_video.mp4",
        "dashboardDemoVideo",
        "Add your video here: assets/dashboard_video.mp4"
    )



################################## site databse #################################################


def show_site_database_page():

    components.html("""
<style>
.database-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(0,255,120,0.22), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(0,229,255,0.20), transparent 26%);
    border: 1px solid rgba(0,255,120,0.22);
    box-shadow: 0 0 55px rgba(0,255,120,0.12);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.database-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: rgba(0,255,120,0.16);
    border: 1px solid rgba(0,255,120,0.35);
    color: #dfffea;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}

.database-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #00ff88, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.database-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.database-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="database-hero">
    <div class="database-badge">🗄️ SITE DATABASE &nbsp;&nbsp; ACCESS / MDB AUTOMATION</div>
    <div class="database-big">Site Database</div>
    <div class="database-sub">Automated Reference Database Update</div>
    <p class="database-desc">
        Microsoft Access automation linked with RC02, RC03, and RC05 MDB files
        to detect new sites and cells, validate reference data, update changes,
        and export clean database outputs for sharing.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.database-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.database-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,255,120,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,255,120,0.08);
}

.database-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,255,120,0.75);
    box-shadow:
        0 0 28px rgba(0,255,120,0.28),
        0 0 60px rgba(0,255,120,0.12);
}

.database-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.database-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="database-three-wrap">

    <div class="database-info-card">
        <div class="database-card-title">MDB Integration</div>
        <div class="database-line">✅ Linked Access database with RC02 / RC03 / RC05 MDBs</div>
        <div class="database-line">✅ Centralized reference database structure</div>
        <div class="database-line">✅ Supports 4G and 5G tables</div>
        <div class="database-line">✅ Reduces manual lookup work</div>
        <div class="database-line">✅ Keeps site/cell reference data organized</div>
    </div>

    <div class="database-info-card">
        <div class="database-card-title">Auto Validation & Update</div>
        <div class="database-line">✅ Detects new sites and cells automatically</div>
        <div class="database-line">✅ Adds new records into the database</div>
        <div class="database-line">✅ Checks if existing data is correct</div>
        <div class="database-line">✅ Reflects changes into reference tables</div>
        <div class="database-line">✅ Reduces update errors and missing records</div>
    </div>

    <div class="database-info-card">
        <div class="database-card-title">Export & Time Saving</div>
        <div class="database-line">✅ Export database into Excel for sharing</div>
        <div class="database-line">✅ Can be scheduled for daily updates</div>
        <div class="database-line">✅ Manual update completed within few minutes</div>
        <div class="database-line">✅ Replaces hours of manual work</div>
        <div class="database-line">✅ Saves significant operational time</div>
    </div>

</div>
""", height=500)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Database Preview</div>
    <div>Access database view showing site/cell reference validation and update automation.</div>
</div>
""", unsafe_allow_html=True)

    if os.path.exists("assets/database_pic.png"):
        st.image("assets/database_pic.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/database_pic.png")



##################################### LLD Radio #############################################################


def show_radio_lld_page():

    components.html("""
<style>
.lld-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(0,229,255,0.24), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(0,255,120,0.20), transparent 26%);
    border: 1px solid rgba(0,229,255,0.22);
    box-shadow: 0 0 55px rgba(0,229,255,0.14);
    color: white;
    font-family: Inter, Arial, sans-serif;
}



.lld-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #ffd166, #ff9f1c);
    border: 1px solid rgba(255,209,102,0.35);
    color: #1a1a1a;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}                    


.lld-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #ffd166, #ff9f1c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.lld-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.lld-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="lld-hero">
    <div class="lld-badge">📡 RADIO LLD &nbsp;&nbsp; DATABASE / HARDWARE AUTOMATION</div>
    <div class="lld-big">Radio LLD Automation</div>
    <div class="lld-sub">Automated Low-Level Design Generation</div>
    <p class="lld-desc">
        Generates Radio LLD outputs from site database and hardware data in less than
        one minute, replacing hours of manual preparation, repeated VLOOKUPs,
        and error-prone engineering checks.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.lld-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.lld-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,229,255,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,229,255,0.08);
}

.lld-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,229,255,0.75);
    box-shadow:
        0 0 28px rgba(0,229,255,0.32),
        0 0 60px rgba(0,229,255,0.14);
}

.lld-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.lld-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="lld-three-wrap">

    <div class="lld-info-card">
        <div class="lld-card-title">Automated Inputs</div>
        <div class="lld-line">✅ Uses site database / hardware data as main input</div>
        <div class="lld-line">✅ Combines required engineering references</div>
        <div class="lld-line">✅ Reduces manual file preparation</div>
        <div class="lld-line">✅ Avoids repeated manual lookups</div>
    </div>

    <div class="lld-info-card">
        <div class="lld-card-title">LLD Generation Engine</div>
        <div class="lld-line">✅ Generates Radio LLD output automatically</div>
        <div class="lld-line">✅ Produces final output in less than 1 minute</div>
        <div class="lld-line">✅ Replaces hours of manual work</div>
        <div class="lld-line">✅ Removes dependency on many VLOOKUPs</div>
        <div class="lld-line">✅ Improves consistency and accuracy</div>
    </div>

    <div class="lld-info-card">
        <div class="lld-card-title">Operational Benefit</div>
        <div class="lld-line">⚡ Faster LLD preparation cycle</div>
        <div class="lld-line">🎯 Lower risk of human mistakes</div>
        <div class="lld-line">📊 Cleaner and standardized output</div>
        <div class="lld-line">🧩 Easier validation for planning teams</div>
        <div class="lld-line">⏳ Saves significant engineering time</div>
    </div>

</div>
""", height=450)

    st.markdown("<br>", unsafe_allow_html=True)


    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
    <div class="kml-card">
        <div class="kml-section-title">LLD Tool Interface</div>
    </div>
    """, unsafe_allow_html=True)

        if os.path.exists("assets/LLD_Tool.png"):
            st.image(
                "assets/LLD_Tool.png",
                use_container_width=True
            )
        else:
            st.warning("Add image here: assets/LLD_Tool.png")

    with col2:

        st.markdown("""
    <div class="kml-card">
        <div class="kml-section-title">Generated LLD Output</div>
    </div>
    """, unsafe_allow_html=True)

        if os.path.exists("assets/LLD_tool_2.png"):
            st.image(
                "assets/LLD_tool_2.png",
                use_container_width=True
            )
        else:
            st.warning("Add image here: assets/LLD_tool_2.png")






    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <div>End-to-end Radio LLD generation workflow demonstration.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/LLD_VIDEO.mp4",
        "lldDemoVideo",
        "Add your video here: assets/LLD_VIDEO.mp4"
    )



###############################################  GLI_TX_Report ####################################################

def show_gli_tx_page():

    components.html("""
<style>
.gli-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(180,120,255,0.24), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(255,0,200,0.18), transparent 26%);
    border: 1px solid rgba(180,120,255,0.22);
    box-shadow: 0 0 55px rgba(180,120,255,0.12);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.gli-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #c77dff, #9d4edd);
    border: 1px solid rgba(199,125,255,0.35);
    color: white;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 24px;
}

.gli-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #e0aaff, #9d4edd);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.gli-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.gli-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="gli-hero">
    <div class="gli-badge">📡 GLI TX &nbsp;&nbsp; TRANSMISSION / AUTOMATION</div>
    <div class="gli-big">GLI TX Report</div>
    <div class="gli-sub">Automated Transmission Reporting</div>
    <p class="gli-desc">
        Automated GLI TX reporting and analysis platform designed to simplify
        transmission monitoring, reduce manual engineering effort, and generate
        faster operational insights using clean automated workflows.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.gli-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.gli-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(180,120,255,0.22);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(180,120,255,0.08);
}

.gli-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(180,120,255,0.75);
    box-shadow:
        0 0 28px rgba(180,120,255,0.28),
        0 0 60px rgba(180,120,255,0.12);
}

.gli-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.gli-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="gli-three-wrap">
    <div class="gli-info-card">
        <div class="gli-card-title">Automated Workflow</div>
        <div class="gli-line">✅ Automated GLI TX report generation</div>
        <div class="gli-line">✅ Reduces manual engineering effort</div>
        <div class="gli-line">✅ Faster daily operational visibility</div>
        <div class="gli-line">✅ Cleaner reporting structure</div>
        <div class="gli-line">✅ Simplifies transmission analysis</div>
    </div>

    <div class="gli-info-card">
        <div class="gli-card-title">Analysis & Monitoring</div>
        <div class="gli-line">📊 Easy KPI visualization</div>
        <div class="gli-line">📈 Quick transmission issue detection</div>
        <div class="gli-line">⚡ Faster troubleshooting workflow</div>
        <div class="gli-line">🎯 Cleaner operational insights</div>
        <div class="gli-line">🚨 Better performance visibility</div>
    </div>

    <div class="gli-info-card">
        <div class="gli-card-title">Business Value</div>
        <div class="gli-line">⏳ Saves engineering time</div>
        <div class="gli-line">✅ Standardized reporting output</div>
        <div class="gli-line">📉 Reduces manual mistakes</div>
        <div class="gli-line">📡 Better transmission monitoring</div>
        <div class="gli-line">🚀 Improves operational efficiency</div>
    </div>
</div>
""", height=390)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.gli-speed-card {
    max-width: 980px;
    margin: 0 auto;
    padding: 36px;
    border-radius: 28px;
    background:
        linear-gradient(135deg,
            rgba(25,18,35,0.96),
            rgba(65,30,85,0.92));
    border: 1px solid rgba(199,125,255,0.35);
    box-shadow:
        0 0 30px rgba(199,125,255,0.22),
        0 0 80px rgba(157,78,221,0.12);
    color: white;
    text-align: center;
    font-family: Inter, Arial, sans-serif;
    transition: all 0.35s ease;
}

.gli-speed-card:hover {
    transform: translateY(-8px) scale(1.015);
    border-color: rgba(199,125,255,0.75);
    box-shadow:
        0 0 40px rgba(199,125,255,0.35),
        0 0 100px rgba(157,78,221,0.18);
}

.gli-speed-title {
    font-size: 24px;
    font-weight: 900;
    color: #e0aaff;
    margin-bottom: 14px;
}

.gli-speed-number {
    font-size: 62px;
    font-weight: 900;
    background: linear-gradient(90deg, #e0aaff, #c77dff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}

.gli-speed-desc {
    margin-top: 16px;
    font-size: 19px;
    font-weight: 700;
    color: #f3eaff;
}
</style>

<div class="gli-speed-card">
    <div class="gli-speed-title">⚡ Performance Benchmark</div>
    <div class="gli-speed-number">114 Sites / Relations</div>
    <div class="gli-speed-desc">
        Report generated in only
        <b style="color:white;">3.2 seconds</b>
        instead of around
        <b style="color:white;">3 hours</b>
    </div>
</div>
""", height=270)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">GLI TX Tool Interface</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/GLI_1.png"):
            st.image("assets/GLI_1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/GLI_1.png")

    with col2:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Generated GLI TX Output</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/GLI_2.png"):
            st.image("assets/GLI_2.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/GLI_2.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <div>GLI TX automation and reporting workflow demonstration.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/GLI_VIDEO.mp4",
        "gliVideo",
        "Add your video here: assets/GLI_VIDEO.mp4"
    )
################################################### TMR report  ######################################################################################

def show_tmr_report_page():

    components.html("""
<style>
.tmr-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(255,140,180,0.24), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(180,120,255,0.20), transparent 26%);
    border: 1px solid rgba(255,140,180,0.25);
    box-shadow: 0 0 55px rgba(255,140,180,0.12);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.tmr-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #ffb3c6, #c77dff);
    border: 1px solid rgba(255,179,198,0.35);
    color: #1a1a1a;
    font-weight: 900;
    font-size: 14px;
    margin-bottom: 24px;
}

.tmr-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #ffb3c6, #c77dff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tmr-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.tmr-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="tmr-hero">
    <div class="tmr-badge">📊 TMR REPORT &nbsp;&nbsp; FMR / CUSTOMER TEMPLATE AUTOMATION</div>
    <div class="tmr-big">TMR Report Builder</div>
    <div class="tmr-sub">Automated Customer Report Generation</div>
    <p class="tmr-desc">
        Builds customer-ready TMR reports from FMR input files and customer output templates,
        automating data extraction, formatting, KPI filling, and final report preparation.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.tmr-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.tmr-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(255,140,180,0.25);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(255,140,180,0.08);
}

.tmr-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(255,140,180,0.75);
    box-shadow:
        0 0 28px rgba(255,140,180,0.30),
        0 0 60px rgba(180,120,255,0.12);
}

.tmr-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.tmr-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="tmr-three-wrap">

    <div class="tmr-info-card">
        <div class="tmr-card-title">Input Processing</div>
        <div class="tmr-line">✅ Uses FMR report as main input</div>
        <div class="tmr-line">✅ Reads required KPI and test-result sections</div>
        <div class="tmr-line">✅ Extracts key values automatically</div>
        <div class="tmr-line">✅ Reduces manual copy/paste work</div>
        <div class="tmr-line">✅ Avoids repeated manual checks</div>
    </div>

    <div class="tmr-info-card">
        <div class="tmr-card-title">Template Automation</div>
        <div class="tmr-line">✅ Uses customer output template</div>
        <div class="tmr-line">✅ Fills values into correct report fields</div>
        <div class="tmr-line">✅ Keeps customer format standardized</div>
        <div class="tmr-line">✅ Reduces formatting mistakes</div>
        <div class="tmr-line">✅ Generates clean final TMR output</div>
    </div>

    <div class="tmr-info-card">
        <div class="tmr-card-title">Business Value</div>
        <div class="tmr-line">⚡ Faster TMR report preparation</div>
        <div class="tmr-line">📉 Less manual workload</div>
        <div class="tmr-line">🎯 Improved accuracy and consistency</div>
        <div class="tmr-line">📊 Customer-ready reporting output</div>
        <div class="tmr-line">⏳ Saves significant engineering time</div>
    </div>

</div>
""", height=390)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.tmr-speed-card {
    max-width: 980px;
    margin: 0 auto;
    padding: 36px;
    border-radius: 28px;
    background:
        linear-gradient(135deg,
            rgba(25,18,35,0.96),
            rgba(70,30,55,0.92));
    border: 1px solid rgba(255,140,180,0.30);
    box-shadow:
        0 0 30px rgba(255,140,180,0.18),
        0 0 80px rgba(180,120,255,0.10);
    color: white;
    text-align: center;
    font-family: Inter, Arial, sans-serif;
    transition: all 0.35s ease;
}

.tmr-speed-card:hover {
    transform: translateY(-8px) scale(1.015);
    border-color: rgba(255,140,180,0.75);
    box-shadow:
        0 0 40px rgba(255,140,180,0.28),
        0 0 100px rgba(180,120,255,0.18);
}

.tmr-speed-title {
    font-size: 24px;
    font-weight: 900;
    color: #ffb3c6;
    margin-bottom: 14px;
}

.tmr-speed-number {
    font-size: 62px;
    font-weight: 900;
    background: linear-gradient(90deg, #ffb3c6, #c77dff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}

.tmr-speed-desc {
    margin-top: 16px;
    font-size: 19px;
    font-weight: 700;
    color: #f3eaff;
}
</style>

<div class="tmr-speed-card">
    <div class="tmr-speed-title">⚡ Performance Benchmark</div>
    <div class="tmr-speed-number">20 Sites</div>
    <div class="tmr-speed-desc">
        Report generated in only
        <b style="color:white;">11 seconds</b>
        instead of around
        <b style="color:white;">2 hours</b>
    </div>
</div>
""", height=270)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">TMR Builder Interface</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/TMR_1.png"):
            st.image("assets/TMR_1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/TMR_1.png")

    with col2:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Generated TMR Output</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/TMR_2.png"):
            st.image("assets/TMR_2.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/TMR_2.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <div>TMR report generation workflow demonstration.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/TMR_VIDEO.mp4",
        "tmrVideo",
        "Add your video here: assets/TMR_VIDEO.mp4"
    )


####################################################### SSV BUILDER  ################################################################

def show_ssv_builder_page():

    components.html("""
<style>
.ssv-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(0,255,200,0.22), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(255,209,102,0.18), transparent 26%);
    border: 1px solid rgba(0,255,200,0.24);
    box-shadow: 0 0 55px rgba(0,255,200,0.13);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.ssv-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #00f5d4, #ffd166);
    border: 1px solid rgba(0,245,212,0.35);
    color: #06111f;
    font-weight: 900;
    font-size: 14px;
    margin-bottom: 24px;
}

.ssv-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #00f5d4, #ffd166);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.ssv-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.ssv-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="ssv-hero">
    <div class="ssv-badge">📑 SSV BUILDER &nbsp;&nbsp; 2G / 4G / 5G REPORT AUTOMATION</div>
    <div class="ssv-big">SSV Builder</div>
    <div class="ssv-sub">Automated Site Verification Report Generation</div>
    <p class="ssv-desc">
        Generates customer-ready SSV reports for 2G, 4G, and 5G using predefined templates,
        site classification data, panoramic images, and drive-test plots with a clean,
        standardized output structure.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.ssv-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.ssv-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,255,200,0.24);
    border-radius: 22px;
    padding: 26px;
    min-height: 330px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,255,200,0.08);
}

.ssv-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,255,200,0.75);
    box-shadow:
        0 0 28px rgba(0,255,200,0.28),
        0 0 60px rgba(255,209,102,0.12);
}

.ssv-card-title {
    color: #ffffff;
    font-size: 29px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
}

.ssv-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 600;
}
</style>

<div class="ssv-three-wrap">

    <div class="ssv-info-card">
        <div class="ssv-card-title">Template-Based SSV</div>
        <div class="ssv-line">✅ Generates SSV reports for 2G / 4G / 5G</div>
        <div class="ssv-line">✅ Uses customer-approved templates</div>
        <div class="ssv-line">✅ Supports full-technology site reporting</div>
        <div class="ssv-line">✅ Standardized output format</div>
        <div class="ssv-line">✅ Reduces formatting and copy/paste work</div>
    </div>

    <div class="ssv-info-card">
        <div class="ssv-card-title">Site Classification</div>
        <div class="ssv-line">✅ Adds coordinates and cells information</div>
        <div class="ssv-line">✅ Includes PCI, height, and azimuth details</div>
        <div class="ssv-line">✅ Inserts panoramic 360° images</div>
        <div class="ssv-line">✅ Organizes images by azimuth direction</div>
        <div class="ssv-line">✅ Improves consistency of site documentation</div>
    </div>

    <div class="ssv-info-card">
        <div class="ssv-card-title">Drive Test Visualization</div>
        <div class="ssv-line">✅ Adds RSRP plots by technology layer</div>
        <div class="ssv-line">✅ Adds PCI and SINR drive-test plots</div>
        <div class="ssv-line">✅ Supports 2G / 4G / 5G reporting views</div>
        <div class="ssv-line">✅ Clean visualization inside template</div>
        <div class="ssv-line">✅ Faster customer-ready SSV delivery</div>
    </div>

</div>
""", height=510)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.ssv-speed-card {
    max-width: 980px;
    margin: 0 auto;
    padding: 36px;
    border-radius: 28px;
    background:
        linear-gradient(135deg,
            rgba(8,20,38,0.96),
            rgba(25,70,65,0.92));
    border: 1px solid rgba(0,245,212,0.35);
    box-shadow:
        0 0 30px rgba(0,245,212,0.18),
        0 0 80px rgba(255,209,102,0.10);
    color: white;
    text-align: center;
    font-family: Inter, Arial, sans-serif;
    transition: all 0.35s ease;
}

.ssv-speed-card:hover {
    transform: translateY(-8px) scale(1.015);
    border-color: rgba(0,245,212,0.75);
    box-shadow:
        0 0 40px rgba(0,245,212,0.28),
        0 0 100px rgba(255,209,102,0.18);
}

.ssv-speed-title {
    font-size: 24px;
    font-weight: 900;
    color: #00f5d4;
    margin-bottom: 14px;
}

.ssv-speed-number {
    font-size: 62px;
    font-weight: 900;
    background: linear-gradient(90deg, #00f5d4, #ffd166);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
}

.ssv-speed-desc {
    margin-top: 16px;
    font-size: 19px;
    font-weight: 700;
    color: #e9fff9;
}
</style>

<div class="ssv-speed-card">
    <div class="ssv-speed-title">⚡ Performance Benchmark</div>
    <div class="ssv-speed-number">1 Minute</div>
    <div class="ssv-speed-desc">
        Full-technology SSV generated in around
        <b style="color:white;">1 minute</b>
        instead of
        <b style="color:white;">30–45 minutes per site</b>
    </div>
</div>
""", height=270)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">SSV Builder Interface</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/SSV_1.png"):
            st.image("assets/SSV_1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/SSV_1.png")

    with col2:
        st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Generated SSV Output</div>
</div>
""", unsafe_allow_html=True)

        if os.path.exists("assets/SSV_2.png"):
            st.image("assets/SSV_2.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/SSV_2.png")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div class="kml-card">
    <div class="kml-section-title">Demo Video</div>
    <div>SSV report generation workflow demonstration.</div>
</div>
""", unsafe_allow_html=True)

    show_video(
        "assets/SSV_VIDEO.mp4",
        "ssvVideo",
        "Add your video here: assets/SSV_VIDEO.mp4"
    )



####################################################### SSV plot proccesing  ##############################################################################

def show_ssv_plot_processing_page():

    components.html("""
<style>
.plot-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98), rgba(2,8,23,0.80), rgba(2,8,23,0.30)),
        radial-gradient(circle at 75% 40%, rgba(0,180,255,0.24), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(255,80,180,0.18), transparent 26%);
    border: 1px solid rgba(0,180,255,0.25);
    box-shadow: 0 0 55px rgba(0,180,255,0.14);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.plot-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #00b4ff, #ff4fd8);
    color: white;
    font-weight: 900;
    font-size: 14px;
    margin-bottom: 24px;
}

.plot-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #00b4ff, #ff4fd8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.plot-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
}

.plot-desc {
    color: #d7e7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
}
</style>

<div class="plot-hero">
    <div class="plot-badge">🗺️ SSV PLOT &nbsp;&nbsp; LOGOS CSV / DRIVE TEST AUTOMATION</div>
    <div class="plot-big">SSV Plot Processing</div>
    <div class="plot-sub">Automated LOGOS Plot Generation</div>
    <p class="plot-desc">
        Processes LOGOS CSV files generated after Nokia BTS Manager parsing
        to create RSRP, PCI, SINR and technology-layer plots without visiting
        sites or using expensive external plotting tools.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.plot-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    font-family: Inter, Arial, sans-serif;
}

.plot-info-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 22px;
    padding: 26px;
    min-height: 335px;
    color: white;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(0,180,255,0.08);
}

.plot-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,180,255,0.75);
    box-shadow: 0 0 28px rgba(0,180,255,0.30), 0 0 60px rgba(255,80,180,0.12);
}

.plot-card-title {
    color: white;
    font-size: 29px;
    font-weight: 900;
    margin-bottom: 20px;
}

.plot-line {
    color: #d7e7ff;
    font-size: 15px;
    line-height: 1.9;
    font-weight: 600;
}
</style>

<div class="plot-three-wrap">
    <div class="plot-info-card">
        <div class="plot-card-title">LOGOS-Based Processing</div>
        <div class="plot-line">✅ Uses LOGOS CSV files as input</div>
        <div class="plot-line">✅ Files generated after Nokia BTS Manager parsing</div>
        <div class="plot-line">✅ Avoids physical site drive-test visits</div>
        <div class="plot-line">✅ Reduces transportation and field resources</div>
        <div class="plot-line">✅ Supports faster remote site analysis</div>
    </div>

    <div class="plot-info-card">
        <div class="plot-card-title">MUSA Alternative</div>
        <div class="plot-line">✅ Avoids MUSA license dependency and cost</div>
        <div class="plot-line">✅ Faster than MUSA import and processing flow</div>
        <div class="plot-line">✅ Easier site-specific filtering</div>
        <div class="plot-line">✅ Easier distance filtering</div>
        <div class="plot-line">✅ Avoids complicated polygon preparation</div>
    </div>

    <div class="plot-info-card">
        <div class="plot-card-title">Visualization Output</div>
        <div class="plot-line">📊 Generates RSRP plots</div>
        <div class="plot-line">📡 Generates PCI plots</div>
        <div class="plot-line">⚡ Generates SINR plots</div>
        <div class="plot-line">✅ Supports technology-layer views</div>
        <div class="plot-line">🎯 Cleaner filtering and better visualization</div>
    </div>
</div>
""", height=420)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.plot-speed-card {
    max-width: 980px;
    margin: 0 auto;
    padding: 36px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(8,20,38,0.96), rgba(50,20,75,0.92));
    border: 1px solid rgba(0,180,255,0.35);
    color: white;
    text-align: center;
    font-family: Inter, Arial, sans-serif;
    transition: all 0.35s ease;
}

.plot-speed-card:hover {
    transform: translateY(-8px) scale(1.015);
    box-shadow: 0 0 40px rgba(0,180,255,0.32), 0 0 100px rgba(255,80,180,0.18);
}

.plot-speed-title {
    font-size: 24px;
    font-weight: 900;
    color: #7dd3ff;
    margin-bottom: 14px;
}

.plot-speed-number {
    font-size: 62px;
    font-weight: 900;
    background: linear-gradient(90deg, #00b4ff, #ff4fd8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.plot-speed-desc {
    font-size: 19px;
    font-weight: 700;
    color: #eef6ff;
}
</style>

<div class="plot-speed-card">
    <div class="plot-speed-title">⚡ Performance Benchmark</div>
    <div class="plot-speed-number">1 Site / All Frequencies</div>
    <div class="plot-speed-desc">
        Plot generated in around <b style="color:white;">1 minute</b>
        instead of <b style="color:white;">hours in MUSA and Field Visit</b>
    </div>
</div>
""", height=290)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        components.html("""
<style>
.img-title {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 20px;
    padding: 20px;
    color: white;
    font-size: 30px;
    font-weight: 900;
    font-family: Inter, Arial, sans-serif;
}
</style>
<div class="img-title">LOGOS Output</div>
""", height=90)

        if os.path.exists("assets/LOGOS_1.png"):
            st.image("assets/LOGOS_1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/LOGOS_1.png")

    with col2:
        components.html("""
<style>
.img-title {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 20px;
    padding: 20px;
    color: white;
    font-size: 30px;
    font-weight: 900;
    font-family: Inter, Arial, sans-serif;
}
</style>
<div class="img-title">Legacy Output</div>
""", height=90)

        if os.path.exists("assets/LEGACY_1.png"):
            st.image("assets/LEGACY_1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/LEGACY_1.png")

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.info-title-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 22px;
    padding: 24px;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.info-title {
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 12px;
}

.info-desc {
    color: #d7e7ff;
    font-size: 18px;
    line-height: 1.6;
}
</style>

<div class="info-title-card">
    <div class="info-title">LOGOS Added Details</div>
    <div class="info-desc">
        LOGOS can also show Handover Types and EARFCN directly from the parsed LOGOS data.
    </div>
</div>
""", height=150)

    g1, g2, g3 = st.columns([1, 2, 1])

    with g2:
        if os.path.exists("assets/LOGOS_1.1.png"):
            st.image("assets/LOGOS_1.1.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/LOGOS_1.1.png")

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.info-title-card {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 22px;
    padding: 24px;
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.info-title {
    font-size: 30px;
    font-weight: 900;
    margin-bottom: 12px;
}

.info-desc {
    color: #d7e7ff;
    font-size: 18px;
    line-height: 1.6;
}
</style>

<div class="info-title-card">
    <div class="info-title">LOGOS vs Legacy Distance Coverage</div>
    <div class="info-desc">
        LOGOS can cover longer distance than the legacy workflow with simpler filtering and more accurate values.
    </div>
</div>
""", height=150)

    if os.path.exists("assets/LOGOS VS LEGACY.png"):
        st.image("assets/LOGOS VS LEGACY.png", use_container_width=True)
    else:
        st.warning("Add image here: assets/LOGOS VS LEGACY.png")

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.img-title {
    background: rgba(8,20,38,0.92);
    border: 1px solid rgba(0,180,255,0.25);
    border-radius: 20px;
    padding: 20px;
    color: white;
    font-size: 30px;
    font-weight: 900;
    font-family: Inter, Arial, sans-serif;
}
</style>
<div class="img-title">LOGOS Tool GUI</div>
""", height=90)

    g1, g2, g3 = st.columns([1, 2, 1])

    with g2:
        if os.path.exists("assets/LOGOS_GUI.png"):
            st.image("assets/LOGOS_GUI.png", use_container_width=True)
        else:
            st.warning("Add image here: assets/LOGOS_GUI.png")


################################ acceptance tracker #######################################################################

def show_acceptance_tracker_page():

    components.html("""
<style>
.tracker-hero {
    min-height: 430px;
    padding: 50px;
    border-radius: 30px;
    background:
        linear-gradient(90deg, rgba(2,8,23,0.98) 0%, rgba(2,8,23,0.80) 45%, rgba(2,8,23,0.30) 100%),
        radial-gradient(circle at 75% 40%, rgba(120,90,255,0.30), transparent 28%),
        radial-gradient(circle at 85% 70%, rgba(0,229,255,0.18), transparent 26%);
    border: 1px solid rgba(120,90,255,0.35);
    box-shadow: 0 0 55px rgba(120,90,255,0.18);
    color: white;
    font-family: Inter, Arial, sans-serif;
}

.tracker-badge {
    display: inline-block;
    padding: 10px 20px;
    border-radius: 999px;
    background: linear-gradient(90deg, #7c4dff, #00e5ff);
    border: 1px solid rgba(120,90,255,0.45);
    color: #ffffff;
    font-weight: 900;
    font-size: 14px;
    margin-bottom: 24px;
    box-shadow: 0 0 20px rgba(0,229,255,0.22);
}

.tracker-big {
    font-size: 74px;
    font-weight: 900;
    line-height: 0.95;
    background: linear-gradient(90deg, #b388ff, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(0,229,255,0.18);
}

.tracker-sub {
    font-size: 34px;
    font-weight: 900;
    margin-top: 14px;
    color: #ffffff;
}

.tracker-desc {
    color: #f3f7ff;
    font-size: 20px;
    line-height: 1.6;
    margin-top: 22px;
    font-weight: 500;
}
</style>

<div class="tracker-hero">
    <div class="tracker-badge">
        ✅ ACCEPTANCE TRACKER &nbsp;&nbsp; MICROSOFT TEAMS / TASK MANAGEMENT
    </div>

    <div class="tracker-big">
        Acceptance Tracker
    </div>

    <div class="tracker-sub">
        Secure Collaborative Acceptance Workflow
    </div>

    <p class="tracker-desc">
        Microsoft Teams-based tracker for managing acceptance requests,
        assigning tasks, attaching evidence, tracking checklists,
        and enabling secure project collaboration over the internet
        with clear ownership and visibility.
    </p>
</div>
""", height=480)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.tracker-three-wrap {
    display: grid;
    grid-template-columns: repeat(3, 340px);
    gap: 24px;
    justify-content: center;
    align-items: stretch;
    font-family: Inter, Arial, sans-serif;
}

.tracker-info-card {
    background: rgba(8,20,38,0.94);
    border: 1px solid rgba(120,90,255,0.45);
    border-radius: 22px;
    padding: 26px;
    min-height: 315px;
    color: #ffffff;
    transition: all 0.35s ease;
    cursor: pointer;
    box-shadow: 0 0 25px rgba(120,90,255,0.16);
}

.tracker-info-card:hover {
    transform: translateY(-10px) scale(1.02);
    border-color: rgba(0,229,255,0.85);
    box-shadow:
        0 0 28px rgba(0,229,255,0.32),
        0 0 65px rgba(120,90,255,0.22);
}

.tracker-card-title {
    color: #ffffff;
    font-size: 30px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 20px;
    text-shadow: 0 0 14px rgba(255,255,255,0.18);
}

.tracker-line {
    color: #f4f8ff;
    font-size: 15px;
    line-height: 1.9;
    margin-bottom: 8px;
    font-weight: 700;
}
</style>

<div class="tracker-three-wrap">
    <div class="tracker-info-card">
        <div class="tracker-card-title">Task Assignment</div>
        <div class="tracker-line">✅ Create tracker directly inside Microsoft Teams</div>
        <div class="tracker-line">✅ Assign requests to specific persons</div>
        <div class="tracker-line">✅ Track ownership and responsibility</div>
        <div class="tracker-line">✅ Support multiple request types</div>
        <div class="tracker-line">✅ Improve follow-up visibility</div>
    </div>

    <div class="tracker-info-card">
        <div class="tracker-card-title">Evidence & Checklist</div>
        <div class="tracker-line">📎 Attach files and supporting evidence</div>
        <div class="tracker-line">☑️ Add checklist items for each request</div>
        <div class="tracker-line">📝 Track acceptance progress clearly</div>
        <div class="tracker-line">📌 Keep all request details centralized</div>
        <div class="tracker-line">📊 Reduce scattered communication</div>
    </div>

    <div class="tracker-info-card">
        <div class="tracker-card-title">Secure Collaboration</div>
        <div class="tracker-line">💬 Chat and discuss inside Teams</div>
        <div class="tracker-line">🔐 High-security Microsoft environment</div>
        <div class="tracker-line">🌐 Secure access over the internet</div>
        <div class="tracker-line">👥 Better collaboration with customer/team</div>
        <div class="tracker-line">⚡ Faster acceptance closure</div>
    </div>
</div>
""", height=390)

    st.markdown("<br>", unsafe_allow_html=True)

    components.html("""
<style>
.tracker-demo-card {
    max-width: 980px;
    margin: 0 auto;
    padding: 34px;
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(8,20,38,0.96), rgba(45,30,95,0.92));
    border: 1px solid rgba(120,90,255,0.45);
    box-shadow:
        0 0 35px rgba(120,90,255,0.30),
        0 0 90px rgba(0,229,255,0.14);
    color: white;
    text-align: center;
    font-family: Inter, Arial, sans-serif;
    transition: all 0.35s ease;
}

.tracker-demo-card:hover {
    transform: translateY(-8px) scale(1.015);
    border-color: rgba(0,229,255,0.85);
    box-shadow:
        0 0 45px rgba(0,229,255,0.35),
        0 0 110px rgba(120,90,255,0.22);
}

.tracker-demo-title {
    font-size: 34px;
    font-weight: 900;
    background: linear-gradient(90deg, #7c4dff, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 12px;
}

.tracker-demo-desc {
    color: #f4f8ff;
    font-size: 18px;
    font-weight: 700;
    line-height: 1.6;
}
</style>

<div class="tracker-demo-card">
    <div class="tracker-demo-title">Demo Video</div>
    <div class="tracker-demo-desc">
        Microsoft Teams acceptance tracker creation, task assignment,
        checklist management, attachment handling, and secure collaboration workflow.
    </div>
</div>
""", height=210)

    show_video(
        "assets/teams_video.mp4",
        "teamsVideo",
        "Add your video here: assets/teams_video.mp4"
    )


#####################################################################################################



def show_cards_page():

    components.html("""
<style>

.cards-title {
    font-size: 58px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 10px;
    font-family: Inter, Arial, sans-serif;
    background: linear-gradient(90deg, #65f7ff, #1688ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cards-sub {
    text-align: center;
    color: #d7e7ff;
    font-size: 22px;
    margin-bottom: 40px;
    font-family: Inter, Arial, sans-serif;
}

.section-title {
    font-size: 36px;
    font-weight: 900;
    margin-top: 45px;
    margin-bottom: 20px;
    font-family: Inter, Arial, sans-serif;
}

.optimization-title {
    color: #00e5ff;
    text-shadow: 0 0 18px rgba(0,229,255,0.45);
}

.planning-title {
    color: #a878ff;
    text-shadow: 0 0 18px rgba(124,77,255,0.45);
}

.xhaul-title {
    color: #ffd166;
    text-shadow: 0 0 18px rgba(255,190,60,0.45);
}

.tools-card-wrap-6 {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 18px;
    font-family: Inter, Arial, sans-serif;
}

.tools-card-wrap-4 {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    font-family: Inter, Arial, sans-serif;
}

.tool-card {
    background: rgba(8,20,38,0.94);
    border-radius: 20px;
    padding: 20px;
    min-height: 455px;
    color: white;
    transition: all 0.35s ease;
}

.tool-card:hover {
    transform: translateY(-10px) scale(1.02);
}

.optimization-card {
    border: 1px solid rgba(0,229,255,0.34);
    box-shadow: 0 0 25px rgba(0,229,255,0.10);
}

.optimization-card:hover {
    border-color: rgba(0,229,255,0.95);
    box-shadow:
        0 0 30px rgba(0,229,255,0.36),
        0 0 70px rgba(0,229,255,0.18);
}

.planning-card {
    border: 1px solid rgba(124,77,255,0.38);
    box-shadow: 0 0 25px rgba(124,77,255,0.12);
}

.planning-card:hover {
    border-color: rgba(170,120,255,0.95);
    box-shadow:
        0 0 30px rgba(124,77,255,0.36),
        0 0 70px rgba(124,77,255,0.20);
}

.xhaul-card {
    border: 1px solid rgba(255,190,60,0.38);
    box-shadow: 0 0 25px rgba(255,190,60,0.12);
}

.xhaul-card:hover {
    border-color: rgba(255,209,102,0.95);
    box-shadow:
        0 0 30px rgba(255,190,60,0.36),
        0 0 70px rgba(255,190,60,0.20);
}

.management-card {
    border: 1px solid rgba(0,255,140,0.36);
    box-shadow: 0 0 25px rgba(0,255,140,0.12);
}

.management-card:hover {
    border-color: rgba(0,255,140,0.95);
    box-shadow:
        0 0 30px rgba(0,255,140,0.34),
        0 0 70px rgba(0,255,140,0.18);
}

.team-pill {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(0,229,255,0.14);
    color: #00e5ff;
    font-size: 12px;
    font-weight: 900;
    margin-bottom: 14px;
}

.planning-pill {
    background: rgba(124,77,255,0.18);
    color: #b79cff;
}

.xhaul-pill {
    background: rgba(255,190,60,0.18);
    color: #ffd166;
}

.management-pill {
    background: rgba(0,255,140,0.16);
    color: #48ff9b;
}

.status-pill {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(0,255,140,0.16);
    color: #48ff9b;
    font-size: 12px;
    font-weight: 900;
    margin-top: 14px;
}

.status-progress {
    background: rgba(255,190,60,0.18);
    color: #ffd166;
}

.tool-title {
    font-size: 24px;
    font-weight: 900;
    color: white;
    line-height: 1.2;
    margin-bottom: 14px;
}

.info-label {
    color: #00e5ff;
    font-size: 14px;
    font-weight: 900;
    margin-top: 14px;
    margin-bottom: 6px;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.info-value {
    color: #f1f7ff;
    font-size: 15px;
    line-height: 1.7;
    font-weight: 700;
}

</style>

<div class="cards-title">Automation Tools Portfolio</div>
<div class="cards-sub">Telecom automation, analytics, planning and optimization solutions</div>

<div class="section-title optimization-title">Optimization Tools</div>

<div class="tools-card-wrap-6">

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">SSV Builder</div>
        <div class="info-label">Project</div>
        <div class="info-value">SSV automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Reduced manual SSV preparation effort and improved consistency.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Generated 40 SSVs in ~10 minutes compared to ~3.5 hours manually.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">SSV Plot Processing</div>
        <div class="info-label">Project</div>
        <div class="info-value">SSV plot from LOGOS</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated RSRP, SINR, PCI, HO and SWAP performance plots.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced total processing time from day-level effort to ~10 minutes.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">TMR Report Builder</div>
        <div class="info-label">Project</div>
        <div class="info-value">WBB report saving time</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated report creation and formatting with minimal manual work.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced reporting effort by ~80%.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">SPARK</div>
        <div class="info-label">Project</div>
        <div class="info-value">XML preparation and LTE/5G audit automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated LTE/5G parsing, auditing and optimization workflows.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced audit time from hours to minutes with &gt;95% saving.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">4G / 5G Dashboard</div>
        <div class="info-label">Project</div>
        <div class="info-value">Daily KPI monitoring dashboard</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Power BI</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Improved LTE performance monitoring and reporting efficiency.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Advanced KPI visualization and expanded monitoring insights.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card optimization-card">
        <div class="team-pill">Optimization</div>
        <div class="tool-title">Worst Cells Dashboard</div>
        <div class="info-label">Project</div>
        <div class="info-value">Top worst cells and zero traffic</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Power BI</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Rapid identification of degraded and zero-traffic cells.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced worst-cell investigation time from hours to minutes.</div>
        <div class="status-pill">Completed</div>
    </div>

</div>

<div class="section-title planning-title">Radio Planning Tools</div>

<div class="tools-card-wrap-4">

    <div class="tool-card planning-card">
        <div class="team-pill planning-pill">Radio Planning</div>
        <div class="tool-title">Radio LLD</div>
        <div class="info-label">Project</div>
        <div class="info-value">Low-level design automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Accelerated radio LLD generation with improved accuracy.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced 200-site preparation from hours to less than 1 minute.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card planning-card">
        <div class="team-pill planning-pill">Radio Planning</div>
        <div class="tool-title">Site Database</div>
        <div class="info-label">Project</div>
        <div class="info-value">Database update automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Access Database</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated site database synchronization and updates.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced manual effort by ~90%.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card planning-card">
        <div class="team-pill planning-pill">Radio Planning</div>
        <div class="tool-title">Ookla Weekly</div>
        <div class="info-label">Project</div>
        <div class="info-value">Ookla KPI analytics</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Power BI</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated Ookla data processing and visualization.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced weekly report preparation from hours to minutes.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card planning-card">
        <div class="team-pill planning-pill">Radio Planning</div>
        <div class="tool-title">KML Plotter</div>
        <div class="info-label">Project</div>
        <div class="info-value">Google Earth LTE/5G visualization</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Professional LTE/5G visualization and network analysis.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced KML generation effort from hours to minutes.</div>
        <div class="status-pill">Completed</div>
    </div>

</div>

<div class="section-title xhaul-title">X-Haul & Management Tools</div>

<div class="tools-card-wrap-4">

    <div class="tool-card xhaul-card">
        <div class="team-pill xhaul-pill">X-haul Planning</div>
        <div class="tool-title">LINK Perf Chart</div>
        <div class="info-label">Project</div>
        <div class="info-value">X-haul chart automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated X-haul chart generation and analysis.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced chart preparation effort by ~85%.</div>
        <div class="status-pill status-progress">In Progress</div>
    </div>

    <div class="tool-card xhaul-card">
        <div class="team-pill xhaul-pill">X-haul Planning</div>
        <div class="tool-title">GLI TX Reports</div>
        <div class="info-label">Project</div>
        <div class="info-value">Transmission reporting automation</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Python</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Automated GLI TX reporting with standardized outputs.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Reduced reporting effort from hours to minutes.</div>
        <div class="status-pill">Completed</div>
    </div>

    <div class="tool-card management-card">
        <div class="team-pill management-pill">Management</div>
        <div class="tool-title">Acceptance Tracker</div>
        <div class="info-label">Project</div>
        <div class="info-value">Acceptance management platform</div>
        <div class="info-label">Technology</div>
        <div class="info-value">Microsoft Teams</div>
        <div class="info-label">Business Impact</div>
        <div class="info-value">Centralized acceptance tracking and coordination.</div>
        <div class="info-label">Operational Gain</div>
        <div class="info-value">Enhanced tracking efficiency and reduced communication delays.</div>
        <div class="status-pill status-progress">In Progress</div>
    </div>

</div>

""", height=2700)







#################################################################

if page == "Home":


    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "assets", "home_bg.png")

    bg_base64 = get_base64(image_path)
    components.html(f"""

<style>
.home-wrap {{
    min-height: 800px;
    padding: 60px;
    border-radius: 30px;
    position: relative;
    overflow: hidden;
    color: white;
    
    background: 
        linear-gradient(
            110deg, 
            rgba(2, 8, 23, 1) 0%, 
            rgba(2, 8, 23, 0.9) 10%, 
            rgba(2, 8, 23, 0) 50%
        ),
        url("data:image/png;base64,{bg_base64}");
    
    /* FIX FOR ZOOM: Change 'cover' to a percentage or use 'contain' */
    background-size: 60%; 
    background-position: right center; 
    background-repeat: no-repeat;
    background-color: #020817; 

    /* SHARPENING TOOLS: This reduces browser-side scaling blur */
    image-rendering: -webkit-optimize-contrast;
    image-rendering: crisp-edges;    


    border: 1px solid rgba(255, 255, 255, 0.1);
}}               



.badge {{
    display: inline-block;
    padding: 9px 18px;
    border-radius: 999px;
    background: rgba(0, 120, 255, 0.25);
    border: 1px solid rgba(0, 229, 255, 0.4);
    font-weight: 800;
    text-transform: uppercase;
    font-size: 14px;
    letter-spacing: 1px;
}}



.big {{
    margin-top: 30px;
    font-size: 110px;
    font-weight: 900;
    line-height: 0.9;
    background: linear-gradient(90deg, #65f7ff, #1688ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 15px 30px rgba(0, 0, 0, 0.7));
}}


.sub {{
    margin-top: 15px;
    font-size: 44px;
    font-weight: 900;
    letter-spacing: 1px;
}}

.desc {{
    margin-top: 25px;
    max-width: 650px;
    color: #d7e7ff;
    font-size: 22px;
    line-height: 1.6;
}}

.btns {{
    margin-top: 40px;
    display: flex;
    gap: 20px;
}}

.btn {{
    padding: 16px 32px;
    border-radius: 16px;
    font-weight: 800;
    text-decoration: none;
    color: white;
    transition: all 0.3s ease;
    cursor: pointer;
}}

.primary {{
    background: linear-gradient(90deg, #007bff, #00e5ff);
    box-shadow: 0 10px 30px rgba(0, 229, 255, 0.3);
}}

.primary:hover {{
    transform: scale(1.05);
    box-shadow: 0 15px 40px rgba(0, 229, 255, 0.5);
}}

.secondary {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(5px);
}}

.secondary:hover {{
    background: rgba(255, 255, 255, 0.1);
}}

.kpis {{
    margin-top: 70px;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    max-width: 950px;
}}

.kpi {{
    background: rgba(8, 20, 38, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 229, 255, 0.2);
    border-radius: 20px;
    padding: 24px;
}}

.kpi h3 {{
    color: #00e5ff;
    font-size: 36px;
    margin: 0;
    font-weight: 900;
}}

.kpi p {{
    margin: 5px 0 0 0;
    color: #a0c4ff;
    font-weight: 600;
}}

.modules {{
    margin-top: 40px;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 18px;
}}

.module {{
    background: rgba(8, 20, 38, 0.8);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 229, 255, 0.15);
    border-radius: 22px;
    padding: 28px 15px;
    text-align: center;
    color: white;
    transition: all 0.3s ease;
}}

.module:hover {{
    transform: translateY(-8px);
    border-color: #00e5ff;
    background: rgba(10, 30, 60, 0.9);
    box-shadow: 0 15px 35px rgba(0, 229, 255, 0.2);
}}

.icon {{
    font-size: 48px;
    margin-bottom: 15px;
    display: block;
    filter: drop-shadow(0 0 10px rgba(0, 229, 255, 0.4));
}}

.module h3 {{
    font-size: 18px;
    margin: 10px 0;
}}

.module p {{
    font-size: 14px;
    color: #b0c4de;
    line-height: 1.4;
}}










.table-title {{
    margin-top: 80px;
    font-size: 36px;
    font-weight: 900;
    color: white;
}}

.table-wrap {{
    margin-top: 25px;
    overflow-x: auto;
}}




.spark-table td:nth-child(6),
.spark-table td:nth-child(7) {{
    min-width: 520px;
}}

.spark-table td:nth-child(5),
.spark-table th:nth-child(5) {{
    min-width: 130px;
    white-space: nowrap;
}}

.spark-table td:nth-child(4),
.spark-table th:nth-child(4) {{
    min-width: 130px;
    white-space: nowrap;
}}


.spark-table td:nth-child(3),
.spark-table th:nth-child(3) {{
    min-width: 320px;
    white-space: nowrap;
}}

.spark-table td:nth-child(1),
.spark-table th:nth-child(1) {{
    min-width: 170px;
    white-space: nowrap;
}}



.spark-table td:nth-child(2),
.spark-table th:nth-child(2) {{
    min-width: 320px;
    white-space: nowrap;
}}



.spark-table tbody tr:nth-child(odd) {{
    background: rgba(255,255,255,0.02);
}}

.spark-table tbody tr:nth-child(even) {{
    background: rgba(0,229,255,0.07);
}}

.spark-table tbody tr:hover {{
    background: rgba(0,229,255,0.10) !important;
    transition: 0.2s ease;
}}



.spark-table {{
    width: 100%;
    border-collapse: collapse;
    background: rgba(8,20,38,.82);
    border: 1px solid rgba(0,229,255,.22);
    border-radius: 24px;
    overflow: hidden;

    table-layout: auto;
}}

.spark-table th {{
    background: rgba(0,229,255,.12);
    color: #00e5ff;
    text-align: left;

    padding: 22px;
    font-size: 18px;
    font-weight: 800;

    white-space: nowrap;
}}

.spark-table td {{
    padding: 14px;
    border-bottom: 1px solid rgba(255,255,255,.06);

    color: #d7e7ff;
    vertical-align: middle;

    font-size: 16px;
    line-height: 1.3;

    word-break: break-word;
}}

.spark-table tr:hover {{
    background: rgba(0,229,255,.05);
}}

.table-wrap {{
    margin-top: 25px;
    overflow-x: auto;
    border-radius: 24px;
}}






.team-badge {{
    padding: 10px 16px;
    border-radius: 999px;

    font-size: 13px;
    font-weight: 800;

    display: inline-block;
    white-space: nowrap;   

}}

.opt {{
    background: rgba(0,229,255,.15);
    color: #00e5ff;
}}

.radio {{
    background: rgba(124,77,255,.18);
    color: #b388ff;
}}

.mgmt {{
    background: rgba(255,193,7,.16);
    color: #ffd54f;
}}

.tech {{
    padding: 8px 14px;
    border-radius: 12px;

    font-size: 13px;
    font-weight: 700;

    display: inline-block;
    white-space: nowrap;


}}

.python {{
    background: rgba(55,118,171,.20);
    color: #6cb6ff;
}}

.teams {{
    background: rgba(98,100,167,.20);
    color: #aab2ff;
    display: inline-block;
    min-width: 95px;
    text-align: center;
    white-space: nowrap;


}}

.status {{
    padding: 8px 14px;
    border-radius: 999px;

    font-size: 13px;
    font-weight: 800;

    display: inline-block;
    min-width: 95px;
    text-align: center;
    white-space: nowrap;

}}




.done {{
    background: rgba(54,255,145,.14);
    color: #36ff91;
}}

.progress {{
    background: rgba(255,170,0,.14);
    color: #ffcc66;
}}



.powerbi {{
    background: rgba(255, 193, 7, .18);
    color: #ffd54f;
}}

.access {{
    background: rgba(76, 175, 80, .18);
    color: #81c784;
}}

.xhaul {{
    background: rgba(255, 152, 0, .16);
    color: #ffcc80;
}}















</style>                    
                    






<div class="home-wrap">
    <div class="badge">● AI-POWERED &nbsp;&nbsp; LTE / 5G AUTOMATION</div>

    <div class="big">SPARK ⚡</div>
    <div class="sub">AUTOMATION PLATFORM</div>

    <div class="desc">
        Smart Parsing, Deep Analysis & Automated RAN Optimization
        for LTE & 5G Networks.
    </div>

    <div class="btns">
        <a class="btn primary">Explore Modules →</a>
        <a class="btn secondary">▶ Watch Demo</a>
    </div>

    <div class="kpis">
        <div class="kpi"><h3>95%</h3><p>Faster Audits</p></div>
        <div class="kpi"><h3>4000+</h3><p>Sites Analyzed</p></div>
        <div class="kpi"><h3>15M+</h3><p>Records Processed</p></div>
        <div class="kpi"><h3>24/7</h3><p>Automation</p></div>
    </div>

    <h2 style="margin-top:45px;">Powerful SPARK Modules</h2>

    <div class="modules">
        <div class="module"><div class="icon">📄</div><h3>XML Parser</h3><p>Parse large XML/RAML files.</p></div>
        <div class="module"><div class="icon">⚙️</div><h3>Parameter Audit</h3><p>LTE/5G validation.</p></div>
        <div class="module"><div class="icon">🌍</div><h3>KML Generator</h3><p>Google Earth layers.</p></div>
        <div class="module"><div class="icon">📡</div><h3>Neighbor Analysis</h3><p>Relation analysis.</p></div>
        <div class="module"><div class="icon">🛡️</div><h3>PCI Audit</h3><p>Conflict detection.</p></div>
        <div class="module"><div class="icon">📊</div><h3>Performance Suite</h3><p>KPI reporting.</p></div>
    </div>
</div>







<h2 class="table-title">Automation Portfolio Matrix</h2>

<div class="table-wrap">

<table class="spark-table">

<thead>
<tr>
    <th>Team</th>
    <th>Project</th>
    <th>Tool Name</th>
    <th>Technology</th>
    <th>Status</th>
    <th>Business Impact</th>
    <th>Operational Gain</th>
</tr>
</thead>

<tbody>




<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>SSV automation</td>
<td>SSV_Builder</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Reduced manual SSV preparation effort and improved consistency</td>
<td>Generated 40 SSVs in ~10 minutes compared to ~3.5 hours manually (&gt;90% time saving)</td>
</tr>

<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>SSV plot from LOGOS</td>
<td>SSV_Plot_Processing_Tool_zain</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated generation of RSRP, SINR, PCI, HO, and SWAP performance plots for remote network analysis without field visits</td>
<td>Generated SSVs remotely without site visits, reducing total processing time from day to ~10 minutes per site</td>
</tr>

<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>WBB report Saving time</td>
<td>TMR_Report_Builder</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated report creation and formatting with minimal manual work</td>
<td>Reduced reporting effort by ~80%</td>
</tr>

<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>Automate New site preparation XML &amp; Audit</td>
<td>SPARK</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated LTE/5G parsing, auditing, and optimization workflows with improved audit accuracy</td>
<td>Reduced analysis and audit time from hours to minutes (&gt;95% time saving), especially for large-scale bulk site processing</td>
</tr>



<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>4G / 5G Dashboard for daily use</td>
<td>5G PowerBi_Dashbaord_for sites</td>
<td><span class="tech powerbi">Power BI</span></td>
<td><span class="status done">Completed</span></td>
<td>Improved LTE performance monitoring and reporting efficiency</td>
<td>Improved LTE performance analysis with advanced KPI dashboards, detailed visualizations, and expanded monitoring capabilities for better operational insights</td>
</tr>

<tr>
<td><span class="team-badge opt">Optimization</span></td>
<td>5G DashBoard Top Worst Cells and Zero Traffic</td>
<td>5G Dashboard Top Worst Cells &amp; KPI</td>
<td><span class="tech powerbi">Power BI</span></td>
<td><span class="status done">Completed</span></td>
<td>Rapid identification of degraded and zero-traffic cells</td>
<td>Reduced worst-cell identification time from hours to minutes</td>
</tr>

<tr>
<td><span class="team-badge xhaul">X-haul planning</span></td>
<td>LINK Perf Chart creation</td>
<td>LINK Perf Chart creation</td>
<td><span class="tech python">Python</span></td>
<td><span class="status progress">In Progress</span></td>
<td>Automated X-haul performance chart generation and analysis</td>
<td>Reduced chart preparation effort by ~85%</td>
</tr>

<tr>
<td><span class="team-badge xhaul">X-haul planning</span></td>
<td>GLI sheet</td>
<td>GLI_TX_Report_Builder</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated GLI TX reporting with standardized outputs</td>
<td>Reduced reporting time from several hours to minutes</td>
</tr>

<tr>
<td><span class="team-badge radio">Radio Planning</span></td>
<td>Radio LLD automation</td>
<td>Radio_LLD_Automation_Report</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Accelerated Low-Level Design generation with improved accuracy</td>
<td>Reduced time from approximately 3 hours for 200 sites to less than 1 minute through full automation</td>
</tr>

<tr>
<td><span class="team-badge radio">Radio Planning</span></td>
<td>Site Database update automation</td>
<td>Zian_Database.accdb</td>
<td><span class="tech access">Access Database</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated site database synchronization and updates</td>
<td>Reducing manual effort by ~90% with support for scheduled daily updates</td>
</tr>

<tr>
<td><span class="team-badge radio">Radio Planning</span></td>
<td>Ookla Weekly report</td>
<td>ookla_Zain</td>
<td><span class="tech powerbi">Power BI</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated Ookla data processing and visualization</td>
<td>Reduced weekly report preparation from hours to minutes</td>
</tr>

<tr>
<td><span class="team-badge radio">Radio Planning</span></td>
<td>Ookla_API</td>
<td>Ookla_API</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Automated Ookla API data extraction directly from the server without manual website access or file downloads</td>
<td>Automatically retrieves latest Ookla data within seconds without manual intervention</td>
</tr>

<tr>
<td><span class="team-badge radio">Radio Planning</span></td>
<td>KML</td>
<td>Zain Network KML Plotter</td>
<td><span class="tech python">Python</span></td>
<td><span class="status done">Completed</span></td>
<td>Professional LTE/5G Google Earth visualization and network analysis</td>
<td>Reduced KML generation effort from hours to minutes (&gt;90% saving)</td>
</tr>

<tr>
<td><span class="team-badge mgmt">Management Tools</span></td>
<td>Acceptance tracker</td>
<td>Nokia_Zain_Tracker</td>
<td><span class="tech teams">Microsoft Teams</span></td>
<td><span class="status progress">In Progress</span></td>
<td>Centralized acceptance tracking and task management platform integrated with Microsoft Teams for better coordination and visibility with Customer</td>
<td>Enhanced tracking efficiency and reduced communication delays through real-time collaborative updates</td>
</tr>









</tbody>
</table>
</div>





""", height=2500)






elif page == "SPARK":
    show_spark_page()

elif page == "KML Plotter":
    show_kml_page()

elif page == "Ookla Weekly & API Script":
    show_ookla_page()

elif page == "Worst Cells Dashboard":
    show_worst_cells_page()

elif page == "4G / 5G Dashboard":
    show_4g5g_dashboard_page()

elif page == "Site Database":
    show_site_database_page()

elif page == "Radio LLD Automation":
    show_radio_lld_page()

elif page == "GLI_TX_Report":
    show_gli_tx_page()


elif page == "TMR Report Builder":
    show_tmr_report_page()

elif page == "SSV Builder":
    show_ssv_builder_page()

elif page == "SSV Plot Processing":
    show_ssv_plot_processing_page()


elif page == "Acceptance Tracker":
    show_acceptance_tracker_page()


elif page == "Automation Portfolio":
    show_cards_page()

else:
    st.info("This page is under construction.")
