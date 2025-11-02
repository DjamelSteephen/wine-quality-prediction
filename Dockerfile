# Étape 1 : image de base Python
FROM python:3.11-slim

# Étape 2 : définir le répertoire de travail
WORKDIR /app

# Étape 3 : copier requirements
COPY requirements.txt .

# Étape 4 : installer les dépendances
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : copier tout le code source
COPY . .

# Étape 6 : exposer le port 8000
EXPOSE 8000

# Étape 7 : commande pour lancer l'app
CMD ["uvicorn", "main_regression:app", "--host", "0.0.0.0", "--port", "8000"]
