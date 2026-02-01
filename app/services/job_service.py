from app.data.jobs import jobs

def recommend_jobs(user_skills):
    results = []
    for job in jobs:
        score = len(set(user_skills) & set(job["skills"]))
        if score > 0:
            results.append({"job": job["title"], "score": score})
    return sorted(results, key=lambda x: x["score"], reverse=True)
