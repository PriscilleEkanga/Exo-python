# td14_ex1.py
from dataclasses import dataclass

@dataclass
class Produit:
    """
    Représente un produit avec un prix HT et un taux de TVA,
    incluant la validation des contraintes métier via __post_init__.
    """
    nom: str
    prix_ht: float
    taux_tva: float = 0.2  # Valeur par défaut de 20%

    def __post_init__(self):
        """
        Appelée juste après l'initialisation générée par @dataclass.
        Utilisée ici pour la normalisation et la validation des données.
        """
        
        # 1. Normalisation du nom (supprimer les espaces inutiles)
        self.nom = self.nom.strip()
        
        # 2. Validation des contraintes métier
        if self.prix_ht <= 0:
            raise ValueError(f"Le prix HT doit être positif. Reçu : {self.prix_ht}")
            
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(
                f"Le taux de TVA doit être entre 0 et 1 (0% et 100%). Reçu : {self.taux_tva}"
            )

    def prix_ttc(self):
        """
        Calcule et renvoie le prix TTC du produit.
        """
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self):
        """
        Redéfinit l'affichage lisible de l'objet (utilisé par print()).
        """
        prix_ttc = self.prix_ttc()
        # Formattage avec 2 décimales pour les prix
        return (f"Produit {self.nom} "
                f"– {self.prix_ht:.2f} € HT "
                f"– {prix_ttc:.2f} € TTC "
                f"(TVA: {self.taux_tva * 100:.0f}%)")


if __name__ == "__main__":
    
    print("--- 1. Création et affichage des produits valides ---")
    
    # 1a. Produit avec espaces (normalisation via __post_init__)
    try:
        p1 = Produit(" Clavier Mécanique ", 120.00)
        print(f"P1 (Normalisé) : {p1}") 
    except ValueError as e:
        print(f"Erreur inattendue : {e}")
        
    # 1b. Produit avec TVA personnalisée
    try:
        p2 = Produit("Aliment", 10.00, taux_tva=0.055)
        print(f"P2 (TVA 5.5%)  : {p2}") 
    except ValueError as e:
        print(f"Erreur inattendue : {e}")

    # 1c. Produit avec TVA par défaut
    try:
        p3 = Produit("Écran", 350.50)
        print(f"P3 (TVA 20%)   : {p3}") 
    except ValueError as e:
        print(f"Erreur inattendue : {e}")
    
    print("\n--- 2. Test des cas invalides (Validation __post_init__) ---")
    
    # Cas 2a : Prix HT négatif
    try:
        Produit("Service", -5.00)
    except ValueError as e:
        print(f"Erreur attrapée (Prix < 0) : {e}")
        
    # Cas 2b : Taux de TVA trop élevé
    try:
        Produit("Luxe", 500.00, taux_tva=1.5)
    except ValueError as e:
        print(f"Erreur attrapée (TVA > 1) : {e}")