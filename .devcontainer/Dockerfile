# Utiliser l'image officielle de Python
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3

SHELL ["/bin/bash", "-c"]

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    --mount=type=cache,target=/root/.cache/pip \
<<EOF
set -e

# Mettre à jour et installer des dépendances
apt-get update && apt-get install -y 

# Mettre à jour pip et installer d'autres dépendances courantes
pip install --upgrade pip setuptools

# Setup base for development
pip --disable-pip-version-check \
    install --root-user-action ignore shtab

# Faire du menage dans les dossiers temp 
rm -rf /tmp/* /var/tmp/*
EOF
