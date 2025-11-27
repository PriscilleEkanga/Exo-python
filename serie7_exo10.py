import csv
import matplotlib.pyplot as plt

# -----------------------------
# 1. Lecture du CSV
# -----------------------------
dates = []
trafic = []
nb_commandes = []
revenus = []

with open("ventes_journalieres.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    next(lecteur)  # ignorer l'en-tête
    for ligne in lecteur:
        dates.append(ligne[0])
        trafic.append(int(ligne[1]))
        nb_commandes.append(int(ligne[2]))
        revenus.append(float(ligne[3]))

# -----------------------------
# 2. Calcul du CA hebdomadaire (Exercice 7)
# -----------------------------
totaux_semaines = []
taille_semaine = 7
for i in range(0, len(revenus), taille_semaine):
    bloc = revenus[i:i+taille_semaine]
    totaux_semaines.append(sum(bloc))

labels_semaines = [f"S{i+1}" for i in range(len(totaux_semaines))]

# -----------------------------
# 3. Création de la figure avec 2 lignes x 2 colonnes
# -----------------------------
plt.figure(figsize=(12, 8))

# --- (1,1) Courbe du trafic ---
plt.subplot(2, 2, 1)
plt.plot(dates, trafic, marker="o", color="tab:blue")
plt.title("Trafic quotidien")
plt.xticks(rotation=45)
plt.ylabel("Visiteurs")

# --- (1,2) Courbe du revenu ---
plt.subplot(2, 2, 2)
plt.plot(dates, revenus, marker="o", color="tab:green")
plt.title("Revenu quotidien")
plt.xticks(rotation=45)
plt.ylabel("Revenu (€)")

# --- (2,1) Histogramme des revenus ---
plt.subplot(2, 2, 3)
plt.hist(revenus, bins=7, color="tab:orange", edgecolor="black")
plt.title("Distribution des revenus")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence")

# --- (2,2) Barres du CA hebdomadaire ---
plt.subplot(2, 2, 4)
plt.bar(labels_semaines, totaux_semaines, color="tab:red", edgecolor="black")
plt.title("CA hebdomadaire")
plt.xlabel("Semaines")
plt.ylabel("Revenu total (€)")

# -----------------------------
# 4. Titre global et ajustement
# -----------------------------
plt.suptitle("Tableau de bord e-commerce", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])  # laisse de la place pour le suptitle

# -----------------------------
# 5. Sauvegarde en image (bonus)
# -----------------------------
plt.savefig("dashboard.png")
plt.show()
