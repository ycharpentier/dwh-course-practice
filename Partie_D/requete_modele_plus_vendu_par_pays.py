
# Importation des librairies
import pandas as pd
import os

# Obtenir l'endroit ou se situe ce fichier pour enregistrer le resultat au meme endroit
file_path = "/".join(os.path.abspath(__file__).split("/")[:-1]) + "/"

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"
abs_path = '/Users/arthur/Desktop/5A IMDS/dwh-course-practice/polytech2024edd_suj_source/'

venteProduit_path = abs_path + "tb_venteproduit_data.csv"
produit_path = abs_path + "tb_produit_data.csv"
model_path = abs_path + "tb_modele_data.csv"
marque_path = abs_path + "tb_marque_data.csv"
pays_path = abs_path + "tb_pays_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)
df_marque = pd.read_csv(marque_path)
df_pays = pd.read_csv(pays_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")
merged_df = pd.merge(merged_df, df_marque, on="idmarque", how="inner")
merged_df = pd.merge(merged_df, df_pays, on="idpays", how="inner")

# Calcul des ventes totales par modele et par pays
merged_df["prixvente"] = merged_df["prixvente"].fillna(0)
result = merged_df.groupby(["nompays", "nommodele"])["prixvente"].sum().reset_index()

# Trouver le modele le plus vendu pour chaque pays (maximum des ventes)
result = result.loc[result.groupby("nompays")["prixvente"].idxmax()]

# Selectionner les colonnes d'interet
result = result[["nompays", "nommodele"]].reset_index(drop=True)

# Affichage des resultats
print(result.to_string(index=False))