

def ajouter_bonus(score_actuel):
    """
    Ajoute 5 points au score et retourne le nouveau score.
    Ne modifie aucune variable globale.
    """
    return score_actuel + 5

def ajouter_malus(score_actuel):
    """
    Retire 3 points au score et retourne le nouveau score.
    Ne modifie aucune variable globale.
    """
    return score_actuel - 3

# --- Scénario de test (Code appelant qui gère la variable globale) ---

score = 0
print("Score initial:", score)

# 1. Ajout de bonus
score = ajouter_bonus(score) # On passe le score, on récupère le nouveau score
print("Nouveau score après 1er bonus :", score)

# 2. Ajout de bonus
score = ajouter_bonus(score) # On repasse le nouveau score
print("Nouveau score après 2ème bonus :", score)

# 3. Ajout de malus
score = ajouter_malus(score) # On repasse le score actuel
print("Nouveau score après malus :", score)

print("Score final (mis à jour par le code principal) :", score)