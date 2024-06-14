# Utiliser l'image officielle de Python
FROM python:3.11-slim

# Installer les dépendances de base y compris git
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    git \
    && apt-get clean

# Mettre à jour pip et installer d'autres dépendances courantes
RUN pip install --upgrade pip setuptools

# Définir le répertoire de travail
WORKDIR /workspace

# Copier les fichiers de dépendances dans le conteneur
COPY requirements.txt /workspace/requirements.txt

# Installer les dépendances du projet
RUN pip install -r requirements.txt

# Copier le reste du code dans le conteneur
COPY . /workspace
