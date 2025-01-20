\copy Categorie(idCategorie, nomCategorie) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_categorie_data.csv' DELIMITER ',' CSV HEADER;

\copy Pays(idPays, nomPays, supPays) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_pays_data.csv' DELIMITER ',' CSV HEADER;

\copy Ville(idVille, nomVille, supVille, idPays) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_ville_data.csv' DELIMITER ',' CSV HEADER;

\copy Client(idClient, nomClient, naissanceClient, idVille) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_client_data.csv' DELIMITER ',' CSV HEADER;

\copy Usine(idUsine, nomUsine, idVille) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_usine_data.csv' DELIMITER ',' CSV HEADER;

\copy Marque(idMarque, nomMarque, idPays) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_marque_data.csv' DELIMITER ',' CSV HEADER;

\copy Modele(idModele, nomModele, idMarque, idCategorie) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_modele_data.csv' DELIMITER ',' CSV HEADER;

\copy Produit(idProduit, idModele) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_produit_data.csv' DELIMITER ',' CSV HEADER;

\copy Fabrication(idProduit, idUsine, dateFabrication, coutFabrication) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_fabrication_data.csv' DELIMITER ',' CSV HEADER;

\copy Magasin(idMagasin, nomMagasin, idVille) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_magasin_data.csv' DELIMITER ',' CSV HEADER;

\copy PaysHabitant(idPays, annee, nbHabitant) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_payshabitant_data.csv' DELIMITER ',' CSV HEADER;

\copy Vente(idVente, idMagasin, idClient, dateVente, satisfactionClient) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_vente_data.csv' DELIMITER ',' CSV HEADER;

\copy VenteProduit(idVente, idProduit, prixVente, dateLivraison) from 'P:/Bureau/5A/dwh-course-practice/polytech2024edd_suj_source/tb_venteproduit_data.csv' DELIMITER ',' CSV HEADER;