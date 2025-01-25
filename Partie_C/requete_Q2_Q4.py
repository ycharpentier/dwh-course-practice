
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
magasin_path = abs_path + "tb_magasin_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_vente = pd.read_csv(vente_path)
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)
df_categorie = pd.read_csv(categorie_path)
df_magasin = pd.read_csv(magasin_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_vente, on="idvente", how="inner")
merged_df = pd.merge(merged_df, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")
merged_df = pd.merge(merged_df, df_categorie, on="idcategorie", how="inner")
merged_df = pd.merge(merged_df, df_magasin, on="idmagasin", how="inner")

# Extraire l'annee de la date de vente
merged_df["annee"] = pd.to_datetime(merged_df["datevente"]).dt.year

# On ne garde que les colonnes qui nous interessent pour optimiser le calcul
merged_df = merged_df[["nomcategorie", "nommagasin", "annee", "idproduit"]]

# Agregation par (nomcategorie, nommagasin, annee)
level1 = merged_df.groupby(["nomcategorie", "nommagasin", "annee"]).agg({"idproduit": "count"}).reset_index()

# Agregation par (nomcategorie, nommagasin)
level2 = merged_df.groupby(["nomcategorie", "nommagasin"]).agg({"idproduit": "count"}).reset_index()
level2["annee"] = ""

# Agregation par nomcategorie
level3 = merged_df.groupby("nomcategorie").agg({"idproduit": "count"}).reset_index()
level3["nommagasin"] = ""
level3["annee"] = ""

# Total general
total = pd.DataFrame({
    "nomcategorie": [""],
    "nommagasin": [""],
    "annee": [""],
    "idproduit": [merged_df["idproduit"].count()]
})

# Combiner les resultats
result = pd.concat([level1, level2, level3, total], ignore_index=True)

# Renommage de la colonne du nombre de produits vendus
result = result.rename(columns={"idproduit": "nbtot"})

# Trie pour un affichage dans le meme style que le rollup sql
result = result.sort_values(by=["nomcategorie", "nommagasin", "annee"], na_position="last", key=lambda col: col.replace("", "\uffff")).reset_index(drop=True)

# On arrange l'ordre des colonnes pour avoir le meme qu'en sql
result = result[["nbtot", "nomcategorie", "nommagasin", "annee"]]

# Affichage du resultat
#print(result.head(10).to_string(index=False))

# Sauvegarde du fichier
result.to_csv(file_path + "requete_Q2_Q4_resultat.csv", index=False, header=True)