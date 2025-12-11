import requests

# -----------------------------
# 1. Fonction pour récupérer les posts
# -----------------------------
def recuperer_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # retourne la liste de posts
        else:
            print(f"Erreur HTTP : {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erreur réseau : {e}")
        return []

# -----------------------------
# 2. Fonction pour afficher un résumé des posts
# -----------------------------
def afficher_resume_posts(posts, n=5):
    for post in posts[:n]:
        print(f"Post #{post['id']} (user {post['userId']}) : {post['title']}")

# -----------------------------
# 3. Bloc principal
# -----------------------------
if __name__ == "__main__":
    posts = recuperer_posts()
    print(f"Nombre total de posts : {len(posts)}\n")
    print(f"Aperçu des {min(5, len(posts))} premiers posts :\n")
    afficher_resume_posts(posts, n=5)
