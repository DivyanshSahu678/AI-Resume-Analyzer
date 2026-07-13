from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.analyzer import analyze_resume
from src.similarity import calculate_similarity

resume_path = "data/resumes/Divyansh_Sahu_Resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

resume_skills = extract_skills(resume_text)

# Read Job Description
with open("data/job_descriptions/python_developer.txt", "r") as file:
    job_description = file.read()

job_skills = extract_skills(job_description)

similarity_score = calculate_similarity(
    resume_text,
    job_description
)

result = analyze_resume(resume_skills, job_skills)



print("=" * 50)
print("Resume Analysis")
print("=" * 50)

print(f"\nResume Score : {result['score']}%")

print("\nOverall Resume Similarity :", similarity_score,"%")

print("\nMatched Skills:")
for skill in result["matched"]:
    print("✔", skill.title())

print("\nMissing Skills:")
for skill in result["missing"]:
    print("❌", skill.title())