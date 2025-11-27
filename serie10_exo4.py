import requests

# -----------------------------
# 1. Définition de la classe
# -----------------------------
class JsonPlaceholderClient:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    # Méthode interne pour les GET
    def _get(self, endpoint, timeout=5):
        url = self.base_url + endpoint
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Erreur HTTP {response.status_code} pour {url}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erreur réseau pour {url} : {e}")
            return None

    # Retourne la liste de tous les posts
    def get_posts(self):
        return self._get("/posts") or []

    # Retourne un post unique par ID
    def get_post(self, post_id):
        return self._get(f"/posts/{post_id}")

# -----------------------------
# 2. Bloc principal
# -----------------------------
if __name__ == "__main__":
    client = JsonPlaceholderClient()

    # Récupération de tous les posts
    posts = client.get_posts()
    print(f"Nombre total de posts : {len(posts)}\n")

    # Récupération du post d'id 1
    post1 = client.get_post(1)
    if post1:
        print(f"Titre du post #1 : {post1['title']}")
        print(f"Contenu du post #1 :\n{post1['body']}")
    else:
        print("Impossible de récupérer le post #1.")
