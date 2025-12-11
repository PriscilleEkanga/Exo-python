#Exercice 4: boucle for , while, range

# 1. Saisie de n
n_str = input("Entrez un entier n : ")
n = int(n_str)

#Table de multiplication (for)
print("Table de multiplication de", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#Somme des entiers de 1 à n (while)
compteur = 1
somme = 0

while compteur <= n:
    somme = somme + compteur
    compteur = compteur + 1

#Affichage de la somme
print("La somme des entiers de 1 à", n, "vaut", somme)
