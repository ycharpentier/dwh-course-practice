CREATE TABLE dCategorie(
    idCategorie VARCHAR(100) PRIMARY KEY,
    nomCategorie VARCHAR(1000)
);

CREATE TABLE dModele(
    idModele VARCHAR(100) PRIMARY KEY,
    nomModele VARCHAR(1000),
    idCategorie VARCHAR(100),
    FOREIGN KEY (idCategorie) REFERENCES Categorie(idCategorie) ON DELETE CASCADE
);

CREATE TABLE dPays(
    idPays VARCHAR(100) PRIMARY KEY,
    nomPays VARCHAR(1000),
    supPays NUMERIC
);

CREATE TABLE dVille(
    idVille VARCHAR(100) PRIMARY KEY,
    nomVille VARCHAR(1000),
    supVille NUMERIC,
    idPays VARCHAR(100),
    FOREIGN KEY (idPays) REFERENCES Pays(idPays) ON DELETE CASCADE
);

CREATE TABLE dMagasin(
    idMagasin VARCHAR(100) PRIMARY KEY,
    nomMagasin VARCHAR(1000),
    idVille VARCHAR(100),
    FOREIGN KEY (idVille) REFERENCES Ville(idVille) ON DELETE CASCADE
);

CREATE TABLE fNbProduitsVendus(
    idTemps DATE,
    idMagasin VARCHAR(100),
    idModele VARCHAR(100),
    montant NUMERIC,
    quantite NUMERIC,
    PRIMARY KEY (idTemps, idMagasin, idModele),
    FOREIGN KEY (idMagasin) REFERENCES Magasin(idMagasin) ON DELETE CASCADE,
    FOREIGN KEY (idModele) REFERENCES Modele(idModele) ON DELETE CASCADE
);