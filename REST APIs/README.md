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

1. **Créez un environnement virtuel Python** :

   Utilisez un environnement virtuel pour garder les dépendances du projet isolées.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Sur Linux/MacOS
   venv\Scripts\activate     # Sur Windows

2. **Installez les dépendances requises** :

Installez Flask, Flask-Smorest, Flask-SQLAlchemy, Marshmallow, et d'autres dépendances nécessaires avec pip :

   pip install flask flask-smorest flask-sqlalchemy marshmallow flask-migrate

3. **Installez Docker :**
4. **Créer un fichier Dockerfile :**

Le fichier Dockerfile permet de définir l'environnement dans lequel votre application sera exécutée. Exemple :
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

5. **Construire et exécuter le projet avec Docker :**

Pour construire l'image Docker et exécuter le conteneur, utilise les commandes suivantes :
   **Exécution de l'Application Option 1**
 1. Construire l'image Docker :
docker build -t mon_api_flask .
 2. Lancer le conteneur Docker :
docker run -p 5000:5000 mon_api_flask
Ton application sera accessible à l'adresse http://localhost:5000.
 ***Exécution via un éditeur (ex. : VS Code) Option 2***
    source venv/bin/activate  # Sur Linux/MacOS
    venv\Scripts\activate     # Sur Windows
    flask run








