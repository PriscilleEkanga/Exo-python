# td15_ex2.py

class CompteBancaire:
    """
    Classe de base pour un compte bancaire standard.
    """
    def __init__(self, titulaire: str, solde_initial: float = 0.0):
        self.titulaire = titulaire
        self.solde = solde_initial

    def deposer(self, montant: float):
        if montant <= 0:
            raise ValueError("Le montant du dépôt doit être positif.")
        self.solde += montant
        print(f"Dépôt de {montant:.2f} € effectué.")

    def retirer(self, montant: float):
        """
        Retire un montant, avec vérification de solde suffisant.
        """
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")
            
        # Règle métier : le solde ne doit pas devenir négatif
        if self.solde - montant < 0:
            raise ValueError(
                f"Solde insuffisant pour retirer {montant:.2f} € (Solde actuel : {self.solde:.2f} €)."
            )
            
        self.solde -= montant
        print(f"Retrait de {montant:.2f} € effectué.")

    def afficher(self):
        """
        Affiche l'état actuel du compte.
        """
        print(f"Compte de {self.titulaire} – Solde : {self.solde:.2f} €")

# ----------------------------------------------------------------------

class CompteEpargne(CompteBancaire):
    """
    Hérite de CompteBancaire. Ajoute la notion de taux d'intérêt.
    """
    def __init__(self, titulaire: str, solde_initial: float = 0.0, taux_interet: float = 0.02):
        # Utilisation de super() : appelle le constructeur de la classe parente (CompteBancaire)
        # pour initialiser 'titulaire' et 'solde'.
        super().__init__(titulaire, solde_initial) 
        self.taux_interet = taux_interet
        
    def appliquer_interets(self):
        """
        Ajoute les intérêts au solde en fonction du taux d'intérêt.
        """
        interets = self.solde * self.taux_interet
        self.solde += interets
        print(f"Intérêts appliqués ({self.taux_interet*100:.1f}%) : +{interets:.2f} €")

# ----------------------------------------------------------------------

class CompteCourant(CompteBancaire):
    """
    Hérite de CompteBancaire. Surcharge la méthode retirer() pour autoriser un découvert.
    """
    def __init__(self, titulaire: str, solde_initial: float = 0.0, decouvert_autorise: float = 500.0):
        # Utilisation de super() : appelle le constructeur de la classe parente
        super().__init__(titulaire, solde_initial)
        self.decouvert_autorise = decouvert_autorise

    # Surcharge (Overriding) de CompteBancaire.retirer
    def retirer(self, montant: float):
        """
        Redéfinit la méthode retirer pour permettre un solde négatif 
        jusqu'à la limite du découvert autorisé.
        """
        if montant <= 0:
            raise ValueError("Le montant du retrait doit être positif.")

        # Le solde ne doit pas descendre sous ( - decouvert_autorise )
        limite_min = -self.decouvert_autorise
        
        if self.solde - montant < limite_min:
            raise ValueError(
                f"Retrait de {montant:.2f} € impossible. La limite de découvert "
                f"autorisé ({self.decouvert_autorise:.2f} €) serait dépassée."
            )
            
        self.solde -= montant
        print(f"Retrait de {montant:.2f} € effectué (Découvert max : {self.decouvert_autorise:.2f} €).")

# ----------------------------------------------------------------------

if __name__ == "__main__":
    
    # Création des comptes
    cpt_standard = CompteBancaire("Paul Standard", 100.00)
    cpt_epargne = CompteEpargne("Alice Épargne", 500.00, taux_interet=0.03)
    cpt_courant = CompteCourant("Bob Courant", 50.00, decouvert_autorise=300.00)
    
    print("--- 1. Scénario Comptes ---")
    
    # Compte Standard
    cpt_standard.deposer(20.00)
    try:
        cpt_standard.retirer(150.00) # Doit échouer (solde 120.00)
    except ValueError as e:
        print(f"Standard ERREUR : {e}")

    # Compte Épargne
    print("\n[Compte Épargne]")
    cpt_epargne.deposer(100.00) # Solde passe à 600.00
    cpt_epargne.appliquer_interets() # Intérêts appliqués sur 600.00 (18.00 €)
    
    # Compte Courant (Test du découvert)
    print("\n[Compte Courant]")
    # Solde initial 50.00, Découvert -300.00
    
    cpt_courant.retirer(200.00) # Solde passe à -150.00 (Autorisé)
    cpt_courant.deposer(10.00) # Solde passe à -140.00
    
    try:
        # Tente de retirer 200.00 € de -140.00 €. Nouveau solde : -340.00 € (Limite -300.00 €)
        cpt_courant.retirer(200.00) 
    except ValueError as e:
        print(f"Courant ERREUR : {e}") # Doit afficher l'erreur de découvert
        
    print("\n--- 2. Soldes finaux ---")
    
    cpt_standard.afficher()
    cpt_epargne.afficher()
    cpt_courant.afficher()
