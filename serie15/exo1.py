# td15_ex1.py

# =======================================================
# 1. Classes de Base et Dérivées
# =======================================================

class Animal:
    """
    Classe de base représentant un animal générique.
    """
    def __init__(self, nom: str):
        """
        Constructeur qui initialise l'attribut d'instance 'nom'.
        """
        self.nom = nom
        
    def parler(self):
        """
        Méthode générique que les classes dérivées vont surcharger.
        """
        print(f"{self.nom} (Animal générique) fait un bruit.")

# Commentaire : Explication de l'héritage
# L'héritage (class Chien(Animal)) signifie que la classe Chien reçoit 
# automatiquement tous les attributs et méthodes de la classe Animal.
# Chien est une sous-classe ou classe dérivée, et Animal est la classe parente.

class Chien(Animal):
    """
    Classe dérivée d'Animal, représentant un chien.
    """
    def __init__(self, nom: str):
        # Appel du constructeur de la classe parente (Animal) pour initialiser self.nom
        super().__init__(nom)
    
    # Surcharge (Overriding) de la méthode parler()
    def parler(self, action="aboie"):
        """
        Redéfinit la méthode parler pour adapter le comportement au Chien.
        """
        print(f"{self.nom} {action} : Wouf !")

# Commentaire : Explication de la surcharge de méthode
# La surcharge (Overriding) consiste à redéfinir une méthode héritée (parler())
# dans la classe dérivée (Chien ou Chat). Lorsque parler() est appelé sur une 
# instance de Chien, c'est la version Chien.parler qui est exécutée, et non 
# la version Animal.parler. Cela permet d'adapter le comportement.

class Chat(Animal):
    """
    Classe dérivée d'Animal, représentant un chat.
    """
    def __init__(self, nom: str):
        # Utilisation de super()
        super().__init__(nom)
    
    # Surcharge (Overriding) de la méthode parler()
    def parler(self, action="miaule"):
        """
        Redéfinit la méthode parler pour adapter le comportement au Chat.
        """
        print(f"{self.nom} {action} : Miaou !")

# =======================================================
# 2. Démonstration du Polymorphisme
# =======================================================

if __name__ == "__main__":
    
    # Création des instances
    a1 = Animal("Bête")
    c1 = Chien("Rintintin")
    c2 = Chat("Félix")
    
    # Liste contenant différents types d'objets (Polymorphisme)
    zoo = [a1, c1, c2, Chat("Garfield"), Chien("Milou")]
    
    print("--- Démonstration du Polymorphisme ---")
    
    for animal in zoo:
        # Le même appel de méthode produit un comportement différent selon le type réel de l'objet
        animal.parler() 
    
    print("\n--- Conclusion ---")
    
