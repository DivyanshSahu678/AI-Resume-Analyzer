def analyze_resume(resume_skills, job_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = resume_set.intersection(job_set)

    missing = job_set.difference(resume_set)

    score = (len(matched) / len(job_set)) * 100 if job_set else 0

    return {
        "score": round(score, 2),
        "matched": sorted(matched),
        "missing": sorted(missing)
    }