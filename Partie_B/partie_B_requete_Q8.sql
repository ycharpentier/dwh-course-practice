\copy (SELECT DISTINCT DATE_PART('month', n.idTemps) AS month, SUM(n.quantite) OVER (ORDER BY DATE_PART('month', n.idTemps) RANGE UNBOUNDED PRECEDING) AS SUMQTE FROM fNbProduitsVendus n ORDER BY month) TO 'P:/Bureau/5A/dwh-course-practice/partie_B_requete_Q8_resultat.csv' DELIMITER ',' CSV HEADER;

/*
\copy (
    SELECT DISTINCT DATE_PART('month', n.idTemps) AS month,
        SUM(n.quantite) OVER (
            ORDER BY DATE_PART('month', n.idTemps)
            RANGE UNBOUNDED PRECEDING
        ) AS SUMQTE
    FROM fNbProduitsVendus n
    ORDER BY month
) TO 'P:/Bureau/5A/dwh-course-practice/partie_B_requete_Q8_resultat.csv' DELIMITER ',' CSV HEADER;
*/