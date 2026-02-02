from openai import OpenAI
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Créer le client OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)
