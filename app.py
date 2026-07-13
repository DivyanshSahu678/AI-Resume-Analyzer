from src.resume_parser import extract_text_from_pdf

resume_path = "data/resumes/Divyansh_Sahu_Resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

print("Resume Text:\n")
print(resume_text)