# service_remise_log.py
import logging

# Configuration minimale du logging pour que la fonction puisse s'exécuter
# (Bien que souvent géré dans le script principal, cela garantit que 
# le logger n'est pas silencieux si non configuré ailleurs.)
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def appliquer_remise(prix_ht, remise):
    """
    Applique une remise au prix HT.

    Arguments:
        prix_ht (float): Prix hors taxe.
        remise (float): Taux de remise (entre 0 et 1).

    Retourne:
        float: Le prix après remise.
    
    Lève:
        ValueError: Si le taux de remise est en dehors de l'intervalle [0, 1].
    """
    if remise < 0 or remise > 1:
        logger.error("Remise invalide : %s", remise)
        raise ValueError("Remise doit être entre 0 et 1")
        
    nouveau_prix = prix_ht * (1 - remise)
    
    # Message INFO qui sera généré lors de l'exécution normale (test valide)
    logger.info("Remise appliquée : %s -> %s", prix_ht, nouveau_prix)
    
    return nouveau_prix