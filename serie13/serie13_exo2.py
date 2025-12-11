# td13_ex2.py

class StockProduit:
    """
    Gère le stock d'un produit en protégeant l'accès direct au stock
    pour garantir que le stock ne soit jamais négatif.
    """
    
    def __init__(self, nom, stock_initial=0):
        """
        Initialise le produit avec un nom et un stock initial.
        """
        if stock_initial < 0:
            raise ValueError("Le stock initial ne peut pas être négatif.")
            
        # Attribut d'instance public
        self.nom = nom
        
        # Attribut d'instance "privé" (par convention Python, préfixé par '_')
        # L'utilisation de ce préfixe indique aux développeurs qu'il ne faut pas
        # y accéder directement de l'extérieur.
        self._stock = stock_initial

    def ajouter(self, qte):
        """
        Ajoute une quantité au stock.
        """
        if qte <= 0:
            raise ValueError("La quantité à ajouter doit être positive.")
            
        self._stock += qte
        print(f"INFO: {qte} unités ajoutées à {self.nom}. Nouveau stock : {self._stock}")

    def retirer(self, qte):
        """
        Retire une quantité du stock, avec vérification de la disponibilité.
        """
        if qte <= 0:
            raise ValueError("La quantité à retirer doit être positive.")
            
        # Règle métier (cohérence) : on ne peut pas retirer plus que le stock disponible
        if qte > self._stock:
            raise ValueError(
                f"Stock insuffisant pour retirer {qte} unités de {self.nom} (Stock actuel : {self._stock})"
            )
            
        self._stock -= qte
        print(f"INFO: {qte} unités retirées de {self.nom}. Nouveau stock : {self._stock}")

    def afficher_stock(self):
        """
        Affiche l'état actuel du stock.
        """
        print(f"\n--- État du Stock de {self.nom} ---\nStock actuel : {self._stock} unités")

if __name__ == "__main__":
    
    # 1. Création de l'instance
    clavier_stock = StockProduit("Clavier", 10)
    clavier_stock.afficher_stock()
    
    # --- Scénario Normal ---
    print("\n--- Scénario 1 : Opérations valides ---")
    
    clavier_stock.ajouter(5)
    clavier_stock.retirer(3)
    clavier_stock.afficher_stock()
    
    # --- Scénario Exception ---
    print("\n--- Scénario 2 : Retrait impossible (cohérence métier) ---")
    
    try:
        # Tente de retirer 15 unités, alors que le stock n'est que de 12 (10 + 5 - 3)
        clavier_stock.retirer(15)
    except ValueError as e:
        print(f"ERREUR ATTENDUE : {e}")
        
    clavier_stock.afficher_stock()
    
    # --- Démonstration du danger (ATTENTION : MAUVAISE PRATIQUE) ---
    print("\n--- Scénario 3 : Danger de la modification directe de l'attribut interne ---")
    
    # Le stock est actuellement de 12.
    print(f"Stock avant modification directe : {clavier_stock._stock}")
    
    try:
        # En contournant la méthode 'retirer', on viole la règle métier !
        clavier_stock._stock = -100
        print("ALERTE : L'attribut interne a été modifié directement, violant la cohérence métier.")
    except Exception as e:
        # Normalement, cela ne lève aucune exception car c'est une simple affectation.
        print(f"Erreur inattendue : {e}")

    clavier_stock.afficher_stock()
    
    # Commentaires expliquant le danger
    print("\n--- Explication des commentaires ---")
    
