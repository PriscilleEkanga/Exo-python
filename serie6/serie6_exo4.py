class Employe:
    def __init__(self, nom: str, salaire_base: float):
        """
        Initialise un employé avec son nom et son salaire de base.
        """
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire de base de l'employé.
        """
        return self.salaire_base

    def afficher(self):
        """
        Affiche le nom et le salaire de l'employé.
        """
        print(f"{self.nom} : salaire = {self.calculer_salaire():.2f} €")


class Developpeur(Employe):
    def __init__(self, nom: str, salaire_base: float, prime_technique: float):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire de base + prime technique.
        """
        return self.salaire_base + self.prime_technique


class Manager(Employe):
    def __init__(self, nom: str, salaire_base: float, prime_management: float):
        super().__init__(nom, salaire_base)
        self.prime_management = prime_management

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire de base + prime de management.
        """
        return self.salaire_base + self.prime_management


if __name__ == "__main__":
    # Création des employés
    e1 = Employe("Alice", 2000)
    e2 = Developpeur("Bob", 2200, 300)
    e3 = Manager("Charlie", 2500, 500)
    e4 = Developpeur("Diana", 2100, 400)
    e5 = Manager("Eve", 2400, 600)

    # Stockage dans une liste
    equipe = [e1, e2, e3, e4, e5]

    # Affichage
    for emp in equipe:
        print(f"Type : {type(emp).__name__}")
        print(f"Nom : {emp.nom}")
        print(f"Salaire calculé : {emp.calculer_salaire():.2f} €")
        print("-" * 30)
