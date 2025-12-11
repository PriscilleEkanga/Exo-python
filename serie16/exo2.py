# outils_chaine.py

SEPARATEUR = "-" * 40
"""Constante de module pour un affichage séparateur."""

def compter_mots(texte: str) -> int:
    """
    Renvoie le nombre de mots dans une chaîne de caractères.
    Un mot est défini comme un élément séparé par un espace après split().
    """
    # Utiliser split() sans argument gère automatiquement les multiples espaces
    # et les chaînes vides (si texte.split() renvoie ['']).
    mots = texte.split()
    return len(mots)

def est_palindrome(texte: str) -> bool:
    """
    Vérifie si un texte est un palindrome (sans tenir compte des espaces,
    de la casse ou des signes de ponctuation simples).
    """
    # Étape 1 : Nettoyage du texte (supprimer les espaces et mettre en minuscules)
    texte_nettoye = texte.replace(" ", "").lower()
    
    # Étape 2 : Vérification du palindrome
    # texte_nettoye[::-1] est une façon idiomatique de renverser la chaîne en Python
    return texte_nettoye == texte_nettoye[::-1]