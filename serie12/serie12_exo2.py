# td12_ex2.py
import logging
import os # Utile pour gérer et vérifier le fichier de log

# --- 1. Configuration Avancée du Logging (Vers Fichier) ---

# Définition du nom du fichier de log
LOG_FILENAME = "commande.log"

# Supprimer l'ancien fichier de log s'il existe (pour un test propre à chaque exécution)
if os.path.exists(LOG_FILENAME):
    os.remove(LOG_FILENAME)
    print(f"(Fichier {LOG_FILENAME} précédent supprimé pour un test propre)")


# Configuration de base pour écrire dans le fichier LOG_FILENAME
# NOTE: basicConfig par défaut dirige les logs vers la console ET vers le fichier
logging.basicConfig(
    # Niveau minimal pour l'écriture dans le fichier de log (on veut tout, y compris DEBUG)
    level=logging.DEBUG, 
    
    # Format détaillé incluant la date/heure, le niveau et le nom du logger
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    
    # Spécifie le fichier de destination
    filename=LOG_FILENAME, 
    
    # 'a' pour append (ajouter à la fin), 'w' pour write (écraser à chaque exécution)
    filemode="a", 
    
    # Format de la date (optionnel, mais recommandé pour plus de lisibilité)
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Obtient l'objet logger pour ce module, utilisant la configuration ci-dessus
logger = logging.getLogger(__name__)

# --- 2. Code Métier (Identique à l'Exercice 1) ---

def traiter_commande(commande):
    logger.debug("Commande reçue : %s", commande) 
    
    if not commande:
        logger.error("Commande vide")
        return

    logger.info("Vérification du stock...")
    
    if commande.get("quantite", 0) <= 0:
        logger.error("Quantité invalide pour la commande: %s", commande.get("id"))
        return

    logger.info("Commande validée pour le client %s (ID: %s)", 
                commande.get("client"), 
                commande.get("id"))
    # ... autres traitements ...


if __name__ == "__main__":
    print("\n--- Exécution du scénario (Vérifiez la console et le fichier commande.log) ---")
    
    # Scénario 1 : Commande Valide (Génère des INFO et DEBUG)
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})
    
    # Scénario 2 : Commande Invalide (Génère un ERROR)
    # L'objectif est de s'assurer que les messages d'erreur sont bien écrits dans le fichier.
    traiter_commande({"id": 2, "client": "Bob", "quantite": 0})
    
    # Scénario 3 : Commande Invalide (Vide) (Génère un ERROR)
    traiter_commande({})
    
    print("\n--- Fin de l'exécution ---")
    print(f"Les logs détaillés ont été écrits dans le fichier : {LOG_FILENAME}")

# Le code continue à afficher sur la console ET dans le fichier car basicConfig, par défaut,
# dirige aussi les logs vers le StreamHandler (console) si aucun autre gestionnaire n'est défini.