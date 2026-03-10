import streamlit as st

# Page Configuration
st.set_page_config(page_title="Abhijay Nair - Cybersecurity Portfolio", page_icon="🛡️", layout="wide")

# Sidebar Navigation
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "💼 Work Experience",
    "📂 Projects",
    "🎓 Education",
    "🏆 Certifications"
])

# ------------------ HOME PAGE ------------------
if page == "🏠 Home":
    st.title(" Abhijay Nair")
    st.markdown("### 🛡️ Cybersecurity Operations Analyst | GRC & Incident Response | Security Engineer")
    st.write("""
Cybersecurity professional with hands-on experience monitoring alerts, investigating threats, and implementing incident response in Microsoft cloud environments. Skilled in SIEM monitoring, Defender EDR, vulnerability management, and GRC automation. Adept at translating security data into operational metrics and improving organizational cyber resilience.
""")
    
    st.markdown("---")
    st.subheader("🛠️ Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**💻 Cloud & Identity:** Microsoft Azure, Entra ID, Microsoft 365")
        st.markdown("**🕵️‍♂️ Incident & Monitoring:** Microsoft Defender, SIEM, MITRE ATT&CK Mapping")
        st.markdown("**⚙️ Automation & Tools:** Python, Nmap, OWASP ZAP")
        st.markdown("**🔗 Integration & APIs:** REST API fundamentals, request/response analysis, integration troubleshooting")
    with col2:
        st.markdown("**🛡️ DevOps Exposure:** Azure DevOps, CI/CD pipelines")
        st.markdown("**📄 Documentation:** SOPs, Runbooks, Knowledge Base Articles")
        st.markdown("**📊 Compliance & Governance:** NIST CSF, ISO 27001, PIPEDA")
        st.markdown("**🗣️ Soft Skills:** Problem-solving, Communication, Team Collaboration")
    
    st.markdown("---")
    st.subheader("📞 Contact")
    st.write("📍 **Location:** Calgary, AB")
    st.write("📧 **Email:** abhijay2174@gmail.com")
    st.markdown(
        "[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/abhijay-nair/) "
        "[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github)](https://github.com/Abhijay170901)"
    )

# ------------------ WORK EXPERIENCE ------------------
elif page == "💼 Work Experience":
    st.title("💼 Work Experience")

    st.subheader("🧑‍💻 Cyber Security Operations Analyst – Lead | Project Humancity")
    st.write("📅 May 2025 – Present")
    with st.expander("View Details"):
        st.write("""
- Lead operational cybersecurity monitoring & incident investigation across nonprofit cloud infrastructure.
- Monitored alerts in Microsoft Defender & SIEM; reduced false positives by 30% & improved triage efficiency by 25%.
- Maintained endpoint protection & identity controls (MFA, RBAC) in Azure & Entra ID.
- Conducted vulnerability assessments; reduced high-risk vulnerabilities by 40% in 2 months.
- Designed phishing simulations & security awareness campaigns; click rates reduced from 70% → 20%.
- Developed SOPs, incident escalation frameworks & security KPI reporting.
""")

    st.subheader("💻 Cyber Security Analyst Intern – Team Lead | Project Humancity")
    st.write("📅 Jan 2025 – Apr 2025")
    with st.expander("View Details"):
        st.write("""
- Supported cloud security operations; monitored SIEM & Microsoft Defender alerts.
- Assisted alert triage & escalation; implemented RBAC and MFA policies.
- Performed vulnerability scans with Nmap & OWASP ZAP.
- Developed phishing awareness content & NIST-aligned security policies.
""")

    st.subheader("👨‍💼 IT Recruiter | Novitiate, Mumbai")
    st.write("📅 Jan 2023 – May 2023")
    with st.expander("View Details"):
        st.write("""
- Managed high-volume applicant interactions & ATS.
- Streamlined recruitment operations; ensured compliance & documentation accuracy.
""")

    st.subheader("👨‍💼 IT Recruiter | Conviction HR, Mumbai")
    st.write("📅 Jan 2022 – Dec 2022")
    with st.expander("View Details"):
        st.write("""
- Sourced niche IT candidates; evaluated technical proficiency & cultural fit.
- Maintained ATS records; improved time-to-hire & candidate experience.
""")

# ------------------ PROJECTS ------------------
elif page == "📂 Projects":
    st.title("📂 Projects")

st.markdown("### 🛡️ Cybersecurity Project Portfolio")
st.write("Hands-on security projects demonstrating **GRC auditing, security operations, threat detection, and vulnerability assessment.**")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Projects", "4")
col2.metric("Security Domains", "3")
col3.metric("Frameworks Used", "NIST / PCI / GDPR")
col4.metric("Focus", "SOC + GRC")
    # Project 1
    st.subheader("🛡️ ISO 27001:2022 GRC Automation Framework")
    st.write("📅 Date: 2025")
    st.success("Risk Level: Governance & Compliance")
    with st.expander("View Details"):
        st.write("""
- Simulates GRC workflows aligned with ISO 27001:2022.
- Automated risk register updates (Python) and Annex A control tracking (YAML).
- Streamlit dashboard for compliance metrics & auto-generated SoA.
- GitHub Actions for continuous compliance validation.
**Tech:** Python, YAML, Streamlit, Power BI, GitHub Actions
""")
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/ISO27001-GRC-Automation)", unsafe_allow_html=True)

    # Project 2
    st.subheader("🌐 Web Application Vulnerability Assessment – DVWA")
    st.write("📅 Date: 2025")
    st.error("Risk Level: Critical")
    with st.expander("View Details"):
        st.write("""
- Conducted automated vulnerability scans on DVWA using OWASP ZAP.
- Assessed security headers, cookies, session management, and server info.
- Provided professional recommendations for medium & low-risk findings.
**Tech:** OWASP ZAP, Python, Reporting
""")
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/webapp-vuln-assessment)", unsafe_allow_html=True)

    # Project 3
    st.subheader("🚨 Incident Response Automation")
    st.write("📅 Date: 2025")
    st.warning("Risk Level: High")
    with st.expander("View Details"):
        st.write("""
- Automates detection → response → notification in SOC environment.
- Parses alerts, triages by severity, triggers contextual responses, logs all actions.
- Includes CI/CD workflow using GitHub Actions for repeatable simulation.
**Tech:** Python, PowerShell, GitHub Actions, JSON Reporting
""")
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/incident-response-automation)", unsafe_allow_html=True)

    st.subheader("🔍 Enterprise Cybersecurity Risk Assessment – Botium Toys")
st.write("📅 March 2026")
st.error("Risk Level: Critical")

with st.expander("View Security Audit Details"):
    st.write("""
Conducted a full **cybersecurity risk assessment and control gap analysis** for Botium Toys, a fictional retail organization.

Security assessment evaluated:

• IT infrastructure and employee devices  
• Ecommerce and database systems  
• Data storage and protection mechanisms  
• Network monitoring and threat detection  
• Business continuity and disaster recovery planning  

Key Findings:

• Excessive internal access to sensitive data  
• Lack of encryption for payment information  
• No formal disaster recovery or backup strategy  
• Limited threat detection capabilities  
• Weak password governance  
• Incomplete asset inventory  

Framework Alignment:

• NIST Cybersecurity Framework (CSF)  
• PCI DSS  
• GDPR data protection principles  

Deliverables:

• Executive security audit report  
• Risk prioritization matrix  
• Security control gap analysis  
• Security improvement roadmap  
• Continuous security monitoring metrics
""")

    st.markdown("📂 **View Full Audit Report:**")
    st.markdown("https://github.com/Abhijay170901/Cybersecurity-Risk-Assessment-Botium-Toys")

# ------------------ EDUCATION ------------------
elif page == "🎓 Education":
    st.title("🎓 Education")
    st.write("## Master's in Cybersecurity")
    st.write("📍 Bow Valley College | Sep 2024 – Apr 2025")
    st.write("Focus Areas: Cybersecurity Operations, GRC, Incident Response")

    st.write("---")
    st.write("## Computer Applications Development")
    st.write("📍 Conestoga College | Sep 2023 – Aug 2024")
    
    st.write("---")
    st.write("## Mechanical Engineering")
    st.write("📍 Bhausaheb Vartak Polytechnic | 2019 – 2021")

# ------------------ CERTIFICATIONS ------------------
elif page == "🏆 Certifications":
    st.title("🏆 Certifications")
    st.markdown("""
- **EC-Council Network Defense Essentials V1**
- 
""")