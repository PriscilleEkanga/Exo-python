Exercice 2 – Persistance robuste : fichier manquant ou JSON corrompu
Niveau : Intermédiaire
Rappel de cours
Dans la réalité, le fichier JSON peut :

ne pas exister (premier lancement, suppression manuelle),
être vide ou mal formé (édition manuelle, coupure pendant l’écriture).
Il faut donc gérer au minimum :

from pathlib import Path
import json

FICHIER = Path("donnees.json")

try:
    with FICHIER.open("r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Fichier manquant, création d'une structure par défaut.")
    data = {}
except json.JSONDecodeError as e:
    print("JSON invalide :", e)
    data = {}
Énoncé
Crée un script td19_ex2_securise.py. Tu peux réutiliser / copier certaines parties de ton code de l’exercice 1.
Modifie la fonction de chargement en :
from pathlib import Path
import json

def charger_taches_securise(chemin_fichier: Path) -> list[dict]:
    ...
Cette fonction doit :
si le fichier n’existe pas, afficher un message d’info et renvoyer [] (liste vide),
si le fichier existe mais contient un JSON invalide (par exemple si tu casses volontairement le fichier à la main), intercepter json.JSONDecodeError, afficher un message d’erreur, et renvoyer aussi [], sans écraser le fichier.
Adapte la fonction de sauvegarde :
def sauvegarder_taches(chemin_fichier: Path, taches: list[dict]) -> None:
    ...
en utilisant Path et open avec encoding="utf-8".
Dans le bloc principal :
définis FICHIER_TODOS = Path("todos.json"),
utilise charger_taches_securise pour obtenir la liste de tâches,
ajoute une tâche si la liste est vide (par exemple pour le premier lancement),
sauvegarde ensuite la liste,
affiche un petit résumé (nombre de tâches avant / après ajout).
Fais deux tests manuels :
supprime todos.json et relance le script → observe le comportement,
casse volontairement le JSON (ex. enlève un guillemet) et relance → observe l’erreur et la gestion du cas invalide.
À partir de maintenant, ton code devient plus robuste : il supporte le premier lancement et la corruption du fichier sans planter.