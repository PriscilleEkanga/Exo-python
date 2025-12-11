# td19_ex4_todo_app.py
"""
Mini application console de gestion de tâches avec persistance JSON.
Série 19 – Persistance des données avec JSON.
"""

from pathlib import Path
import json
from typing import List, Dict, Any, Optional
from datetime import datetime

# --- Configuration et structure par défaut ---
FICHIER_TODOS = Path("todos.json")

# Structure de données par défaut pour l'initialisation
DEFAULT_DATA = {
    "utilisateur": "Invité",
    "derniere_id": 0,
    "taches": []
}

# =======================================================
# PERSISTANCE (Charger / Sauvegarder)
# =======================================================

def charger_donnees_securise(chemin_fichier: Path) -> Dict[str, Any]:
    """
    Charge les données JSON ou renvoie la structure par défaut en cas d'erreur/absence.
    """
    if not chemin_fichier.exists():
        return DEFAULT_DATA.copy()
    
    try:
        with chemin_fichier.open("r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Validation simple
        if not isinstance(data, dict) or "taches" not in data:
             return DEFAULT_DATA.copy()

        return data
        
    except (json.JSONDecodeError, IOError):
        # JSON invalide ou autre erreur de lecture
        return DEFAULT_DATA.copy()

def sauvegarder_donnees(chemin_fichier: Path, donnees: Dict[str, Any]) -> None:
    """
    Sauvegarde la structure de données complète dans le fichier JSON.
    """
    try:
        with chemin_fichier.open("w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"ERREUR : Échec de la sauvegarde dans {chemin_fichier} : {e}")

# =======================================================
# LOGIQUE MÉTIER
# =======================================================

def get_taches_filtrees(donnees: Dict[str, Any], statut: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Récupère les tâches, potentiellement filtrées par statut ('fait' ou 'non fait').
    """
    taches = donnees.get("taches", [])
    
    # Tri par ID pour un affichage stable
    taches.sort(key=lambda t: t.get("id", 0)) 
    
    if statut == "fait":
        return [t for t in taches if t.get("fait") is True]
    elif statut == "a faire":
        return [t for t in taches if t.get("fait") is False]
    else:
        return taches

def afficher_taches(donnees: Dict[str, Any], statut_filtre: Optional[str] = None) -> None:
    """Affiche la liste des tâches de façon lisible, avec possibilité de filtre."""
    
    taches_a_afficher = get_taches_filtrees(donnees, statut_filtre)
    utilisateur = donnees.get("utilisateur", "Inconnu")
    
    titre_filtre = ""
    if statut_filtre == "a faire":
        titre_filtre = " (À FAIRE)"
    elif statut_filtre == "fait":
        titre_filtre = " (TERMINÉES)"

    print("\n" + "=" * 40)
    print(f" TÂCHES de {utilisateur}{titre_filtre} ({len(taches_a_afficher)} éléments)")
    print("=" * 40)
    
    if not taches_a_afficher:
        print("La liste est vide ou aucun élément ne correspond au filtre.")
        return

    for tache in taches_a_afficher:
        statut = "✅ FAIT" if tache.get("fait") else "❌ À FAIRE"
        print(f"[{tache.get('id', '?'):<3}] {tache.get('titre', 'Sans titre')} ({statut})")
    print("-" * 40)

def ajouter_tache(donnees: Dict[str, Any], titre: str) -> None:
    """Ajoute une tâche en incrémentant l'ID."""
    donnees["derniere_id"] = donnees.get("derniere_id", 0) + 1
    nouvel_id = donnees["derniere_id"]
    
    nouvelle_tache = {
        "id": nouvel_id,
        "titre": titre,
        "fait": False,
        "cree_le": datetime.now().isoformat(timespec='seconds')
    }
    donnees["taches"].append(nouvelle_tache)
    print(f"-> Ajouté : ID {nouvel_id} - '{titre}'")

def marquer_tache_faite(donnees: Dict[str, Any], id_tache: int) -> bool:
    """Marque la tâche d'identifiant id_tache comme faite."""
    taches = donnees.get("taches", [])
    tache = next((t for t in taches if t.get("id") == id_tache), None)
    
    if tache:
        tache["fait"] = True
        print(f"-> Cochée : ID {id_tache} - {tache['titre']}")
        return True
    
    return False

def supprimer_tache(donnees: Dict[str, Any], id_tache: int) -> bool:
    """Supprime la tâche d'identifiant id_tache."""
    taches_originales = donnees.get("taches", [])
    
    # Filtrer et créer une nouvelle liste sans l'élément à supprimer
    nouvelle_liste_taches = [t for t in taches_originales if t.get("id") != id_tache]
    
    if len(nouvelle_liste_taches) < len(taches_originales):
        donnees["taches"] = nouvelle_liste_taches 
        print(f"-> Supprimée : Tâche d'ID {id_tache}.")
        return True
    
    return False

# =======================================================
# INTERFACE UTILISATEUR (Menu)
# =======================================================

def afficher_menu() -> str:
    """Affiche le menu et demande le choix de l'utilisateur."""
    print("\n" + "="*25)
    print("=== Todo JSON – Série 19 ===")
    print("="*25)
    print("1) Afficher toutes les tâches")
    print("2) Ajouter une tâche")
    print("3) Marquer une tâche comme faite")
    print("4) Supprimer une tâche")
    print("5) Afficher uniquement les tâches À FAIRE (Optionnel)")
    print("6) Afficher uniquement les tâches TERMINÉES (Optionnel)")
    print("0) Quitter")
    
    return input("Votre choix : ").strip()

def lire_id_safe(message: str) -> Optional[int]:
    """Demande un ID et gère les erreurs de conversion."""
    try:
        return int(input(message).strip())
    except ValueError:
        print("Erreur : L'ID doit être un nombre entier.")
        return None

def boucle_principale():
    """
    Contient la boucle principale de l'application console.
    """
    # 1. Chargement initial des données
    donnees = charger_donnees_securise(FICHIER_TODOS)
    nb_taches = len(donnees.get("taches", []))
    
    print("\nBienvenue dans Todo JSON – Série 19")
    print(f"Tâches chargées : {nb_taches}")
    
    en_cours = True
    while en_cours:
        
        choix = afficher_menu()
        
        if choix == '1':
            afficher_taches(donnees)
            
        elif choix == '2':
            titre = input("Titre de la nouvelle tâche : ").strip()
            if titre:
                ajouter_tache(donnees, titre)
                sauvegarder_donnees(FICHIER_TODOS, donnees)
            else:
                print("Le titre ne peut pas être vide.")
                
        elif choix == '3':
            id_choisi = lire_id_safe("ID de la tâche à marquer comme FAITE : ")
            if id_choisi is not None:
                if marquer_tache_faite(donnees, id_choisi):
                    sauvegarder_donnees(FICHIER_TODOS, donnees)
                else:
                    print(f"Opération annulée : Tâche d'ID {id_choisi} introuvable.")
                    
        elif choix == '4':
            id_choisi = lire_id_safe("ID de la tâche à SUPPRIMER : ")
            if id_choisi is not None:
                if supprimer_tache(donnees, id_choisi):
                    sauvegarder_donnees(FICHIER_TODOS, donnees)
                else:
                    print(f"Opération annulée : Tâche d'ID {id_choisi} introuvable.")
                    
        # Options facultatives (Filtres)
        elif choix == '5':
            afficher_taches(donnees, statut_filtre="a faire")
        
        elif choix == '6':
            afficher_taches(donnees, statut_filtre="fait")
        
        elif choix == '0':
            en_cours = False
            
        else:
            print("Choix invalide. Veuillez saisir un numéro du menu.")

    print("\nMerci d'avoir utilisé Todo JSON. Au revoir !")

if __name__ == "__main__":
    boucle_principale()