#Exercice 8:
import json

# --- 1. Les Fonctions de calcul (Notre "Moteur") ---

def calculer_ca(liste_commandes):
    """Calcule le total des commandes avec le statut 'payee'."""
    total = 0
    for cmd in liste_commandes:
        if cmd["statut"] == "payee":
            total += cmd["montant"]
    return total

def compter_commandes_par_statut(liste_commandes):
    """Renvoie un dictionnaire {statut: nombre}."""
    compteur = {}
    for cmd in liste_commandes:
        statut = cmd["statut"]
        if statut in compteur:
            compteur[statut] += 1
        else:
            compteur[statut] = 1
    return compteur

def totaux_par_client(liste_commandes):
    """Renvoie un dictionnaire {client: montant_total}."""
    depenses = {}
    for cmd in liste_commandes:
        client = cmd["client"]
        montant = cmd["montant"]
        
        # Astuce : .get() permet de récupérer la valeur ou 0 si elle n'existe pas
        # C'est une version raccourcie du "if client in depenses..."
        depenses[client] = depenses.get(client, 0) + montant
            
    return depenses

# --- 2. Le Programme Principal (L'affichage) ---

if __name__ == "__main__":
    nom_fichier = "commandes.json"
    
    try:
        # A. Chargement des données
        with open(nom_fichier, "r", encoding="utf-8") as f:
            commandes = json.load(f)
            
        # B. Calculs
        ca_total = calculer_ca(commandes)
        stats_statuts = compter_commandes_par_statut(commandes)
        stats_clients = totaux_par_client(commandes)
        
        # C. Le Bonus : Tri des clients (Le plus gros acheteur en premier)
        # On transforme le dictionnaire en liste de tuples pour pouvoir le trier
        # item[1] signifie "trier selon la valeur (le montant)"
        # reverse=True signifie "du plus grand au plus petit"
        clients_tries = sorted(stats_clients.items(), key=lambda item: item[1], reverse=True)

        # D. Affichage du Tableau de Bord
        print("=" * 40)
        print("       TABLEAU DE BORD COMMANDES")
        print("=" * 40)
        
        print(f"\n💰 Chiffre d'Affaires (payé) : {ca_total:.2f} €")
        
        print("\n📊 État des commandes :")
        for statut, nombre in stats_statuts.items():
            print(f"  - {statut:<12} : {nombre}") 
            # {statut:<12} sert à aligner le texte sur 12 espaces
            
        print("\n🏆 Top Clients (par dépenses) :")
        for client, montant in clients_tries:
            print(f"  - {client:<20} : {montant:.2f} €")
            
        print("\n" + "=" * 40)

    except FileNotFoundError:
        print(f"❌ Erreur : Impossible de trouver le fichier '{nom_fichier}'.")
    except json.JSONDecodeError:
        print(f"❌ Erreur : Le fichier '{nom_fichier}' n'est pas un JSON valide.")