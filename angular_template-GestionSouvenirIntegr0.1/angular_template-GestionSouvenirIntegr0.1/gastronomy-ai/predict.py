import sys
import joblib
import pandas as pd

# Vérifier les arguments
if len(sys.argv) != 3:
    print("Usage: python predict.py <location> <rating>")
    sys.exit(1)

location = sys.argv[1]
rating = float(sys.argv[2])

# Charger le modèle et les colonnes
model = joblib.load('C:\\Users\\asmab\\OneDrive\\Bureau\\pidev\\angular_template-GestionSouvenirIntegr0.1\\gastronomy-ai\\gastronomy_model.pkl')
model_columns = joblib.load('C:\\Users\\asmab\\OneDrive\\Bureau\\pidev\\angular_template-GestionSouvenirIntegr0.1\\gastronomy-ai\\model_columns.pkl')

# Initialiser toutes les colonnes à 0
input_data = {col: 0 for col in model_columns}

# Encodage one-hot de la location
location_col = f'location_{location}'
if location_col in model_columns:
    input_data[location_col] = 1
else:
    print(f"⚠️ La location '{location}' n’a pas été vue pendant l'entraînement.")

# Ajouter la note
if 'rating' in model_columns:
    input_data['rating'] = rating

# Créer le DataFrame
X_new = pd.DataFrame([input_data])

# Prédiction
prediction = model.predict(X_new)
print(prediction)
