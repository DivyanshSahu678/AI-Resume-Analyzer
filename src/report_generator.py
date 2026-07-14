from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    resume_score,
    similarity_score,
    ats_score,
    matched_skills,
    missing_skills,
    suggestions
):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Resume Analysis Report</b>", styles["Title"]))

    story.append(Paragraph(f"<b>Resume Score:</b> {resume_score}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Similarity Score:</b> {similarity_score}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>ATS Score:</b> {ats_score}%", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))

    for skill in matched_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        story.append(Paragraph(f"• {skill}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>Suggestions</b>", styles["Heading2"]))

    for tip in suggestions:
        story.append(Paragraph(f"• {tip}", styles["BodyText"]))

    doc.build(story)