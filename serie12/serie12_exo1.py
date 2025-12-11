# td12_ex1.py
import logging

# 1. Configuration minimale du logging
# Définit le niveau minimum de messages à afficher (ici, INFO et plus élevé)
logging.basicConfig(level=logging.INFO, 
                    format='%(levelname)s - %(message)s')

# Obtient un objet logger pour ce module
logger = logging.getLogger(__name__)

def traiter_commande(commande):
    # Remplacement de 'print("DEBUG - ...")' par logger.debug(...)
    # Note: Étant donné que le niveau est réglé sur INFO, ce message n'apparaîtra pas
    # dans le scénario de test actuel, ce qui est le but du logging.
    logger.debug("Commande reçue : %s", commande) 
    
    if not commande:
        # Remplacement de 'print("ERREUR - ...")' par logger.error(...)
        logger.error("Commande vide")
        return

    # Remplacement de 'print("INFO - ...")' par logger.info(...)
    logger.info("Vérification du stock...")
    
    if commande.get("quantite", 0) <= 0:
        logger.error("Quantité invalide pour la commande: %s", commande.get("id"))
        return

    logger.info("Commande validée pour le client %s (ID: %s)", 
                commande.get("client"), 
                commande.get("id"))
    # ... autres traitements ...

if __name__ == "__main__":
    print("--- Test 1 : Commande Valide (Niveau INFO) ---")
    traiter_commande({"id": 1, "client": "Alice", "quantite": 3})
    
    print("\n--- Test 2 : Commande Invalide (Quantité) ---")
    traiter_commande({"id": 2, "client": "Bob", "quantite": 0})
    
    print("\n--- Test 3 : Commande Invalide (Vide) ---")
    traiter_commande({})