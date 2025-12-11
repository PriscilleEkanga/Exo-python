# td18_ex4_outil.py

"""
Outil de maintenance de fichiers (logs, CSV, JSON) pour la série 18.

Cet outil regroupe trois fonctionnalités :
1. Nettoyage des logs (~ suppression des lignes [DEBUG])
2. Nettoyage des clients CSV (séparation OK / erreurs, validation des données)
3. Mise à jour d'un fichier de configuration JSON (sauvegarde et remplacement atomique)
"""

import json
import csv
import shutil
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple

# --- CHEMINS PAR DÉFAUT ---
DEFAULT_LOG_PATH = Path("logs") / "app.log"
DEFAULT_CSV_PATH = Path("donnees") / "clients_brut.csv"
DEFAULT_JSON_PATH = Path("config_app.json")

# Création des dossiers nécessaires si non existants
Path("logs").mkdir(exist_ok=True)
Path("donnees").mkdir(exist_ok=True)

# =======================================================
# 1. NETTOYAGE DES LOGS (Basé sur Exercice 1)
# =======================================================

def nettoyer_logs(chemin_log: Path):
    """
    Filtre les lignes [DEBUG] d'un fichier log et écrit le résultat.
    """
    if not chemin_log.exists():
        print(f"ERREUR : Fichier log source introuvable : {chemin_log}")
        return

    # Chemin de sortie : logs/app_sans_debug.log
    nom_sans_ext = chemin_log.stem
    chemin_cible = chemin_log.parent / f"{nom_sans_ext}_sans_debug.log"

    print(f"\n--- Démarrage du nettoyage des logs : {chemin_log} ---")
    
    total_lignes = 0
    lignes_conservees = 0

    try:
        with chemin_log.open("r", encoding="utf-8") as fin, \
             chemin_cible.open("w", encoding="utf-8") as fout:
            
            for ligne in fin:
                total_lignes += 1
                
                if "[DEBUG]" not in ligne:
                    fout.write(ligne)
                    lignes_conservees += 1
                    
        print("\nNettoyage réussi !")
        print(f"Lignes totales lues : {total_lignes}")
        print(f"Lignes conservées   : {lignes_conservees}")
        print(f"Fichier de sortie   : {chemin_cible}")

    except IOError as e:
        print(f"ERREUR : Problème de lecture/écriture : {e}")


# =======================================================
# 2. NETTOYAGE DU CSV CLIENTS (Basé sur Exercice 2)
# =======================================================

CHAMPS_ORIGINAUX = ["nom", "age", "ville"]
DELIMITER = ";"

def est_ligne_valide(ligne: Dict[str, str]) -> Tuple[bool, str]:
    """Valide les champs et le type de l'âge."""
    for champ in CHAMPS_ORIGINAUX:
        if not ligne.get(champ) or ligne[champ].strip() == "":
            return False, f"Champ '{champ}' est vide"
    try:
        age = int(ligne["age"])
        if age <= 0:
            return False, "Âge non positif"
    except ValueError:
        return False, f"Le champ 'age' n'est pas un entier valide: '{ligne['age']}'"
    return True, ""


def nettoyer_clients_csv(chemin_csv: Path):
    """
    Filtre, valide et sépare les lignes CSV en deux fichiers : propre et erreurs.
    """
    if not chemin_csv.exists():
        print(f"ERREUR : Fichier CSV source introuvable : {chemin_csv}")
        return

    # Chemins de sortie : donnees/clients_propre.csv, donnees/clients_erreurs.csv
    nom_sans_ext = chemin_csv.stem
    chemin_propre = chemin_csv.parent / f"{nom_sans_ext}_propre.csv"
    chemin_erreurs = chemin_csv.parent / f"{nom_sans_ext}_erreurs.csv"

    print(f"\n--- Démarrage du nettoyage CSV : {chemin_csv} ---")

    lignes_valides: List[Dict[str, str]] = []
    lignes_invalides: List[Dict[str, str]] = []
    total_lignes_lues = 0

    try:
        with chemin_csv.open("r", encoding="utf-8", newline="") as f:
            lecteur = csv.DictReader(f, delimiter=DELIMITER)
            
            for ligne in lecteur:
                total_lignes_lues += 1
                ligne_complete = {k: ligne.get(k, '').strip() for k in CHAMPS_ORIGINAUX}
                valide, raison = est_ligne_valide(ligne_complete)
                
                if valide:
                    lignes_valides.append(ligne_complete)
                else:
                    ligne_complete["raison"] = raison
                    lignes_invalides.append(ligne_complete)

    except Exception as e:
        print(f"ERREUR : Problème de lecture CSV : {e}")
        return

    # Écriture des résultats
    try:
        with chemin_propre.open("w", encoding="utf-8", newline="") as f_propre:
            ecrivain_propre = csv.DictWriter(f_propre, fieldnames=CHAMPS_ORIGINAUX, delimiter=DELIMITER)
            ecrivain_propre.writeheader()
            ecrivain_propre.writerows(lignes_valides)
            
        with chemin_erreurs.open("w", encoding="utf-8", newline="") as f_erreurs:
            ecrivain_erreurs = csv.DictWriter(f_erreurs, fieldnames=CHAMPS_ORIGINAUX + ["raison"], delimiter=DELIMITER)
            ecrivain_erreurs.writeheader()
            ecrivain_erreurs.writerows(lignes_invalides)

        print("\nNettoyage réussi !")
        print(f"Lignes lues      : {total_lignes_lues}")
        print(f"Lignes valides   : {len(lignes_valides)} -> {chemin_propre}")
        print(f"Lignes invalides : {len(lignes_invalides)} -> {chemin_erreurs}")

    except IOError as e:
        print(f"ERREUR : Problème d'écriture des fichiers de sortie : {e}")


# =======================================================
# 3. MISE À JOUR JSON (Basé sur Exercice 3)
# =======================================================

def mettre_a_jour_config_json(chemin_config: Path):
    """
    Sauvegarde, met à jour et remplace de manière atomique le fichier JSON.
    """
    if not chemin_config.exists():
        print(f"ERREUR : Fichier de configuration JSON introuvable : {chemin_config}")
        return

    FICHIER_BACKUP = chemin_config.with_name(f"{chemin_config.stem}_backup.json")
    FICHIER_TEMP = chemin_config.with_name(f"{chemin_config.stem}.json.tmp")
    
    ancienne_config: Dict[str, Any] = {}
    
    # Lecture
    try:
        with chemin_config.open("r", encoding="utf-8") as f:
            ancienne_config = json.load(f)
            config_avant_maj = ancienne_config.copy()
            
    except json.JSONDecodeError as e:
        print(f"ERREUR : Le fichier JSON est invalide. Détails : {e}")
        return
    except IOError as e:
        print(f"ERREUR de lecture : {e}")
        return

    print(f"\n--- Démarrage de la mise à jour JSON : {chemin_config} ---")
    
    # Sauvegarde
    try:
        shutil.copy(chemin_config, FICHIER_BACKUP)
        print(f"Sauvegarde créée : {FICHIER_BACKUP}")
    except Exception as e:
        print(f"AVERTISSEMENT : Échec de la sauvegarde : {e}")
        
    # Modification en mémoire (logique de l'Ex 3)
    nouvelle_config = ancienne_config # Commence avec l'ancienne config

    # Logique de mise à jour:
    nouvelle_config["debug"] = False
    nouvelle_config["max_connexions"] = nouvelle_config.get("max_connexions", 0) + 10
    
    if "version" in nouvelle_config:
        try:
            v_parts = nouvelle_config["version"].split('.')
            if len(v_parts) == 3:
                v_parts[2] = str(int(v_parts[2]) + 1)
                nouvelle_config["version"] = ".".join(v_parts)
        except:
            pass # Ignorer l'erreur si le format de version est mauvais

    if "services" in nouvelle_config and "admin" not in nouvelle_config["services"]:
        nouvelle_config["services"].append("admin")
        
    nouvelle_config["theme"] = "dark"

    # Écriture atomique
    try:
        with FICHIER_TEMP.open("w", encoding="utf-8") as f:
            json.dump(nouvelle_config, f, ensure_ascii=False, indent=2)
            
        FICHIER_TEMP.replace(chemin_config)
        print(f"Mise à jour réussie et remplacée dans '{chemin_config}'.")

    except Exception as e:
        print(f"ERREUR CRITIQUE lors de l'écriture ou du remplacement : {e}")
        return

    # Affichage du diff
    print("\n--- DIFFÉRENCES CLÉS ---")
    keys_to_show = ["version", "debug", "max_connexions", "theme"]
    for key in keys_to_show:
        if key in config_avant_maj:
            print(f"{key:<18}: Avant: {config_avant_maj[key]!r:<10} | Après: {nouvelle_config[key]!r}")
        

# =======================================================
# 4. SCRIPT PRINCIPAL (Menu)
# =======================================================

def get_chemin_utilisateur(default_path: Path) -> Path:
    """Optionnel avancé : Demande à l'utilisateur un chemin, sinon prend le chemin par défaut."""
    chemin_str = input(f"Entrez le chemin du fichier (laissez vide pour {default_path}) : ")
    if not chemin_str:
        return default_path
    
    custom_path = Path(chemin_str)
    
    if not custom_path.exists():
        print(f"AVERTISSEMENT : Le chemin spécifié '{custom_path}' n'existe pas. Utilisation du chemin par défaut.")
        return default_path
    
    return custom_path

def main():
    """Fonction principale gérant le menu de l'outil."""
    
    while True:
        print("\n" + "=" * 40)
        print("OUTIL DE MAINTENANCE DE FICHIERS (Série 18)")
        print("=" * 40)
        print("1) Nettoyer les logs (Supprimer [DEBUG])")
        print("2) Nettoyer le CSV clients (Séparer OK/KO)")
        print("3) Mettre à jour config JSON (vendre le thème dark)")
        print("0) Quitter")
        
        choix = input("Votre choix : ").strip()
        
        if choix == '1':
            chemin = get_chemin_utilisateur(DEFAULT_LOG_PATH)
            nettoyer_logs(chemin)
            
        elif choix == '2':
            chemin = get_chemin_utilisateur(DEFAULT_CSV_PATH)
            nettoyer_clients_csv(chemin)
            
        elif choix == '3':
            chemin = get_chemin_utilisateur(DEFAULT_JSON_PATH)
            mettre_a_jour_config_json(chemin)
            
        elif choix == '0':
            print("Arrêt de l'outil.")
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()