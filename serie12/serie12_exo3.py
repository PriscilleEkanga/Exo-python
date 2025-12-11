# remise.py

def calculer_prix_ttc(prix_ht, taux_tva):
    """
    Calcule le prix TTC à partir du prix hors taxe et du taux de TVA.

    Arguments:
        prix_ht (float): Prix hors taxe.
        taux_tva (float): Taux de TVA (ex: 0.20 pour 20%).

    Retourne:
        float: Le prix TTC.
    
    Lève:
        ValueError: Si le prix HT est négatif.
    """
    if prix_ht < 0:
        raise ValueError("Le prix HT doit être positif ou nul")
    
    # Le calcul est : prix_ht * (1 + taux_tva)
    return prix_ht * (1 + taux_tva)

# Note : Pas besoin du bloc if __name__ == "__main__" ici, car c'est un module
# destiné à être importé.