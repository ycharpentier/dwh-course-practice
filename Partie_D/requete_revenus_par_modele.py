
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

# Ouverture des fichiers de donnees csv en dataframe
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")

# Calcul des revenus par modele
revenus_par_modele = merged_df.groupby("nommodele")["prixvente"].sum().reset_index().sort_values("prixvente", ascending=False).reset_index(drop=True)

# Affichage des résultats
print(revenus_par_modele.head(5).to_string(index=False))