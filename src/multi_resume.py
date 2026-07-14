import pandas as pd

from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.analyzer import analyze_resume
from src.similarity import calculate_similarity
from src.ats_score import calculate_ats_score


def analyze_multiple_resumes(uploaded_resumes, job_description):

    results = []

    job_skills = extract_skills(job_description)

    for uploaded_resume in uploaded_resumes:

        resume_text = extract_text_from_pdf(uploaded_resume)

        resume_skills = extract_skills(resume_text)

        result = analyze_resume(
            resume_skills,
            job_skills
        )

        similarity = calculate_similarity(
            resume_text,
            job_description
        )

        ats_score = calculate_ats_score(
            result,
            similarity,
            resume_text
        )

        results.append({
            "Resume": uploaded_resume.name,
            "Resume Score": result["score"],
            "Similarity": similarity,
            "ATS Score": ats_score
        })

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="ATS Score",
        ascending=False
    )

    return df