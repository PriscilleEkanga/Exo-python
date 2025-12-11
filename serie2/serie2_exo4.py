#Exercice 4: Structurer en fonctions de l'analyse des commandes

# --- Partie 1 : Définition des fonctions (Les outils) ---

def calculer_ca(liste_commandes):
    """Calcule la somme des montants des commandes payées."""
    total = 0
    for cmd in liste_commandes:
        if cmd["statut"] == "payee":
            total += cmd["montant"]
    return total  # Important : on renvoie le résultat, on ne l'affiche pas ici

def compter_commandes_par_statut(liste_commandes):
    """Compte le nombre de commandes pour chaque statut."""
    compteur = {}
    for cmd in liste_commandes:
        statut = cmd["statut"]
        if statut in compteur:
            compteur[statut] += 1
        else:
            compteur[statut] = 1
    return compteur

def totaux_par_client(liste_commandes):
    """Calcule le total dépensé par chaque client."""
    depenses = {}
    for cmd in liste_commandes:
        client = cmd["client"]
        montant = cmd["montant"]
        
        if client in depenses:
            depenses[client] += montant
        else:
            depenses[client] = montant
    return depenses

# --- Partie 2 : Le bloc principal (L'exécution) ---

if __name__ == "__main__":
    # 1. Les données
    commandes = [
        {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
        {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
        {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
        {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
        {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
    ]

    # 2. Appel des fonctions
    # On stocke le résultat de la fonction dans une variable
    ca_total = calculer_ca(commandes)
    stats_statuts = compter_commandes_par_statut(commandes)
    stats_clients = totaux_par_client(commandes)

    # 3. Affichage des résultats
    print(f"💰 Chiffre d'affaires (payé) : {ca_total:.2f} €")
    print("-" * 30)
    
    print("📊 Commandes par statut :")
    print(stats_statuts)
    print("-" * 30)

    print("busts_in_silhouette Dépenses par client :")
    for client, total in stats_clients.items():
        print(f"- {client} : {total:.2f} €")

