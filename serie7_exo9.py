import csv

revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        revenu = float(ligne[3])
        revenus.append(revenu)

def moyenne_mobile(liste_valeurs, fenetre):
    resultat = []
    for i in range(len(liste_valeurs)):
        if i < fenetre - 1:
            resultat.append(None)  # pas assez de données
        else:
            bloc = liste_valeurs[i-fenetre+1 : i+1]
            resultat.append(sum(bloc) / fenetre)
    return resultat

mm3 = moyenne_mobile(revenus, 3)

import matplotlib.pyplot as plt

jours = list(range(1, len(revenus) + 1))  # simple index 1,2,3,... pour l'axe X

plt.plot(jours, revenus, marker="o", label="Revenus")
plt.plot(jours, mm3, linestyle="--", label="Moyenne mobile (3 jours)")

plt.title("Revenus journaliers + moyenne mobile")
plt.xlabel("Jour")
plt.ylabel("Revenu (€)")
plt.legend()
plt.tight_layout()
plt.show()
