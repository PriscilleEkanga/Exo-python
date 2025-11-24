#Exercie 2: saisie clavier et conversions dde types

# Saisie clavier
prix_ht_str = input("Entrez le prix HT : ")
taux_tva_str = input("Entrez le taux de TVA (en %) : ")

# Conversions en float
prix_ht = float(prix_ht_str)
taux_tva = float(taux_tva_str)

# Calculs
tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

# Affichage du résultat
print("Pour un prix HT de", prix_ht, "€ et une TVA de", taux_tva, "%, le prix TTC est de", prix_ttc, "€.")
