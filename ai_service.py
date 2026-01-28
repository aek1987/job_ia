# ai_service.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Liste de test des offres d'emploi
job_offers = [
    {"id": 1, "title": "Développeur Java", "skills": ["Java", "Spring"]},
    {"id": 2, "title": "Développeur Angular", "skills": ["Angular", "TypeScript"]},
    {"id": 3, "title": "Data Scientist", "skills": ["Python", "Machine Learning"]}
]

# Endpoint pour recommandations
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    candidate_skills = data.get("skills", [])
    
    recommendations = []
    for job in job_offers:
        match_count = len(set(candidate_skills) & set(job["skills"]))
        if match_count > 0:
            recommendations.append({"job": job["title"], "score": match_count})
    
    # Tri décroissant
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return jsonify(recommendations)

# Endpoint test CV simple
@app.route("/analyze-cv", methods=["POST"])
def analyze_cv():
    data = request.json
    text = data.get("text", "").lower()
    
    possible_skills = ["java", "spring", "angular", "typescript", "python", "machine learning"]
    skills_found = [skill for skill in possible_skills if skill in text]
    
    return jsonify({"skills": skills_found})

if __name__ == "__main__":
    print("AI Service running on http://localhost:5000")
    app.run(port=5000)
