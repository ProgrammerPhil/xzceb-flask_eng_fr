import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test when hello is given as input
    def test2(self):
        self.assertEqual(english_to_french(0), "0") # test when null is given as input

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") #test when Bonjour is given as input
    def test2(self):
        self.assertEqual(french_to_english(0), "0") # test when null is given as input

unittest.main()