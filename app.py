import streamlit as st
import os

st.set_page_config(
    page_title="SPARK Automation Showcase",
    page_icon="⚡",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

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

            












.main-title {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.1;
}

.gradient-text {
    background: linear-gradient(90deg, #7c4dff, #00e5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 22px;
    color: #d7e7ff;
    margin-top: -10px;
}

.card {
    background: rgba(8, 20, 38, 0.82);
    border: 1px solid rgba(0, 229, 255, 0.16);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 0 25px rgba(0, 229, 255, 0.06);
}

.kpi-number {
    font-size: 42px;
    font-weight: 800;
    color: #00e5ff;
}

.kpi-label {
    color: #b8c7dd;
    font-size: 15px;
}

.section-title {
    font-size: 26px;
    font-weight: 800;
    margin-bottom: 14px;
}

.good {
    color: #36ff91;
    font-weight: 700;
}

.bad {
    color: #ff4d6d;
    font-weight: 700;
}

.flow-box {
    background: linear-gradient(145deg, rgba(21, 42, 74, 0.9), rgba(6, 13, 26, 0.9));
    border: 1px solid rgba(0, 229, 255, 0.18);
    border-radius: 16px;
    padding: 22px;
    text-align: center;
    min-height: 120px;
}

.footer {
    color: #8ea6c5;
    font-size: 13px;
    text-align: center;
    padding-top: 25px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## ⚡ SPARK")
st.sidebar.markdown("Automation Engine")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "SPARK", "KML Plotter", "Performance", "Live Demo", "Impact"]
)






def show_kml_page():
    st.markdown("""
    <div class="main-title">
        KML <span class="gradient-text">Network Plotter</span>
    </div>
    <p class="subtitle">
        Automated LTE/5G/2G Google Earth visualization engine
    </p>
    <p style="color:#b8c7dd; font-size:17px;">
        Converts network site data into clean, optimized KML/KMZ layers with sector visualization,
        technology separation, category-based sizing, and map-ready outputs.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

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
            <div class="card">
                <div class="kpi-number" style="font-size:30px;">{num}</div>
                <div class="kpi-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
        <div class="card">
            <div class="section-title">Problem Solved</div>
            <p>❌ Manual Google Earth plotting</p>
            <p>❌ Large KML/KMZ file sizes</p>
            <p>❌ Difficult technology separation</p>
            <p>❌ Time-consuming sector visualization</p>
            <p>❌ No standard visual output</p>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="card">
            <div class="section-title">Automation Result</div>
            <p>✅ One-click KMZ generation</p>
            <p>✅ LTE/5G/2G layers organized automatically</p>
            <p>✅ Sector azimuth and beam visualization</p>
            <p>✅ Smaller optimized output</p>
            <p>✅ Professional map-ready delivery</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-title">KML Processing Flow</div>
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
            <div class="flow-box">
                <div style="font-size:38px;">{icon}</div>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-title">Demo Video</div>
        <p style="color:#b8c7dd;">End-to-end demonstration of automated network visualization processing.</p>
    </div>
    """, unsafe_allow_html=True)

    video_path = "assets/kml_demo.mp4"
    if os.path.exists(video_path):

        video_file = open(video_path, "rb")
        video_bytes = video_file.read()

        import base64
        video_base64 = base64.b64encode(video_bytes).decode()

        st.markdown(f"""
        <div style="display:flex; justify-content:center;">
            <video width="60%" autoplay muted controls style="border-radius:18px;" id="demoVideo">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        </div>

        <script>
        const video = document.getElementById("demoVideo");

        video.playbackRate = 1.3;

        video.onloadedmetadata = function() {{
            video.play();
        }};
        </script>
        """, unsafe_allow_html=True)

    else:
        st.warning("Add your video here: assets/kml_demo.mp4")




    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="section-title">Visual Gallery</div>
        <p style="color:#b8c7dd;">KML visualization outputs and Google Earth rendering examples.</p>
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
                    st.image(path, caption=caption, use_container_width=True)
                else:
                    st.markdown(f"""
                    <div class="flow-box">
                        <div style="font-size:48px;">🖼️</div>
                        <b>{caption}</b>
                        <p style="color:#8ea6c5;">Add: {path}</p>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown("""
    <div class="card">
        <div class="section-title">Business Impact</div>
        <p>⚡ Faster site visualization for planning and optimization teams</p>
        <p>🌍 Cleaner Google Earth delivery for field and management review</p>
        <p>📉 Reduced file size and easier sharing</p>
        <p>🎯 Better visibility of coverage, sectors, and technology layers</p>
    </div>
    """, unsafe_allow_html=True)
















if page == "Home":
    # Hero
    col1, col2 = st.columns([1.4, 1])

    with col1:
        st.markdown("""
        <div class="main-title">
            From <span class="gradient-text">Days</span> to 
            <span class="gradient-text">Seconds.</span>
        </div>
        <p class="subtitle">
            LTE/5G Optimization Automation Framework
        </p>
        <p style="color:#b8c7dd; font-size:17px;">
            Automating repetitive telecom audits, XML parsing, KPI analysis,
            KML generation, and reporting workflows with Python.
        </p>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([1, 1])
        with c1:
            st.button("▶ Watch Demo")
        with c2:
            st.button("Explore Dashboard")

    with col2:
        st.markdown("""
        <div class="card" style="text-align:center;">
            <div style="font-size:100px;">⚡</div>
            <h2 style="color:#00e5ff;">Automation Engine</h2>
            <p style="color:#b8c7dd;">Python-powered telecom intelligence platform</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI Cards
    k1, k2, k3, k4, k5 = st.columns(5)

    kpis = [
        ("3", "Days Manual Work"),
        ("7", "Seconds Execution"),
        ("120K+", "Relations Parsed"),
        ("99%", "Time Saved"),
        ("High", "Accuracy")
    ]

    for col, (num, label) in zip([k1, k2, k3, k4, k5], kpis):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="kpi-number">{num}</div>
                <div class="kpi-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Before / After + Flow
    left, right = st.columns([1, 1.4])

    with left:
        st.markdown("""
        <div class="card">
            <div class="section-title">Before vs After</div>
            <div style="display:flex; gap:20px;">
                <div style="width:50%;">
                    <p class="bad">BEFORE</p>
                    <p>❌ Multiple Excel files</p>
                    <p>❌ Manual XML parsing</p>
                    <p>❌ Repetitive checks</p>
                    <p>❌ High human error</p>
                    <p>❌ 2–3 days to complete</p>
                </div>
                <div style="width:50%;">
                    <p class="good">AFTER</p>
                    <p>✅ One-click analysis</p>
                    <p>✅ Automatic parsing</p>
                    <p>✅ Smart audit engine</p>
                    <p>✅ Minimal human error</p>
                    <p>✅ Completed in seconds</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="card"><div class="section-title">Core Automation Engine</div>', unsafe_allow_html=True)

        f1, f2, f3, f4, f5 = st.columns(5)
        flow = [
            ("📄", "Input Data<br>XML / SCF"),
            ("⚙️", "Python<br>Engine"),
            ("📊", "KPI & Audit<br>Analysis"),
            ("🗺️", "KML / Map<br>Generation"),
            ("📑", "Report<br>Generation")
        ]

        for col, (icon, text) in zip([f1, f2, f3, f4, f5], flow):
            with col:
                st.markdown(f"""
                <div class="flow-box">
                    <div style="font-size:38px;">{icon}</div>
                    <p>{text}</p>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Demo + Outputs
    demo, outputs = st.columns([1, 1.4])

    with demo:
        st.markdown("""
        <div class="card">
            <div class="section-title">Live Demo</div>
            <p>✅ Parsing LTE Relations...</p>
            <p>✅ Parsing 5G Files...</p>
            <p>✅ Checking Neighbor Relations...</p>
            <p>✅ Detecting PCI Conflicts...</p>
            <p>✅ Generating KML...</p>
            <p>✅ Building Report...</p>
            <br>
            <div style="text-align:center;">
                <div style="
                    width:140px;
                    height:140px;
                    border-radius:50%;
                    border:10px solid #36ff91;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    margin:auto;
                    font-size:32px;
                    font-weight:800;
                    color:#36ff91;">
                    100%
                </div>
                <p style="color:#b8c7dd;">Completed in 00:00:07</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with outputs:
        st.markdown("""
        <div class="card">
            <div class="section-title">Outputs & Visuals</div>
            <p style="color:#b8c7dd;">
                Add your real screenshots here: KML maps, KPI dashboard, PCI reports,
                XML results, Excel reports, and GUI screenshots.
            </p>
        </div>
        """, unsafe_allow_html=True)

        img1, img2, img3, img4 = st.columns(4)
        for col, title in zip([img1, img2, img3, img4], ["KML Map", "KPI Dashboard", "PCI Report", "Auto Report"]):
            with col:
                st.markdown(f"""
                <div class="flow-box">
                    <div style="font-size:42px;">🖥️</div>
                    <b>{title}</b>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Business Impact
    st.markdown("""
    <div class="card">
        <div class="section-title">Business Impact</div>
    </div>
    """, unsafe_allow_html=True)

    b1, b2, b3, b4, b5 = st.columns(5)

    impact = [
        ("90%+", "Reduction in manual effort"),
        ("Faster", "Decision making"),
        ("Improved", "Network performance tracking"),
        ("Scalable", "Across regions and sites"),
        ("Cost Saving", "Reduced operational effort")
    ]

    for col, (title, desc) in zip([b1, b2, b3, b4, b5], impact):
        with col:
            st.markdown(f"""
            <div class="card">
                <h3 style="color:#00e5ff;">{title}</h3>
                <p class="kpi-label">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        ⚡ SPARK Automation Engine — Built by Mohamed Alameh
    </div>
    """, unsafe_allow_html=True)



elif page == "KML Plotter":
    show_kml_page()

else:
    st.info("This page is under construction.")
