# 1️⃣ Import de matplotlib
import matplotlib.pyplot as plt

# 2️⃣ Données
jours = [1, 2, 3, 4, 5, 6, 7]
trafic = [1200, 1350, 900, 1500, 1700, 1600, 1800]

# 3️⃣ Tracer la première courbe avec des points ronds
plt.plot(jours, trafic, marker="o", color="blue", label="Trafic")  # marker="o" : point rond
plt.title("Trafic du site sur 7 jours")
plt.xlabel("Jour")
plt.ylabel("Nombre de visites")
plt.grid(True)
plt.legend()  # affiche la légende
plt.show()

# 4️⃣ Bonus : tracer une deuxième courbe avec des marqueurs carrés
plt.plot(jours, trafic, marker="s", color="green", linestyle="--", label="Trafic (marqueur carré)")
plt.title("Trafic du site sur 7 jours - Marqueurs carrés")
plt.xlabel("Jour")
plt.ylabel("Nombre de visites")
plt.grid(True)
plt.legend()
plt.show()
