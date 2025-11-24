#Exercice 5: Liste et parcours

# 1. Création de la liste
prix = [9.99, 14.5, 3.2, 29.0]

# 2. Affichage de tous les prix
print("Liste des prix :")
for p in prix:
    print(p)

# 3. Calcul du total
total = 0
for p in prix:
    total = total + p

print("Total :", total)

# 4. Calcul du prix moyen
moyenne = total / len(prix)
print("Prix moyen :", moyenne)

# 5. Bonus : prix > 10€
print("Prix strictement supérieurs à 10€ :")
for p in prix:
    if p > 10:
        print(p)
