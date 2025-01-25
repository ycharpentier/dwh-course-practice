
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
categorie_path = abs_path + "tb_categorie_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_vente = pd.read_csv(vente_path)
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)
df_categorie = pd.read_csv(categorie_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_vente, on="idvente", how="inner")
merged_df = pd.merge(merged_df, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")
merged_df = pd.merge(merged_df, df_categorie, on="idcategorie", how="inner")

# On ne garde que les colonnes qui nous interessent pour optimiser le calcul
merged_df = merged_df[["nomcategorie", "idproduit"]]

# Calculer sumqte par categorie
result = merged_df.groupby('nomcategorie').count().reset_index()
result.rename(columns={'idproduit': 'sumqte'}, inplace=True)

# Calcul du nombre par intervalle
result = {
    "[0,5000]": (result['sumqte'] < 5001).sum(),
    "]5000, 10000]": ((result['sumqte'] >= 5001) & (result['sumqte'] <= 10000)).sum(),
    "]10000, 15000]": ((result['sumqte'] >= 10001) & (result['sumqte'] <= 15000)).sum(),
    "]15000, +infini[": (result['sumqte'] > 15001).sum(),
}

result = pd.DataFrame([result]) 

# Affichage des resultats
#print(result.to_string(index=False))

# Sauvegarde du fichier
result.to_csv(file_path + "requete_Q2_Q7_resultat.csv", index=False, header=True)