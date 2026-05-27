import json
import re


def extract_skills(text):

    with open("data/skills_database.json") as f:
        skills_db = json.load(f)

    skills_list = skills_db["skills"]

    found_skills = []

    for skill in skills_list:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return list(set(found_skills))