# td13_ex3.py

# =======================================================
# VERSION 1 : Approche Fonctionnelle (Fonctions Libres)
# =======================================================

def creer_panier():
    """Crée un nouvel état (une liste vide) pour le panier."""
    return []

def ajouter_article_fn(panier, article):
    """Modifie l'état 'panier' passé en paramètre."""
    panier.append(article)

def total_articles_fn(panier):
    """Calcule le total en fonction de l'état 'panier' passé en paramètre."""
    return len(panier)

# =======================================================
# VERSION 2 : Approche Orientée Objet (Classe Panier)
# =======================================================

class Panier:
    """
    Encapsule l'état (self.articles) et le comportement du panier dans un objet.
    """

    def __init__(self):
        """
        Constructeur. Initialise l'état interne de l'objet (l'attribut d'instance).
        """
        # Attribut d'instance : stocke l'état unique de ce panier.
        self.articles = []
        
        # Ce que représente 'self' ici : c'est l'objet Panier en cours de création.
        # Par exemple, pour panier_alice = Panier(), self est panier_alice.

    def ajouter_article(self, article):
        """
        Méthode pour ajouter un article.
        
        Arguments:
            self: Représente l'instance (l'objet) sur laquelle la méthode est appelée
                  (ex: panier_alice). Il permet d'accéder à l'état interne (self.articles).
            article: L'article à ajouter.
        """
        self.articles.append(article)
        
    def total_articles(self):
        """
        Méthode pour calculer le total.
        
        Arguments:
            self: Représente l'instance courante. Permet d'accéder à self.articles
                  pour calculer le total spécifique à cet objet.
        """
        return len(self.articles)

# =======================================================
# DÉMONSTRATION
# =======================================================

if __name__ == "__main__":
    
    # --- Test de la Version Fonctionnelle ---
    print("--- V1 : Test Fonctionnel ---")
    
    panier_a = creer_panier()
    ajouter_article_fn(panier_a, "Pommes")
    ajouter_article_fn(panier_a, "Poires")
    
    # La fonction a besoin de l'état (panier_a) comme premier argument
    print(f"Total Panier A : {total_articles_fn(panier_a)}") # Affiche 2
    
    # --- Test de la Version Orientée Objet (POO) ---
    print("\n--- V2 : Test Orienté Objet (Indépendance) ---")
    
    # Création de deux instances (deux paniers indépendants)
    panier_alice = Panier()
    panier_bob = Panier()

    # 1. Panier d'Alice
    panier_alice.ajouter_article("Livre Python") # L'instance panier_alice est passée comme 'self'
    panier_alice.ajouter_article("Souris")
    
    # 2. Panier de Bob
    panier_bob.ajouter_article("Café")           # L'instance panier_bob est passée comme 'self'
    
    # Affichage des totaux (les états sont séparés)
    print(f"Total Alice : {panier_alice.total_articles()}") # Affiche 2
    print(f"Total Bob   : {panier_bob.total_articles()}")   # Affiche 1
    
    # Vérification que le contenu est bien indépendant
    # Notez : print(panier_alice.articles) renvoie ['Livre Python', 'Souris']
    
    print("\n--- Explication ---")
    
    