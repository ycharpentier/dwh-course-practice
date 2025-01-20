\copy (SELECT SUM(CASE WHEN R.SUMQTE < 5001 THEN 1 ELSE 0 END) AS "[0,5000]", SUM(CASE WHEN R.SUMQTE BETWEEN 5001 AND 10000 THEN 1 ELSE 0 END) AS "]5000, 10000]", SUM(CASE WHEN R.SUMQTE BETWEEN 10001 AND 15000 THEN 1 ELSE 0 END) AS "]10000, 15000]", SUM(CASE WHEN R.SUMQTE > 15001 THEN 1 ELSE 0 END) AS "]15000, +infini[" FROM (SELECT c.nomCategorie, SUM(n.quantite) as SUMQTE FROM fNbProduitsVendus n JOIN dModele mo ON n.idModele=mo.idModele JOIN dCategorie c ON mo.idCategorie=c.idCategorie GROUP BY c.nomCategorie) AS R) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q7_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT
        SUM(CASE WHEN R.SUMQTE < 5001 THEN 1 ELSE 0 END) AS "[0,5000]",
        SUM(CASE WHEN R.SUMQTE BETWEEN 5001 AND 10000 THEN 1 ELSE 0 END) AS "]5000, 10000]",
        SUM(CASE WHEN R.SUMQTE BETWEEN 10001 AND 15000 THEN 1 ELSE 0 END) AS "]10000, 15000]",
        SUM(CASE WHEN R.SUMQTE > 15001 THEN 1 ELSE 0 END) AS "]15000, +infini["
    FROM (
        SELECT c.nomCategorie, SUM(n.quantite) as SUMQTE
        FROM fNbProduitsVendus n JOIN dModele mo ON n.idModele=mo.idModele
        JOIN dCategorie c ON mo.idCategorie=c.idCategorie
        GROUP BY c.nomCategorie
    ) AS R
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q7_resultat.csv' DELIMITER ',' CSV HEADER;
*/