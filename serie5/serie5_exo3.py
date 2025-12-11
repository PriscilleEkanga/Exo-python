from typing import List


def calculer_moyenne(notes: List[float]) -> float:
    return sum(notes) / len(notes)


def filtrer_notes_suffisantes(notes: List[float], seuil: float) -> List[float]:
    result: List[float] = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result


def formater_message(nom: str, moyenne: float) -> str:
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"

if __name__ == "__main__":
    notes = [12.5, 9.0, 16.0, 7.5, 14.0]

    moyenne = calculer_moyenne(notes)
    notes_suffisantes = filtrer_notes_suffisantes(notes, 10.0)

    message = formater_message("Priscille", moyenne)

    print("Notes :", notes)
    print("Notes >= 10 :", notes_suffisantes)
    print(message)
