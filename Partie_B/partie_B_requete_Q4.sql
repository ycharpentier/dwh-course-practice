\copy (SELECT SUM(n.quantite) AS NbTot, c.nomCategorie, ma.nomMagasin, DATE_PART('year', n.idTemps) as annee FROM fNbProduitsVendus n JOIN dModele m ON n.idModele=m.idModele JOIN dCategorie c ON m.idCategorie=c.idCategorie JOIN dMagasin ma ON n.idMagasin=ma.idMagasin GROUP BY ROLLUP(c.nomCategorie, ma.nomMagasin, annee)) TO 'P:/Bureau/5A/dwh-course-practice/partie_B_requete_Q4_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT SUM(n.quantite) AS NbTot,
        c.nomCategorie,
        ma.nomMagasin,
        DATE_PART('year', n.idTemps) as annee
    FROM fNbProduitsVendus n JOIN dModele m ON n.idModele=m.idModele
    JOIN dCategorie c ON m.idCategorie=c.idCategorie
    JOIN dMagasin ma ON n.idMagasin=ma.idMagasin
    GROUP BY ROLLUP(c.nomCategorie, ma.nomMagasin, annee)
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B_requete_Q4_resultat.csv' DELIMITER ',' CSV HEADER;
*/