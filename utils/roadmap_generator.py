from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_roadmap(role, missing_skills):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile",
        temperature=0.2
    )

    prompt = f"""
    You are an expert AI Career Mentor.

    Create a SHORT and CLEAN roadmap for becoming a:

    {role}

    Missing Skills:
    {missing_skills}

    STRICT RULES:
    1. Give ONLY 6 roadmap steps
    2. Each step should be MAXIMUM 1 sentence
    3. Do NOT use markdown
    4. Do NOT use headings
    5. Do NOT use symbols like *, #, -, **
    6. Do NOT generate long paragraphs
    7. Return ONLY plain text
    8. One step per line

    Example Output:

    Learn Python fundamentals and data structures

    Build machine learning projects using Scikit-learn

    Learn deep learning using TensorFlow and PyTorch
    """

    response = llm.invoke(prompt)

    return response.content.strip()