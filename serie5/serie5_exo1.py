utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}

# 1. Fonction LBYL
def get_age_lbyl(utilisateur):
    if "age" in utilisateur:               # On vérifie avant
        return utilisateur["age"]
    else:
        print("LBYL : Clé 'age' absente.")
        return None


# 2. Fonction EAFP
def get_age_eafp(utilisateur):
    try:
        return utilisateur["age"]          # On essaie directement
    except KeyError:
        print("EAFP : Clé 'age' absente.")
        return None


# --- Bloc principal ---
dico_complet = {"nom": "Alice", "age": 30}
dico_incomplet = {"nom": "Bob"}

# Tests
print("=== Tests LBYL ===")
print(get_age_lbyl(dico_complet))     # devrait retourner 30
print(get_age_lbyl(dico_incomplet))   # devrait afficher un message + None

print("\n=== Tests EAFP ===")
print(get_age_eafp(dico_complet))     # devrait retourner 30
print(get_age_eafp(dico_incomplet))   # devrait afficher un message + None
