import unittest
import os

from src.moment import Moment
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
                "bonjour": {
                    Moment.MATIN: "Good morning",
                    Moment.APRES_MIDI: "Good afternoon",
                    Moment.SOIR: "Good evening",
                    Moment.NUIT: "Good night",
                    Moment.INCONNU: "Hello"
                },
                "au_revoir": "Goodbye"
                }
               ],
                [LangueFr(),
                {
                "bien_dit": "Bien dit",
                "bonjour": {
                    Moment.MATIN: "Bonjour",
                    Moment.APRES_MIDI: "Bon après-midi",
                    Moment.SOIR: "Bonsoir",
                    Moment.NUIT: "Bonne nuit",
                    Moment.INCONNU: "Salut"
                },
                "au_revoir": "Au revoir"
                }]]

class TestPalindrome(unittest.TestCase):
    def test_mirroir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().mirroir(cas), cas[::-1])

    def test_palindrome(self):
        for cas in cas_palindrome_valide:
            with self.subTest(cas):
                langue_spy = LangueSpy()
                PalindromeBuilder().set_langue(langue_spy).build().palindrome(cas).split(os.linesep)
                self.assertTrue(langue_spy.bien_dit_appel())

    def test_palindrome_langue(self):
        for cas in cas_palindrome_valide:
            for cas_lang in cas_langue:
                attendu = cas_lang[1]["bien_dit"]
                with self.subTest(cas):
                    cas_resultat = PalindromeBuilder().set_langue(cas_lang[0]).build().palindrome(cas).split(os.linesep)
                    self.assertEqual(cas_resultat[2], attendu)
                    self.assertEqual(cas_resultat[1], cas)
                    self.assertEqual(len(cas_resultat), 4)

    def test_palindrome_invalide(self):
        for cas in cas_palindrome_invalide:
            with self.subTest(cas):
                langue_spy = LangueSpy()
                builder = PalindromeBuilder().set_langue(langue_spy).build()
                result_split = builder.palindrome(cas).split(os.linesep)
                self.assertFalse(langue_spy.bien_dit_appel())
                self.assertEqual(result_split[1], cas)
                

    def test_palindrome_bonjour(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                langue_spy = LangueSpy()
                PalindromeBuilder().set_langue(langue_spy).build().palindrome(cas)
                self.assertTrue(langue_spy.dit_bonjour_appel())

    def test_palindrome_bonjour_langue(self):
        for cas in cas_palindrome_valide_invalide:
            for cas_lang in cas_langue:
                attendu = cas_lang[1]["bonjour"]
                for time in attendu.keys():
                    with self.subTest( (cas, cas_lang, time) ):
                        cas_resultat = PalindromeBuilder().set_langue(cas_lang[0]).set_moment(time).build().palindrome(cas).split(os.linesep)
                        self.assertEqual(cas_resultat[0], attendu[time])
                        self.assertEqual(cas_resultat[1], cas)

    def test_palindrome_au_revoir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                langue_spy = LangueSpy()
                PalindromeBuilder().set_langue(langue_spy).build().palindrome(cas)
                self.assertTrue(langue_spy.au_revoir_appel())

    def test_palindrome_au_revoir_langue(self):
        for cas in cas_palindrome_valide_invalide:
            for cas_lang in cas_langue:
                attendu = cas_lang[1]["au_revoir"]
                with self.subTest(cas):
                    cas_resultat = PalindromeBuilder().set_langue(cas_lang[0]).build().palindrome(cas).split(os.linesep)
                    self.assertEqual(cas_resultat[-1], attendu)
                    self.assertEqual(cas_resultat[1], cas)