# td11_ex4.py

class ScoreBoard:
    """
    Gère les scores de plusieurs joueurs en encapsulant l'état (le dictionnaire des scores)
    et les opérations associées (ajout de points, affichage).
    """
    
    def __init__(self):
        """
        Initialise le tableau de scores avec un dictionnaire vide.
        Ce dictionnaire est l'attribut d'instance qui stocke l'état.
        """
        # Attribut d'instance : stocke les scores sous la forme {nom_joueur: score}
        self.scores = {}

    def ajouter_points(self, nom_joueur, points):
        """
        Ajoute des points à un joueur. Crée le joueur si inexistant.

        Arguments:
            nom_joueur (str): Nom du joueur.
            points (int): Nombre de points à ajouter.
        """
        # Utilise .get() pour récupérer le score actuel (0 si le joueur est nouveau)
        ancien_score = self.scores.get(nom_joueur, 0)
        
        # Met à jour l'attribut d'instance
        self.scores[nom_joueur] = ancien_score + points
        
        # Note : Pas besoin de "return self.scores" car la méthode modifie l'état interne de l'objet.

    def afficher(self):
        """
        Affiche les scores de tous les joueurs enregistrés.
        """
        print("\n--- Tableau des Scores ---")
        if not self.scores:
            print("Aucun joueur n'a encore de score.")
            return

        # Itère sur tous les joueurs stockés dans l'attribut d'instance
        for joueur, score in self.scores.items():
            print(f"- {joueur.capitalize():<10} : {score:>3} points")
        print("--------------------------")


if __name__ == "__main__":
    # 1. Création de l'objet ScoreBoard (initialisation de l'état)
    jeu = ScoreBoard()
    
    print("Début du scénario de jeu.")

    # 2. Scénario de test : Ajout de points
    jeu.ajouter_points("joueur1", 10)
    jeu.ajouter_points("joueur2", 5)
    jeu.ajouter_points("joueur1", 7) # Le joueur 1 marque à nouveau
    
    # Ajout d'un troisième joueur ("invité")
    jeu.ajouter_points("invité", 15)
    jeu.ajouter_points("joueur2", 2)
    
    # 3. Affichage final
    jeu.afficher()
    
    # Affichage du dictionnaire interne pour vérification (Optionnel)
    # print(jeu.scores)