commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

# --- 1. Calculer le Chiffre d'Affaires (CA) ---
chiffre_affaires = 0

for cmd in commandes:
    # On vérifie si le statut est "payee"
    if cmd["statut"] == "payee":
        # On ajoute le montant au total
        chiffre_affaires = chiffre_affaires + cmd["montant"]

print(f"Chiffre d'affaires total : {chiffre_affaires} €")


# --- 2. Compter le nombre de commandes par statut ---
# On crée un dictionnaire vide pour stocker les résultats
compteur_statuts = {}

for cmd in commandes:
    statut_actuel = cmd["statut"]
    
    # Si le statut existe déjà dans le dictionnaire, on ajoute 1
    if statut_actuel in compteur_statuts:
        compteur_statuts[statut_actuel] += 1
    # Sinon, c'est la première fois qu'on le voit, on l'initialise à 1
    else:
        compteur_statuts[statut_actuel] = 1

print("Compte par statut :", compteur_statuts)


# --- 3. Total dépensé par client ---
depenses_clients = {}

for cmd in commandes:
    client = cmd["client"]
    montant = cmd["montant"]
    
    # Même logique : si le client existe déjà, on ajoute le montant
    if client in depenses_clients:
        depenses_clients[client] += montant
    # Sinon, on crée l'entrée pour ce client avec le premier montant
    else:
        depenses_clients[client] = montant

print("Dépenses par client :", depenses_clients)