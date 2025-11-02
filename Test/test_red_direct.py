import os
import pickle
import pandas as pd

# chemin relatif
pipe_red_path = os.path.join("Pipeline vin rouge", "pipeline_multiple.mod")

pipe_red = pickle.load(open(pipe_red_path, "rb"))


# --- Définir les nouvelles données à tester ---
new_red = pd.DataFrame({
    "fixed acidity":        [7.4],
    "volatile acidity":     [0.70],
    "citric acid":          [0.00],
    "residual sugar":       [1.9],
    "chlorides":            [0.076],
    "free sulfur dioxide":  [11.0],
    "total sulfur dioxide": [34.0],
    "density":              [0.9978],
    "pH":                   [3.51],
    "sulphates":            [0.56],
    "alcohol":              [9.4]
})

# --- Prédiction ---
classe_predite = pipe_red.predict(new_red)[0]
proba_bon = pipe_red.predict_proba(new_red)[0][1]
qualite_txt = "BON vin (classe 1)" if classe_predite == 1 else "MAUVAIS vin (classe 0)"

# --- Affichage ---
print("🔴 Vin rouge")
print(f"Classe prédite : {classe_predite} → {qualite_txt}")
print(f"Probabilité d’être un bon vin : {proba_bon:.2%}")
