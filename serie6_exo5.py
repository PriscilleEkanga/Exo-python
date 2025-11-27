class Client:
    def __init__(self, nom: str, email: str):
        """
        Initialise un client avec son nom et son email.
        """
        self.nom = nom
        self.email = email


class LigneCommande:
    def __init__(self, description: str, quantite: int, prix_unitaire: float):
        """
        Initialise une ligne de commande avec description, quantité et prix unitaire.
        """
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def total_ligne(self) -> float:
        """
        Retourne le montant total de la ligne (quantité * prix unitaire).
        """
        return self.quantite * self.prix_unitaire


class Commande:
    def __init__(self, client: Client):
        """
        Initialise une commande pour un client avec une liste de lignes vide.
        """
        self.client = client
        self.lignes = []

    def ajouter_ligne(self, ligne: LigneCommande):
        """
        Ajoute une ligne de commande à la commande.
        """
        self.lignes.append(ligne)

    def total(self) -> float:
        """
        Calcule le montant total de la commande.
        """
        return sum(l.total_ligne() for l in self.lignes)


if __name__ == "__main__":
    # Création du client
    client1 = Client("Alice Dupont", "alice@example.com")

    # Création des lignes de commande
    ligne1 = LigneCommande("Pack 10h de support", 2, 150.0)
    ligne2 = LigneCommande("Formation Python", 1, 300.0)
    ligne3 = LigneCommande("Abonnement annuel", 1, 120.0)

    # Création de la commande
    commande1 = Commande(client1)

    # Ajout des lignes
    commande1.ajouter_ligne(ligne1)
    commande1.ajouter_ligne(ligne2)
    commande1.ajouter_ligne(ligne3)

    # Affichage récapitulatif
    print(f"Commande pour : {commande1.client.nom} ({commande1.client.email})")
    print("Lignes de commande :")
    for ligne in commande1.lignes:
        print(f"- {ligne.description} | Quantité : {ligne.quantite} | "
              f"Prix unitaire : {ligne.prix_unitaire:.2f} € | Total ligne : {ligne.total_ligne():.2f} €")
    print(f"Montant total de la commande : {commande1.total():.2f} €")
