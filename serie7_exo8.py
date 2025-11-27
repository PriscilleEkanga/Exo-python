import csv

revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        revenu = float(ligne[3])
        revenus.append(revenu)

import matplotlib.pyplot as plt

plt.boxplot(revenus)
plt.title("Distribution des revenus journaliers")
plt.ylabel("Revenu (€)")
plt.show()

revenus_S1S2 = revenus[:14]   # jours 1 à 14
revenus_S3S4 = revenus[14:28] # jours 15 à 28

plt.boxplot([revenus_S1S2, revenus_S3S4],
            labels=["Semaines 1–2", "Semaines 3–4"])

plt.title("Comparaison des revenus par période")
plt.ylabel("Revenu (€)")
plt.show()
