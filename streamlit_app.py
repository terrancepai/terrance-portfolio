import streamlit as st
from PIL import Image

# --- Personal Info ---
st.set_page_config(page_title="Terrance Pai | Portfolio", layout="wide")
st.title("👋 Hi, I'm Terrance Pai")
st.subheader("Aspiring Investment Professional | USC | Space Security Enthusiast")

st.write("I'm passionate about building the future of finance, public policy, and tech. I'm currently a student at USC, exploring opportunities in investment management and private equity.")

# Socials
st.markdown(
    '''
    [💼 LinkedIn](https://www.linkedin.com/in/terrancepai/) 
    | [📧 Email](mailto:terrance.pai554@gmail.com)
    '''
)

# --- Projects ---
st.markdown("## 🔍 Selected Projects")

projects = [
    {
        "title": "End Overdose Training Platform",
        "description": "Built training scripts and led community education sessions focused on harm reduction and naloxone distribution.",
        "tags": ["Public Health", "Non-Profit", "Leadership"]
    },
    {
        "title": "Space Security Research Paper",
        "description": "Capstone research project at USC: 'Navigating the Final Frontier: Reconceptualizing Space Security and Governance Beyond Terrestrial Analogies'.",
        "tags": ["IR", "Security", "Policy", "Space"]
    },
    {
        "title": "ITAD Market Sourcing Project",
        "description": "Led deal sourcing in the IT Asset Disposition industry under private equity mentorship. Conducted TAM analysis, outreach, and valuation modeling.",
        "tags": ["Private Equity", "Deal Sourcing", "Valuation"]
    }
]

for proj in projects:
    with st.container():
        st.markdown(f"### {proj['title']}")
        st.write(proj["description"])
        st.write("Tags: " + ", ".join(proj["tags"]))
        st.markdown("---")

# Footer
st.caption("© 2025 Terrance Pai")