\copy (SELECT DATE_PART('year', n.idTemps) as annee, c.nomCategorie, SUM(n.quantite) AS SUMQTE,RANK() OVER (PARTITION BY DATE_PART('year', n.idTemps) ORDER BY SUM(n.quantite) DESC) AS RANG FROM fNbProduitsVendus n JOIN dModele m ON n.idModele=m.idModele JOIN dCategorie c ON m.idCategorie=c.idCategorie GROUP BY annee, c.nomCategorie) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q5_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT DATE_PART('year', n.idTemps) as annee, c.nomCategorie, SUM(n.quantite) AS SUMQTE,
    RANK() OVER (PARTITION BY DATE_PART('year', n.idTemps) ORDER BY SUM(n.quantite) DESC) AS RANG
    FROM fNbProduitsVendus n JOIN dModele m ON n.idModele=m.idModele
    JOIN dCategorie c ON m.idCategorie=c.idCategorie
    GROUP BY annee, c.nomCategorie
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q5_resultat.csv' DELIMITER ',' CSV HEADER;
*/