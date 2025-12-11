# td18_ex2_csv.py
import csv
from pathlib import Path
from typing import List, Dict, Any, Tuple

# Chemins des fichiers
DATA_DIR = Path("donnees")
FICHIER_SOURCE = DATA_DIR / "clients_brut.csv"
FICHIER_PROPRE = DATA_DIR / "clients_propre.csv"
FICHIER_ERREURS = DATA_DIR / "clients_erreurs.csv"

# Assurez-vous que le répertoire existe
DATA_DIR.mkdir(exist_ok=True)

# Définition des champs attendus dans les données
CHAMPS_ORIGINAUX = ["nom", "age", "ville"]
CHAMPS_ERREURS = CHAMPS_ORIGINAUX + ["raison"]
DELIMITER = ";"

def est_age_valide(age_str: str) -> bool:
    """Vérifie si la chaîne de l'âge peut être convertie en entier positif."""
    try:
        age = int(age_str)
        return age > 0
    except ValueError:
        return False

def est_ligne_valide(ligne: Dict[str, str]) -> Tuple[bool, str]:
    """
    Vérifie la validité d'une ligne de données.
    Renvoie (True, "") si valide, sinon (False, "Raison de l'erreur").
    """
    # 1. Vérification des champs vides
    for champ in CHAMPS_ORIGINAUX:
        if not ligne.get(champ) or ligne[champ].strip() == "":
            return False, f"Champ '{champ}' est vide"

    # 2. Vérification du type (conversion en entier pour l'âge)
    if not est_age_valide(ligne["age"]):
        return False, f"Le champ 'age' n'est pas un entier positif valide: '{ligne['age']}'"

    return True, ""

def nettoyer_csv():
    """
    Lit le CSV brut, filtre les lignes valides et écrit les résultats
    dans deux fichiers séparés.
    """
    lignes_valides: List[Dict[str, str]] = []
    lignes_invalides: List[Dict[str, str]] = []
    
    total_lignes_lues = 0

    # --- Étape 1 : Lecture et Filtration (Extract & Transform) ---
    print(f"Lecture et analyse de : {FICHIER_SOURCE}")

    try:
        with FICHIER_SOURCE.open("r", encoding="utf-8", newline="") as f:
            # DictReader est utilisé car il lit les données sous forme de dictionnaires.
            lecteur = csv.DictReader(f, delimiter=DELIMITER)
            
            for ligne in lecteur:
                total_lignes_lues += 1
                
                # S'assurer que les clés existent même si la ligne est courte (cas rare mais possible)
                ligne_complete = {k: ligne.get(k, '').strip() for k in CHAMPS_ORIGINAUX}
                
                valide, raison = est_ligne_valide(ligne_complete)
                
                if valide:
                    lignes_valides.append(ligne_complete)
                else:
                    # Ajout de la raison de l'erreur pour le fichier de log
                    ligne_complete["raison"] = raison
                    lignes_invalides.append(ligne_complete)

    except FileNotFoundError:
        print(f"ERREUR : Le fichier source est introuvable à {FICHIER_SOURCE}")
        return
    except Exception as e:
        print(f"ERREUR inattendue lors de la lecture : {e}")
        return


    # --- Étape 2 : Écriture des résultats (Load) ---

    # Écriture des lignes valides (clients_propre.csv)
    with FICHIER_PROPRE.open("w", encoding="utf-8", newline="") as f_propre:
        ecrivain_propre = csv.DictWriter(f_propre, fieldnames=CHAMPS_ORIGINAUX, delimiter=DELIMITER)
        ecrivain_propre.writeheader()
        ecrivain_propre.writerows(lignes_valides)
        
    # Écriture des lignes invalides (clients_erreurs.csv)
    with FICHIER_ERREURS.open("w", encoding="utf-8", newline="") as f_erreurs:
        ecrivain_erreurs = csv.DictWriter(f_erreurs, fieldnames=CHAMPS_ERREURS, delimiter=DELIMITER)
        ecrivain_erreurs.writeheader()
        ecrivain_erreurs.writerows(lignes_invalides)


    # --- Étape 3 : Affichage du résumé ---
    print("\n--- RÉSULTAT DU NETTOYAGE (Mini-ETL) ---")
    print(f"Lignes lues      : {total_lignes_lues}")
    print(f"Lignes valides   : {len(lignes_valides)}")
    print(f"Lignes invalides : {len(lignes_invalides)}")
    print(f"\nFichier propre   : {FICHIER_PROPRE} (Succès)")
    print(f"Fichier erreurs  : {FICHIER_ERREURS} (À corriger)")

    # ----------------------------------------------------
    # Commentaires sur la méthode d'approche
    # ----------------------------------------------------
    """
    DIFFÉRENCE CSV.READER (liste de listes) vs CSV.DICTREADER (dictionnaires) :

    1. csv.reader (liste de listes) :
       - Les données sont traitées comme des listes Python.
       - Accès aux données par index (ligne[0], ligne[1], ...).
       - Avantage : Légèrement plus rapide, utile si le CSV n'a pas d'en-tête ou si l'ordre 
         des colonnes est garanti.
       - Inconvénient : Fragile. Si l'ordre des colonnes change (ex: 'age' passe en index 2), 
         le code casse car on utilise un index fixe.

    2. csv.DictReader (dictionnaires) :
       - Les données sont traitées comme des dictionnaires (clé=nom de colonne, valeur=donnée).
       - Accès aux données par nom (ligne['age'], ligne['nom']).
       - Avantage : Plus robuste et lisible. Le code reste fonctionnel même si l'ordre des 
         colonnes change, tant que les noms de colonnes restent les mêmes. Indispensable pour l'ETL.
       - Inconvénient : Légèrement plus lent (création de dictionnaires à chaque ligne).
    
    Pour le nettoyage de données et l'ETL, l'approche Dictionnaire (DictReader/DictWriter) 
    est largement préférée pour sa robustesse et sa lisibilité.
    """


if __name__ == "__main__":
    nettoyer_csv()