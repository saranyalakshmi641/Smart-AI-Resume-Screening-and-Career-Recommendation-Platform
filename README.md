# Smart-AI-Resume-Screening-and-Career-Recommendation-Platform

AI Career Assistant is an intelligent resume analysis platform that helps users evaluate their resumes, identify missing skills for target roles, and generate personalized AI-powered career roadmaps.

The application combines Resume Parsing, ATS Scoring, Skill Gap Analysis, RAG-based AI Chatbot, and Career Guidance into one interactive platform with a modern Streamlit interface.

Built using Python, Streamlit, FAISS, LangChain, and Groq LLMs, the system provides an end-to-end AI career assistance experience for students, freshers, and job seekers.

---

# 🌟 Features

- AI-powered Resume Analysis
- ATS Resume Score Calculation
- Automatic Skill Extraction
- Dynamic Skill Gap Analysis
- Personalized AI Learning Roadmap
- RAG-based Resume Chatbot
- Role-based Career Guidance
- FAISS Vector Database Integration
- Interactive and Modern UI
- Real-time AI Responses using Groq LLM

---

# 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- Plotly
- LangChain
- FAISS Vector Store
- HuggingFace Embeddings
- Groq LLM (LLaMA 3)
- HTML & CSS

---

# 📂 Project Structure

```bash
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── assets/
│   └── style.css
│
├── utils/
│   ├── resume_parser.py
│   ├── skill_extractor.py
│   ├── role_matcher.py
│   ├── roadmap_generator.py
│   ├── vector_store.py
│   ├── chatbot.py
│   └── ats_score.py
│
├── data/
└── models/

---

# ⚙️ How It Works

1️⃣ Resume Upload

Users upload their resume in PDF format through the Streamlit interface.

2️⃣ Resume Parsing

The system extracts resume text and automatically identifies technical skills from the uploaded resume.

3️⃣ ATS Score Analysis

An ATS compatibility score is generated based on resume content, skill relevance, and formatting quality.

4️⃣ Skill Gap Detection

Users enter a target role such as:

ML Engineer
Data Scientist
AI Engineer
Python Developer
Data Analyst

The system compares existing resume skills with industry-required skills and identifies missing areas.

5️⃣ AI Career Roadmap

A personalized AI-generated roadmap is created with:

Learning Steps
Recommended Technologies
Project Ideas
Skill-building Guidance
Career Improvement Suggestions
6️⃣ AI Resume Chatbot

Users can interact with the AI chatbot and ask questions like:

What skills am I missing?
How can I improve my resume?
Which projects should I build?
What should I learn next?
Interview preparation guidance

---
# **🚀 How to Run the Project**
Install Dependencies
pip install -r requirements.txt
Run the Application
streamlit run app.py
