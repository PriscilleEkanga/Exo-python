class CompteBancaire:
    def __init__(self, titulaire: str):
        """
        Initialise un compte bancaire avec un titulaire et un solde à 0.
        """
        self.titulaire = titulaire
        self.solde = 0.0

    def deposer(self, montant: float):
        """
        Dépose un montant positif sur le compte.
        """
        if montant <= 0:
            print("Erreur : le montant à déposer doit être positif.")
            return
        self.solde += montant
        print(f"Dépôt de {montant:.2f} € effectué. Nouveau solde : {self.solde:.2f} €")

    def retirer(self, montant: float):
        """
        Retire un montant du compte si le solde est suffisant.
        """
        if montant <= 0:
            print("Erreur : le montant à retirer doit être positif.")
            return
        if montant > self.solde:
            print("Erreur : solde insuffisant pour ce retrait.")
            return
        self.solde -= montant
        print(f"Retrait de {montant:.2f} € effectué. Nouveau solde : {self.solde:.2f} €")

    def afficher(self):
        """
        Affiche le titulaire du compte et le solde actuel.
        """
        print(f"Titulaire : {self.titulaire}")
        print(f"Solde actuel : {self.solde:.2f} €")
        print("-" * 30)

if __name__ == "__main__":
    # Création du compte
    compte_alice = CompteBancaire("Alice")

    # Dépôts
    compte_alice.deposer(100)
    compte_alice.deposer(50)

    # Retraits
    compte_alice.retirer(30)
    compte_alice.retirer(150)  # solde insuffisant
    compte_alice.retirer(-10)  # montant négatif

    # Affichage final
    compte_alice.afficher()
