import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Chargement des données
df = pd.read_csv('diabetes.csv')

# Afficher les informations du dataframe : types, valeurs non-nulles, etc.
# print(df.info())

# Afficher les 5 premières lignes pour aperçu des données
# print(df.head())

# 2. Valeurs manquantes
print("\nNombre de valeurs manquantes par colonne :")
print(df.isnull().sum())
