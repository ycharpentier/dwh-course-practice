
# Importation des librairies
import pandas as pd

# Chemins d'acces aux differents fichiers
abs_path = "P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/"

model_path = "tb_modele_data.csv"
produit_path = "tb_produit_data.csv"
venteProduit_path = "tb_venteproduit_data.csv"

# Ouverture des fichiers de donnees csv en dataframe
df_modele = pd.read_csv(model_path)
df_produit = pd.read_csv(produit_path)
df_venteProduit = pd.read_csv(venteProduit_path)

# Jointure des tables Produit et VenteProduit
df_merge = df_venteProduit.merge(df_produit, on='idproduit')

# Trie selon le nombre de ventes
ventes_par_modele = df_merge['idmodele'].value_counts()

# On recupere le nombre de ventes maximal
nb_ventes = ventes_par_modele.max()

# On recupere l'identifiant du modele le plus vendu
id_modele_le_plus_vendu = ventes_par_modele.idxmax()

# On recupere le nom du modele le plus vendu dans la table Modele
nom_modele_le_plus_vendu = df_modele.loc[df_modele['idmodele'] == id_modele_le_plus_vendu, 'nommodele'].iloc[0]

# Afficher le resultat
nb1 = max(len("nomModele"), len(nom_modele_le_plus_vendu)) + 3
nb2 = max(len("nbVentes"), len(str(nb_ventes))) + 3
print(f"{'nomModele':^{nb1}}|{'nbVentes':^{nb2}}")
print("-" * nb1 + "+" + "-" * nb2)
print(f"{nom_modele_le_plus_vendu:^{nb1}}|{nb_ventes:^{nb2}}")