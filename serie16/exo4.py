# todo/modele.py
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Tache:
    """Modèle représentant une tâche dans la liste de choses à faire."""
    titre: str
    description: Optional[str] = None
    statut: str = "à faire" # Valeurs possibles : "à faire", "en cours", "terminée"

    def afficher(self):
        """Affiche les détails de la tâche de façon lisible."""
        status_symb = "✅" if self.statut == "terminée" else "⏳"
        
        print(f"{status_symb} {self.titre}")
        if self.description:
            print(f"   Description: {self.description}")
        print(f"   Statut actuel: {self.statut}")
        print("-" * 20)