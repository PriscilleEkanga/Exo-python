#Exercice 2: Statistiques sur des notes

notes = [12, 5.5, 17, 9, 13, 8, 10]

# 1. Note Minimum et Maximum
note_min = min(notes)
note_max = max(notes)

print("La note minimale est :", note_min)
print("La note maximale est :", note_max)

# 2. Calculer la moyenne
somme = sum(notes)
nombre_notes = len(notes)
moyenne = somme / nombre_notes

print("La moyenne de la classe est :", moyenne)

# 3. Compter les réussites (>= 10)
reussites = 0

for note in notes:
    if note >= 10:
        reussites = reussites + 1  # On ajoute 1 au compteur

print("Nombre de réussites :", reussites)

# 4. Bonus : Pourcentage de réussite
pourcentage = (reussites / nombre_notes) * 100
# On arrondit à 2 chiffres après la virgule pour que ce soit joli
print(f"Pourcentage de réussite : {pourcentage:.2f}%")