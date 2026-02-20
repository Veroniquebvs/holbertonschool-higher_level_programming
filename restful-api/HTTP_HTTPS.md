#  HTTP / HTTPS

##  Différence entre HTTP et HTTPS

###  HTTP (HyperText Transfer Protocol)

HTTP est un protocole de communication utilisé pour transférer des données sur le Web.
Il permet aux navigateurs et aux serveurs de communiquer.

Les données sont transmises **en clair** (non sécurisées).

---

### HTTPS (HyperText Transfer Protocol Secure)

HTTPS est la version sécurisée de HTTP.
Il utilise le chiffrement **TLS/SSL** pour protéger les communications.

Il permet de :

* Chiffrer les données échangées
* Empêcher leur modification pendant le transfert
* Vérifier l’identité du serveur


# Représentation d’une requête et d’une réponse HTTP

## Exemple de requête HTTP

```http
GET /hello.txt HTTP/1.1
User-Agent: Mozilla/5.0
Host: www.example.com
Accept-Language: fr
```

---

## Exemple de réponse HTTP

```http
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Content-Type: text/html
Content-Length: 29769
```

---

# Éléments d'une requête HTTP

* **Méthode HTTP** : indique l'opération à effectuer (GET, POST, PUT, DELETE, etc.)
* **Chemin de la ressource** : l'URL sans protocole, domaine et port
* **Version du protocole HTTP** : HTTP/1.1, HTTP/2, etc.
* **En-têtes (Headers)** : informations supplémentaires envoyées au serveur
* **Corps (Body)** : utilisé pour certaines méthodes comme POST


# Éléments d'une réponse HTTP

* **Version du protocole HTTP**
* **Code de statut**
* **Message de statut**
* **En-têtes HTTP**
* **Corps (optionnel)** : ressource demandée


# Méthodes HTTP courantes

## GET

* **Description** : Récupère des données
* **Utilisation** : Charger une page web ou récupérer des données via API

## POST

* **Description** : Envoie des données pour créer une ressource
* **Utilisation** : Créer un utilisateur, envoyer un formulaire

## PUT

* **Description** : Remplace complètement une ressource existante
* **Utilisation** : Mettre à jour toutes les informations d’un utilisateur

## PATCH

* **Description** : Modifie partiellement une ressource
* **Utilisation** : Modifier seulement l’email ou le nom

## DELETE

* **Description** : Supprime une ressource
* **Utilisation** : Supprimer un compte ou une entrée en base


# Codes d'état HTTP courants


## Succès (2xx)

### 200 OK

* Requête réussie
* Page ou données récupérées correctement

### 201 Created

* Ressource créée
* Après un POST réussi

### 204 No Content

* Succès sans contenu renvoyé
* Suppression réussie


## Erreurs côté client (4xx)

### 400 Bad Request

* Requête invalide
* Exemple : données mal formatées

### 401 Unauthorized

* Authentification requise
* Exemple : accès sans connexion

### 403 Forbidden

* Accès refusé
* Exemple : utilisateur connecté sans droits

### 404 Not Found

* Ressource introuvable
* Exemple : page inexistante


## Erreurs côté serveur (5xx)

### 500 Internal Server Error

* Erreur interne du serveur
* Exemple : bug backend

### 503 Service Unavailable

* Serveur indisponible temporairement
* Exemple : maintenance ou surcharge


# Remarque

HTTP fonctionne sur le port **80**
HTTPS fonctionne sur le port **443**
