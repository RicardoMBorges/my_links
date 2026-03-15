import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Ricardo M Borges Link Hub",
    page_icon="🔗",
    layout="centered",
)

# =========================================================
# PROFILE
# =========================================================
PROFILE = {
    "name": "Ricardo M. Borges",
    "headline_pt": "Professor • Researcher • Natural Products • Metabolomics",
    "headline_en": "Professor • Researcher • Natural Products • Metabolomics",
    "headline_es": "Profesor • Investigador • Productos Naturales • Metabolómica",
    "about_pt": (
        "Professor e pesquisador na UFRJ trabalhando com produtos naturais, "
        "metabolômica, espectrometria de massas e desenvolvimento de ferramentas científicas."
    ),
    "about_en": (
        "Professor and researcher at UFRJ working on natural products, "
        "metabolomics, mass spectrometry, and development of scientific tools."
    ),
    "about_es": (
        "Profesor e investigador en la UFRJ trabajando en productos naturales, "
        "metabolómica, espectrometría de masas y desarrollo de herramientas científicas."
    ),
    "profile_image": "profile.jpg",
}

# =========================================================
# LINKS
# =========================================================
LINKS = {
    "Português": {
        "profile_key": "pt",
        "sections": [
            {
                "title": "Redes e contato",
                "buttons": [
                    {"label": "Instagram", "icon": "📸", "url": "https://instagram.com/borgesmricardo"},
                    {"label": "LinkedIn", "icon": "💼", "url": "https://www.linkedin.com/in/ricardo-borges-b7a16a36/"},
                    {"label": "YouTube", "icon": "▶️", "url": "https://www.youtube.com/@ricardomborges5295"},
                    {"label": "GitHub", "icon": "💻", "url": "https://github.com/RicardoMBorges"},
                    {"label": "Website", "icon": "🌐", "url": "https://laabioippn.wordpress.com/"},
                    {"label": "IPPN-Website", "icon": "🌐", "url": "https://www.ippn.ufrj.br/ricardo-moreira-borges/"},
                    {"label": "WhatsApp", "icon": "💬", "url": "https://wa.me/5521972125754"},
                ],
            },
            {
                "title": "Redes acadêmicas",
                "buttons": [
                    {"label": "ORCID", "icon": "🧬", "url": "https://orcid.org/0000-0002-7662-6734"},
                    {"label": "ResearchGate", "icon": "📚", "url": "https://www.researchgate.net/profile/Ricardo-Borges-7"},
                ],
            },
            {
                "title": "Plataforma Digital LAABio-IPPN",
                "buttons": [
                    {"label": "TLC2Chrom", "icon": "🧪", "url": "https://tlc2chrom.streamlit.app/"},
                    {"label": "DAFdiscovery", "icon": "📊", "url": "https://dafdiscovery.streamlit.app/"},
                    {"label": "Batch Organizer", "icon": "🗂️", "url": "https://batchorganizer.streamlit.app/"},
                    {"label": "DBsimilarity", "icon": "🧬", "url": "https://dbsimilarity.streamlit.app/"},
                    {"label": "DBsimilarity-unique", "icon": "🧬", "url": "https://dbsimilarity-unique.streamlit.app/"},
                    {"label": "DOE Pipeline", "icon": "📈", "url": "https://doe-pipeline.streamlit.app/"},
                    {"label": "MGF2Frag", "icon": "⚛️", "url": "https://mgf2frag.streamlit.app/"},
                    {"label": "pyMetaFlow HPLC", "icon": "🧪", "url": "https://pymetaflow-hplc.streamlit.app/"},
                    {"label": "Filter GNPS MGF", "icon": "🧬", "url": "https://filter-gnps-mgf.streamlit.app/"},
                    {"label": "MassQL Builder", "icon": "⚛️", "url": "https://massql-builder-from-csv.streamlit.app/"},
                    {"label": "MassQL Compendium Runner", "icon": "⚛️", "url": "https://massql-compendium-runner.streamlit.app/"},
                    {"label": "MassQL Structure Viewer", "icon": "🧪", "url": "https://structure-viewer-massql.streamlit.app/"},
                ],
            },
            {
                "title": "Cursos e materiais",
                "buttons": [
                    {"label": "Basic Statistics Course", "icon": "📊", "url": "https://basic-statistics-course.streamlit.app/"},
                    {"label": "Multivariate Analysis Course", "icon": "📈", "url": "https://mva-course.streamlit.app/"},
                ],
            },
        ],
    },
    "English": {
        "profile_key": "en",
        "sections": [
            {
                "title": "Social and contact",
                "buttons": [
                    {"label": "Instagram", "icon": "📸", "url": "https://instagram.com/borgesmricardo"},
                    {"label": "LinkedIn", "icon": "💼", "url": "https://www.linkedin.com/in/ricardo-borges-b7a16a36/"},
                    {"label": "YouTube", "icon": "▶️", "url": "https://www.youtube.com/@ricardomborges5295"},
                    {"label": "GitHub", "icon": "💻", "url": "https://github.com/RicardoMBorges"},
                    {"label": "Website", "icon": "🌐", "url": "https://laabioippn.wordpress.com/"},
                    {"label": "IPPN-Website", "icon": "🌐", "url": "https://www.ippn.ufrj.br/ricardo-moreira-borges/"},
                    {"label": "WhatsApp", "icon": "💬", "url": "https://wa.me/5521972125754"},
                ],
            },
            {
                "title": "Academic networks",
                "buttons": [
                    {"label": "ORCID", "icon": "🧬", "url": "https://orcid.org/0000-0002-7662-6734"},
                    {"label": "ResearchGate", "icon": "📚", "url": "https://www.researchgate.net/profile/Ricardo-Borges-7"},
                ],
            },
            {
                "title": "LAABio-IPPN Digital Platform",
                "buttons": [
                    {"label": "TLC2Chrom", "icon": "🧪", "url": "https://tlc2chrom.streamlit.app/"},
                    {"label": "DAFdiscovery", "icon": "📊", "url": "https://dafdiscovery.streamlit.app/"},
                    {"label": "Batch Organizer", "icon": "🗂️", "url": "https://batchorganizer.streamlit.app/"},
                    {"label": "DBsimilarity", "icon": "🧬", "url": "https://dbsimilarity.streamlit.app/"},
                    {"label": "DBsimilarity-unique", "icon": "🧬", "url": "https://dbsimilarity-unique.streamlit.app/"},
                    {"label": "DOE Pipeline", "icon": "📈", "url": "https://doe-pipeline.streamlit.app/"},
                    {"label": "MGF2Frag", "icon": "⚛️", "url": "https://mgf2frag.streamlit.app/"},
                    {"label": "pyMetaFlow HPLC", "icon": "🧪", "url": "https://pymetaflow-hplc.streamlit.app/"},
                    {"label": "Filter GNPS MGF", "icon": "🧬", "url": "https://filter-gnps-mgf.streamlit.app/"},
                    {"label": "MassQL Builder", "icon": "⚛️", "url": "https://massql-builder-from-csv.streamlit.app/"},
                    {"label": "MassQL Compendium Runner", "icon": "⚛️", "url": "https://massql-compendium-runner.streamlit.app/"},
                    {"label": "MassQL Structure Viewer", "icon": "🧪", "url": "https://structure-viewer-massql.streamlit.app/"},
                ],
            },
            {
                "title": "Courses",
                "buttons": [
                    {"label": "Basic Statistics Course", "icon": "📊", "url": "https://basic-statistics-course.streamlit.app/"},
                    {"label": "Multivariate Analysis Course", "icon": "📈", "url": "https://mva-course.streamlit.app/"},
                ],
            },
        ],
    },
    "Español": {
        "profile_key": "es",
        "sections": [
            {
                "title": "Redes y contacto",
                "buttons": [
                    {"label": "Instagram", "icon": "📸", "url": "https://instagram.com/borgesmricardo"},
                    {"label": "LinkedIn", "icon": "💼", "url": "https://www.linkedin.com/in/ricardo-borges-b7a16a36/"},
                    {"label": "YouTube", "icon": "▶️", "url": "https://www.youtube.com/@ricardomborges5295"},
                    {"label": "GitHub", "icon": "💻", "url": "https://github.com/RicardoMBorges"},
                    {"label": "Website", "icon": "🌐", "url": "https://laabioippn.wordpress.com/"},
                    {"label": "IPPN-Website", "icon": "🌐", "url": "https://www.ippn.ufrj.br/ricardo-moreira-borges/"},
                    {"label": "WhatsApp", "icon": "💬", "url": "https://wa.me/5521972125754"},
                ],
            },
            {
                "title": "Redes académicas",
                "buttons": [
                    {"label": "ORCID", "icon": "🧬", "url": "https://orcid.org/0000-0002-7662-6734"},
                    {"label": "ResearchGate", "icon": "📚", "url": "https://www.researchgate.net/profile/Ricardo-Borges-7"},
                ],
            },
            {
                "title": "Plataforma Digital LAABio-IPPN",
                "buttons": [
                    {"label": "TLC2Chrom", "icon": "🧪", "url": "https://tlc2chrom.streamlit.app/"},
                    {"label": "DAFdiscovery", "icon": "📊", "url": "https://dafdiscovery.streamlit.app/"},
                    {"label": "Batch Organizer", "icon": "🗂️", "url": "https://batchorganizer.streamlit.app/"},
                    {"label": "DBsimilarity", "icon": "🧬", "url": "https://dbsimilarity.streamlit.app/"},
                    {"label": "DBsimilarity-unique", "icon": "🧬", "url": "https://dbsimilarity-unique.streamlit.app/"},
                    {"label": "DOE Pipeline", "icon": "📈", "url": "https://doe-pipeline.streamlit.app/"},
                    {"label": "MGF2Frag", "icon": "⚛️", "url": "https://mgf2frag.streamlit.app/"},
                    {"label": "pyMetaFlow HPLC", "icon": "🧪", "url": "https://pymetaflow-hplc.streamlit.app/"},
                    {"label": "Filter GNPS MGF", "icon": "🧬", "url": "https://filter-gnps-mgf.streamlit.app/"},
                    {"label": "MassQL Builder", "icon": "⚛️", "url": "https://massql-builder-from-csv.streamlit.app/"},
                    {"label": "MassQL Compendium Runner", "icon": "⚛️", "url": "https://massql-compendium-runner.streamlit.app/"},
                    {"label": "MassQL Structure Viewer", "icon": "🧪", "url": "https://structure-viewer-massql.streamlit.app/"},
                ],
            },
            {
                "title": "Cursos",
                "buttons": [
                    {"label": "Basic Statistics Course", "icon": "📊", "url": "https://basic-statistics-course.streamlit.app/"},
                    {"label": "Multivariate Analysis Course", "icon": "📈", "url": "https://mva-course.streamlit.app/"},
                ],
            },
        ],
    },
}

# =========================================================
# HELPERS
# =========================================================
def image_to_base64(path_str: str) -> str | None:
    path = Path(path_str)
    if not path.exists():
        return None

    try:
        encoded = base64.b64encode(path.read_bytes()).decode()
        suffix = path.suffix.lower().replace(".", "")
        mime = "jpeg" if suffix == "jpg" else suffix
        return f"data:image/{mime};base64,{encoded}"
    except Exception:
        return None


def render_profile(name: str, headline: str, about: str, image: str) -> None:
    image_data = image_to_base64(image)

    if image_data:
        st.markdown(
            f"""
            <div class="profile-wrap">
                <img src="{image_data}" class="profile-image" alt="Profile image">
                <div class="profile-name">{name}</div>
                <div class="profile-headline">{headline}</div>
                <div class="profile-about">{about}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="profile-wrap">
                <div class="profile-placeholder">👤</div>
                <div class="profile-name">{name}</div>
                <div class="profile-headline">{headline}</div>
                <div class="profile-about">{about}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_buttons(buttons: list[dict]) -> None:
    for item in buttons:
        st.link_button(
            f"{item['icon']}  {item['label']}",
            item["url"],
            use_container_width=True,
        )

# =========================================================
# STYLES
# =========================================================
st.markdown(
    """
    <style>
    .stApp{
        background:
        radial-gradient(circle at top left, rgba(120,119,198,0.35), transparent 30%),
        radial-gradient(circle at top right, rgba(255,99,132,0.18), transparent 25%),
        linear-gradient(135deg,#0f172a 0%,#111827 45%,#1e293b 100%);
        background-attachment: fixed;
    }

    .block-container{
        max-width:760px;
        margin-top:2rem;
        margin-bottom:2rem;
        padding:2rem 1.4rem;
        background:rgba(255,255,255,0.10);
        border-radius:28px;
        border:1px solid rgba(255,255,255,0.14);
        backdrop-filter:blur(18px);
        -webkit-backdrop-filter:blur(18px);
        box-shadow:0 10px 35px rgba(0,0,0,0.28);
    }

    .profile-wrap{
        text-align:center;
        margin-bottom:1rem;
    }

    .profile-image{
        width:120px;
        height:120px;
        border-radius:50%;
        object-fit:cover;
        border:4px solid white;
        margin-bottom:0.7rem;
    }

    .profile-placeholder{
        width:120px;
        height:120px;
        border-radius:50%;
        background:rgba(255,255,255,0.2);
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:50px;
        margin:0 auto 0.7rem auto;
        border:4px solid white;
    }

    .profile-name{
        color:white;
        font-size:1.9rem;
        font-weight:800;
        margin-bottom:0.25rem;
    }

    .profile-headline{
        color:rgba(255,255,255,0.85);
        margin-bottom:0.45rem;
    }

    .profile-about{
        color:rgba(255,255,255,0.75);
        max-width:600px;
        margin:auto;
        margin-top:0.5rem;
        line-height:1.5;
    }

    .section-title{
        text-align:center;
        color:white;
        font-weight:700;
        margin-top:1.2rem;
        margin-bottom:0.6rem;
        font-size:1.05rem;
    }

    .stTabs [data-baseweb="tab-list"]{
        gap:0.6rem;
        justify-content:center;
    }

    .stTabs [data-baseweb="tab"]{
        height:48px;
        white-space:pre-wrap;
        border-radius:999px;
        padding-left:18px;
        padding-right:18px;
        background:rgba(255,255,255,0.08);
        color:white;
        border:1px solid rgba(255,255,255,0.12);
    }

    .stTabs [aria-selected="true"]{
        background:rgba(255,255,255,0.18) !important;
    }

    div.stLinkButton > a{
        border-radius:16px;
        font-weight:700;
        margin-bottom:0.5rem;
        background:rgba(255,255,255,0.12);
        border:1px solid rgba(255,255,255,0.2);
        color:white !important;
    }

    div.stLinkButton > a:hover{
        background:rgba(255,255,255,0.22);
        transform:translateY(-1px);
    }

    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    header{visibility:hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# LAYOUT
# =========================================================
tab_pt, tab_en, tab_es = st.tabs(["Português", "English", "Español"])

tab_map = {
    "Português": tab_pt,
    "English": tab_en,
    "Español": tab_es,
}

for lang, tab in tab_map.items():
    profile_key = LINKS[lang]["profile_key"]

    with tab:
        render_profile(
            PROFILE["name"],
            PROFILE[f"headline_{profile_key}"],
            PROFILE[f"about_{profile_key}"],
            PROFILE["profile_image"],
        )

        for section in LINKS[lang]["sections"]:
            st.markdown(
                f'<div class="section-title">{section["title"]}</div>',
                unsafe_allow_html=True,
            )
            render_buttons(section["buttons"])