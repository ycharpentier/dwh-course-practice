SELECT m.nomModele, COUNT(vp.idProduit) AS nbVentes
FROM Modele m
JOIN Produit p ON m.idModele = p.idModele
JOIN VenteProduit vp ON p.idProduit = vp.idProduit
GROUP BY m.nomModele
ORDER BY nbVentes DESC
LIMIT 1;