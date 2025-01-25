
# Importation des librairies
import pandas as pd
import os

# Obtenir l'endroit ou se situe ce fichier pour enregistrer le resultat au meme endroit
file_path = "/".join(os.path.abspath(__file__).split("/")[:-1]) + "/"

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"
abs_path = '/Users/arthur/Desktop/5A IMDS/dwh-course-practice/polytech2024edd_suj_source/'

venteProduit_path = abs_path + "tb_venteproduit_data.csv"
vente_path = abs_path + "tb_vente_data.csv"
produit_path = abs_path + "tb_produit_data.csv"
model_path = abs_path + "tb_modele_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_venteProduit = pd.read_csv(venteProduit_path)
df_vente = pd.read_csv(vente_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)

# Fusionner les DataFrames necessaires
merged_df = pd.merge(df_venteProduit, df_vente, on="idvente", how="inner")
merged_df = pd.merge(merged_df, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")

# On filtre les ventes par date
merged_df["datevente"] = pd.to_datetime(merged_df["datevente"])
revenus_periode_df = merged_df[(merged_df["datevente"] >= '2024-01-01') & (merged_df["datevente"] <= '2024-12-31')]

# Calcul des revenus par modele pour la periode
revenus_par_modele_periode = revenus_periode_df.groupby("nommodele")["prixvente"].sum().reset_index()

# Affichage des resultats
print(revenus_par_modele_periode)