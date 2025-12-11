#Exercice 2: Division sécurisée

def division_securisee():
    try:
        x = int(input("Numérateur : "))
        y = int(input("Dénominateur : "))
        resultat = x / y
    except ValueError:
        print("Erreur : veuillez entrer des entiers uniquement.")
        return None
    except ZeroDivisionError:
        print("Erreur : le dénominateur ne peut pas être zéro.")
        return None
    else:
        return resultat


# --- Bloc principal ---
resultat = division_securisee()

if resultat is not None:
    print("Résultat :", resultat)
else:
    print("La division a échoué.")
