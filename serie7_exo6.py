import csv

dates = []
trafic = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # sauter l'en-tête

    for ligne in lecteur:
        date = ligne[0]
        t = int(ligne[1])
        revenu = float(ligne[3])

        dates.append(date)
        trafic.append(t)
        revenus.append(revenu)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))  # taille globale

# --- Subplot 1 : Trafic ---
plt.subplot(2, 1, 1)   # 2 lignes, 1 colonne, case n°1
plt.plot(dates, trafic, marker="o")
plt.title("Trafic quotidien")
plt.xlabel("")          # on enlève l'étiquette X ici pour éviter la répétition
plt.ylabel("Visiteurs")
plt.xticks(rotation=45)

# --- Subplot 2 : Revenu ---
plt.subplot(2, 1, 2)   # 2 lignes, 1 colonne, case n°2
plt.plot(dates, revenus, marker="o")
plt.title("Revenu quotidien")
plt.xlabel("Date")
plt.ylabel("Revenu (€)")
plt.xticks(rotation=45)

plt.tight_layout()     # ajuste les marges automatiquement
plt.show()
