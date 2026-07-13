import re
import pandas as pd

# Load skills from CSV
skills_df = pd.read_csv("data/skills.csv")

SKILLS = skills_df["Skill"].dropna().tolist()


def extract_skills(text):
    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return sorted(list(set(found_skills)))