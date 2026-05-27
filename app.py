import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px

from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.role_matcher import (
    generate_role_requirements,
    find_skill_gap
)
from utils.roadmap_generator import generate_roadmap
from utils.vector_store import create_vector_store
from utils.chatbot import build_chatbot
from utils.ats_score import calculate_ats_score

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🚀",
    layout="wide"
)

# ======================================================
# LOAD CSS
# ======================================================

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ======================================================
# SESSION STATE
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ======================================================
# HERO SECTION
# ======================================================

st.markdown(
    """
    <h1 class="main-title">
    🚀 AI Career Assistant
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="subtitle">
    AI-Powered Resume Analyzer 
    </p>
    """,
    unsafe_allow_html=True
)

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.title("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    st.divider()

    st.markdown(
        """
        ### 🎯 Features

        ✅ ATS Resume Score  
        ✅ Skill Extraction  
        ✅ Skill Gap Analysis  
        ✅ AI Career Roadmap  
        ✅ Resume Chatbot  
        ✅ Dynamic Role Matching  
        """
    )

# ======================================================
# MAIN APP
# ======================================================

if uploaded_file:

    # ==================================================
    # EXTRACT RESUME
    # ==================================================

    resume_text = extract_resume_text(
        uploaded_file
    )

    # ==================================================
    # SKILLS
    # ==================================================

    skills = extract_skills(
        resume_text
    )

    # ==================================================
    # ATS SCORE
    # ==================================================

    ats_score = calculate_ats_score(
        skills
    )

    # ==================================================
    # TARGET ROLE
    # ==================================================

    st.subheader(
        "🎯 Enter Your Target Role"
    )

    target_role = st.text_input(
        "Dream Job Role",
        placeholder="Example: AI Engineer"
    )

    result = None
    required_skills = []

    if target_role:

        with st.spinner(
            "Analyzing role requirements..."
        ):

            required_skills = (
                generate_role_requirements(
                    target_role
                )
            )

            result = find_skill_gap(
                skills,
                required_skills
            )

    # ==================================================
    # VECTOR STORE
    # ==================================================

    text_chunks = [
        resume_text[i:i + 1000]
        for i in range(
            0,
            len(resume_text),
            1000
        )
    ]

    vectorstore = create_vector_store(
        text_chunks
    )

    chatbot = build_chatbot(
        vectorstore
    )

    # ==================================================
    # TABS
    # ==================================================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Resume Analysis",
        "📉 Skill Gap",
        "🛣 AI Roadmap",
        "🤖 AI Chat"
    ])

    # ==================================================
    # TAB 1
    # ==================================================

    with tab1:

        st.subheader(
            "📊 ATS Resume Score"
        )

        st.progress(
            ats_score / 100
        )

        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

        st.divider()

        st.subheader(
            "🛠 Extracted Skills"
        )

        cols = st.columns(4)

        for i, skill in enumerate(
            skills
        ):
            cols[
                i % 4
            ].success(skill)

        st.divider()

        st.subheader(
            "📄 Resume Preview"
        )

        st.text_area(
            "Resume Content",
            resume_text[:3000],
            height=300
        )

    # ==================================================
    # TAB 2
    # ==================================================

    with tab2:

        if target_role and result:

            st.subheader(
                "🎯 Match Analysis"
            )

            st.metric(
                "Job Match %",
                f"{result['score']}%"
            )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "✅ Matched Skills"
                )

                if result["matched"]:

                    for skill in result[
                        "matched"
                    ]:
                        st.success(skill)

                else:

                    st.warning(
                        "No matched skills found."
                    )

            with col2:

                st.subheader(
                    "❌ Missing Skills"
                )

                if result["missing"]:

                    for skill in result[
                        "missing"
                    ]:
                        st.error(skill)

                else:

                    st.success(
                        "No missing skills!"
                    )

            st.divider()

            st.subheader(
                "📋 Required Skills For Role"
            )

            required_df = pd.DataFrame({
                "Required Skills":
                required_skills
            })

            st.dataframe(
                required_df,
                use_container_width=True
            )

        else:

            st.info(
                "Enter a target role to analyze skill gaps."
            )

    # ==================================================
    # TAB 3 ROADMAP
    # ==================================================

    with tab3:

        if target_role and result:

            st.subheader(
                "🛣 AI Learning Roadmap"
            )

            if st.button(
                "Generate Personalized Roadmap"
            ):

                with st.spinner(
                    "Generating roadmap..."
                ):

                    roadmap = generate_roadmap(
                        target_role,
                        result["missing"]
                    )

                # CLEAN ROADMAP

                steps = roadmap.split("\n")

                filtered_steps = [
                    s.strip(
                        "-•1234567890. "
                    )
                    for s in steps
                    if len(
                        s.strip()
                    ) > 15
                ]

                unique_steps = []

                for step in filtered_steps:

                    if step not in unique_steps:
                        unique_steps.append(
                            step
                        )

                # HEADER

                st.markdown(
                    f"""
                    <h2 class="roadmap-header">
                    🚀 Personalized Roadmap for {target_role}
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

                icons = [
                    "📘",
                    "🧠",
                    "💻",
                    "🚀",
                    "☁️",
                    "🎯"
                ]

                # ROADMAP CARDS

                for i, step in enumerate(
                    unique_steps
                ):

                    icon = icons[
                        i % len(icons)
                    ]

                    card_html = f"""
                    <style>
                    body {{
                        margin:0;
                        background:transparent;
                        font-family:'Segoe UI';
                    }}

                    .roadmap-card {{
                        display:flex;
                        gap:20px;
                        align-items:center;
                        background:#0f172a;
                        border:1px solid #334155;
                        border-radius:24px;
                        padding:22px;
                        margin:10px 0;
                    }}

                    .step-circle {{
                        min-width:65px;
                        height:65px;
                        border-radius:50%;
                        background:linear-gradient(
                            135deg,
                            #0ea5e9,
                            #2563eb
                        );
                        display:flex;
                        justify-content:center;
                        align-items:center;
                        color:white;
                        font-size:24px;
                        font-weight:800;
                    }}

                    .step-content {{
                        flex:1;
                    }}

                    .step-title {{
                        color:#38bdf8;
                        font-size:22px;
                        font-weight:700;
                        margin-bottom:8px;
                    }}

                    .step-text {{
                        color:#f8fafc;
                        font-size:17px;
                        line-height:1.8;
                    }}
                    </style>

                    <div class="roadmap-card">
                        <div class="step-circle">
                            {i+1}
                        </div>

                        <div class="step-content">
                            <div style="font-size:30px;">
                                {icon}
                            </div>

                            <div class="step-title">
                                Step {i+1}
                            </div>

                            <div class="step-text">
                                {step}
                            </div>
                        </div>
                    </div>
                    """

                    components.html(
                        card_html,
                        height=190,
                        scrolling=False
                    )

                    st.progress(
                        (i + 1)
                        / len(unique_steps)
                    )

                with st.expander(
                    "📄 Full AI Generated Roadmap"
                ):

                    for i, step in enumerate(
                        unique_steps
                    ):

                        st.markdown(
                            f"✅ Step {i+1}: {step}"
                        )

        else:

            st.info(
                "Enter a target role first."
            )

    # ==================================================
    # TAB 4 CHATBOT
    # ==================================================

    with tab4:

        st.subheader(
            "🤖 AI Career Chatbot"
        )

        for msg in st.session_state.messages:

            with st.chat_message(
                msg["role"]
            ):
                st.markdown(
                    msg["content"]
                )

        prompt = st.chat_input(
            "Ask career-related questions..."
        )

        if prompt:

            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })

            with st.chat_message(
                "user"
            ):
                st.markdown(
                    prompt
                )

            with st.chat_message(
                "assistant"
            ):

                with st.spinner(
                    "Thinking..."
                ):

                    # FIXED CHATBOT BUG
                    response = chatbot.invoke(
                        prompt
                    )

                    answer = response[
                        "result"
                    ]

                    st.markdown(
                        answer
                    )

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

# ======================================================
# NO FILE
# ======================================================

else:

    st.info(
        "📄 Please upload your resume PDF to begin."
    )