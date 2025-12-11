# td15_ex4.py
from datetime import datetime

# =======================================================
# 1. Logging par Héritage (Relation "est un")
# =======================================================

class Logger:
    """
    Classe de base pour un logger simple.
    """
    def log(self, message: str):
        """Affiche le message loggué."""
        print(f"[INFO] {message}")

class TimestampLogger(Logger):
    """
    Ajoute l'horodatage au logging en surchargeant et utilisant super().
    """
    def log(self, message: str):
        # Ajoute le timestamp, puis utilise super().log pour l'affichage de base.
        timestamped_message = f"{datetime.now().isoformat(timespec='seconds')} - {message}"
        # super().log(message) aurait affiché le message sans timestamp car
        # l'affichage [INFO] est dans la classe parente.
        # Pour que super() affiche le message modifié, on passe le nouveau message complet :
        super().log(timestamped_message)

class UppercaseLogger(Logger):
    """
    Affiche le message en majuscules en surchargeant et utilisant super().
    """
    def log(self, message: str):
        # Met le message en majuscules
        upper_message = message.upper()
        # Appelle la méthode de la classe parente pour l'affichage formaté.
        super().log(upper_message)

# =======================================================
# 2. Application utilisant la Composition (Relation "a un")
# =======================================================

class Application:
    """
    Simule une application qui utilise un logger via la composition.
    """
    def __init__(self, logger: Logger):
        # Composition : L'Application "a un" objet logger
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
    
    # 1. Logger de base
    Logger().log("Message de base")
    
    # 2. Logger avec horodatage
    TimestampLogger().log("Message horodaté")
    
    # 3. Logger en majuscules
    UppercaseLogger().log("Message en majuscules")
    
    # Problème d'Héritage : Comment créer un Logger qui est à la fois 
    # Uppercase ET Timestamped ? Cela mènerait au "problème du diamant"
    # ou nécessiterait un héritage complexe et fragile.

    print("\n--- B. Composition dans l'Application ---")

    # 1. Application utilisant le Logger avec horodatage
    app_timestamp = Application(logger=TimestampLogger())
    print("Application avec TimestampLogger :")
    app_timestamp.executer("Démarrage du service A")

    print("\nApplication avec UppercaseLogger :")
    # 2. Application utilisant le Logger en majuscules (même classe Application)
    app_uppercase = Application(logger=UppercaseLogger())
    app_uppercase.executer("Envoi d'un rapport")

    # Conclusion de la flexibilité (Composition) :
    # La classe Application n'a pas besoin d'être modifiée pour changer son 
    # comportement de log. Nous changeons simplement l'objet Logger qui lui 
    # est injecté à l'initialisation.

    # =======================================================
    # 4. Réflexion sur la Conception (Réponses aux questions)
    # =======================================================

    print("\n--- C. Réflexion ---")
    
    # 1. Quelles classes sont liées par héritage ?
    #    - TimestampLogger et UppercaseLogger sont liés à Logger par héritage 
    #      (relation "est un" type de Logger).
    
    # 2. Quelle classe utilise la composition ?
    #    - La classe Application utilise la composition (relation "a un") 
    #      en stockant un objet logger dans self.logger.
    
    # 3. Pourquoi la composition offre-t-elle ici plus de flexibilité ?
    #    - Flexibilité : La composition permet d'injecter *n'importe quel* #      objet qui respecte l'interface Logger (qui a une méthode log()).
    #      Si nous devions créer un nouveau type de log (ex: HTMLLogger), 
    #      nous n'aurions qu'à créer la nouvelle classe Logger, et la classe 
    #      Application pourrait l'utiliser sans aucune modification.
    #    - Combinaison des comportements : Si nous devions combiner 
    #      Timestamp et Uppercase, l'héritage deviendrait complexe. Avec la 
    #      composition, on pourrait créer un 'CompositeLogger' qui encapsule 
    #      les deux, sans modifier la classe Application. Cela respecte le 
    #      principe "Favoriser la Composition sur l'Héritage".