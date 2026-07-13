import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.analyzer import analyze_resume
from src.similarity import calculate_similarity
from src.suggestions import generate_suggestions
from src.ats_score import calculate_ats_score

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste a Job Description.")
        st.stop()

    # Extract Resume Text
    resume_text = extract_text_from_pdf(uploaded_resume)

    # Extract Skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Analyze Resume
    result = analyze_resume(resume_skills, job_skills)

    # Calculate Similarity
    similarity = calculate_similarity(
        resume_text,
        job_description
    )

    # Calculate ATS Score
    ats_score = calculate_ats_score(
        result,
        similarity,
        resume_text
    )

    # Generate Suggestions
    suggestions = generate_suggestions(result["missing"])

    st.success("Analysis Completed ✅")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Resume Score", f"{result['score']}%")

    with col2:
        st.metric("Similarity Score", f"{similarity}%")

    with col3:
        st.metric("ATS Score", f"{ats_score}%")

    st.subheader("✅ Matched Skills")

    for skill in result["matched"]:
        st.success(skill.title())

    st.subheader("❌ Missing Skills")

    for skill in result["missing"]:
        st.error(skill.title())

    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.info(suggestion)

    st.subheader("📋 Resume Skills")

    st.write(resume_skills)