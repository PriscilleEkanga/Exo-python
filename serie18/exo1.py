# td18_ex1_logs.py
from pathlib import Path
import sys

# Chemins des fichiers
LOG_DIR = Path("logs")
FICHIER_SOURCE = LOG_DIR / "app.log"
FICHIER_CIBLE = LOG_DIR / "app_sans_debug.log"

# Assurez-vous que le répertoire logs existe
LOG_DIR.mkdir(exist_ok=True)

# --- Partie 1 : Vérification de l'existence et comptage ---

total_lignes = 0
nb_error = 0
nb_warning = 0

# Vérification de l'existence du fichier
if not FICHIER_SOURCE.exists():
    print(f"ERREUR : Fichier de log source introuvable : {FICHIER_SOURCE}")
    sys.exit(1) # Arrêt propre du programme

print(f"Analyse du fichier : {FICHIER_SOURCE}")

try:
    # L'itération ligne par ligne est essentielle pour les fichiers volumineux.
    with FICHIER_SOURCE.open("r", encoding="utf-8") as f:
        for ligne in f:
            total_lignes += 1
            
            if "[ERROR]" in ligne:
                nb_error += 1
            elif "[WARNING]" in ligne:
                nb_warning += 1

except IOError as e:
    print(f"Erreur de lecture du fichier : {e}")
    sys.exit(1)

# Affichage du rapport
print("\n--- Rapport d'Analyse ---")
print(f"Lignes totales  : {total_lignes}")
print(f"Lignes WARNING  : {nb_warning}")
print(f"Lignes ERROR    : {nb_error}")
print("--------------------------")

# Commentaires sur la lecture de fichiers volumineux
"""
POURQUOI NE PAS UTILISER f.read() POUR LES GROS FICHIERS :
f.read() charge l'intégralité du contenu du fichier dans une seule variable (une 
seule chaîne de caractères) en mémoire vive (RAM).

Si le fichier 'app.log' fait plusieurs centaines de mégaoctets, voire gigaoctets,
l'utilisation de f.read() va saturer la mémoire vive de l'ordinateur, entraînant 
un plantage ou un ralentissement extrême (thrashing).

L'itération 'for ligne in f:' est efficace car elle lit et traite le fichier 
ligne par ligne, ne maintenant qu'une seule ligne à la fois en mémoire. 
C'est la méthode à privilégier pour les fichiers dont la taille est inconnue ou très grande.
"""

# --- Partie 2 : Filtrage et écriture ---

print(f"\nFiltrage et écriture vers : {FICHIER_CIBLE}")

try:
    # Utilisation du 'with' combiné pour garantir que les deux fichiers sont fermés
    # même en cas d'erreur.
    with FICHIER_SOURCE.open("r", encoding="utf-8") as fin, \
         FICHIER_CIBLE.open("w", encoding="utf-8") as fout:
        
        lignes_filtrees = 0
        
        for ligne in fin:
            # On ignore la ligne si elle contient [DEBUG]
            if "[DEBUG]" in ligne:
                continue
            
            # Sinon, on écrit la ligne dans le fichier cible
            fout.write(ligne)
            lignes_filtrees += 1
            
    print(f"Succès ! {lignes_filtrees} lignes conservées dans {FICHIER_CIBLE}")

except IOError as e:
    print(f"Erreur lors du filtrage et de l'écriture : {e}")