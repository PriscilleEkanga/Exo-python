
score = 0

def ajouter_points(score_actuel, points):
    """
    Calcule le nouveau score en ajoutant les points donnés.

    Args:
        score_actuel (int): Le score actuel.
        points (int): Les points à ajouter.

    Returns:
        int: Le nouveau score calculé.
    """
    nouveau_score = score_actuel + points
    return nouveau_score

# -- Code global qui gère la variable globale --

print("Score global initial:", score)

# 1. Appel de la fonction et mise à jour de la variable globale
points_gagnes = 10
score = ajouter_points(score, points_gagnes)
print(f"Après avoir gagné {points_gagnes} points, le score est mis à jour à:", score)

# 2. Deuxième appel pour montrer l'accumulation
points_gagnes = 5
score = ajouter_points(score, points_gagnes)
print(f"Après avoir gagné {points_gagnes} points, le score est mis à jour à:", score)