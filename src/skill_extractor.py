import re

# List of skills we want to detect
SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "React",
    "Node.js",
    "Git",
    "GitHub",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "TensorFlow",
    "PyTorch",
    "Pandas",
    "NumPy",
    "Scikit-learn"
]


def extract_skills(text):
    """
    Extract skills from resume text.
    """

    found_skills = []

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills