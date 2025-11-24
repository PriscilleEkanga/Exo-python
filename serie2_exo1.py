#Exercie 1: Vérification ddu mots de passe 

# 1. Demandons le mot de passe à l'utilisateur
mot_de_passe = input("Entrez votre mot de passe : ")

# 2. Initialiser les variables booléennes à False (Faux)
# Au début, on part du principe qu'on n'a rien trouvé.
a_minuscule = False
a_majuscule = False
a_chiffre = False

# 3. Vérifier la longueur (c'est le plus simple, pas besoin de boucle)
longueur_ok = len(mot_de_passe) >= 8

# 4. Parcourir chaque caractère du mot de passe pour vérifier le contenu
for caractere in mot_de_passe:
    # Si le caractère est une minuscule, on passe la variable à True
    if caractere.islower():
        a_minuscule = True
    
    # Si le caractère est une majuscule
    if caractere.isupper():
        a_majuscule = True
        
    # Si le caractère est un chiffre
    if caractere.isdigit():
        a_chiffre = True

# 5. Vérification finale et affichage du résultat
# Le mot de passe est valide SEULEMENT SI toutes les conditions sont Vraies
if longueur_ok and a_minuscule and a_majuscule and a_chiffre:
    print("✅ Mot de passe valide !")
else:
    print("❌ Mot de passe invalide. Voici pourquoi :")
    # On affiche les erreurs spécifiques
    if not longueur_ok:
        print("- Il faut au moins 8 caractères.")
    if not a_minuscule:
        print("- Il manque une lettre minuscule.")
    if not a_majuscule:
        print("- Il manque une lettre majuscule.")
    if not a_chiffre:
        print("- Il manque un chiffre.")