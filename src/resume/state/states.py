import typing


class ResumeGenerationState:
    """
    Class to regenerate resume based on the fit of the user to the job description.
    """

    resume_enhancement_plan: str
    original_resume: str
    company_description: str
    job_description: str
    resume_annotation: str
    N_tries: int
    generated_resume: str
