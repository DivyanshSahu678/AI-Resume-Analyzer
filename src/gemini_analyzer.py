import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def analyze_with_gemini(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the resume against the given Job Description.

Give the response in Markdown.

Include:

# Overall Score

# Resume Summary

# Strengths

# Weaknesses

# Missing Skills

# ATS Improvement Tips

# Interview Questions

Resume:

{resume_text}

Job Description:

{job_description}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text