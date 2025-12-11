# test_remise.py

import unittest
# Importe la fonction du module que l'on souhaite tester
from serie12_exo3 import calculer_prix_ttc 

class TestCalculerPrixTTC(unittest.TestCase):
    """
    Classe de tests unitaires pour la fonction calculer_prix_ttc.
    """

    def test_cas_normal_20_pourcent(self):
        """
        Teste un cas simple avec un prix HT et un taux de TVA standard de 20%.
        100 * (1 + 0.20) = 120
        """
        prix_ht = 100.00
        taux = 0.20
        attendu = 120.00
        
        # On peut utiliser assertEqual ici car le résultat est exact.
        self.assertEqual(calculer_prix_ttc(prix_ht, taux), attendu)

    def test_cas_flottant_non_entier(self):
        """
        Teste un cas où le résultat est un flottant, nécessitant assertAlmostEqual.
        25.50 * (1 + 0.055) = 25.50 * 1.055 = 26.9025
        """
        prix_ht = 25.50
        taux = 0.055 # TVA à 5.5%
        attendu = 26.9025
        
        # assertAlmostEqual compare des flottants avec une certaine précision (par défaut 7 décimales)
        self.assertAlmostEqual(calculer_prix_ttc(prix_ht, taux), attendu)

    def test_prix_nul(self):
        """
        Teste le cas où le prix HT est nul. Le prix TTC doit aussi être nul.
        """
        prix_ht = 0.00
        taux = 0.20
        attendu = 0.00
        
        self.assertEqual(calculer_prix_ttc(prix_ht, taux), attendu)
        
    def test_taux_tva_nul(self):
        """
        Teste le cas où le taux de TVA est nul (prix TTC = prix HT).
        """
        prix_ht = 50.00
        taux = 0.00
        attendu = 50.00
        
        self.assertEqual(calculer_prix_ttc(prix_ht, taux), attendu)


    def test_exception_prix_negatif(self):
        """
        Vérifie qu'une exception ValueError est levée si le prix HT est négatif.
        """
        # Utilisation du gestionnaire de contexte 'assertRaises'
        with self.assertRaises(ValueError):
            calculer_prix_ttc(-10.00, 0.20) # Cet appel DOIT lever l'exception


if __name__ == "__main__":
    # Lance tous les tests de la classe TestCalculerPrixTTC
    # argv=['first-arg-is-ignored'], exit=False permet de ne pas quitter le script
    # après l'exécution des tests si le code est exécuté dans certains environnements.
    # Ici, nous pouvons utiliser la version simple.
    unittest.main()