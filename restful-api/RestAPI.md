# FICHE REST API


# PARTIE 1 — Les 5 commandes `curl` indispensables

## 1 Faire une requête GET (récupérer des données)

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

✔ Récupère une ressource
✔ Méthode par défaut = **GET**


## 2️ Voir seulement les headers (très demandé en exercice)

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

✔ Affiche uniquement les headers
✔ Permet de voir le code HTTP
✔ Utile pour tester HTTP vs HTTPS

---

## 3️ Voir headers + body

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

✔ Affiche la réponse complète
✔ Permet d’analyser les codes d’état

---

## 4️ Faire une requête POST (créer une ressource)

```bash
curl -X POST -d "title=test&body=hello&userId=1" \
https://jsonplaceholder.typicode.com/posts
```

✔ Envoie des données
✔ Simule la création d’un élément

---

## 5️ Spécifier le type JSON (plus propre)

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"test","body":"hello","userId":1}'
```

✔ Envoie des données au format JSON
✔ Très utilisé en projets API

---

#  PARTIE 2 — Les 5 commandes `jq` indispensables

 On combine avec le pipe `|`

---

## 1️ Formater proprement le JSON

```bash
curl https://jsonplaceholder.typicode.com/posts/1 | jq
```

✔ Rend le JSON lisible

---

## 2️ Extraire un champ précis

```bash
curl https://jsonplaceholder.typicode.com/posts/1 | jq '.title'
```

✔ Affiche uniquement le champ `title`

---

## 3️ Récupérer le premier élément d’une liste

```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[0]'
```

✔ Affiche le premier élément du tableau

---

## 4️ Extraire un champ pour tous les éléments

```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[].title'
```

✔ Liste tous les titres

---

## 5️ Filtrer par condition (niveau 🔥)

```bash
curl https://jsonplaceholder.typicode.com/posts | jq '.[] | select(.userId == 1)'
```

✔ Affiche uniquement les posts de l’utilisateur 1

---

# À retenir

## Côté `curl`

| Option | Signification           |
| ------ | ----------------------- |
| `-I`   | Headers seulement       |
| `-i`   | Headers + body          |
| `-X`   | Choisir la méthode HTTP |
| `-d`   | Envoyer des données     |
| `-H`   | Ajouter un header       |

---

## Côté `jq`

| Syntaxe     | Signification                |
| ----------- | ---------------------------- |
| `.`         | Tout le JSON                 |
| `.field`    | Champ précis                 |
| `.[0]`      | Premier élément              |
| `.[].field` | Champ pour tous les éléments |
| `select()`  | Filtrer selon condition      |
