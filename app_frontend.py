import streamlit as st
import requests

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=['pdf', 'docx'])
job_desc = st.text_area("Paste job description (optional)")

if st.button("Get Feedback"):
    if uploaded_file is None:
        st.error("Please upload a file.")
    else:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        data = {"job_description": job_desc} if job_desc else {}

        try:
            response = requests.post("http://127.0.0.1:8000/resume-feedback/", files=files, data=data)
            if response.status_code == 200:
                st.subheader("Raw Response JSON")
                result = response.json()
                st.success("Feedback:")
                st.write(result.get("feedback", "No feedback returned."))
                if "keyword_match" in result:
                    km = result["keyword_match"]
                    st.subheader("Keyword Matches")
                    st.write(f"**Matched Keywords:** {', '.join(km.get('matched', [])) or 'None'}")
                    st.write(f"**Missing Keywords:** {', '.join(km.get('missing', [])) or 'None'}")
                    st.write(f"**Match Percentage:** {km.get('match_percentage', 0)}%")
                    st.subheader("Suggestions to Improve")
                    suggestions = km.get("improvement_suggestions", [])
                    if suggestions:
                        for suggestion in suggestions:
                            st.write(f"- {suggestion}")
                    else:
                        st.write("No suggestions available.")

            else:
                st.error(f"Error {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
