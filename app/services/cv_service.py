def analyze_cv(text: str):
    skills = ["java", "spring", "angular", "typescript", "python", "devops", "docker"]
    found = [s for s in skills if s in text.lower()]
    return {"skills": found}
