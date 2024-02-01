import os
import datetime
import locale
from src.language.LangueFr import LangueFr
from src.language.LangueEn import LangueEn
from src.moment import Moment

class Palindrome:

    @classmethod
    def defaultConstructeur(cls):
        langue_systeme = locale.getdefaultlocale()[0]
        if langue_systeme == "fr_FR":
            cls.__langue = LangueFr()
        else:
            cls.__langue = LangueEn()
        date_time = datetime.datetime.now()
        heure = date_time.hour
        if heure >= 5 and heure <12:
            cls.__moment = Moment.MATIN
        elif heure >= 12 and heure <18:
            cls.__moment = Moment.APRES_MIDI
        elif heure >= 18 and heure <22:
            cls.__moment = Moment.SOIR
        elif heure >= 22 or heure <5:
            cls.__moment = Moment.NUIT
        else:
            cls.__moment = Moment.INCONNU
        return cls(cls.__langue, cls.__moment)
    
    def __init__(self, langue, moment):
        self.__langue = langue
        self.__moment = moment
        print(locale.getdefaultlocale()[0])
        date_time = datetime.datetime.now()
        heure = date_time.hour
        print(heure)


    def mirroir(self, mot):
        return mot[::-1]
    
    def palindrome(self, mot):
        resultat = self.__langue.dit_bonjour(self.__moment) + os.linesep + mot
        if mot == self.mirroir(mot):
            resultat += os.linesep + self.__langue.bien_dit()
        return resultat + os.linesep + self.__langue.au_revoir(self.__moment) + os.linesep
