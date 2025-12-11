#Exercice 1: Sécuriser une saisie utilisateur (ValueError)

while True:
    try:
        age = int(input("Votre âge : "))
        break   # Sort de la boucle si tout va bien
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier valide (ex : 25).")

print(f"Vous avez {age} ans.")
