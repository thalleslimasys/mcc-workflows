class Greeter:
    """
    Une classe simple Greeter pour démontrer une implémentation de base.

    Méthodes
    --------
    greet(nom: str) -> str
        Retourne un message de salutation pour le nom donné.
    """

    def greet(self, nom: str) -> str:
        """
        Retourne un message de salutation pour le nom donné.

        Paramètres
        ----------
        nom : str
            Le nom de la personne à saluer.

        Retours
        -------
        str
            Un message de salutation.
        """
        return f"Bonjour, {nom}!"

if __name__ == "__main__":
    greeter = Greeter()
    message = greeter.greet("le Monde!")
    print(message)
