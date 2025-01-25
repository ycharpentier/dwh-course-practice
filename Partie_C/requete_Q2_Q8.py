
# Importation des librairies
import pandas as pd
import os

# Obtenir l'endroit ou se situe ce fichier pour enregistrer le resultat au meme endroit
file_path = "/".join(os.path.abspath(__file__).split("/")[:-1]) + "/"

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"

vente_path = abs_path + "tb_vente_data.csv"
venteProduit_path = abs_path + "tb_venteproduit_data.csv"
produit_path = abs_path + "tb_produit_data.csv"
model_path = abs_path + "tb_modele_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_vente = pd.read_csv(vente_path)
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_vente, on="idvente", how="inner")
merged_df = pd.merge(merged_df, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")

# Extraction de l'annee et du mois
merged_df['year'] = pd.to_datetime(merged_df['datevente']).dt.year
merged_df['month'] = pd.to_datetime(merged_df['datevente']).dt.month

#print(merged_df[["year", "month", "idproduit"]].head(30))

# Ajout d'une colonne auxiliaire pour compter chaque ligne
merged_df['count'] = 1

# On ne garde que les colonnes qui nous interessent pour optimiser le calcul
merged_df = merged_df[["year", "month", "idproduit", "count"]]

# Calculer la somme cumulative par annee et mois
result = (
    merged_df.groupby(['year', 'month'])
    .agg({'count': 'sum'})
    .reset_index()
    .sort_values(['year', 'month'])
)

# Ajouter la colonne sumqte avec une somme cumulative
result['sumqte'] = result['count'].cumsum()

# On ne garde pas la colonne count
result = result[["year", "month", "sumqte"]]

# Affichage des resultats
#print(result.to_string(index=False))

# Sauvegarde du fichier
result.to_csv(file_path + "requete_Q2_Q8_resultat.csv", index=False, header=True)