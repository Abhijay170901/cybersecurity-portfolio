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
• Led end-to-end recruitment and onboarding for **six cybersecurity intern teams**, accelerating talent pipeline development by **70%** and ensuring alignment with project skill requirements.

• Authorized hiring decisions and built specialized security teams supporting **SOC monitoring, vulnerability management, and secure development initiatives**.

• Established operational policies, SOPs, and intern governance frameworks, resulting in **zero policy violations across three active applications**.

• Mentored and managed intern performance across engineering and security teams, improving onboarding efficiency and team productivity by **25%**.

• Coordinated vulnerability assessments, incident response collaboration, and internal security audits, improving threat detection and remediation speed by **30%**.

• Partnered with engineering teams to enforce **secure SDLC practices**, mitigating **OWASP Top 10 risks** across development environments.

• Conducted recurring cybersecurity risk assessments and policy reviews aligned with **ISO 27001 and NIST CSF**.

• Organized enterprise-wide **Cybersecurity Awareness Week**, including phishing simulations and tabletop exercises that reduced phishing click-through rates by **65%**.
""")



    st.subheader("🏦 Business & Technology Recruiter (BFSI Domain) | Novitiate")
    st.write("📅 Feb 2023 – Jul 2023 | Mumbai, India")

    with st.expander("View Details"):
        st.write("""
• Managed full-cycle recruitment for **banking, technology, and operations roles**, successfully closing **40+ strategic hires**.

• Implemented internal hiring programs that reduced external recruitment costs by **20%** while maintaining talent quality.

• Leveraged **headhunting, LinkedIn sourcing, and market intelligence** to identify high-value candidates for niche roles.

• Conducted competency-based interviews and reference verification processes, improving **new hire retention by 15%**.

• Coordinated onboarding, payroll documentation, and compliance workflows, achieving **100% audit compliance**.

• Partnered with leadership teams to support workforce planning and staffing for **three major banking transformation projects**.
""")



    st.subheader("👥 IT & Business Recruiter | Conviction HR")
    st.write("📅 Jun 2022 – Jan 2023 | Mumbai, India")

    with st.expander("View Details"):
        st.write("""
• Closed **50+ technical and business positions** across IT and non-IT functions within targeted hiring timelines.

• Built high-quality candidate pipelines through advanced sourcing strategies, reducing **time-to-hire by 25%**.

• Conducted structured interviews and technical screenings achieving **95% hiring manager satisfaction**.

• Supported workforce planning initiatives across multiple departments, enabling scalable organizational growth.

• Streamlined recruitment operations and hiring processes, reducing overall hiring cycle time by **20%**.
""")



    st.subheader("📊 Recruitment Specialist | Bhavishya Consulting Services")
    st.write("📅 Jan 2022 – May 2022 | Mumbai, India")

    with st.expander("View Details"):
        st.write("""
• Executed large-scale recruitment operations filling **150+ roles across IT and operational functions**.

• Led mass hiring campaigns achieving **95% fulfillment of bulk hiring requirements** within project timelines.

• Coordinated candidate assessments, interview panels, and offer negotiations while ensuring HR policy compliance.

• Partnered with hiring managers to define technical and business role requirements, reducing **mis-hire risks by 15%**.

• Managed onboarding coordination and candidate engagement initiatives improving **new hire experience metrics**.
""")

# ------------------ PROJECTS ------------------
elif page == "📂 Projects":
    st.title("📂 Projects")

    st.markdown("### 🛡️ Cybersecurity Project Portfolio")
    st.write("Hands-on security projects demonstrating **GRC auditing, security operations, threat detection, and vulnerability assessment.**")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projects", "5")
    col2.metric("Security Domains", "4")
    col3.metric("Frameworks Used", "NIST / PCI / GDPR")
    col4.metric("Focus", "SOC + GRC + AI-SecOps")

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
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/ISO27001-GRC-Automation)")
        st.markdown("[🚀 Launch App](https://iso27001-grc-automation-vbscmti96vsawyegwlpfwj.streamlit.app/)")

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
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/webapp-vuln-assessment)")

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
        st.markdown("[📂 GitHub Repository](https://github.com/Abhijay170901/incident-response-automation)")

    # Project 4
    st.subheader("🔍 Enterprise Cybersecurity Risk Assessment – Botium Toys")
    st.write("📅 Date: March 2026")
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
        st.markdown("[📂 View Full Audit Report](https://github.com/Abhijay170901/Cybersecurity-Risk-Assessment-Botium-Toys)")

    # Project 5 – NEW
    st.subheader("🛡️ AI-SecOps Prompt Intelligence Platform")
    st.write("📅 Date: 2026")
    st.info("Focus: AI-assisted SOC Operations & Threat Intelligence")

    with st.expander("View Project Details"):
        st.write("""
- Developed an **AI-powered cybersecurity operations platform** to generate structured prompts for SOC analysts.  
- Covers **20+ prompts across Web Security, Threat Hunting, Phishing, Identity & Password Security, and DevSecOps**.  
- Includes **MITRE ATT&CK mapping, threat context, detection methodology, and recommended remediation**.  
- Features a **searchable prompt library, filtering by security domain, and AI prompt generator** for real-time investigations.

**Tech:** Python, Streamlit, JSON, GitHub, AI-assisted Prompt Engineering
""")
        st.markdown("[🚀 Launch AI-SecOps Platform](https://cyber-prompt-app.streamlit.app/)")
# ------------------ EDUCATION ------------------
elif page == "🎓 Education":
    st.title("🎓 Education")
    st.write("## Cybersecurity")
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
