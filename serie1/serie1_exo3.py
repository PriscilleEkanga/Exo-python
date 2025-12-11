#Exerce 3: Conditions

# Demander l'âge
age_str = input("Quel est votre âge ? ")
age = int(age_str)

# Détermination du tarif
if age < 12:
    tarif = 5.0
elif age <= 17:
    tarif = 7.0
elif age <= 25:
    tarif = 8.5
else:
    tarif = 10.0

# Affichage du résultat
print("Tarif :", str(tarif) + "€")
