#Exercice 4:  Fichiers & exceptions

def lire_fichier_securise(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            contenu = f.read()
        return contenu

    except FileNotFoundError:
        print(f"Erreur : le fichier '{nom_fichier}' est introuvable.")
        return None


# --- Bloc principal ---
nom = input("Nom du fichier à lire : ")

contenu = lire_fichier_securise(nom)

if contenu is not None:
    print("\n--- Contenu du fichier ---")
    print(contenu)
else:
    print("Lecture impossible.")
