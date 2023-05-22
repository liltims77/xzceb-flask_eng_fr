import unittest
from translator import french_to_english, english_to_french

class TranslatorTests(unittest.TestCase):
    def test_english_to_french(self):
        # Test case 1: Test translation of a simple English phrase
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

        # Test case 2: Test translation of an empty string
        result = english_to_french("Null")
        self.assertEqual(result, "Null")

        # Test case 3: Test translation of a longer sentence
        result = english_to_french("I'm Mister Tim.")
        self.assertEqual(result, "Je suis Mister Tim.")

    def test_french_to_english(self):
        # Test case 1: Test translation of a simple French phrase
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

        # Test case 2: Test translation of an empty string
        result = french_to_english("Null")
        self.assertEqual(result, "Null")

        # Test case 3: Test translation of a longer sentence
        result = french_to_english("Je suis Mister Tim.")
        self.assertEqual(result, "I'm Mister Tim.")

if __name__ == '__main__':
    unittest.main()




