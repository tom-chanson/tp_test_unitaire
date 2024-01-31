import os


class Palindrome:

    def __init__(self, langue):
        self.__langue = langue


    def mirroir(self, mot):
        return mot[::-1]
    
    def palindrome(self, mot):
        resultat = self.__langue.dit_bonjour() + os.linesep + mot
        if mot == self.mirroir(mot):
            resultat += os.linesep + self.__langue.bien_dit()
        return resultat + os.linesep + "au revoir"

