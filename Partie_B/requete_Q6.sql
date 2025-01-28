\copy (SELECT r.nomCategorie, r.nomMagasin, r.SUMQTE FROM (SELECT c.nomCategorie, ma.nomMagasin, SUM(n.quantite) AS SUMQTE, RANK() OVER(PARTITION BY c.nomCategorie ORDER BY SUM(n.quantite) DESC) AS RANG FROM fNbProduitsVendus n JOIN dModele mo ON n.idModele=mo.idModele JOIN dCategorie c ON mo.idCategorie=c.idCategorie JOIN dMagasin ma ON n.idMagasin=ma.idMagasin GROUP BY c.nomCategorie, ma.nomMagasin) AS r WHERE (r.RANG = 1 OR r.RANG = 2)) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q6_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT r.nomCategorie, r.nomMagasin, r.SUMQTE
    FROM
    (
        SELECT c.nomCategorie, ma.nomMagasin, SUM(n.quantite) AS SUMQTE,
            RANK() OVER(PARTITION BY c.nomCategorie
            ORDER BY SUM(n.quantite) DESC) AS RANG
        FROM fNbProduitsVendus n JOIN dModele mo ON n.idModele=mo.idModele
        JOIN dCategorie c ON mo.idCategorie=c.idCategorie
        JOIN dMagasin ma ON n.idMagasin=ma.idMagasin
        GROUP BY c.nomCategorie, ma.nomMagasin) AS r
    WHERE (r.RANG = 1 OR r.RANG = 2)
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q6_resultat.csv' DELIMITER ',' CSV HEADER;
*/