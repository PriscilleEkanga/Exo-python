# td19_ex3_operations.py
from pathlib import Path
import json
from typing import List, Dict, Any, Optional

# --- Chemins et structure par défaut ---
FICHIER_TODOS = Path("todos.json")

# Structure de données par défaut pour l'initialisation
DEFAULT_DATA = {
    "utilisateur": "Invité",
    "derniere_id": 0,
    "taches": []
}

# ----------------------------------------------------------------------
# Fonctions de Persistance (Sécurisées - Réutilisées de l'Ex. 2)
# ----------------------------------------------------------------------

def charger_donnees_securise(chemin_fichier: Path) -> Dict[str, Any]:
    """
    Charge les données JSON ou renvoie la structure par défaut en cas d'erreur/absence.
    """
    if not chemin_fichier.exists():
        print(f"INFO : Fichier '{chemin_fichier}' manquant. Initialisation des données.")
        return DEFAULT_DATA.copy()
    
    try:
        with chemin_fichier.open("r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Vérification simple (doit être un dictionnaire et contenir la clé 'taches')
        if not isinstance(data, dict) or "taches" not in data:
             print(f"ERREUR : Contenu de '{chemin_fichier}' non conforme. Renvoyer structure par défaut.")
             return DEFAULT_DATA.copy()

        print(f"INFO : Données chargées avec succès pour {data.get('utilisateur')}.")
        return data
        
    except json.JSONDecodeError as e:
        print(f"ERREUR : Le fichier '{chemin_fichier}' contient du JSON invalide. Utilisation de la structure par défaut.")
        print(f"Détails de l'erreur JSON : {e}")
        return DEFAULT_DATA.copy()
    except IOError as e:
        print(f"ERREUR de lecture : {e}")
        return DEFAULT_DATA.copy()

def sauvegarder_donnees(chemin_fichier: Path, donnees: Dict[str, Any]) -> None:
    """
    Sauvegarde la structure de données complète dans le fichier JSON.
    """
    nb_taches = len(donnees.get("taches", []))
    print(f"<- Sauvegarde de {nb_taches} tâches dans {chemin_fichier}...")
    try:
        with chemin_fichier.open("w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        print("Sauvegarde terminée.")
    except IOError as e:
        print(f"ERREUR : Échec de la sauvegarde dans {chemin_fichier} : {e}")


# ----------------------------------------------------------------------
# Fonctions Métier (Modification en mémoire)
# ----------------------------------------------------------------------

def afficher_taches(donnees: Dict[str, Any]) -> None:
    """Affiche la liste des tâches de façon lisible."""
    utilisateur = donnees.get("utilisateur", "Inconnu")
    taches = donnees.get("taches", [])
    nb_taches = len(taches)
    
    print("\n" + "=" * 40)
    print(f" LISTE DES TÂCHES de {utilisateur} ({nb_taches} tâches)")
    print("=" * 40)
    
    if not taches:
        print("La liste est vide.")
        return

    for tache in taches:
        statut = "✅ FAIT" if tache.get("fait") else "❌ À FAIRE"
        print(f"[{tache.get('id', '?'):<3}] {tache.get('titre', 'Sans titre')} ({statut})")
    print("-" * 40)


def ajouter_tache(donnees: Dict[str, Any], titre: str) -> None:
    """
    Ajoute une tâche dans donnees["taches"] et met à jour donnees["derniere_id"].
    """
    # Rôle de "derniere_id" : Il est crucial pour garantir que chaque nouvelle 
    # tâche ait un identifiant unique (ID) qui ne sera jamais réutilisé, 
    # même après la suppression d'anciennes tâches.
    donnees["derniere_id"] += 1
    nouvel_id = donnees["derniere_id"]
    
    nouvelle_tache = {
        "id": nouvel_id,
        "titre": titre,
        "fait": False
    }
    donnees["taches"].append(nouvelle_tache)
    print(f"-> Ajouté : ID {nouvel_id} - {titre}")


def trouver_tache_par_id(taches: List[Dict[str, Any]], id_tache: int) -> Optional[Dict[str, Any]]:
    """Fonction utilitaire pour trouver une tâche par ID."""
    for tache in taches:
        if tache.get("id") == id_tache:
            return tache
    return None

def marquer_tache_faite(donnees: Dict[str, Any], id_tache: int) -> bool:
    """
    Marque la tâche d'identifiant id_tache comme faite.
    """
    taches = donnees.get("taches", [])
    tache = trouver_tache_par_id(taches, id_tache)
    
    if tache:
        tache["fait"] = True
        print(f"-> Cochée : ID {id_tache} - {tache['titre']}")
        return True
    
    print(f"-> Échec : Tâche d'ID {id_tache} introuvable.")
    return False

def supprimer_tache(donnees: Dict[str, Any], id_tache: int) -> bool:
    """
    Supprime la tâche d'identifiant id_tache.
    """
    taches = donnees.get("taches", [])
    
    # Suppression par compréhension de liste ou itération/pop est souvent utilisée.
    # Ici, nous utilisons une compréhension de liste pour filtrer.
    
    taille_avant = len(taches)
    
    # Créer une nouvelle liste qui exclut la tâche à supprimer
    nouvelle_liste_taches = [t for t in taches if t.get("id") != id_tache]
    
    taille_apres = len(nouvelle_liste_taches)
    
    if taille_apres < taille_avant:
        # La liste doit être remplacée dans le dictionnaire donnees pour refléter le changement
        donnees["taches"] = nouvelle_liste_taches 
        print(f"-> Supprimée : Tâche d'ID {id_tache}.")
        return True
    
    print(f"-> Échec : Tâche d'ID {id_tache} introuvable pour suppression.")
    return False


# ----------------------------------------------------------------------
# Bloc Principal
# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    # 1. Charger les données (sécurisé)
    donnees = charger_donnees_securise(FICHIER_TODOS)
    
    # 2. Afficher l'état initial
    afficher_taches(donnees)
    
    # 3. Opérations métier (Modification en mémoire)
    
    # a) Ajouter une nouvelle tâche
    ajouter_tache(donnees, "Faire la vaisselle")
    
    # b) Marquer une tâche existante comme faite (ID 2 était False)
    marquer_tache_faite(donnees, 2) 
    
    # c) Supprimer une tâche (ID 1 était True)
    supprimer_tache(donnees, 1)
    
    # d) Tester une opération sur un ID qui n'existe plus
    supprimer_tache(donnees, 99)
    
    # 4. Afficher l'état final (en mémoire)
    afficher_taches(donnees)
    
    # 5. Sauvegarder les données (écriture sur le disque)
    # Commentaire : C'est seulement à cette étape que les modifications faites 
    # en mémoire (ajout, cocher, suppression) sont rendues permanentes sur le disque.
    # Sans cette étape, toutes les modifications seraient perdues à la fin du script.
    sauvegarder_donnees(FICHIER_TODOS, donnees)