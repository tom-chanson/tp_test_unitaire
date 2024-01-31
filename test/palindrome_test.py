import unittest
import os

from src.language.LangueEn import LangueEn
from src.language.LangueFr import LangueFr
from test.utilities.LangueSpy import LangueSpy
from test.utilities.palindrome_builder import PalindromeBuilder

cas_palindrome_valide = ["kayak", "radar", "s.o.s", "été"]
cas_palindrome_invalide = ["bonjour", "hello", "au revoir", "bien dit"]
cas_palindrome_valide_invalide = cas_palindrome_valide + cas_palindrome_invalide

cas_langue = [[LangueEn(), 
               {
                "bien_dit": "Well said",
                }
               ],
                [LangueFr(),
                {
                "bien_dit": "Bien dit",
                }]]

class TestPalindrome(unittest.TestCase):
    def test_mirroir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().mirroir(cas), cas[::-1])

    def test_palindrome(self):
        for cas in cas_palindrome_valide:
            for cas_lang in cas_langue:
                attendu = cas_lang[1]["bien_dit"]
                with self.subTest(cas):
                    langue_spy = LangueSpy()
                    PalindromeBuilder().set_langue(langue_spy).build().palindrome(cas, cas_lang[0]).split(os.linesep)
                    self.assertTrue(langue_spy.bien_dit_appel())

    def test_palindrome_langue(self):
        for cas in cas_palindrome_valide:
            for cas_lang in cas_langue:
                attendu = cas_lang[1]["bien_dit"]
                with self.subTest(cas):
                    cas_resultat = PalindromeBuilder().build().palindrome(cas, cas_lang[0]).split(os.linesep)
                    self.assertEqual(cas_resultat[2], attendu)
                    self.assertEqual(cas_resultat[1], cas)
                    self.assertEqual(len(cas_resultat), 4)

    def test_palindrome_invalide(self):
        for cas in cas_palindrome_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                self.assertEqual(result_split[1], cas)
                self.assertEqual(len(result_split), 3)
                

    def test_palindrome_bonjour(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                attendu = "bonjour"
                self.assertEqual(result_split[0], attendu)

    def test_palindrome_au_revoir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                attendu = "au revoir"
                self.assertEqual(result_split[-1], attendu)