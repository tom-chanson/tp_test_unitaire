import unittest
import os

from test.utilities.palindrome_builder import PalindromeBuilder

cas_palindrome_valide = ["kayak", "radar", "s.o.s", "été"]
cas_palindrome_invalide = ["bonjour", "hello", "au revoir", "bien dit"]
cas_palindrome_valide_invalide = cas_palindrome_valide + cas_palindrome_invalide

class TestPalindrome(unittest.TestCase):
    def test_mirroir(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().mirroir(cas), cas[::-1])

    def test_palindrome(self):
        for cas in cas_palindrome_valide:
            attendu = "bonjour" + os.linesep + cas + os.linesep + "bien dit"
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().palindrome(cas), attendu)

    def test_palindrome_invalide(self):
        for cas in cas_palindrome_invalide:
            attendu = "bonjour" + os.linesep + cas
            with self.subTest(cas):
                self.assertEqual(PalindromeBuilder().build().palindrome(cas), attendu)

    def test_palindrome_bonjour(self):
        for cas in cas_palindrome_valide_invalide:
            with self.subTest(cas):
                builder = PalindromeBuilder().build()
                result_split = builder.palindrome(cas).split(os.linesep)
                attendu = "bonjour"
                self.assertEqual(result_split[0], attendu)