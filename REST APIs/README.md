
# Build Professional REST APIs with Python, Flask, Docker, Flask-Smorest, and Flask-SQLAlchemy

## Description

Ce projet démontre la création d'une API RESTful professionnelle avec Flask, Flask-Smorest et Flask-SQLAlchemy. Il est conteneurisé à l'aide de Docker pour garantir une portabilité maximale. L'API permet de gérer des utilisateurs avec des fonctionnalités d'ajout et de consultation.

## Fonctionnalités

- Créer et consulter des utilisateurs via une API RESTful.
- Authentification et gestion sécurisée des utilisateurs.
- Intégration avec Docker pour une portabilité maximale.

## Technologies

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Smorest
- Docker

## Installation

### 1. Créez un environnement virtuel Python

Utilisez un environnement virtuel pour garder les dépendances du projet isolées.

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Linux/MacOS
venv\Scripts\activate     # Sur Windows
```

### 2. Installez les dépendances requises

Installez Flask, Flask-Smorest, Flask-SQLAlchemy, Marshmallow, et d'autres dépendances nécessaires avec pip :

```bash
pip install flask flask-smorest flask-sqlalchemy marshmallow flask-migrate
```

### 3. Installez Docker

Assurez-vous d'avoir Docker installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Docker](https://www.docker.com/get-started).

### 4. Créer un fichier Dockerfile

Le fichier Dockerfile permet de définir l'environnement dans lequel votre application sera exécutée. Exemple :

```dockerfile
# Utiliser l'image Python officielle comme base
FROM python:3.12

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de votre projet
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port de l'application
EXPOSE 5000

# Lancer l'application Flask
CMD ["flask", "run", "--host", "0.0.0.0"]
```

### 5. Construire et exécuter le projet avec Docker

Pour construire l'image Docker et exécuter le conteneur, utilisez les commandes suivantes :

```bash
docker build -t mon_api_flask .
docker run -p 5000:5000 mon_api_flask

```
Ton application sera accessible à l'adresse `http://localhost:5000`.


## Mise à jour de la base de données

Lorsqu'il y a des changements dans la structure de la base de données (comme l'ajout ou la modification de modèles), il est important de faire une migration et une mise à jour de la base de données pour refléter ces changements.

### Étapes pour effectuer une migration et une mise à jour :

1. **Migrate** : Crée une migration basée sur les modifications de tes modèles.
   ```bash
   flask db migrate -m "Message de migration"
   ```

2. **Upgrade** : Applique la migration à la base de données.
   ```bash
   flask db upgrade
   ```

Cela permettra de mettre à jour la structure de la base de données en fonction des changements dans tes modèles sans perdre de données existantes.


### Réinitialiser la base de données (facultatif) :

Si tu veux repartir de zéro avec une nouvelle base de données (attention, cela effacera toutes les données), tu peux faire une réinitialisation de la base de données avec :

```bash
flask db downgrade
flask db upgrade
```




## Exécution de l'Application

### Option 1 : Utilisation de Docker Desktop

1. **Construire l'image Docker** :

   Dans le répertoire de ton projet, exécute cette commande pour créer l'image Docker :

   ```bash
   docker build -t mon_api_flask .
   ```

2. **Lancer le conteneur Docker** :

   Ensuite, exécute le conteneur pour démarrer ton application Flask sur le port 5000 :

   ```bash
   docker run -p 5000:5000 mon_api_flask
   ```

   Ton application sera accessible à l'adresse `http://localhost:5000`.

Si tu utilises **Docker Desktop**, tu peux également ouvrir l'interface graphique de Docker et gérer l'exécution de ton conteneur via l'interface.

### Option 2 : Exécution via un éditeur (ex. : VS Code)

1. **Activer l'environnement virtuel** :

   Avant de lancer l'application, assure-toi que ton environnement virtuel est activé :

   ```bash
   source venv/bin/activate  # Sur Linux/MacOS
   venv\Scripts\activate     # Sur Windows
   ```

2. **Lancer l'application Flask** :

   Dans ton terminal, lance l'application Flask avec la commande suivante :

   ```bash
   flask run
   ```

   L'application sera alors accessible à l'adresse `http://localhost:5000`.

## Contribuer

Si tu souhaites contribuer à ce projet, voici comment procéder :

1. Fork ce dépôt.
2. Crée une branche pour ta fonctionnalité (`git checkout -b ma-fonctionnalite`).
3. Fais tes modifications et commit-les (`git commit -am 'Ajout de ma fonctionnalité'`).
4. Pousse tes modifications sur ton fork (`git push origin ma-fonctionnalite`).
5. Ouvre une pull request pour que nous puissions examiner tes modifications.
## Démonstration

Pour voir un exemple de l'affichage de l'application, vous pouvez consulter ce fichier de démonstration :

[Voir la démonstration sur Google Drive](https://docs.google.com/document/d/1Xta3Nj-M2Nkp-6z9pcv70Q9wLuUuRwI4IHlwnL8IDCk/edit?tab=t.0)






