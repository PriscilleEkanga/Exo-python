# td13_ex4.py
from dataclasses import dataclass
from typing import ClassVar # Souvent utilisé pour les attributs de classe, non requis ici, mais bonne pratique

@dataclass
class Client:
    """
    Représente un client.
    
    Le décorateur @dataclass génère automatiquement :
    - La méthode __init__(self, nom, email, actif)
    - La méthode __repr__ pour un affichage clair (utile pour print(client))
    - Les méthodes __eq__ (pour la comparaison ==), etc.
    """
    
    # 1. Déclaration des champs avec annotations de type (obligatoire pour dataclass)
    nom: str
    email: str
    
    # Champ avec valeur par défaut. Les champs sans valeur par défaut doivent venir en premier.
    actif: bool = True 

    # Note : Le __init__ et le __repr__ manuels de la version V1 sont supprimés.
    
    def desactiver(self):
        """
        Méthode d'instance pour changer l'état du client à inactif.
        """
        if self.actif:
            self.actif = False
            print(f"INFO : Le client {self.nom} a été désactivé.")
        else:
            print(f"INFO : Le client {self.nom} est déjà inactif.")


if __name__ == "__main__":
    
    print("--- 1. Création et affichage des dataclasses ---")
    
    # Client avec statut par défaut (actif=True)
    client_alice = Client("Alice Dubois", "alice@example.com")
    
    # Client avec statut spécifié
    client_bob = Client("Bob Martin", "bob@example.com", actif=False)
    
    # 1a. Affichage (utilise le __repr__ généré automatiquement)
    print("Client Alice :", client_alice)
    print("Client Bob   :", client_bob)
    
    print("\n--- 2. Utilisation de la méthode d'instance ---")
    
    # 2a. Désactiver Alice
    client_alice.desactiver()
    
    # 2b. Afficher à nouveau Alice pour voir l'effet
    print("Client Alice après désactivation :", client_alice)
    
    # 2c. Tenter de désactiver Bob (déjà inactif)
    client_bob.desactiver()
    
    print("\n--- 3. Test de la comparaison (générée par dataclass) ---")
    
    # Créer un troisième client identique à Alice avant désactivation
    client_test_eq = Client("Alice Dubois", "alice@example.com")
    
    # client_alice est maintenant actif=False, tandis que client_test_eq est actif=True
    print(f"client_alice == client_test_eq : {client_alice == client_test_eq}") # Doit être False

    # Modification de client_alice pour qu'il corresponde exactement
    client_alice.actif = True
    print(f"client_alice == client_test_eq après correction : {client_alice == client_test_eq}") # Doit être True