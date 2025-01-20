
# Importation des librairies
import pandas as pd

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"

venteProduit_path = "tb_venteproduit_data.csv"
vente_path = "tb_vente_data.csv"
produit_path = "tb_produit_data.csv"
model_path = "tb_modele_data.csv"
categorie_path = "tb_categorie_data.csv"
magasin_path = "tb_magasin_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_venteProduit = pd.read_csv(venteProduit_path)
df_vente = pd.read_csv(vente_path)
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

# Extraire l'année de la date de vente
merged_df['annee'] = pd.to_datetime(merged_df['datevente']).dt.year

# Compter le nombre total de produits vendus par catégorie
result = merged_df.groupby('nomcategorie').size().reset_index(name="nb_produits_vendus")

# Appliquer les intervalles demandés
categories_5000 = result[result['nb_produits_vendus'] <= 5000].shape[0]
categories_5000_10000 = result[(result['nb_produits_vendus'] > 5000) & (result['nb_produits_vendus'] <= 10000)].shape[0]
categories_10000_15000 = result[(result['nb_produits_vendus'] > 10000) & (result['nb_produits_vendus'] <= 15000)].shape[0]
categories_15000 = result[result['nb_produits_vendus'] > 15000].shape[0]

print("[0, 5 000] :", categories_5000)
print("]5 000, 10 000] :", categories_5000_10000)
print("]10 000, 15 000] :", categories_10000_15000)
print("]15 000, +infini[ :", categories_15000)
