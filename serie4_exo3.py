#Exercice 3: Indice de liste avec message utilisateur

produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]

indice_str = input("Entrez l'indice du produit : ")

try:
    indice = int(indice_str)               # Peut lever ValueError
    produit = produits[indice]             # Peut lever IndexError
    print("Produit :", produit)

except ValueError:
    print("Erreur : veuillez entrer un nombre entier.")

except IndexError:
    print(f"Indice invalide (doit être entre 0 et {len(produits)-1}).")
