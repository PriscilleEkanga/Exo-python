class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        """
        Initialise un rectangle avec sa largeur et sa hauteur.
        """
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self) -> float:
        """
        Calcule et retourne l'aire du rectangle.
        """
        return self.largeur * self.hauteur

    def perimetre(self) -> float:
        """
        Calcule et retourne le périmètre du rectangle.
        """
        return 2 * (self.largeur + self.hauteur)

    def afficher(self):
        """
        Affiche les informations du rectangle : largeur, hauteur, surface, périmètre.
        """
        print(f"Rectangle {self.largeur} x {self.hauteur}")
        print(f"Surface : {self.surface()}")
        print(f"Périmètre : {self.perimetre()}")
        print("-" * 30)


if __name__ == "__main__":
    r1 = Rectangle(4, 5)
    r2 = Rectangle(10, 2)

    r1.afficher()
    r2.afficher()
