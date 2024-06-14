import unittest
from src.main import Greeter


class TestGreeter(unittest.TestCase):
    """
    Classe de test pour la classe Greeter.

    Méthodes
    --------
    test_greet():
        Teste si la méthode greet retourne le bon message de salutation.
    """

    def test_greet(self):
        """
        Teste la méthode greet de la classe Greeter.

        Vérifie que la méthode greet retourne "Bonjour, le monde!" 
        lorsqu'elle est appelée avec "le monde".
        """
        greeter = Greeter()
        self.assertEqual(greeter.greet("le monde"), "Bonjour, le monde!")


if __name__ == "__main__":
    unittest.main()
