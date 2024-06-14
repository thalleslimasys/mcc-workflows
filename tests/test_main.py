import unittest
from src.main import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("le monde"), "Bonjour, le monde!")

if __name__ == "__main__":
    unittest.main()
