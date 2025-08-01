from app.services.ai_feedback import get_resume_feedback

if __name__ == "__main__":
    sample_resume_text = """
    Simar Kaur
    Email: simarpreetkaur2799@gmail.com
    Experience:
    - Software Engineer at Programmics Technology, Oct 2022 - Mar 2023
    - Project Manager at Energy Efficiency Group, Feb 2024 - Present
    Skills: Python, SQL, ETL, Agile, GCP, Azure
    Education:
    - MSc Engineering with Management, King's College London, 2022-2024
    - BTech Computer Science, Chandigarh Engineering College, 2017-2021
    Certifications:
    - Python Alpha Course, Google Analytics, Bloomberg Market Concepts
    """

    print(get_resume_feedback(sample_text))
