import os


class Palindrome:
    def mirroir(self, mot):
        return mot[::-1]
    
    def palindrome(self, mot):
        resultat = mot
        if mot == self.mirroir(mot):
            resultat += os.linesep + "bien dit"
        return resultat

