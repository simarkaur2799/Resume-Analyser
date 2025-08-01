import google.generativeai as genai

genai.configure(api_key="AIzaSyA8MdelbWZihmlvGNTYw2j3OL7kh3u81_8")  # Use your key here

def get_resume_feedback(resume_text: str) -> str:
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    prompt = f"""You're an expert recruiter. Review the following resume and provide concise, constructive feedback:\n\n{resume_text}"""
    response = model.generate_content(prompt)
    return response.text.strip()

def format_feedback(feedback: str, keyword_match: dict | None = None) -> str:
    if keyword_match:
        matched = keyword_match.get("matched", [])
        missing = keyword_match.get("missing", [])
        percentage = keyword_match.get("match_percentage", 0)

        keyword_section = f"""
🔍 **Keyword Match**:
- ✅ Matched Keywords: {len(matched)}
- ❗ Missing Keywords: {len(missing)}
- 📊 Match Percentage: {percentage:.2f}%
"""
    else:
        keyword_section = "\n🔍 **Keyword Match**: Not provided.\n"

    return f"""
📝 **Resume Feedback Summary**:

{feedback}
{keyword_section}
📌 **Recommendations**:
- Tailor your resume to the job description
- Quantify achievements with numbers
- Use action verbs like “Developed”, “Led”, “Optimized”
- Emphasize relevant skills, tools, and certifications
"""
