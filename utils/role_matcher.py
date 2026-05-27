# utils/role_matcher.py

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()


# GENERATE REQUIRED SKILLS
# FOR ANY JOB ROLE

def generate_role_requirements(role):

    llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.2)

    prompt = f"""
    You are an AI career expert.

    Generate the most important technical skills
    required for this role.

    Role:
    {role}

    Return ONLY skill names as comma-separated values.
    Example:
    Python, SQL, Machine Learning, Docker
    """

    response = llm.invoke(prompt)

    skills = response.content.split(",")

    cleaned_skills = [
        skill.strip()
        for skill in skills
        if skill.strip()
    ]

    return cleaned_skills


# FIND SKILL GAP

def find_skill_gap(user_skills, target_skills):

    matched = list(
        set(user_skills).intersection(
            set(target_skills)
        )
    )

    missing = list(
        set(target_skills) - set(user_skills)
    )

    score = 0

    if len(target_skills) > 0:

        score = int(
            (len(matched) / len(target_skills)) * 100
        )

    return {
        "matched": matched,
        "missing": missing,
        "score": score
    }