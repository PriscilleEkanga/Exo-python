class Produit:
    def __init__(self, nom: str, prix_ht: float, stock: int):
        """
        Initialise un produit avec son nom, son prix HT et son stock.
        """
        self.nom = nom
        self.prix_ht = prix_ht
        self.stock = stock

    def prix_ttc(self, taux_tva: float) -> float:
        """
        Calcule le prix TTC du produit selon le taux de TVA donné.
        """
        return self.prix_ht * (1 + taux_tva)

    def valeur_stock_ttc(self, taux_tva: float) -> float:
        """
        Calcule la valeur totale du stock TTC pour ce produit.
        """
        return self.prix_ttc(taux_tva) * self.stock


if __name__ == "__main__":
    # Taux de TVA
    TVA = 0.2  # 20%

    # Création des produits
    p1 = Produit("Clavier", 49.99, 10)
    p2 = Produit("Souris", 19.99, 25)
    p3 = Produit("Écran", 149.99, 5)

    # Catalogue
    catalogue = [p1, p2, p3]

    # Affichage des informations et calcul total
    total_stock_ttc = 0.0

    for produit in catalogue:
        prix_ttc = produit.prix_ttc(TVA)
        valeur_stock = produit.valeur_stock_ttc(TVA)
        total_stock_ttc += valeur_stock

        print(f"Produit : {produit.nom}")
        print(f"  Prix HT : {produit.prix_ht:.2f} €")
        print(f"  Prix TTC : {prix_ttc:.2f} €")
        print(f"  Stock : {produit.stock}")
        print(f"  Valeur stock TTC : {valeur_stock:.2f} €")
        print("-" * 40)

    print(f"Valeur totale du stock TTC : {total_stock_ttc:.2f} €")
