#Exercice 6:

# 1. On crée une liste vide pour accueillir les notes
notes = []

# 2. Ouverture et lecture du fichier
# "r" signifie "read" (lire)
# encoding="utf-8" permet de bien gérer les caractères spéciaux (accents, etc.)
try:
    with open("notes.txt", "r", encoding="utf-8") as fichier:
        print("📂 Lecture du fichier en cours...")
        
        for ligne in fichier:
            # ligne.strip() enlève les espaces et les retours à la ligne (\n) invisibles
            # float() convertit le texte "12" en nombre 12.0
            valeur_propre = ligne.strip()
            
            # On vérifie que la ligne n'est pas vide avant de convertir
            if valeur_propre: 
                note = float(valeur_propre)
                notes.append(note)

    print(f"✅ Fichier lu avec succès ! {len(notes)} notes trouvées.\n")

    # 3. Traitement des données (Logique de l'exercice 2)
    if len(notes) > 0:
        note_min = min(notes)
        note_max = max(notes)
        moyenne = sum(notes) / len(notes)
        
        # Compter les notes >= 10
        reussites = 0
        for n in notes:
            if n >= 10:
                reussites += 1

        # 4. Affichage des résultats
        print("--- Résultats ---")
        print(f"Note minimale : {note_min}")
        print(f"Note maximale : {note_max}")
        print(f"Moyenne       : {moyenne:.2f}")
        print(f"Notes >= 10   : {reussites}")
        
    else:
        print("⚠️ Le fichier est vide, aucun calcul possible.")

except FileNotFoundError:
    print("❌ Erreur : Le fichier 'notes.txt' est introuvable.")
    print("Vérifiez qu'il est bien dans le même dossier que votre script python.")