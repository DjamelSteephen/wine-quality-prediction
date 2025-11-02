🍷 Wine Quality Prediction
📖 1️⃣ Description du projet

Ce projet a pour objectif de prédire la qualité des vins rouges et blancs à partir de leurs caractéristiques physico-chimiques.
Il repose sur des modèles de machine learning enregistrés sous forme de pipelines scikit-learn.

🔴 Vin rouge → pipeline_multiple.mod (classification avec standardisation et modèle multiple)

⚪ Vin blanc → pipeline_polynomiale.mod (classification avec features polynomiales)

Le projet permet :

de tester directement des échantillons de vins via des scripts Python,

ou d’utiliser une API REST basée sur FastAPI (optionnel).

⚙️ 2️⃣ Pré-requis

Python ≥ 3.10 (installé via Anaconda ou manuel)

pip

Windows, Linux ou macOS

VS Code (environnement de développement utilisé)

🧩 3️⃣ Installation de l’environnement
🔹 Étape 1 – Cloner le projet
git clone https://github.com/<ton-utilisateur>/wine-quality-prediction.git
cd wine-quality-prediction

🔹 Étape 2 – Créer un environnement virtuel
python -m venv env

🔹 Étape 3 – Activer l’environnement

Sous Windows :

.\env\Scripts\activate


Sous Linux / macOS :

source env/bin/activate


(Si tu utilises Anaconda, l’environnement base peut déjà être actif.)

🔹 Étape 4 – Installer les dépendances
pip install -r requirements.txt


ou manuellement :

pip install numpy pandas scikit-learn matplotlib seaborn joblib streamlit python-multipart fastapi uvicorn

🔹 Étape 5 – (Optionnel) Générer un fichier requirements.txt
pip freeze > requirements.txt

🗂️ 4️⃣ Organisation du projet
wine+quality/
│
├─ Pipeline vin rouge/
│   └─ pipeline_multiple.mod
│
├─ Pipeline vin blanc/
│   └─ pipeline_polynomiale.mod
│
├─ Test/
│   ├─ test_red_direct.py        # script de test vin rouge
│   ├─ test_white_direct.py      # script de test vin blanc
│
├─ main_regression.py            # API FastAPI (optionnel)
├─ requirements.txt
└─ README.md

🍇 5️⃣ Tester les modèles
🔴 Vin rouge

Modifier Test/test_red_direct.py avec les caractéristiques du vin, puis exécuter :

python Test/test_red_direct.py


Exemple de sortie :

🔴 Vin rouge
Classe prédite : 1 → BON vin (classe 1)
Probabilité d’être un bon vin : 85.00%

⚪ Vin blanc

Modifier Test/test_white_direct.py, puis exécuter :

python Test/test_white_direct.py


Exemple de sortie :

⚪ Vin blanc
Classe prédite : 1 → BON vin (classe 1)
Probabilité d’être un bon vin : 78.00%

🚀 6️⃣ Utiliser l’API FastAPI (optionnel)

Lancer le serveur :

python main_regression.py


ou avec Uvicorn :

uvicorn main_regression:app --reload


📄 Accéder à la documentation interactive :
👉 http://127.0.0.1:8000/docs

Endpoints disponibles :

POST /predict/red_csv → prédiction pour vins rouges (fichier CSV)

POST /predict/white_csv → prédiction pour vins blancs (fichier CSV)

🧠 7️⃣ Notes techniques

Les modèles sont sauvegardés au format pickle (.mod).

Les scripts test_red_direct.py et test_white_direct.py permettent de tester directement les prédictions sans fichiers CSV.

Le module python-multipart est nécessaire pour l’upload de fichiers via FastAPI.

Le projet peut être étendu avec Streamlit pour une interface web.

👨‍💻 8️⃣ Auteur

Djamel Zongo
Projet développé avec VS Code et Python (env)
📅 Année : 2025