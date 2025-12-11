# td14_ex4.py
from dataclasses import dataclass, field
from typing import List

# ====================================================
# CLASSES PRÉCÉDENTES (Pour rendre le fichier autonome)
# ====================================================

@dataclass
class Produit:
    nom: str
    prix_ht: float
    taux_tva: float = 0.2

    @staticmethod
    def format_euro(montant: float) -> str:
        """Méthode statique pour formater un montant en Euro."""
        return f"{montant:.2f} €"

    def __post_init__(self):
        # ... (Validations omises pour la concision, mais nécessaires en vrai)
        self.nom = self.nom.strip()
        if self.prix_ht <= 0 or not (0 <= self.taux_tva <= 1):
             raise ValueError("Prix ou TVA invalide dans Produit")

    def prix_ttc(self):
        return self.prix_ht * (1 + self.taux_tva)

    def __str__(self):
        return f"Produit {self.nom} – {Produit.format_euro(self.prix_ht)} HT"

@dataclass
class LigneFacture:
    produit: Produit
    quantite: int
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)

    def __post_init__(self):
        if self.quantite <= 0:
            raise ValueError("La quantité doit être positive.")
        self.total_ht = self.quantite * self.produit.prix_ht
        self.total_ttc = self.quantite * self.produit.prix_ttc()
        
    def __str__(self):
        return (f"    - {self.quantite} x {self.produit.nom} | "
                f"HT: {Produit.format_euro(self.total_ht)} "
                f"| TTC: {Produit.format_euro(self.total_ttc)}")

# ====================================================
# 2. DATACLASS FACTURE
# ====================================================

@dataclass
class Facture:
    numero: int
    client: str
    lignes: List[LigneFacture] # Liste d'objets LigneFacture
    
    # Champs dérivés : calculés dans __post_init__
    total_ht: float = field(init=False)
    total_ttc: float = field(init=False)
    
    def _recalculer_totaux(self):
        """Méthode privée pour calculer la somme des totaux des lignes."""
        # Utilisation de la fonction sum() avec des expressions génératrices pour l'efficacité
        self.total_ht = sum(ligne.total_ht for ligne in self.lignes)
        self.total_ttc = sum(ligne.total_ttc for ligne in self.lignes)

    def __post_init__(self):
        """
        Vérifie la contrainte métier (lignes non vides) et calcule les totaux.
        """
        if not self.lignes:
            raise ValueError("La facture doit contenir au moins une ligne.")

        self._recalculer_totaux()
        
    def ajouter_ligne(self, ligne: LigneFacture):
        """
        Ajoute une ligne à la facture et met à jour les totaux globaux.
        """
        self.lignes.append(ligne)
        self._recalculer_totaux() # IMPORTANT : Mettre à jour les champs dérivés

    def __str__(self):
        """
        Redéfinit l'affichage lisible de la facture complète.
        """
        # Création de l'en-tête
        output = f"\n========================================\n"
        output += f"FACTURE N°{self.numero} - Client : {self.client}\n"
        output += f"========================================\n"
        
        # Affichage de chaque ligne (utilise __str__ de LigneFacture)
        for ligne in self.lignes:
            output += f"{str(ligne)}\n"
            
        # Affichage des totaux finaux (utilise la méthode statique format_euro)
        output += f"----------------------------------------\n"
        output += f"TOTAL HT : {Produit.format_euro(self.total_ht)}\n"
        output += f"TOTAL TTC: {Produit.format_euro(self.total_ttc)}\n"
        output += f"========================================\n"
        return output

# ====================================================
# 3. DÉMONSTRATION
# ====================================================

if __name__ == "__main__":
    
    # --- 3.1 Création des objets et de la Facture initiale ---
    
    p1 = Produit("PC Portable", 800.00)   # TTC: 960.00 (TVA 20%)
    p2 = Produit("Assistance", 50.00, 0.055) # TTC: 52.75 (TVA 5.5%)
    
    l1 = LigneFacture(p1, 1) # HT: 800.00, TTC: 960.00
    l2 = LigneFacture(p2, 4) # HT: 200.00, TTC: 211.00
    
    # Création de la facture
    try:
        facture_client_a = Facture(
            numero=2024001,
            client="Alice Dubois",
            lignes=[l1, l2]
        )
        print("--- 1. Facture Initiale ---")
        print(facture_client_a)

        # --- 3.2 Test de l'ajout d'une ligne (méthode d'instance) ---
        
        p3 = Produit("Souris", 20.00) # TTC: 24.00
        l3 = LigneFacture(p3, 2)      # HT: 40.00, TTC: 48.00
        
        facture_client_a.ajouter_ligne(l3)
        
        print("\n--- 2. Facture après Ajout d'une ligne ---")
        print(facture_client_a)
        
        # Vérification des totaux après ajout (doit être mis à jour)
        # Total HT attendu : 800 + 200 + 40 = 1040.00
        print(f"Vérification Total HT : {facture_client_a.total_ht:.2f}")

    except ValueError as e:
        print(f"Erreur inattendue : {e}")

    # --- 3.3 Test du cas invalide (lignes vides) ---
    
    print("\n--- 3. Test de la Facture Invalide (lignes vides) ---")
    
    try:
        Facture(numero=2024002, client="Bob Martin", lignes=[])
    except ValueError as e:
        print(f"Erreur attrapée (Validation __post_init__) : {e}")