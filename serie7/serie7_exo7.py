import csv

revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        revenu = float(ligne[3])
        revenus.append(revenu)

totaux_semaines = []
taille_semaine = 7

for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]   # prend 7 jours
    totaux_semaines.append(sum(bloc))    # somme sur 7 jours

labels_semaines = [f"S{i+1}" for i in range(len(totaux_semaines))]

import matplotlib.pyplot as plt

plt.bar(labels_semaines, totaux_semaines)
plt.title("Chiffre d'affaires total par semaine")
plt.xlabel("Semaines")
plt.ylabel("Revenu total (€)")

plt.show()
