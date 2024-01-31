import os


class Palindrome:

    def __init__(self, langue, moment):
        self.__langue = langue
        self.__moment = moment


    def mirroir(self, mot):
        return mot[::-1]
    
    def palindrome(self, mot):
        resultat = self.__langue.dit_bonjour(self.__moment) + os.linesep + mot
        if mot == self.mirroir(mot):
            resultat += os.linesep + self.__langue.bien_dit()
        return resultat + os.linesep + self.__langue.au_revoir()

