# td13_ex1.py

class Produit:
    """
    Représente un produit avec un prix HT, en utilisant un taux de TVA
    qui est un attribut de classe, partagé par toutes les instances.
    """
    # Attribut de classe : Partagé par tous les objets Produit.
    # Représente le taux de TVA standard (20% ou 0.2)
    taux_tva = 0.20

    def __init__(self, nom, prix_ht):
        """
        Initialise un nouveau produit.
        """
        # Vérification de la contrainte : prix_ht doit être positif
        if prix_ht <= 0:
            raise ValueError("Le prix HT doit être strictement positif.")
        
        # Attributs d'instance : Spécifiques à chaque produit
        self.nom = nom
        self.prix_ht = prix_ht

    def prix_ttc(self):
        """
        Calcule et renvoie le prix TTC en utilisant le taux_tva de la classe.
        Le taux_tva est accédé via self.taux_tva ou Produit.taux_tva.
        """
        # On accède à l'attribut de classe via 'self'
        return self.prix_ht * (1 + self.taux_tva)

def afficher_produit(produit):
    """Fonction utilitaire pour afficher les détails du produit."""
    print(f"Produit : {produit.nom:<10} | HT: {produit.prix_ht:>6.2f} € | TTC: {produit.prix_ttc():>6.2f} €")

if __name__ == "__main__":
    
    # 1. Création de deux produits
    print("--- Phase 1 : Taux de TVA initial (20%) ---")
    
    p1 = Produit("Ordinateur", 1000.00)
    p2 = Produit("Souris", 20.00)
    
    print(f"Taux de TVA (Classe) : {Produit.taux_tva:.2f}")
    afficher_produit(p1)
    afficher_produit(p2)
    
    # --- 2. Modification de l'attribut de classe ---
    
    # Simuler une baisse de TVA (de 20% à 10%)
    Produit.taux_tva = 0.10
    
    print("\n--- Phase 2 : Changement du Taux de TVA (10%) ---")
    print(f"Nouveau Taux de TVA (Classe) : {Produit.taux_tva:.2f}")

    # 3. Observation de l'effet sur les instances existantes
    print("\nEffet sur les instances existantes :")
    afficher_produit(p1)
    afficher_produit(p2)
    
    # Création d'un nouveau produit après le changement
    p3 = Produit("Clavier", 50.00)
    print("\nNouvelle instance créée après le changement :")
    afficher_produit(p3)
    
    # Observation des attributs (Indice)
    print("\n--- Observation des références ---")
    print(f"Produit.taux_tva : {Produit.taux_tva}")
    print(f"p1.taux_tva      : {p1.taux_tva} (accède à la classe)")
    print(f"p3.taux_tva      : {p3.taux_tva} (accède à la classe)")