from fastapi import FastAPI, UploadFile, File
import pandas as pd
import pickle
import uvicorn
import os

app = FastAPI(title="API Qualité du Vin 🍷", description="Prédiction de la qualité des vins rouges et blancs", version="1.1")

# --- Chemins relatifs des modèles ---
pipe_red_path = os.path.join("Pipeline vin rouge", "pipeline_multiple.mod")
pipe_white_path = os.path.join("Pipeline vin blanc", "pipeline_polynomiale.mod")

# --- Chargement des modèles ---
try:
    pipe_red = pickle.load(open(pipe_red_path, "rb"))
    pipe_white = pickle.load(open(pipe_white_path, "rb"))
except Exception as e:
    raise RuntimeError(f"Erreur de chargement des modèles : {e}")

# --- Route d'accueil ---
@app.get("/")
def home():
    return {"message": "Bienvenue sur l’API de prédiction de la qualité du vin 🍇"}

# --- Prédiction CSV vin rouge ---
@app.post("/predict/red_csv")
async def predict_red_csv(file: UploadFile = File(...)):
    try:
        # Lecture du CSV
        df = pd.read_csv(file.file)

        # Prédiction
        pred = pipe_red.predict(df)
        proba = pipe_red.predict_proba(df)[:, 1]

        # Ajout des colonnes
        df['classe_predite'] = pred
        df['probabilite_bon'] = proba
        df['qualite_txt'] = ["BON vin 🍷" if c == 1 else "MAUVAIS vin ❌" for c in pred]

        # Sauvegarde dans dossier Test
        os.makedirs("Test", exist_ok=True)
        output_path = os.path.join("Test", "red_test_results.csv")
        df.to_csv(output_path, index=False)

        # Création de la réponse JSON
        resultats = df[['qualite_txt', 'probabilite_bon']].to_dict(orient='records')

        return {
            "message": "✅ Prédiction terminée pour le vin rouge.",
            "resultats": resultats,
            "nombre_de_vins": len(resultats)
        }

    except Exception as e:
        return {"erreur": f"⚠️ Erreur lors de la prédiction : {e}"}

# --- Prédiction CSV vin blanc ---
@app.post("/predict/white_csv")
async def predict_white_csv(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        pred = pipe_white.predict(df)
        proba = pipe_white.predict_proba(df)[:, 1]

        df['classe_predite'] = pred
        df['probabilite_bon'] = proba
        df['qualite_txt'] = ["BON vin 🍷" if c == 1 else "MAUVAIS vin ❌" for c in pred]

        os.makedirs("Test", exist_ok=True)
        output_path = os.path.join("Test", "white_test_results.csv")
        df.to_csv(output_path, index=False)

        resultats = df[['qualite_txt', 'probabilite_bon']].to_dict(orient='records')

        return {
            "message": "✅ Prédiction terminée pour le vin blanc.",
            "resultats": resultats,
            "nombre_de_vins": len(resultats)
        }

    except Exception as e:
        return {"erreur": f"⚠️ Erreur lors de la prédiction : {e}"}

# --- Lancement ---
if __name__ == "__main__":
    print("🚀 Lancement de l'API FastAPI...")
    print("📖 Documentation : http://127.0.0.1:8000/docs")
    uvicorn.run("main_regression:app", host="127.0.0.1", port=8000, reload=True)
