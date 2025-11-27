import matplotlib.pyplot as plt

# 1. Catégories
categories = ["Électronique", "Mode", "Maison", "Sport", "Beauté"]

# 2. Chiffres d'affaires correspondants
ca = [12000, 8000, 6000, 4000, 5000]

# 3. Diagramme en barres
plt.bar(categories, ca)

# 4. Titre et labels
plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA (€)")

plt.show()


import matplotlib.pyplot as plt

categories = ["Électronique", "Mode", "Maison", "Sport", "Beauté"]
ca = [12000, 8000, 6000, 4000, 5000]

plt.bar(categories, ca)

plt.title("Chiffre d'affaires par catégorie")
plt.xlabel("Catégorie")
plt.ylabel("CA (€)")

# BONUS : afficher les valeurs au-dessus de chaque barre
for i, valeur in enumerate(ca):
    plt.text(i, valeur + 200, f"{valeur}€", ha='center')

plt.show()
