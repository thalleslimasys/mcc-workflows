# Modèle de DevContainer Python

## Introduction

Ce dépôt sert de gabarit pour la création de projets Python avec un environnement de développement standardisé en utilisant DevContainer. Il inclut toutes les configurations nécessaires pour démarrer rapidement un projet Python, y compris les dépendances courantes, les configurations/extensions de l'éditeur et les outils de développement.

## Objectif

Fournir un environnement de développement cohérent et reproductible pour les projets Python.

## Contenu du Gabarit

- **Dockerfile** configuré pour Python 3.11.
- **devcontainer.json** pour les paramètres spécifiques du DevContainer.
- Inclusion des dépendances de base comme `pip` et autres librairies couramment utilisées.
- Intégration avec Visual Studio Code pour une expérience de développement optimisée.
- Documentation pour l'installation et l'utilisation du DevContainer.

## Comment Utiliser ce Gabarit

Pour utiliser ce gabarit comme base pour votre propre projet, suivez les étapes ci-dessous :

1. **Créer un Nouveau Dépôt**:
   - Créez un nouveau dépôt sur GitHub (ou sur une autre plateforme de gestion de code source).
   - Clonez votre nouveau dépôt localement :

     ```sh
     git clone https://github.com/votre-utilisateur/votre-nouveau-repo.git
     ```

2. **Copier les Fichiers du Gabarit**

   - Téléchargez ou clonez ce gabarit :

     ```sh
     git clone https://github.com/votre-utilisateur/repo-gabarit-python.git
     ```

   - Copiez les fichiers du gabarit dans votre nouveau dépôt :

     ```sh
     cp -r repo-gabarit-python/* votre-nouveau-repo/
     ```

3. **Configurer Votre Nouveau Projet**

   - Naviguez vers votre nouveau dépôt :

     ```sh
     cd votre-nouveau-repo
     ```

   - Modifiez les fichiers `setup.py`, `README.md`, et autres fichiers de configuration selon les besoins de votre projet.

4. **Initialiser le Dépôt Git**

   - Si ce n'est pas déjà fait, initialisez le dépôt Git et ajoutez tous les fichiers :

     ```sh
     git init
     git add .
     git commit -m "Initial commit based on template"
     git remote add origin https://github.com/votre-utilisateur/votre-nouveau-repo.git
     git push -u origin main
     ```

5. **Utiliser DevContainer**

   - Ouvrez le projet dans Visual Studio Code.
   - Si vous avez l'extension Remote - Containers installée, VS Code vous proposera d'ouvrir le projet dans un DevContainer. Acceptez cette proposition.
   - Si ce n'est pas le cas, vous pouvez ouvrir la palette de commandes (`Ctrl+Shift+P` ou `Cmd+Shift+P` sur macOS) et exécuter `Remote-Containers: Reopen in Container`.

## Structure du Projet

Voici une vue d'ensemble de la structure du projet incluse dans ce gabarit :

``` bash
gabarit-python/
│
├── .devcontainer/
│ ├── Dockerfile
│ ├── devcontainer.json
│
├── src/
│ ├── init.py
│ └── main.py
│
├── .github/
│ └── workflows/
│ └── python-app.yml
│
├── .vscode/
│ ├── settings.json
│ └── extensions.json
│
├── tests/
│ ├── init.py
│ └── test_main.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

## Prise en Main

### Prérequis

- Docker/Rancher Desktop
- Visual Studio Code
- Extension Remote - Containers pour VS Code

## Configuration des Principaux Fichiers

### Dockerfile

Le Dockerfile configure l'image de base et installe les dépendances nécessaires pour Python.

### devcontainer.json

Le fichier `devcontainer.json` configure les paramètres spécifiques pour DevContainer, intégrant Visual Studio Code et définissant les dépendances et les extensions à installer.

### setup.py

Le fichier `setup.py` est utilisé pour configurer la distribution du package Python. Pour plus d'informations sur l'utilisation de `setuptools`, consultez
[ce lien.](https://setuptools.pypa.io/en/latest/userguide/quickstart.html)

### settings.json

Le fichier `.vscode/settings.json` contient les configurations spécifiques à l'éditeur pour améliorer l'expérience de développement.

## Contributions

Les contributions à ce gabarit sont les bienvenues. Veuillez soumettre des pull requests ou ouvrir des issues pour toute suggestion ou amélioration.
