import matplotlib.pyplot as plt

revenus = [
    1800, 2200, 2500, 2600, 2700, 3000, 3200, 3300, 3500,
    4000, 4200, 4500, 4800, 5000, 5200, 5500, 6000, 6200,
    6500, 7000, 7200, 7500, 8000
]

plt.hist(revenus, bins=7)
plt.title("Distribution des revenus journaliers")
plt.xlabel("Revenu (€)")
plt.ylabel("Fréquence")
plt.show()

plt.hist(revenus, bins=5)
plt.title("5 bins")
plt.show()

plt.hist(revenus, bins=10)
plt.title("10 bins")
plt.show()
