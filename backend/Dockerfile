# Image Python légère
FROM python:3.11-slim

# Empêche Python de bufferiser la sortie (logs visibles en temps réel)
ENV PYTHONUNBUFFERED=1

# Dossier de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app ./app

# Exposer le port de l'API
EXPOSE 8000

# Commande de lancement du serveur FastAPI avec Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]