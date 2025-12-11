
#Exercices: Fonctiosn

def est_pair(n):
    if n % 2 == 0:
        return True
    else:
        return False


def calculer_tva(prix_ht, taux):
    tva = prix_ht * taux / 100
    prix_ttc = prix_ht + tva
    return prix_ttc


def moyenne(liste_nombres):
    total = 0
    for n in liste_nombres:
        total = total + n
    return total / len(liste_nombres)


# Bloc principal
if __name__ == "__main__":

    # Tests de est_pair
    print("est_pair(4) ->", est_pair(4))
    print("est_pair(7) ->", est_pair(7))

    # Tests de calculer_tva
    print("TTC pour 100€ à 20% :", calculer_tva(100, 20))
    print("TTC pour 50€ à 10%  :", calculer_tva(50, 10))

    # Tests de moyenne
    liste1 = [10, 20, 30]
    liste2 = [5.5, 8.2, 3.1, 12.0]

    print("Moyenne de", liste1, "=", moyenne(liste1))
    print("Moyenne de", liste2, "=", moyenne(liste2))
