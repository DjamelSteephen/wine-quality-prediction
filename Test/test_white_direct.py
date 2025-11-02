import pandas as pd
import pickle
import os

# --- Charger le pipeline vin blanc ---
pipe_white_path = os.path.join("Pipeline vin blanc", "pipeline_polynomiale.mod")
pipe_white = pickle.load(open(pipe_white_path, "rb"))


# --- Définir les nouvelles données à tester ---
new_white = pd.DataFrame({
    'fixed acidity': [7.0],
    'volatile acidity': [0.27],
    'citric acid': [0.36],
    'residual sugar': [20.7],
    'chlorides': [0.045],
    'free sulfur dioxide': [45.0],
    'total sulfur dioxide': [170.0],
    'density': [1.0010],
    'pH': [3.00],
    'sulphates': [0.45],
    'alcohol': [8.8]
})

# --- Prédiction ---
classe_predite = pipe_white.predict(new_white)[0]
proba_bon = pipe_white.predict_proba(new_white)[0][1]
qualite_txt = "BON vin (classe 1)" if classe_predite == 1 else "MAUVAIS vin (classe 0)"

# --- Affichage ---
print("⚪ Vin blanc")
print(f"Classe prédite : {classe_predite} → {qualite_txt}")
print(f"Probabilité d’être un bon vin : {proba_bon:.2%}")
