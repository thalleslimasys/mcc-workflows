# Utiliser l'image officielle de Python
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3

# Mettre à jour et installer des dépendances
RUN apt-get update && apt-get install -y 

# Mettre à jour pip et installer d'autres dépendances courantes
RUN pip install --upgrade pip setuptools

# Faire du menage dans les dossiers temp 
RUN rm -rf /tmp/* /var/tmp/*

# Setup base for development
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    pip --disable-pip-version-check \
    install --root-user-action ignore shtab

