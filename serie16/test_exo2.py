# td16_ex1_main.py

# Style 1 : Importe le module entier
import test_exo2

def executer_import_style():
    """Exécute la démonstration avec le style 'import module'."""
    
    phrase = input("Veuillez saisir une phrase : ")
    
    # --- Affichage 1 : Nombre de mots ---
    nb_mots = outils_chaine.compter_mots(phrase)
    print(f"\nLe nombre de mots est : {nb_mots}")
    
    # --- Séparateur ---
    print(outils_chaine.SEPARATEUR)
    
    # --- Affichage 2 : Palindrome ---
    if outils_chaine.est_palindrome(phrase):
        print(f"'{phrase}' est un palindrome (en ignorant la casse et les espaces).")
    else:
        print(f"'{phrase}' n'est PAS un palindrome.")

# Si ce fichier est exécuté directement
if __name__ == "__main__":
    executer_import_style()