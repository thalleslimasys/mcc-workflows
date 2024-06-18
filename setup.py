"""
Ce fichier de configuration est utilisé pour configurer la distribution
du package Python. Il contient des informations essentielles telles que le nom
du package, la version, les packages inclus et les dépendances requises.

Ce fichier utilise setuptools, une bibliothèque pour faciliter la création,
la distribution et l'installation de packages Python.

Pour plus d'informations sur l'utilisation de setuptools, consultez :
https://setuptools.pypa.io/en/latest/userguide/quickstart.html
"""

from setuptools import setup, find_packages

setup(
    name="gabarit-python",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Ajoutez les dépendances de votre projet ici
    ],
)
