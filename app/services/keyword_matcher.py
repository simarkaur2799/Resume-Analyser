import re

def match_keywords(resume_text: str, job_description: str) -> dict:
    def normalize(text):
        return re.findall(r'\b\w+\b', text.lower())

    resume_words = set(normalize(resume_text))
    job_words = set(normalize(job_description))

    if not job_words:
        return {
            "matched": [],
            "missing": [],
            "match_percentage": 0,
            "improvement_suggestions": ["Job description text is empty or invalid."]
        }

    matched = [word for word in job_words if word in resume_words]
    missing = [word for word in job_words if word not in resume_words]
    match_percentage = round((len(matched) / len(job_words)) * 100, 2)

    if missing:
        suggestions = [f"Consider including keywords related to: {', '.join(missing)}"]
    else:
        suggestions = ["Your resume covers all key terms from the job description."]

    return {
        "matched": matched,
        "missing": missing,
        "match_percentage": match_percentage,
        "improvement_suggestions": suggestions
    }
