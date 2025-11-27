import math

# --- 1. Définition de la classe Produit ---
class Produit:
    """
    Modélise un produit avec ses propriétés de base.
    """
    def __init__(self, id, nom, categorie, prix, stock):
        """
        Constructeur de la classe Produit.

        Args:
            id (int): Identifiant unique du produit.
            nom (str): Nom du produit.
            categorie (str): Catégorie à laquelle appartient le produit.
            prix (float): Prix unitaire du produit.
            stock (int): Quantité disponible en stock.
        """
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock

    def est_en_rupture(self):
        """
        Vérifie si le produit est en rupture de stock.

        Returns:
            bool: True si le stock est égal à 0, False sinon.
        """
        return self.stock == 0

    def afficher_resume(self):
        """
        Affiche un résumé formaté du produit.
        Format : [Catégorie] Nom - Prix€ (stock: X)
        """
        statut_stock = f"stock: {self.stock}"
        if self.est_en_rupture():
            statut_stock = "EN RUPTURE"

        # Utilisation de f-string pour un formatage clair et précis
        print(f"[{self.categorie}] {self.nom} - {self.prix:.2f}€ ({statut_stock})")


# --- 2. Définition de la classe Catalogue ---
class Catalogue:
    """
    Gère une collection d'objets Produit.
    """
    def __init__(self):
        """
        Constructeur de la classe Catalogue. Initialise la liste des produits.
        """
        self.produits = []

    def ajouter_produit(self, produit):
        """
        Ajoute un objet Produit au catalogue.

        Args:
            produit (Produit): L'objet Produit à ajouter.
        """
        self.produits.append(produit)

    def produits_par_categorie(self, categorie):
        """
        Filtre et renvoie la liste des produits d'une catégorie donnée.

        Args:
            categorie (str): Le nom de la catégorie à filtrer.

        Returns:
            list[Produit]: Liste des produits correspondant à la catégorie.
        """
        # Utilisation d'une compréhension de liste pour un filtrage efficace
        return [p for p in self.produits if p.categorie == categorie]

    def prix_moyen(self):
        """
        Calcule le prix moyen de tous les produits du catalogue.

        Returns:
            float: Le prix moyen. 0.0 si le catalogue est vide.
        """
        if not self.produits:
            return 0.0

        somme_prix = sum(p.prix for p in self.produits)
        return somme_prix / len(self.produits)

    def produits_en_rupture(self):
        """
        Renvoie la liste des produits actuellement en rupture de stock.

        Returns:
            list[Produit]: Liste des produits dont le stock est égal à 0.
        """
        # Utilisation de la méthode est_en_rupture() de la classe Produit
        return [p for p in self.produits if p.est_en_rupture()]


# --- 3. Données brutes ---
donnees_produits = [
    {"id": 1, "nom": "Clavier",  "categorie": "Informatique", "prix": 39.99, "stock": 10},
    {"id": 2, "nom": "Souris",   "categorie": "Informatique", "prix": 19.99, "stock": 0},
    {"id": 3, "nom": "Écran",    "categorie": "Informatique", "prix": 129.90, "stock": 5},
    {"id": 4, "nom": "Chaise",   "categorie": "Bureau",       "prix": 89.90, "stock": 2}
]


# --- 4. Bloc principal d'exécution ---
if __name__ == "__main__":
    print("--- Initialisation du Catalogue ---")
    catalogue = Catalogue()

    # Convertir chaque dictionnaire en objet Produit et les ajouter au Catalogue
    for data in donnees_produits:
        # L'opérateur **data permet de passer tous les éléments du dictionnaire
        # comme arguments nommés au constructeur Produit.__init__
        produit_obj = Produit(**data)
        catalogue.ajouter_produit(produit_obj)
        print(f"Produit ajouté : {produit_obj.nom}")


    # --- Tests des fonctionnalités ---

    print("\n--- 1. Affichage du Prix Moyen ---")
    prix_moyen_cat = catalogue.prix_moyen()
    # Affichage avec deux décimales
    print(f"Le prix moyen des produits dans le catalogue est de : {prix_moyen_cat:.2f}€")

    print("\n--- 2. Produits en Rupture de Stock ---")
    ruptures = catalogue.produits_en_rupture()
    if ruptures:
        print(f"Nombre de produits en rupture : {len(ruptures)}")
        for p in ruptures:
            p.afficher_resume()
    else:
        print("Aucun produit n'est actuellement en rupture de stock.")

    print('\n--- 3. Produits de la catégorie "Informatique" ---')
    produits_info = catalogue.produits_par_categorie("Informatique")

    if produits_info:
        print(f"Nombre de produits 'Informatique' : {len(produits_info)}")
        for p in produits_info:
            p.afficher_resume()
    else:
        print("Aucun produit trouvé dans cette catégorie.")

    print("\n--- 4. Démonstration de l'affichage résumé (avec un produit) ---")
    # On choisit le premier produit du catalogue pour la démonstration
    p1 = catalogue.produits[0]
    p1.afficher_resume()
    
    # Démonstration du produit en rupture (Souris)
    p_souris = catalogue.produits_par_categorie("Informatique")[1] 
    p_souris.afficher_resume()