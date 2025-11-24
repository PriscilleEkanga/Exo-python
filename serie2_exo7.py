#Exercice 7:

import json

# 1. Nos données brutes (Liste de dictionnaires)
commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

# 2. Conversion en chaîne de caractères JSON (dumps = dump string)
# ensure_ascii=False permet de garder les accents s'il y en a
# indent=2 permet de rendre le texte joli et aéré
json_str = json.dumps(commandes, indent=2, ensure_ascii=False)

print("Aperçu du JSON généré :")
print(json_str)

# 3. Écriture dans le fichier
with open("commandes.json", "w", encoding="utf-8") as f:
    f.write(json_str)

print("\n✅ Fichier 'commandes.json' créé avec succès !")