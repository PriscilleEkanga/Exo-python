# td15_ex4.py
from datetime import datetime
from typing import Protocol # Optionnel, pour formaliser l'interface

# =======================================================
# 1. Logging par Héritage (Relation "est un")
# =======================================================

class Logger:
    """
    Classe de base pour un logger simple.
    """
    def log(self, message: str):
        """Affiche le message loggué avec un préfixe INFO."""
        print(f"[INFO] {message}")

class TimestampLogger(Logger):
    """
    Ajoute l'horodatage au logging en surchargeant la méthode log().
    """
    def log(self, message: str):
        # Ajoute le timestamp, puis utilise super().log pour l'affichage de base.
        timestamped_message = f"{datetime.now().isoformat(timespec='seconds')} - {message}"
        super().log(timestamped_message)

class UppercaseLogger(Logger):
    """
    Affiche le message en majuscules.
    """
    def log(self, message: str):
        # Met le message en majuscules
        upper_message = message.upper()
        # Appelle la méthode de la classe parente.
        super().log(upper_message)

# =======================================================
# 2. Application utilisant la Composition (Relation "a un")
# =======================================================

class Application:
    """
    Simule une application qui utilise un logger via la composition (injection de dépendance).
    """
    def __init__(self, logger: Logger):
        # Composition : L'Application "a un" objet logger (self.logger)
        self.logger = logger

    def executer(self, action: str):
        """
        Exécute une action et loggue le début et la fin.
        """
        message_debut = f"Début de l'action : {action}"
        self.logger.log(message_debut) # Utilisation du logger injecté
        
        # Simuler un traitement...
        
        message_fin = f"Action terminée : {action}"
        self.logger.log(message_fin)

# =======================================================
# 3. Démonstration
# =======================================================

if __name__ == "__main__":
    
    print("--- A. Loggers par Héritage ---")
    
    # Démonstration du polymorphisme par héritage
    Logger().log("Log simple")
    TimestampLogger().log("Log avec horodatage")
    UppercaseLogger().log("Log en majuscules")
    
    print("\n--- B. Composition dans l'Application ---")

    # 1. Application utilisant le Logger avec horodatage
    app_timestamp = Application(logger=TimestampLogger())
    print("Application avec TimestampLogger :")
    app_timestamp.executer("Sauvegarde des données")

    print("\nApplication avec UppercaseLogger :")
    # 2. Application utilisant le Logger en majuscules (même classe Application)
    app_uppercase = Application(logger=UppercaseLogger())
    app_uppercase.executer("Vérification de la licence")

    # =======================================================
    # 4. Réflexion sur la Conception
    # =======================================================

    print("\n--- C. Réflexion (Réponses aux questions) ---")
    
    # 1. Quelles classes sont liées par héritage ?
    #    - TimestampLogger et UppercaseLogger sont liées à Logger par héritage 
    #      (relation "est un" type de Logger).
    
    # 2. Quelle classe utilise la composition ?
    #    - La classe Application utilise la composition (relation "a un") 
    #      en stockant un objet logger dans self.logger et en appelant sa méthode log().
    
    # 3. Pourquoi la composition offre-t-elle ici plus de flexibilité ?
    #    - La composition permet de "brancher" n'importe quel type de logger (tant qu'il 
    #      implémente la méthode log()) à la classe Application sans avoir à modifier
    #      cette dernière. Si nous voulions un logger qui écrit dans un fichier, 
    #      nous n'aurions qu'à créer FileLogger, et Application pourrait l'utiliser 
    #      immédiatement. 
    #    - L'héritage deviendrait problématique si l'on voulait combiner les 
    #      comportements (ex: un logger qui horodate ET met en majuscules), ce qui 
    #      mènerait à des structures complexes. La composition rend ces combinaisons 
    #      plus faciles à gérer (via des patrons de conception comme le Décorateur).