CREATE TABLE Categorie (
    idCategorie VARCHAR(100) PRIMARY KEY,
    nomCategorie VARCHAR(1000)
);

CREATE TABLE Pays (
    idPays VARCHAR(100) PRIMARY KEY,
    nomPays VARCHAR(1000),
    supPays NUMERIC
);

CREATE TABLE Ville (
    idVille VARCHAR(100) PRIMARY KEY,
    nomVille VARCHAR(1000),
    supVille NUMERIC,
    idPays VARCHAR(100),
    FOREIGN KEY (idPays) REFERENCES Pays(idPays) ON DELETE CASCADE
);

CREATE TABLE Client (
    idClient VARCHAR(100) PRIMARY KEY,
    nomClient VARCHAR(1000),
    naissanceClient DATE,
    idVille VARCHAR(100),
    FOREIGN KEY (idVille) REFERENCES Ville(idVille) ON DELETE CASCADE
);

CREATE TABLE Usine (
    idUsine VARCHAR(100) PRIMARY KEY,
    nomUsine VARCHAR(1000),
    idVille VARCHAR(100),
    FOREIGN KEY (idVille) REFERENCES Ville(idVille) ON DELETE CASCADE
);

CREATE TABLE Marque (
    idMarque VARCHAR(100) PRIMARY KEY,
    nomMarque VARCHAR(1000),
    idPays VARCHAR(100),
    FOREIGN KEY (idPays) REFERENCES Pays(idPays) ON DELETE CASCADE
);

CREATE TABLE Modele (
    idModele VARCHAR(100) PRIMARY KEY,
    nomModele VARCHAR(1000),
    idMarque VARCHAR(100),
    idCategorie VARCHAR(100),
    FOREIGN KEY (idMarque) REFERENCES Marque(idMarque) ON DELETE CASCADE,
    FOREIGN KEY (idCategorie) REFERENCES Categorie(idCategorie) ON DELETE CASCADE
);

CREATE TABLE Produit (
    idProduit VARCHAR(100) PRIMARY KEY,
    idModele VARCHAR(100),
    FOREIGN KEY (idModele) REFERENCES Modele(idModele) ON DELETE CASCADE
);

CREATE TABLE Fabrication (
    idProduit VARCHAR(100),
    idUsine VARCHAR(100),
    dateFabrication DATE,
    coutFabrication NUMERIC,
    PRIMARY KEY (idProduit, idUsine),
	FOREIGN KEY (idProduit) REFERENCES Produit(idProduit) ON DELETE CASCADE,
    FOREIGN KEY (idUsine) REFERENCES Usine(idUsine) ON DELETE CASCADE
);

CREATE TABLE Magasin (
    idMagasin VARCHAR(100) PRIMARY KEY,
    nomMagasin VARCHAR(1000),
    idVille VARCHAR(100),
    FOREIGN KEY (idVille) REFERENCES Ville(idVille) ON DELETE CASCADE
);

CREATE TABLE PaysHabitant (
    idPays VARCHAR(100),
    annee NUMERIC,
    nbHabitant NUMERIC,
    PRIMARY KEY (idPays, annee),
    FOREIGN KEY (idPays) REFERENCES Pays(idPays) ON DELETE CASCADE
);

CREATE TABLE Vente (
    idVente VARCHAR(100) PRIMARY KEY,
    idMagasin VARCHAR(100),
    idClient VARCHAR(100),
    dateVente DATE,
    satisfactionClient NUMERIC,
    FOREIGN KEY (idMagasin) REFERENCES Magasin(idMagasin) ON DELETE CASCADE,
    FOREIGN KEY (idClient) REFERENCES Client(idClient) ON DELETE CASCADE
);

CREATE TABLE VenteProduit (
    idVente VARCHAR(100),
    idProduit VARCHAR(100),
    prixVente NUMERIC,
    dateLivraison DATE,
    PRIMARY KEY (idVente, idProduit),
    FOREIGN KEY (idVente) REFERENCES Vente(idVente) ON DELETE CASCADE,
    FOREIGN KEY (idProduit) REFERENCES Produit(idProduit) ON DELETE CASCADE
);