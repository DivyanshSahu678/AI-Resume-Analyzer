def calculate_ats_score(result, similarity, resume_text):

    score = 0

    # Skill Score (40 Marks)
    score += result["score"] * 0.40

    # Similarity Score (30 Marks)
    score += similarity * 0.30

    # Projects (10 Marks)
    if "project" in resume_text.lower():
        score += 10

    # Education (10 Marks)
    if "b.tech" in resume_text.lower() or "bachelor" in resume_text.lower():
        score += 10

    # Certifications (10 Marks)
    if "certificate" in resume_text.lower() or "certification" in resume_text.lower():
        score += 10

    return round(score, 2)