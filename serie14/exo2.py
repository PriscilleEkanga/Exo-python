# td14_ex2.py
from dataclasses import dataclass, field

# ----------------------------------------------------
# 1. CLASSE PRODUIT (Recopiée/Importée de td14_ex1.py)
# ----------------------------------------------------

@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2

    def __post_init__(self):
        # Normalisation et validation
        self.nom = self.nom.strip()
        if self.prix_ht <= 0:
            raise ValueError(f"Le prix HT doit être positif. Reçu : {self.prix_ht}")
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(f"Le taux de TVA doit être entre 0 et 1. Reçu : {self.taux_tva}")

    def prix_ttc(self):
        return self.prix_ht * (1 + self.taux_tva)

# ----------------------------------------------------
# 2. CLASSE LIGNEFACTURE
# ----------------------------------------------------

@dataclass
class LigneFacture:
    """
    Représente une ligne sur une facture.
    Les totaux HT et TTC sont calculés automatiquement dans __post_init__.
    """
    produit: Produit
    quantite: int
    
    # Champs dérivés : Ne doivent pas être passés au constructeur
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        """
        Vérifie la contrainte métier et calcule les totaux.
        """
        # 1. Validation de la quantité
        if self.quantite <= 0:
            raise ValueError(f"La quantité doit être strictement positive. Reçu : {self.quantite}")

        # 2. Calcul des champs dérivés
        # total_ht : basé sur le prix HT du produit
        self.total_ht = self.quantite * self.produit.prix_ht
        
        # total_ttc : basé sur le prix TTC calculé via la méthode de l'objet Produit
        self.total_ttc = self.quantite * self.produit.prix_ttc()
        
    def __str__(self):
        """
        Renvoie un affichage lisible de la ligne de facture.
        """
        # Formattage pour l'affichage (deux décimales pour les montants)
        return (f"{self.quantite} x {self.produit.nom} "
                f"({self.produit.prix_ht:.2f} € HT/u) "
                f"– Total HT: {self.total_ht:.2f} € "
                f"– Total TTC: {self.total_ttc:.2f} €")

# ----------------------------------------------------
# 3. DÉMONSTRATION
# ----------------------------------------------------

if __name__ == "__main__":
    
    # 3a. Création des produits de base
    
    # Prix HT : 120.00, TVA 20% -> TTC : 144.00
    p_clavier = Produit("Clavier Mécanique", 120.00) 
    
    # Prix HT : 10.00, TVA 5.5% -> TTC : 10.55
    p_aliment = Produit("Aliment Bio", 10.00, taux_tva=0.055)
    
    # Prix HT : 350.50, TVA 20% -> TTC : 420.60
    p_ecran = Produit("Écran", 350.50)
    
    print("--- Lignes de Facture Valides ---")

    try:
        # Ligne 1 : 2 Claviers
        # HT : 2 * 120.00 = 240.00
        # TTC : 2 * 144.00 = 288.00
        ligne1 = LigneFacture(p_clavier, 2)
        print(f"Ligne 1 : {ligne1}")
        
        # Ligne 2 : 5 Aliments (TVA différente)
        # HT : 5 * 10.00 = 50.00
        # TTC : 5 * 10.55 = 52.75
        ligne2 = LigneFacture(p_aliment, 5)
        print(f"Ligne 2 : {ligne2}")

        # Ligne 3 : 1 Écran
        ligne3 = LigneFacture(p_ecran, 1)
        print(f"Ligne 3 : {ligne3}")
        
        # Vérification des totaux (optionnel mais utile)
        print(f"\nVérification Ligne 1 : total_ht={ligne1.total_ht:.2f}, total_ttc={ligne1.total_ttc:.2f}")

    except ValueError as e:
        print(f"Erreur inattendue : {e}")
        
    print("\n--- Test Cas Invalide (quantité <= 0) ---")

    # Cas 4 : Quantité invalide
    try:
        LigneFacture(p_clavier, 0)
    except ValueError as e:
        print(f"Erreur attrapée (Quantité 0) : {e}")

    try:
        LigneFacture(p_clavier, -3)
    except ValueError as e:
        print(f"Erreur attrapée (Quantité négative) : {e}")