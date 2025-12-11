# td19_ex1_base_json.py
import json
from pathlib import Path
from typing import List, Dict, Any

# Définition du chemin du fichier de données
FICHIER_TACHES = Path("todos.json")

def charger_taches(chemin_fichier: Path) -> List[Dict[str, Any]]:
    """
    Charge la liste de tâches à partir du fichier JSON.
    Suppose que le fichier existe et est valide.
    """
    print(f"-> Chargement des tâches depuis {chemin_fichier}...")
    with chemin_fichier.open("r", encoding="utf-8") as f:
        taches = json.load(f)
    return taches

def sauvegarder_taches(chemin_fichier: Path, taches: List[Dict[str, Any]]) -> None:
    """
    Sauvegarde la liste de tâches (structure Python) dans le fichier JSON.
    """
    print(f"<- Sauvegarde des tâches dans {chemin_fichier}...")
    with chemin_fichier.open("w", encoding="utf-8") as f:
        # ensure_ascii=False pour supporter les accents, indent=2 pour la lisibilité humaine
        json.dump(taches, f, ensure_ascii=False, indent=2)
    print("Sauvegarde terminée.")

def afficher_taches(taches: List[Dict[str, Any]]):
    """Affiche la liste des tâches de façon lisible."""
    print("\n--- Liste des Tâches Actuelles ---")
    for tache in taches:
        statut = "✅ Fait" if tache["fait"] else "❌ À faire"
        print(f"[{tache['id']}] {tache['titre']} ({statut})")
    print("----------------------------------")

if __name__ == "__main__":
    
    # 1. Charger les tâches
    if not FICHIER_TACHES.exists():
        # Si le fichier n'existe pas, on peut initialiser la liste
        taches_actuelles = []
        print(f"Le fichier {FICHIER_TACHES} n'existe pas, initialisation de la liste.")
    else:
        taches_actuelles = charger_taches(FICHIER_TACHES)
    
    # 2. Afficher toutes les tâches
    afficher_taches(taches_actuelles)
    
    # 3. Ajouter une nouvelle tâche (Modification en mémoire)
    nouvelle_tache = {
        "id": 3,
        "titre": "Finaliser l'exercice de persistance",
        "fait": False
    }
    print(f"\n+ Ajout de la nouvelle tâche: '{nouvelle_tache['titre']}'")
    taches_actuelles.append(nouvelle_tache)
    
    # 4. Afficher la liste mise à jour (en mémoire)
    afficher_taches(taches_actuelles)
    
    # 5. Sauvegarder la nouvelle liste de tâches
    sauvegarder_taches(FICHIER_TACHES, taches_actuelles)
    
    print("\nVérifiez le fichier todos.json pour confirmer la mise à jour.")