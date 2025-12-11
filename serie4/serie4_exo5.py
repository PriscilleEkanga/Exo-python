# 1. Exception personnalisée
class CommandeInvalideError(Exception):
    pass


# 2. Fonction de validation
def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalideError("Le montant doit être supérieur à 0.")
    if montant > 10_000:
        raise CommandeInvalideError("Montant trop élevé : commande suspecte.")
    return True


# 3. Bloc principal
try:
    saisie = input("Montant de la commande : ")
    montant = float(saisie)   # peut déclencher ValueError

    valider_commande(montant)
    print("Commande valide.")

except ValueError:
    print("Erreur : veuillez entrer un nombre valide (ex : 59.99).")

except CommandeInvalideError as e:
    print("Commande refusée :", e)
