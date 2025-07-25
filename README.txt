# 🧠 Classification supervisée basée sur les clusters

## 📌 Description du projet

Ce projet a pour objectif de réaliser une **analyse prédictive** à partir d’un jeu de données en appliquant une **méthodologie de Machine Learning supervisé**, basée sur une étape préalable de **clustering non supervisé**.

Plus précisément, le processus se déroule comme suit :

1. 📊 **Exploration et préparation des données** :
   - Chargement du jeu de données.
   - Traitement des valeurs manquantes et des outliers.
   - Sélection des variables pertinentes.

2. 🔎 **Clustering non supervisé** :
   - Application de l’algorithme `KMeans` pour identifier des groupes naturels dans les données.
   - Attribution d’un label de cluster à chaque échantillon, qui servira ensuite de **cible** (`y`) pour l'étape de classification supervisée.

3. 🎯 **Classification supervisée** :
   - Définition des variables explicatives (`X`) et de la cible (`y` = cluster).
   - Division du jeu de données en ensemble d'entraînement et de test.
   - Traitement du déséquilibre de classes à l’aide de techniques comme `RandomOverSampler`.
   - Entraînement de modèles comme `RandomForestClassifier`.
   - Évaluation avec des métriques telles que la précision, le rappel, le F1-score, et la matrice de confusion.

4. 🔧 **Optimisation des hyperparamètres** :
   - Utilisation de `GridSearchCV` pour améliorer les performances du modèle.

5. ✅ **Validation croisée** :
   - Vérification de la robustesse du modèle via une validation croisée (`cross-validation`).

Ce projet illustre une approche complète de classification supervisée avec une étape amont de regroupement non supervisé, utile dans les cas où la variable cible n’est pas explicitement donnée.

---

## 📁 Structure recommandée

project/
│
├── data/
│ └── dataset.csv
│
├── notebook/
│ └── classification_cluster.ipynb
│
├── models/
│ └── random_forest.pkl
│
├── README.md
└── requirements.txt

yaml
Copy
Edit


---

## 📚 Bibliothèques utilisées

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `sklearn` (KMeans, RandomForestClassifier, GridSearchCV...)
- `imblearn` (RandomOverSampler)

---

## 🔥 Auteur

Projet réalisé par **[Ton Nom]** dans le cadre d’un apprentissage en data science.

