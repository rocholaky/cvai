import typing


class ResumeGenerationState:
    """
    Class to regenerate resume based on the fit of the user to the job description.
    """
    original_resume: str
    company_description: str
    job_description: str
    resume_annotation: str
    resume_score: float
    resume_score_threshold: float
    N_tries: int
    generated_resume: str


class CoverLetterGenerationState:
    """
    Class to generate cover letter based on the fit of the user to the job description.
    """
    original_cover_letter: str
    company_description: str
    job_description: str
    cover_letter_annotation: str
    cover_letter_score: float
    cover_letter_score_threshold: float
    N_tries: int
    generated_cover_letter: str

