from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills

resume_path = "data/resumes/Divyansh_Sahu_Resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

print("=" * 50)
print("Resume Text")
print("=" * 50)
print(resume_text)

skills = extract_skills(resume_text)

print("\n" + "=" * 50)
print("Detected Skills")
print("=" * 50)

for skill in skills:
    print("✔", skill)