
# Importation des librairies
import pandas as pd
import os
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# Obtenir l'endroit ou se situe ce fichier pour enregistrer le resultat au meme endroit
file_path = "/".join(os.path.abspath(__file__).split("/")[:-1]) + "/"

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"

vente_path = abs_path + "tb_vente_data.csv"
venteProduit_path = abs_path + "tb_venteproduit_data.csv"
produit_path = abs_path + "tb_produit_data.csv"
model_path = abs_path + "tb_modele_data.csv"
magasin_path = abs_path + "tb_magasin_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_vente = pd.read_csv(vente_path)
df_venteProduit = pd.read_csv(venteProduit_path)
df_produit = pd.read_csv(produit_path)
df_modele = pd.read_csv(model_path)
df_magasin = pd.read_csv(magasin_path)

# Fusionner les DataFrames nécessaires
merged_df = pd.merge(df_venteProduit, df_vente, on="idvente", how="inner")
merged_df = pd.merge(merged_df, df_produit, on="idproduit", how="inner")
merged_df = pd.merge(merged_df, df_modele, on="idmodele", how="inner")
merged_df = pd.merge(merged_df, df_magasin, on="idmagasin", how="inner")

# Extraire l'annee de la date de vente
merged_df["annee"] = pd.to_datetime(merged_df["datevente"]).dt.year

# Agregation par (nommodele, nommagasin, annee)
level1 = merged_df.groupby(["nommodele", "nommagasin", "annee"]).agg({"idproduit": "count"}).reset_index()

# Agregation par (nommodele, nommagasin)
level2 = merged_df.groupby(["nommodele", "nommagasin"]).agg({"idproduit": "count"}).reset_index()
level2["annee"] = ""

# Agregation par nommodele
level3 = merged_df.groupby("nommodele").agg({"idproduit": "count"}).reset_index()
level3["nommagasin"] = ""
level3["annee"] = ""

# Total general
total = pd.DataFrame({
    "nommodele": [""],
    "nommagasin": [""],
    "annee": [""],
    "idproduit": [merged_df["idproduit"].count()]
})

# Combiner les resultats
result = pd.concat([level1, level2, level3, total], ignore_index=True)

# Renommage de la colonne du nombre de produits vendus
result = result.rename(columns={"idproduit": "nbtot"})

# Trie pour un affichage dans le meme style que le rollup sql
result = result.sort_values(by=["nommodele", "nommagasin", "annee"], na_position="last", key=lambda col: col.replace("", "\uffff")).reset_index(drop=True)

# On arrange l'ordre des colonnes pour avoir le meme qu'en sql
result = result[["nbtot", "nommodele", "nommagasin", "annee"]]

# On recupere le nombre total de produits vendus par modele
temp = result[(result['nommagasin'] == "") & (result['annee'] == "") & (result['nommodele'] != "")][["nbtot", "nommodele"]]

# On convertit en liste
list_models = temp.values.tolist()

# On trie selon le nombre de produits vendus
list_models = sorted(list_models, key=lambda x: x[0], reverse=True)

# On recupere les 5 premiers et les 5 derniers
top_5 = list_models[:5]

# On recupere les annees
annees = [elt for elt in result["annee"].unique() if elt != ""]
annees.sort()
annees_str = [str(annee) for annee in annees]

# On recupere les valeur par annee pour chaque modele
top_5_name = [elt[1] for elt in top_5]
dico_top = {}
for elt in top_5_name:
    dico_top[elt] = []
    for annee in annees:
        dico_top[elt].append(merged_df[(merged_df['nommodele'] == elt) & (merged_df['annee'] == annee)][["prixvente"]].sum()[0])

# On affiche le graphique
for elt in dico_top:
    plt.plot(dico_top[elt], label=elt)
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=['2020', '2021', '2022', '2023', '2024'])
plt.title("Evolution du bénéfice pour les 5 meilleurs modèles")
plt.xlabel("Années")
plt.ylabel("Bénéfice ($)")
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.savefig(file_path + 'requete_benefice_meilleurs_modeles.png', bbox_inches='tight')
plt.show()