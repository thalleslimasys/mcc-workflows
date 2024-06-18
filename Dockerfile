# Utiliser une image officielle de Python comme base
FROM mcr.microsoft.com/vscode/devcontainers/python:0-3

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de configuration du paquet dans le conteneur
COPY setup.py .

# Copier le fichier des dépendances dans le conteneur (s'il existe)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --upgrade pip setuptools && \
    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi && \
    pip install -e .

# Copier le reste du code de l'application dans le conteneur
COPY . .

# Exécuter les tests
RUN python -m unittest discover

# Définir la commande par défaut à exécuter
CMD ["python", "app.py"]
