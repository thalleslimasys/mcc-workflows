# Utiliser l'image officielle de Python
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3

# Mettre à jour pip et installer d'autres dépendances courantes
RUN pip install --upgrade pip setuptools

# Copier les fichiers de dépendances dans le conteneur
COPY requirements.txt /workspaces/requirements.txt

# Copier le reste du code dans le conteneur
COPY . /workspaces
