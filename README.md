# Smart-AI-Resume-Screening-and-Career-Recommendation-Platform

AI Career Assistant is an intelligent resume analysis platform that helps users evaluate their resumes, identify missing skills for target roles, and generate personalized AI-powered career roadmaps.

The application combines Resume Parsing, ATS Scoring, Skill Gap Analysis, RAG-based AI Chatbot, and Career Guidance into one interactive platform with a modern Streamlit interface.

Built using Python, Streamlit, FAISS, LangChain, and Groq LLMs, the system provides an end-to-end AI career assistance experience for students, freshers, and job seekers.

🌟 Features
AI-powered resume analysis
ATS resume score calculation
Automatic skill extraction from resume
Dynamic skill gap analysis
Personalized AI learning roadmap
RAG-based resume chatbot
Role-based career guidance
FAISS vector database integration
Interactive and modern UI
Real-time AI responses using Groq LLM
🛠️ Tech Stack
Python
Streamlit
Pandas
Plotly
LangChain
FAISS Vector Store
HuggingFace Embeddings
Groq LLM (LLaMA 3)
HTML & CSS
📂 Project Structure
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
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
├── README.md
└── .env
⚙️ How It Works
1️⃣ Resume Upload

Users upload their resume in PDF format.

2️⃣ Resume Parsing

The system extracts resume text and identifies technical skills automatically.

3️⃣ ATS Score Analysis

An ATS compatibility score is generated based on extracted skills and resume quality.

4️⃣ Skill Gap Detection

Users enter a target role such as:

ML Engineer
Data Scientist
AI Engineer
Python Developer

The system compares resume skills with industry-required skills.

5️⃣ AI Career Roadmap

A personalized learning roadmap is generated with:

Learning steps
Technologies to learn
Project ideas
Career guidance
6️⃣ AI Chatbot

Users can interact with the resume chatbot and ask:

Missing skills
Resume improvement suggestions
Career guidance
Interview preparation questions
