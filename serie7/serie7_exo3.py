import matplotlib.pyplot as plt

# Données sur 8 à 10 jours
trafic = [900, 1100, 1300, 1600, 1750, 1900, 2100, 2400]
revenu = [2200, 2600, 3100, 3600, 4000, 4300, 4800, 5200]

# Nuage de points
plt.scatter(trafic, revenu)

plt.title("Relation entre trafic et revenu")
plt.xlabel("Trafic (visites)")
plt.ylabel("Revenu (€)")

plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

trafic = [900, 1100, 1300, 1600, 1750, 1900, 2100, 2400]
revenu = [2200, 2600, 3100, 3600, 4000, 4300, 4800, 5200]

plt.scatter(trafic, revenu, alpha=0.7)  # alpha = transparence

plt.title("Relation entre trafic et revenu")
plt.xlabel("Trafic (visites)")
plt.ylabel("Revenu (€)")

plt.grid(True)
plt.show()
