# td14_ex3.py
from dataclasses import dataclass, field
from typing import Self # Permet de référencer la classe elle-même

# ----------------------------------------------------
# 1. CLASSE PRODUIT avec Méthodes Statiques
# ----------------------------------------------------

@dataclass
class Produit:
    """
    Représente un produit avec des méthodes statiques pour la validation 
    et le formatage des données.
    """
    nom: str
    prix_ht: float
    taux_tva: float = 0.2

    # --- Méthodes Statiques pour la Validation et l'Utilitaire ---

    @staticmethod
    def est_prix_valide(prix: float) -> bool:
        """Renvoie True si le prix est valide (>= 0)."""
        return prix >= 0

    @staticmethod
    def format_euro(montant: float) -> str:
        """Formate un montant en chaîne de caractères avec 2 décimales et le symbole euro."""
        # Utilisation des f-strings pour un formatage lisible
        return f"{montant:.2f} €"

    # --- __post_init__ (Utilise la méthode statique de validation) ---

    def __post_init__(self):
        """
        Normalisation et validation des données après l'initialisation.
        """
        self.nom = self.nom.strip()
        
        # Validation du prix HT en utilisant la méthode statique
        if not Produit.est_prix_valide(self.prix_ht):
            raise ValueError(
                f"Le prix HT doit être positif ou nul. Reçu : {self.prix_ht}"
            )
            
        if not (0 <= self.taux_tva <= 1):
            raise ValueError(
                f"Le taux de TVA doit être entre 0 et 1 (0% et 100%). Reçu : {self.taux_tva}"
            )

    # --- Méthodes d'Instance ---

    def prix_ttc(self):
        """Calcule et renvoie le prix TTC du produit."""
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self):
        """
        Redéfinit l'affichage lisible de l'objet, en utilisant la méthode statique
        pour formater les montants.
        """
        prix_ht_str = Produit.format_euro(self.prix_ht)
        prix_ttc_str = Produit.format_euro(self.prix_ttc())
        
        return (f"Produit {self.nom} "
                f"– {prix_ht_str} HT "
                f"– {prix_ttc_str} TTC "
                f"(TVA: {self.taux_tva * 100:.0f}%)")

# ----------------------------------------------------
# 2. DÉMONSTRATION
# ----------------------------------------------------

if __name__ == "__main__":
    
    print("--- A. Test des Méthodes Statiques directes ---")
    
    # Test de la validation
    print(f"Prix 10 est valide ? {Produit.est_prix_valide(10)}")
    print(f"Prix -5 est valide ? {Produit.est_prix_valide(-5)}")
    
    # Test du formatage
    print(f"Formatage de 123.456 : {Produit.format_euro(123.456)}")
    print(f"Formatage de 7.9 : {Produit.format_euro(7.9)}")
    
    print("\n--- B. Création et affichage des produits (vérification __str__) ---")
    
    # Produit avec prix nul (valide selon est_prix_valide)
    p_service = Produit("Support 1h", 0.00, taux_tva=0.2)
    print(f"P Service : {p_service}") 
        
    # Produit normal avec espaces (vérifie la normalisation et le formatage)
    p_livre = Produit(" Livre Python ", 49.99, taux_tva=0.055)
    print(f"P Livre   : {p_livre}") 
    
    print("\n--- C. Test de la Validation dans __post_init__ ---")
    
    # Cas invalide (Prix < 0)
    try:
        # Cette tentative devrait appeler __post_init__ qui utilise est_prix_valide
        Produit("Erreur Prix", -1.00)
    except ValueError as e:
        print(f"Erreur attrapée (Prix < 0) : {e}")
