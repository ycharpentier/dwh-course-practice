\copy dCategorie(idCategorie, nomCategorie) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_categorie_data.csv' DELIMITER ',' CSV HEADER;

INSERT INTO dModele(idModele, nomModele, idCategorie)
SELECT idModele, nomModele, idCategorie
FROM Modele;

\copy dPays(idPays, nomPays, supPays) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_pays_data.csv' DELIMITER ',' CSV HEADER;

\copy dVille(idVille, nomVille, supVille, idPays) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_ville_data.csv' DELIMITER ',' CSV HEADER;

\copy dMagasin(idMagasin, nomMagasin, idVille) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_magasin_data.csv' DELIMITER ',' CSV HEADER;

INSERT INTO fNbProduitsVendus(idTemps, idMagasin, idModele, montant, quantite)
SELECT v.dateVente AS idTemps, v.idMagasin, m.idModele, SUM(vp.prixVente) AS montant, COUNT(vp.idProduit) AS quantite
FROM Vente v JOIN VenteProduit vp ON v.idVente=vp.idVente
JOIN Produit p on vp.idProduit=p.idProduit
JOIN Modele m on p.idModele=m.idModele
GROUP BY v.dateVente, v.idMagasin, m.idModele