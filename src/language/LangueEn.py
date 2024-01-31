import src.language.Langue as Langue
from src.moment import Moment

class LangueEn(Langue.Langue):
    def bien_dit(self):
        return "Well said"
    
    def dit_bonjour(self):
        return "Hello"
    
    def au_revoir(self):
        return "Goodbye"