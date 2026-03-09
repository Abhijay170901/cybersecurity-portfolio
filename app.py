import streamlit as st

st.set_page_config(
    page_title="Abhijay Nair | Cybersecurity Portfolio",
    layout="wide",
    page_icon="🛡️"
)

# ==================== SIDEBAR ====================
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "💼 Work Experience", "📂 Projects", "🎓 Education", "🏆 Certifications & Achievements", "👋 Contact"]
)

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.title("👋 Abhijay Nair")
    st.subheader("Cybersecurity Analyst | GRC & SOC Professional")
    st.write("""
     Cybersecurity professional with expertise in **Threat Detection, Risk & Compliance, Incident Response, Security Auditing, and Vulnerability Management**.  
Passionate about building security tools, performing audits, and improving organizational cybersecurity posture.
    """)

    st.divider()
    st.header("🛠️ Skills")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.subheader("Security & GRC")
        st.write("""
- Incident Response  
- Vulnerability Assessment  
- Risk Management  
- Policy Audits
""")
    with col2:
        st.subheader("Tools")
        st.write("""
- Wireshark  
- Nmap  
- Burp Suite  
- Linux  
- SIEM
""")
    with col3:
        st.subheader("Languages")
        st.write("""
- Python  
- SQL  
- Bash  
- PowerShell
""")
    with col4:
        st.subheader("Soft Skills")
        st.write("""
- Stakeholder Collaboration
- Team Leadership 
- Training & Supervising
- Problem Solving  
- Reporting & Documentation
""")