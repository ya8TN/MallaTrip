import pandas as pd
import requests
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# 1. Charger les données depuis le backend
url = "http://localhost:8089/tourisme/gastronomy/retrieveAllGastronomies"
response = requests.get(url)
data = response.json()

# 2. Extraire les données utiles pour l'apprentissage
rows = []
for gastronomy in data:
    location = gastronomy.get('location')
    rating = gastronomy.get('detailGastronomy', {}).get('rating', 0)
    gastronomy_type = gastronomy.get('type')
    if location and gastronomy_type:
        rows.append({'location': location, 'rating': rating, 'type': gastronomy_type})

# Vérifier s’il y a assez de données
if len(rows) < 5:
    print("Pas assez de données pour entraîner un modèle.")
    exit()

df = pd.DataFrame(rows)

# 3. Convertir les données texte en valeurs numériques (encodage)
df_encoded = pd.get_dummies(df[['location']])
X = pd.concat([df_encoded, df[['rating']]], axis=1)
y = df['type']

# 4. Séparer données en entraînement / test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entraîner le modèle
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 6. Évaluer le modèle
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision du modèle : {accuracy:.2f}")


# 7. Sauvegarder le modèle
joblib.dump(model, 'gastronomy_model.pkl')
print("✅ Modèle enregistré sous 'gastronomy_model.pkl'")

# ✅ Sauvegarder les colonnes utilisées
joblib.dump(X.columns.tolist(), 'model_columns.pkl')
print("✅ Colonnes enregistrées sous 'model_columns.pkl'")

