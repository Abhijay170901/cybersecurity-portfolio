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
    st.title("Abhijay Nair")
    st.markdown("### 🛡️ Cybersecurity Operations Analyst | Detection Engineering | GRC")
    st.write("""
    Cybersecurity professional with hands-on experience engineering detections, investigating threats, and implementing automated incident response in Microsoft cloud environments. Skilled in SIEM/XDR correlation, advanced KQL hunting, vulnerability management, and GRC automation. Adept at translating raw security telemetry into operational metrics and resilient architecture.
    """)
    
    st.markdown("---")
    st.subheader("🛠️ Core Competencies & Skills")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**🕵️‍♂️ Security Operations & Hunting:** Microsoft Sentinel (SIEM), Defender XDR, KQL (Kusto Query Language), MITRE ATT&CK Mapping")
        st.markdown("**💻 Cloud & Identity Security:** Microsoft Azure, Entra ID (Azure AD), RBAC/MFA, Impossible Travel Detection")
        st.markdown("**⚙️ Detection & Automation (SOAR):** Python, Streamlit, Sentinel Playbooks (Logic Apps), API Integrations")
    with col2:
        st.markdown("**📊 Governance, Risk & Compliance:** NIST CSF 2.0, ISO 27001, PIPEDA, Security Auditing")
        st.markdown("**🔍 Vulnerability Management:** Nmap, OWASP ZAP, Attack Surface Reduction")
        st.markdown("**🛡️ DevSecOps & Operations:** GitHub Actions, CI/CD Pipelines, SOP & Runbook Development")
    
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

    st.subheader("🧑‍💻 Cybersecurity Operations Analyst – Lead | Project Humancity")
    st.write("📅 May 2025 – Present | Remote")
    with st.expander("View Details"):
        st.write("""
        • Lead cybersecurity operations across **five technical teams (30+ members)** supporting infrastructure security, cloud environments, and secure development initiatives.
        • Monitor and investigate security alerts across endpoint and cloud environments using **Microsoft Defender and SIEM log analysis**, identifying indicators of compromise and suspicious behavior.
        • Perform incident triage and threat correlation using the **MITRE ATT&CK framework**, improving alert accuracy and reducing false positives by **30%**.
        • Implement identity security controls in **Microsoft Azure and Entra ID**, enforcing **RBAC and MFA policies** to strengthen access governance.
        • Conduct vulnerability assessments across endpoints and web applications using **Nmap and OWASP ZAP**, reducing high-risk vulnerabilities by **40% within two months**.
        • Design and execute **phishing simulation campaigns and security awareness programs**, reducing user click rates from **70% to 20%**.
        • Develop **incident response procedures, escalation frameworks, and security runbooks** aligned with **NIST Cybersecurity Framework (CSF)** operational practices.
        • Deliver executive security posture reports and risk insights to leadership, supporting strategic improvements in cloud and application security.
        """)

    st.subheader("🛡️ Cybersecurity Analyst Intern – Team Lead | Project Humancity")
    st.write("📅 Jan 2025 – Apr 2025 | Remote")
    with st.expander("View Details"):
        st.write("""
        • Performed **SOC monitoring and security alert triage** across Microsoft cloud environments using SIEM and Defender telemetry.
        • Conducted **vulnerability scans and security assessments** using **Nmap and OWASP ZAP**, documenting findings and remediation guidance for development teams.
        • Assisted with **identity and access security implementation**, including MFA enforcement and least-privilege RBAC configuration.
        • Supported the development of **security awareness initiatives**, phishing simulations, and internal training materials.
        • Contributed to **governance documentation and policy frameworks** aligned with **NIST CSF and ISO 27001 security practices**.
        • Investigated security anomalies, supported incident response coordination, and maintained structured security documentation.
        """)

    st.subheader("🏢 Talent & Operations Lead – Cybersecurity Programs | Project Humancity")
    st.write("📅 Jan 2025 – Present | Toronto, ON (Remote)")
    with st.expander("View Details"):
        st.write("""
        • Led end-to-end recruitment and onboarding for **six cybersecurity intern teams**, accelerating talent pipeline development by **70%**.
        • Established operational policies, SOPs, and intern governance frameworks, resulting in **zero policy violations across three active applications**.
        • Coordinated vulnerability assessments, incident response collaboration, and internal security audits, improving threat detection and remediation speed by **30%**.
        • Partnered with engineering teams to enforce **secure SDLC practices**, mitigating **OWASP Top 10 risks**.
        """)

    st.subheader("🏦 Business & Technology Recruiter (BFSI Domain) | Novitiate")
    st.write("📅 Feb 2023 – Jul 2023 | Mumbai, India")
    with st.expander("View Details"):
        st.write("""
        • Managed full-cycle recruitment for **banking, technology, and operations roles**, successfully closing **40+ strategic hires**.
        • Leveraged **headhunting and market intelligence** to identify high-value candidates for niche roles, reducing external recruitment costs by **20%**.
        • Partnered with leadership teams to support workforce planning and staffing for **three major banking transformation projects**.
        """)

    st.subheader("👥 IT & Business Recruiter | Conviction HR")
    st.write("📅 Jun 2022 – Jan 2023 | Mumbai, India")
    with st.expander("View Details"):
        st.write("""
        • Closed **50+ technical and business positions** across IT and non-IT functions within targeted hiring timelines.
        • Built high-quality candidate pipelines through advanced sourcing strategies, reducing **time-to-hire by 25%**.
        """)

    st.subheader("📊 Recruitment Specialist | Bhavishya Consulting Services")
    st.write("📅 Jan 2022 – May 2022 | Mumbai, India")
    with st.expander("View Details"):
        st.write("""
        • Executed large-scale recruitment operations filling **150+ roles across IT and operational functions**.
        • Partnered with hiring managers to define technical and business role requirements, reducing **mis-hire risks by 15%**.
        """)

# ------------------ PROJECTS ------------------
elif page == "📂 Projects":
    st.title("📂 Projects")

    st.markdown("### 🛡️ Cybersecurity Project Portfolio")
    st.write("Hands-on security projects demonstrating **Detection Engineering, GRC auditing, Threat Hunting, and SOC Automation.**")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projects", "6")
    col2.metric("Security Domains", "5")
    col3.metric("Frameworks Used", "NIST / MITRE / ISO")
    col4.metric("Focus", "SOC + GRC + Automation")

    # Project 1 - NEW
    st.subheader("⚙️ Autonomous Security Engineering & Response Framework")
    st.write("📅 Date: April 2026")
    st.success("Focus: Detection Engineering, SIEM/XDR, SOAR Automation")

    with st.expander("View Details", expanded=True):
        st.write("""
        - Engineered a **NIST CSF 2.0-aligned** Detection and Response framework demonstrating advanced Cross-Domain Correlation.
        - Designed complex **KQL inner joins** to correlate Entra ID authentication failures (Error 50121/50126) with Defender endpoint execution (Event 4688, 4732) to catch credential-based lateral movement.
        - Mapped a 6-stage adversary kill chain (Recon to Log Wiping) directly to **MITRE ATT&CK** tactics.
        - Built and visualized conditional **SOAR Playbooks** for automated host isolation based on asset criticality, reducing MTTR to seconds.
        - Developed a custom Streamlit UI to present the detection engine, diagnostic codes, and automation logic.

        **Tech:** KQL, Microsoft Sentinel, Defender XDR, Python, Streamlit, SOAR
        """)
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/Detection-Engineering-Framework)")
        st.markdown("[🚀 Launch Framework App](https://detection-engineering-framework.streamlit.app/)")

    # Project 2
    st.subheader("🛡️ AI-SecOps Prompt Intelligence Platform")
    st.write("📅 Date: 2026")
    st.info("Focus: AI-assisted SOC Operations & Threat Intelligence")

    with st.expander("View Details"):
        st.write("""
        - Developed an **AI-powered cybersecurity operations platform** to generate structured prompts for SOC analysts.  
        - Covers **20+ prompts across Web Security, Threat Hunting, Phishing, Identity & Password Security, and DevSecOps**.  
        - Includes **MITRE ATT&CK mapping, threat context, detection methodology, and recommended remediation**.  
        - Features a **searchable prompt library, filtering by security domain, and AI prompt generator** for real-time investigations.

        **Tech:** Python, Streamlit, JSON, GitHub, AI-assisted Prompt Engineering
        """)
        st.markdown("[🚀 Launch AI-SecOps Platform](https://cyber-prompt-app.streamlit.app/)")

    # Project 3
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
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/ISO27001-GRC-Automation)")
        st.markdown("[🚀 Launch App](https://iso27001-grc-automation-vbscmti96vsawyegwlpfwj.streamlit.app/)")

    # Project 4
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
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/incident-response-automation)")

    # Project 5
    st.subheader("🔍 Enterprise Cybersecurity Risk Assessment – Botium Toys")
    st.write("📅 Date: March 2026")
    st.error("Risk Level: Critical")

    with st.expander("View Security Audit Details"):
        st.write("""
        Conducted a full **cybersecurity risk assessment and control gap analysis** for Botium Toys 
        """)
st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/Cybersecurity-Risk-Assessment-Botium-Toys/blob/main/Cybersecurity-Audit-Report.pdf)")
