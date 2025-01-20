\copy (SELECT DISTINCT DATE_PART('year', n.idTemps) AS year, DATE_PART('month', n.idTemps) AS month, SUM(n.quantite) OVER (ORDER BY DATE_PART('year', n.idTemps), DATE_PART('month', n.idTemps) RANGE UNBOUNDED PRECEDING) AS SUMQTE FROM fNbProduitsVendus n ORDER BY year, month) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q8_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT DISTINCT DATE_PART('year', n.idTemps) AS year, DATE_PART('month', n.idTemps) AS month,
        SUM(n.quantite) OVER (
            ORDER BY DATE_PART('year', n.idTemps), DATE_PART('month', n.idTemps)
            RANGE UNBOUNDED PRECEDING
        ) AS SUMQTE
    FROM fNbProduitsVendus n
    ORDER BY year, month
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B/requete_Q8_resultat.csv' DELIMITER ',' CSV HEADER;
*/