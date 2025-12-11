import os

# 1. LBYL : Look Before You Leap
def lire_fichier_lbyl(nom_fichier):
    if os.path.exists(nom_fichier):          # On vérifie d'abord
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    else:
        print(f"LBYL : fichier introuvable → {nom_fichier}")
        return None


# 2. EAFP : Easier to Ask Forgiveness than Permission
def lire_fichier_eafp(nom_fichier):
    try:
        with open(nom_fichier, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"EAFP : fichier introuvable → {nom_fichier}")
        return None


# --- Bloc principal pour tester ---
print("=== Création d’un fichier pour le test ===")
nom_existant = "test.txt"
with open(nom_existant, "w", encoding="utf-8") as f:
    f.write("Ceci est un fichier de test.\n")

nom_inexistant = "fichier_inexistant.txt"

print("\n=== Test LBYL ===")
print("Fichier existant :", lire_fichier_lbyl(nom_existant))
print("Fichier inexistant :", lire_fichier_lbyl(nom_inexistant))

print("\n=== Test EAFP ===")
print("Fichier existant :", lire_fichier_eafp(nom_existant))
print("Fichier inexistant :", lire_fichier_eafp(nom_inexistant))
