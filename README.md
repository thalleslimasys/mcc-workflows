# Modèle de DevContainer Python

## Introduction

Ce dépôt est un modèle pour créer un environnement de développement standardisé pour les projets Python en utilisant les DevContainers dans Visual Studio Code.

## Prise en Main

### Prérequis

- Docker/Rancher Desktop
- Visual Studio Code
- Extension Remote - Containers pour VS Code

### Configuration

1. Clonez ce dépôt :

    ```bash
    git clone <repository-url>
    cd my-python-template
    ```

2. Ouvrez le dépôt dans Visual Studio Code :

    ```bash
    code .
    ```

3. Lorsque vous y êtes invité, rouvrez le dépôt dans le DevContainer.

4. Le conteneur se construira et installera les dépendances nécessaires. Une fois terminé, vous aurez un environnement de développement fonctionnel.

## Utilisation

- Ajoutez votre code Python dans le répertoire `src/`.
- Ajoutez vos tests dans le répertoire `tests/`.
- Mettez à jour `requirements.txt` avec toutes les dépendances supplémentaires.

## Contribuer

N'hésitez pas à ouvrir des issues ou à soumettre des pull requests pour toute amélioration ou suggestion.
