# test_service_remise_log.py
import unittest
# Importe la fonction du module que l'on souhaite tester
from serie12_exo4 import appliquer_remise 

import logging 

# Meilleure pratique : désactiver ou élever le niveau des logs pendant les tests
# pour éviter qu'ils n'apparaissent dans le rapport de test et ne perturbent l'exécution.
# On élève le niveau au-dessus de ERROR.
logging.disable(logging.CRITICAL) 

class TestAppliquerRemise(unittest.TestCase):
    """
    Tests unitaires pour la fonction appliquer_remise.
    """

    def test_remise_valide(self):
        """
        Teste un cas où la remise est valide et le résultat est correct.
        100 € avec remise de 10% (0.1) -> 100 * (1 - 0.1) = 90.00
        """
        prix_ht = 100.00
        remise = 0.10
        attendu = 90.00
        
        # 1. Vérifie le résultat (le comportement fonctionnel)
        self.assertAlmostEqual(appliquer_remise(prix_ht, remise), attendu)
        
    def test_remise_maximale(self):
        """
        Teste le cas limite d'une remise maximale (100%).
        50 € avec remise de 100% (1.0) -> 0.00
        """
        prix_ht = 50.00
        remise = 1.0
        attendu = 0.00
        
        self.assertAlmostEqual(appliquer_remise(prix_ht, remise), attendu)
        
    def test_exception_remise_trop_petite(self):
        """
        Vérifie qu'une exception ValueError est levée si la remise est négative.
        """
        with self.assertRaises(ValueError):
            appliquer_remise(100.00, -0.05) # Remise négative

    def test_exception_remise_trop_grande(self):
        """
        Vérifie qu'une exception ValueError est levée si la remise est supérieure à 1.
        """
        with self.assertRaises(ValueError):
            appliquer_remise(100.00, 1.50) # Remise > 100%


if __name__ == "__main__":
    # Réactive le logging après les tests si besoin (ici, non nécessaire pour unittest.main)
    logging.disable(logging.NOTSET) 
    
    # Lance tous les tests
    unittest.main()