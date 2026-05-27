# Smart-AI-Resume-Screening-and-Career-Recommendation-Platform

AI Career Assistant is an intelligent resume analysis and career guidance platform designed to help students, freshers, and job seekers improve their career readiness using AI.

The application analyzes resumes, calculates ATS scores, identifies missing skills for specific job roles, and generates personalized learning roadmaps to help users achieve their target careers.

It also includes a RAG-based AI chatbot that can answer resume-related and career-related questions using the uploaded resume as context.

The project is built using Python, Streamlit, LangChain, FAISS, HuggingFace embeddings, and Groq LLMs with a modern and interactive UI.

🌟 Features
AI-powered Resume Analysis
ATS Resume Score Calculation
Automatic Skill Extraction
Dynamic Skill Gap Analysis
Personalized AI Career Roadmap
RAG-based Resume Chatbot
Target Role Matching
Resume-based Career Guidance
FAISS Vector Database Integration
Real-time AI Responses using Groq LLM
Interactive Modern Streamlit UI
🛠️ Tech Stack
Python
Streamlit
Pandas
Plotly
LangChain
FAISS Vector Store
HuggingFace Embeddings
Groq LLM (LLaMA 3)
HTML
CSS
📂 Project Structure
AI-Career-Assistant/
│
├── app.py
├── requirements.txt
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
│
└── README.md
⚙️ How It Works
1️⃣ Resume Upload

Users upload their resume in PDF format through the Streamlit interface.

2️⃣ Resume Parsing

The system extracts resume text and identifies technical skills automatically using NLP techniques.

3️⃣ ATS Score Analysis

An ATS compatibility score is generated based on resume content, extracted skills, and industry relevance.

4️⃣ Skill Gap Detection

Users enter a target role such as:

ML Engineer
Data Scientist
AI Engineer
Python Developer
Data Analyst

The system compares the user's skills with required industry skills and identifies missing areas.

5️⃣ AI Career Roadmap

The platform generates a personalized learning roadmap including:

Technologies to learn
Learning sequence
Project recommendations
Career improvement guidance
Skill development path
6️⃣ AI Resume Chatbot

The AI chatbot uses RAG (Retrieval-Augmented Generation) to answer resume-related questions such as:

What skills am I missing?
How can I improve my resume?
Which projects should I build?
What should I learn next?
Interview preparation guidance

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
