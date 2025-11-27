import requests

# -----------------------------
# 1. Récupération des posts depuis l'API
# -----------------------------
def recuperer_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur HTTP : {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau : {e}")
        return []

# -----------------------------
# 2. Calcul des statistiques par userId
# -----------------------------
def calcul_stats_par_user(posts):
    stats_par_user = {}

    for post in posts:
        uid = post["userId"]
        titre = post["title"]

        if uid not in stats_par_user:
            stats_par_user[uid] = {"nb_posts": 0, "longueur_totale_titres": 0}

        stats_par_user[uid]["nb_posts"] += 1
        stats_par_user[uid]["longueur_totale_titres"] += len(titre)

    # Calcul de la longueur moyenne des titres
    for uid, stats in stats_par_user.items():
        stats["longueur_moyenne_titre"] = round(
            stats["longueur_totale_titres"] / stats["nb_posts"], 1
        )
        del stats["longueur_totale_titres"]  # on supprime le total pour ne garder que la moyenne

    return stats_par_user

# -----------------------------
# 3. Affichage du top 3 des utilisateurs les plus actifs
# -----------------------------
def afficher_top_users(stats_par_user, top_n=3):
    # Tri décroissant par nb_posts
    users_tries = sorted(
        stats_par_user.items(),
        key=lambda item: item[1]["nb_posts"],
        reverse=True
    )

    print(f"Top {top_n} utilisateurs les plus actifs :\n")
    for uid, stats in users_tries[:top_n]:
        print(
            f"User {uid} : {stats['nb_posts']} posts "
            f"(longueur moyenne titre : {stats['longueur_moyenne_titre']})"
        )

# -----------------------------
# 4. Bloc principal
# -----------------------------
if __name__ == "__main__":
    posts = recuperer_posts()
    if posts:
        stats_par_user = calcul_stats_par_user(posts)
        afficher_top_users(stats_par_user, top_n=3)
