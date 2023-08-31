import PyPDF2
import os


class Applicant:
    def __init__(self, name, resume_path):
        self.name = name
        self.resume_path = resume_path
        self.score = 0


def screen_resume(resume_text, job_keywords):
    resume_text = resume_text.lower()
    job_keywords = [keyword.lower() for keyword in job_keywords]
    return sum(1 for keyword in job_keywords if keyword in resume_text)


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text


def main():
    # Sample job keywords
    job_keywords = ["python", "web development", "database", "communication"]

    # Create applicants with sample PDF resumes
    applicants = [
        Applicant("Manish", "Manish's Resume.pdf"),
        # Add more applicants and their resume paths
    ]

    for applicant in applicants:
        resume_text = extract_text_from_pdf(applicant.resume_path)
        applicant.score = screen_resume(resume_text, job_keywords)

    ranked_applicants = sorted(applicants, key=lambda x: x.score, reverse=True)

    print("Ranked Applicants:")
    for idx, applicant in enumerate(ranked_applicants, start=1):
        print(f"{idx}. {applicant.name} - Score: {applicant.score}")


if __name__ == "__main__":
    main()
