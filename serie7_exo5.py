import csv

dates = []
revenus = []
trafic = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        date = ligne[0]
        t = int(ligne[1])
        revenu = float(ligne[3])

        dates.append(date)
        revenus.append(revenu)
        trafic.append(t)

import csv

dates = []
revenus = []
trafic = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        date = ligne[0]
        t = int(ligne[1])
        revenu = float(ligne[3])

        dates.append(date)
        revenus.append(revenu)
        trafic.append(t)

fig, ax1 = plt.subplots()

# Courbe des revenus
ax1.plot(dates, revenus, marker="o")
ax1.set_xlabel("Date")
ax1.set_ylabel("Revenu (€)", color="black")
ax1.tick_params(axis='y', labelcolor="black")
plt.xticks(rotation=45)

# Deuxième axe Y
ax2 = ax1.twinx()
ax2.plot(dates, trafic, linestyle="--")
ax2.set_ylabel("Trafic (visiteurs)", color="black")
ax2.tick_params(axis='y', labelcolor="black")

plt.title("Revenu quotidien + trafic")
plt.tight_layout()
plt.show()
