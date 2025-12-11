def appliquer_remise(prix: float, remise: float) -> float:
    """
    Calcule le prix final après application d'une remise.

    :param prix: (float) prix initial du produit.
    :param remise: (float) remise sous forme décimale (ex: 0.2 = 20%).
    :return: (float) prix après remise.

    Exemple :
    >>> appliquer_remise(100, 0.2)
    80.0
    """
    prix_final = prix * (1 - remise)
    return prix_final


def compter_commandes_superieures(commandes: list[float], seuil: float) -> int:
    """
    Compte combien de montants dans la liste sont supérieurs ou égaux à un seuil.

    :param commandes: (list[float]) liste de montants de commandes.
    :param seuil: (float) montant minimum à considérer.
    :return: (int) nombre de commandes >= seuil.

    Exemple :
    >>> compter_commandes_superieures([10, 50, 70], 40)
    2
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur


def normaliser_email(email: str) -> str:
    """
    Normalise une adresse email en supprimant les espaces et en mettant en minuscule.

    :param email: (str) adresse email à nettoyer.
    :return: (str) email normalisé.

    Exemple :
    >>> normaliser_email("  Test@Example.COM ")
    'test@example.com'
    """
    return email.strip().lower()


# --- Bloc de test ---
if __name__ == "__main__":
    help(appliquer_remise)
    help(compter_commandes_superieures)
    help(normaliser_email)
