import streamlit as st

from src.resume_parser import extract_text_from_pdf
from src.skill_extractor import extract_skills
from src.analyzer import analyze_resume
from src.similarity import calculate_similarity
from src.suggestions import generate_suggestions
from src.ats_score import calculate_ats_score
from src.gemini_analyzer import analyze_with_gemini
from src.report_generator import generate_report
from src.charts import create_skill_pie_chart, create_bar_chart

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("📄 AI Resume Analyzer")

    st.markdown("---")

    st.write("### Features")

    st.write("✅ Resume Parsing")
    st.write("✅ Skill Extraction")
    st.write("✅ Resume Matching")
    st.write("✅ ATS Score")
    st.write("✅ Similarity Score")
    st.write("✅ Charts")
    st.write("✅ PDF Report")
    st.write("✅ Gemini AI Review")

    st.markdown("---")

    st.success("Version 1.0")

# ----------------------------
# Main Title
# ----------------------------

st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a Job Description using AI."
)

# ----------------------------
# Inputs
# ----------------------------

uploaded_resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# ----------------------------
# Analyze Button
# ----------------------------

if st.button("Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a Resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste Job Description.")
        st.stop()

    # ----------------------------
    # Resume Parsing
    # ----------------------------

    resume_text = extract_text_from_pdf(uploaded_resume)

    # ----------------------------
    # Skill Extraction
    # ----------------------------

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    # ----------------------------
    # Resume Analysis
    # ----------------------------

    result = analyze_resume(
        resume_skills,
        job_skills
    )

    # ----------------------------
    # Similarity
    # ----------------------------

    similarity = calculate_similarity(
        resume_text,
        job_description
    )

    # ----------------------------
    # ATS Score
    # ----------------------------

    ats_score = calculate_ats_score(
        result,
        similarity,
        resume_text
    )

    # ----------------------------
    # Suggestions
    # ----------------------------

    suggestions = generate_suggestions(
        result["missing"]
    )

    st.success("✅ Analysis Completed")

    # ----------------------------
    # Metrics
    # ----------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Resume Score",
            f"{result['score']}%"
        )

    with col2:
        st.metric(
            "Similarity",
            f"{similarity}%"
        )

    with col3:
        st.metric(
            "ATS Score",
            f"{ats_score}%"
        )

    st.progress(result["score"] / 100)

    if ats_score >= 80:
        st.success("Excellent Resume ✅")

    elif ats_score >= 60:
        st.warning("Good Resume 👍")

    else:
        st.error("Needs Improvement ❌")

    st.write(f"Matched Skills : {len(result['matched'])}")
    st.write(f"Missing Skills : {len(result['missing'])}")

    # ----------------------------
    # Matched Skills
    # ----------------------------

    st.subheader("✅ Matched Skills")

    if result["matched"]:

        for skill in result["matched"]:
            st.success(skill.title())

    else:
        st.warning("No matched skills found.")

    # ----------------------------
    # Missing Skills
    # ----------------------------

    st.subheader("❌ Missing Skills")

    if result["missing"]:

        for skill in result["missing"]:
            st.error(skill.title())

    else:
        st.success("No Missing Skills")

    # ----------------------------
    # Suggestions
    # ----------------------------

    st.subheader("💡 Suggestions")

    for suggestion in suggestions:
        st.info(suggestion)

    # ----------------------------
    # Resume Skills
    # ----------------------------

    st.subheader("📋 Extracted Resume Skills")

    st.write(resume_skills)

    # ----------------------------
    # Pie Chart
    # ----------------------------

    st.subheader("📊 Skill Analysis")

    fig = create_skill_pie_chart(
        result["matched"],
        result["missing"]
    )

    st.pyplot(fig)

    # ----------------------------
    # Bar Chart
    # ----------------------------

    st.subheader("📈 Skill Comparison")

    fig2 = create_bar_chart(
        result["matched"],
        result["missing"]
    )

    st.pyplot(fig2)
    
        # ----------------------------
    # Gemini AI Review
    # ----------------------------

    st.divider()

    st.subheader("🤖 AI Resume Review")

    try:

        with st.spinner("Gemini is analyzing your resume..."):

            ai_feedback = analyze_with_gemini(
                resume_text,
                job_description
            )

        st.markdown(ai_feedback)

    except Exception:

        st.warning(
            "⚠️ AI Review is currently unavailable due to Gemini API quota limits."
        )

    # ----------------------------
    # Generate PDF Report
    # ----------------------------

    generate_report(
        "resume_report.pdf",
        result["score"],
        similarity,
        ats_score,
        result["matched"],
        result["missing"],
        suggestions
    )

    # ----------------------------
    # Download PDF
    # ----------------------------

    with open("resume_report.pdf", "rb") as pdf_file:

        st.download_button(
            label="📥 Download PDF Report",
            data=pdf_file,
            file_name="Resume_Analysis_Report.pdf",
            mime="application/pdf"
        )

    # ----------------------------
    # View Resume Text
    # ----------------------------

    with st.expander("📄 View Extracted Resume Text"):

        st.write(resume_text)

    # ----------------------------
    # View Job Description
    # ----------------------------

    with st.expander("💼 View Job Description"):

        st.write(job_description)

    # ----------------------------
    # Download Resume Text
    # ----------------------------

    st.download_button(
        label="📥 Download Extracted Resume Text",
        data=resume_text,
        file_name="resume_text.txt",
        mime="text/plain"
    )

    st.divider()

    st.success("🎉 Resume Analysis Completed Successfully!")